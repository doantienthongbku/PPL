class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        o = [{}]
        for i in ctx.decl:
            self.visit(i, o)
        for i in ctx.stmts:
            self.visit(i, o)
 
 
    def searchAndSet(self, typ, name, o):
        for i in o:
            if name in i:
                i[name] = typ
                return
 
    def visitVarDecl(self,ctx:VarDecl,o):
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        o[0][ctx.name] = 0
 
    def visitFuncDecl(self,ctx:FuncDecl,o):
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        o_1 = [{}] + o
        for i in ctx.param:
            self.visit(i, o_1)
        for i in ctx.local:
            self.visit(i, o_1)
        for i in ctx.stmts:
            self.visit(i, o_1)
        lst_param = []
        for i in ctx.param:
            lst_param += [o_1[0][i.name]]
        o[0][ctx.name] = lst_param
 
    def visitCallStmt(self,ctx:CallStmt,o):
        if ctx.name not in o[0]:
            raise UndeclaredIdentifier(ctx.name)
        else:
            lst_param = o[0][ctx.name]
            if len(lst_param) != len(ctx.args):
                raise TypeMismatchInStatement(ctx)
            else:
                for i in range(0, len(lst_param)):
                    typ = self.visit(ctx.args[i], o)
                    if lst_param[i] == 0 and typ != 0:
                        o[0][ctx.name][i] = typ
                        continue
                    if lst_param[i] != 0 and typ == 0:
                        self.searchAndSet(lst_param[i], ctx.args[i].name, o)
                    if lst_param[i] == 0 and typ == 0:
                        raise TypeCannotBeInferred(ctx)
                    if lst_param[i] != self.visit(ctx.args[i], o):
                        raise TypeMismatchInStatement(ctx)
 
    def visitAssign(self,ctx:Assign,o):
        right = self.visit(ctx.rhs, o)
        left = self.visit(ctx.lhs, o)
        if left == 0 and right != 0:
            self.searchAndSet(right, ctx.lhs.name, o) 
        if left != 0 and right == 0:
            self.searchAndSet(left, ctx.rhs.name, o) 
        if left == 0 and right == 0:
            raise TypeCannotBeInferred(ctx)
        if self.visit(ctx.rhs, o) != self.visit(ctx.lhs, o):
            raise TypeMismatchInStatement(ctx)
 
    def visitBinOp(self,ctx:BinOp,o):
        l = self.visit(ctx.e1, o)
        r = self.visit(ctx.e2, o)
        if ctx.op in ["+", "-", "*", "/"]:
            if l == 0:
                self.searchAndSet(1, ctx.e1.name, o) 
            if r == 0:
                self.searchAndSet(1, ctx.e2.name, o)
            if self.visit(ctx.e1, o) != 1 or self.visit(ctx.e2, o) != 1:
                raise TypeMismatchInExpression(ctx)
            else: 
                return 1
 
        elif ctx.op in ["+.", "-.", "*.", "/."]:
            if l == 0:
                self.searchAndSet(2, ctx.e1.name, o) 
            if r == 0:
                self.searchAndSet(2, ctx.e2.name, o) 
            if self.visit(ctx.e1, o) != 2 or self.visit(ctx.e2, o) != 2:
                raise TypeMismatchInExpression(ctx)
            else: 
                return 2
 
        elif ctx.op in [">", "="]:
            if l == 0:
                self.searchAndSet(1, ctx.e1.name, o) 
            if r == 0:
                self.searchAndSet(1, ctx.e2.name, o) 
            if self.visit(ctx.e1, o) != 1 or self.visit(ctx.e2, o) != 1:
                raise TypeMismatchInExpression(ctx)
            else: 
                return 3
 
        elif ctx.op in [">.", "=."]:
            if l == 0:
                self.searchAndSet(2, ctx.e1.name, o) 
            if r == 0:
                self.searchAndSet(2, ctx.e1.name, o) 
            if self.visit(ctx.e1, o) != 2 or self.visit(ctx.e2, o) != 2:
                raise TypeMismatchInExpression(ctx)
            else: 
                return 3
 
        elif ctx.op in ["||", "&&", "=b", ">b"]:
            if l == 0:
                self.searchAndSet(3, ctx.e1.name, o) 
            if r == 0:
                self.searchAndSet(3, ctx.e1.name, o) 
            if self.visit(ctx.e1, o) != 3 or self.visit(ctx.e2, o) != 3:
                raise TypeMismatchInExpression(ctx)
            else: 
                return 3
 
 
    def visitUnOp(self,ctx:UnOp,o):
        typ = self.visit(ctx.e, o)
        if ctx.op == "-":
            if typ != 1:
                if typ == 0:
                    self.searchAndSet(1, ctx.e.name, o) 
                    return 1
                raise TypeMismatchInExpression(ctx)
            return 1
        elif ctx.op == "-.":
            if typ != 2:
                if typ == 0:
                    self.searchAndSet(3, ctx.e.name, o) 
                    return 2
                raise TypeMismatchInExpression(ctx)
            return 2
        elif ctx.op == "!":
            if typ != 3:
                if typ == 0:
                    self.searchAndSet(3, ctx.e.name, o) 
                    return 3
                raise TypeMismatchInExpression(ctx)
            return 3
        elif ctx.op == "i2f":
            if typ != 1:
                if typ == 0:
                    self.searchAndSet(1, ctx.e.name, o) 
                    return 2
                raise TypeMismatchInExpression(ctx)
            return 2
        else: # floor  
            if typ != 2:
                if typ == 0:
                    self.searchAndSet(2, ctx.e.name, o) 
                    return 1
                raise TypeMismatchInExpression(ctx)
            return 1
 
    def visitIntLit(self,ctx:IntLit,o):
        return 1
 
    def visitFloatLit(self,ctx,o):
        return 2
 
    def visitBoolLit(self,ctx,o):
        return 3
 
    def visitId(self,ctx,o):
        for i in o:
            if ctx.name in i:
                return i[ctx.name]
        raise UndeclaredIdentifier(ctx.name)