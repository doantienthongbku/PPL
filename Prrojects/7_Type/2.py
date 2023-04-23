class StaticCheck(Visitor):
    def visitProgram(self,ctx,o):
        self.visit(ctx.exp,ctx.decl)
        
    def visitBinOp(self,ctx:BinOp,o): 
        ltype = self.visit(ctx.e1,o)
        rtype = self.visit(ctx.e2,o)
        ret = ltype
        if type(ltype) != type(rtype):
            if BoolType in [type(ltype),type(rtype)]:
                raise TypeMismatchInExpression(ctx)
            else:
                ret = FloatType()
        if ctx.op in ['+','-','*','/']:
            if type(ret) is BoolType: raise TypeMismatchInExpression(ctx)
            elif ctx.op == '/': return FloatType()
            else: return ret
        elif ctx.op in ["&&","||"]:
            if type(ret) is not BoolType: raise TypeMismatchInExpression(ctx)
            else: return ret
        elif type(ltype) is not type(rtype): raise TypeMismatchInExpression(ctx)
        else: return BoolType()

    def visitUnOp(self,ctx:UnOp,o):
        typ = self.visit(ctx.e,o)
        if (ctx.op == "-" and type(typ) is BoolType) or (ctx.op == "!" and type(typ) is not BoolType): 
            raise TypeMismatchInExpression(ctx)
        else:
            return typ

    def visitIntLit(self,ctx:IntLit,o): return IntType()

    def visitFloatLit(self,ctx,o): return FloatType()

    def visitBoolLit(self,ctx,o): return BoolType()
    
    def visitId(self,ctx,o):
        typ = None
        for x in o:
            if x.name == ctx.name: 
                typ = x.typ
                break
        if not typ:
            raise UndeclaredIdentifier(ctx.name)
        return typ