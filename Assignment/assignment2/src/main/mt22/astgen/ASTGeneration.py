from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import reduce


class ASTGeneration(MT22Visitor):
    # program: decllist EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decllist()))
    
    # Visit a parse tree produced by MT22Parser#decllist.
    # decllist: decl decllist | decl;
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.decl())
        else:
            return self.visit(ctx.decl()) + self.visit(ctx.decllist())


    # Visit a parse tree produced by MT22Parser#decl.
    # decl: vardecl | funcdecl ;
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        if ctx.vardecl(): return self.visit(ctx.vardecl())
        elif ctx.funcdecl(): return self.visit(ctx.funcdecl())


    # Visit a parse tree produced by MT22Parser#funcdecl.
    # funcdecl: ID COLON FUNCTION func_typ LB paramlist RB (LS INHERIT ID RS)? block_stmt;
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        name = ctx.ID(0).getText()
        return_type = self.visit(ctx.func_typ())
        params = self.visit(ctx.paramlist())
        inherit = ctx.ID(1).getText() if ctx.INHERIT() else None
        body = self.visit(ctx.block_stmt())
        
        return [FuncDecl(name, return_type, params, inherit, body)]


    # Visit a parse tree produced by MT22Parser#paramlist.
    # paramlist: paramprime | ;
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        if ctx.paramprime():
            return self.visit(ctx.paramprime())
        else:
            return []


    # Visit a parse tree produced by MT22Parser#paramprime.
    # paramprime: param COMMA paramprime | param;
    def visitParamprime(self, ctx:MT22Parser.ParamprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        else:
            return [self.visit(ctx.param())] + self.visit(ctx.paramprime())


    # Visit a parse tree produced by MT22Parser#param.
    # param: INHERIT? OUT? ID COLON var_typ;
    def visitParam(self, ctx:MT22Parser.ParamContext):
        name = ctx.ID().getText()
        typ = self.visit(ctx.var_typ())
        out = True if ctx.OUT() else False
        inherit = True if ctx.INHERIT() else False
        return ParamDecl(name, typ, out, inherit)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    # block_stmt: LP stmtlist RP;
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        stmtlist = self.visit(ctx.stmtlist())
        return BlockStmt(body=stmtlist)


    # visit a parse tree produced by MT22Parser#stmtlist.
    # stmtlist: stmt stmtlist | ;
    def visitStmtlist(self, ctx:MT22Parser.StmtlistContext):
        if ctx.stmt():
            stmt = [self.visit(ctx.stmt())]
            while len(stmt) > 0 and isinstance(stmt[0], list) == True:
                stmt = reduce(lambda item, sublst: item + sublst, stmt)
            return stmt + self.visit(ctx.stmtlist())
        else:
            return []


    # Visit a parse tree produced by MT22Parser#stmt.
    # stmt: vardecl | assignstmt | returnstmt | callstmt | ifstmt
	#     | forstmt | whilestmt | dowhilestmt | breakstmt | spec_func
	#     | continuestmt | block_stmt;
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        if ctx.vardecl(): return self.visit(ctx.vardecl())
        elif ctx.assignstmt(): return self.visit(ctx.assignstmt())
        elif ctx.returnstmt(): return self.visit(ctx.returnstmt())
        elif ctx.callstmt(): return self.visit(ctx.callstmt())
        elif ctx.ifstmt(): return self.visit(ctx.ifstmt())
        elif ctx.forstmt(): return self.visit(ctx.forstmt())
        elif ctx.whilestmt(): return self.visit(ctx.whilestmt())
        elif ctx.dowhilestmt(): return self.visit(ctx.dowhilestmt())
        elif ctx.breakstmt(): return self.visit(ctx.breakstmt())
        elif ctx.continuestmt(): return self.visit(ctx.continuestmt())
        elif ctx.block_stmt(): return self.visit(ctx.block_stmt())
        elif ctx.spec_func(): return self.visit(ctx.spec_func())


    # Visit a parse tree produced by MT22Parser#assignstmt.
    # assignstmt: scalar_var ASSIGN expr SEMI;
    def visitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        lhs = self.visit(ctx.scalar_var())
        rhs = self.visit(ctx.expr())
        return AssignStmt(lhs, rhs)


    # Visit a parse tree produced by MT22Parser#ifstmt.
    # ifstmt: IF LB expr RB stmt (ELSE stmt)?;
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        cond = self.visit(ctx.expr())
        tstmt = self.visit(ctx.stmt(0))
        if ctx.ELSE():
            fstmt = self.visit(ctx.stmt(1))
        else:
            fstmt = None
        return IfStmt(cond, tstmt, fstmt)


    # Visit a parse tree produced by MT22Parser#forstmt.
    # forstmt: FOR LB scalar_var ASSIGN expr COMMA expr COMMA expr RB stmt;
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        init = AssignStmt(self.visit(ctx.scalar_var()), self.visit(ctx.expr(0)))
        cond = self.visit(ctx.expr(1))
        upd = self.visit(ctx.expr(2))
        stmt = self.visit(ctx.stmt())
        
        return ForStmt(init, cond, upd, stmt)


    # Visit a parse tree produced by MT22Parser#whilestmt.
    # whilestmt: WHILE LB expr RB stmt;
    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        cond = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        return WhileStmt(cond, stmt)


    # Visit a parse tree produced by MT22Parser#dowhilestmt.
    # dowhilestmt: DO block_stmt WHILE LB expr RB SEMI;
    def visitDowhilestmt(self, ctx:MT22Parser.DowhilestmtContext):
        cond = self.visit(ctx.expr())
        stmt = self.visit(ctx.block_stmt())
        return DoWhileStmt(cond, stmt)


    # Visit a parse tree produced by MT22Parser#breakstmt.
    # breakstmt: BREAK SEMI;
    def visitBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        return BreakStmt()


    # Visit a parse tree produced by MT22Parser#continuestmt.
    # continuestmt: CONTINUE SEMI;
    def visitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        return ContinueStmt()


    # Visit a parse tree produced by MT22Parser#returnstmt.
    # returnstmt: RETURN expr? SEMI;
    def visitReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt(None)


    # Visit a parse tree produced by MT22Parser#callstmt.
    # callexpr: ID LB arglist RB | spec_func;
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        name = ctx.ID().getText()
        arglist = self.visit(ctx.arglist())
        return CallStmt(name, arglist)


    # Visit a parse tree produced by MT22Parser#spec_func.
    # spec_func: readInt | printInt | readFloat | printFloat| readBool 
	#          | printBool | readString | printString | superr | preventDefault;
    def visitSpec_func(self, ctx:MT22Parser.Spec_funcContext):
        if ctx.readInt(): return self.visit(ctx.readInt())
        elif ctx.printInt(): return self.visit(ctx.printInt())
        elif ctx.readFloat(): return self.visit(ctx.readFloat())
        elif ctx.printFloat(): return self.visit(ctx.printFloat())
        elif ctx.readBool(): return self.visit(ctx.readBool())
        elif ctx.printBool(): return self.visit(ctx.printBool())
        elif ctx.readString(): return self.visit(ctx.readString())
        elif ctx.printString(): return self.visit(ctx.printString())
        elif ctx.superr(): return self.visit(ctx.superr())
        elif ctx.preventDefault(): return self.visit(ctx.preventDefault())


    # Visit a parse tree produced by MT22Parser#readInt.
    # readInt: 'readInteger' LB RB SEMI;
    def visitReadInt(self, ctx:MT22Parser.ReadIntContext):
        name = 'readInteger'
        return CallStmt(name, [])


    # Visit a parse tree produced by MT22Parser#printInt.
    # printInt: 'printInteger' LB intVal RB SEMI;
    def visitPrintInt(self, ctx:MT22Parser.PrintIntContext):
        name = 'printInteger'
        args = self.visit(ctx.intVal())
        return CallStmt(name, args)


    # Visit a parse tree produced by MT22Parser#readFloat.
    # readFloat: 'readFloat' LB RB SEMI;
    def visitReadFloat(self, ctx:MT22Parser.ReadFloatContext):
        name = 'readFloat'
        return CallStmt(name, [])


    # Visit a parse tree produced by MT22Parser#printFloat.
    # printFloat: 'printFloat' LB floatVal RB SEMI;
    def visitPrintFloat(self, ctx:MT22Parser.PrintFloatContext):
        name = 'printFloat'
        args = self.visit(ctx.floatVal())
        return CallStmt(name, args)


    # Visit a parse tree produced by MT22Parser#readBool.
    # readBool: 'readBoolean' LB RB SEMI;
    def visitReadBool(self, ctx:MT22Parser.ReadBoolContext):
        name = 'readBoolean'
        return CallStmt(name, [])


    # Visit a parse tree produced by MT22Parser#printBool.
    # printBool: 'printBoolean' LB boolVal RB SEMI;
    def visitPrintBool(self, ctx:MT22Parser.PrintBoolContext):
        name = 'printBoolean'
        args = self.visit(ctx.boolVal())
        return CallStmt(name, args)


    # Visit a parse tree produced by MT22Parser#readString.
    # readString: 'readString' LB RB SEMI;
    def visitReadString(self, ctx:MT22Parser.ReadStringContext):
        name = 'readString'
        return CallStmt(name, [])


    # Visit a parse tree produced by MT22Parser#printString.
    # printString: 'printString' LB stringVal RB SEMI;
    def visitPrintString(self, ctx:MT22Parser.PrintStringContext):
        name = 'printString'
        args = self.visit(ctx.stringVal())
        return CallStmt(name, args)


    # Visit a parse tree produced by MT22Parser#superr.
    # superr: 'super' LB exprlist RB SEMI;
    def visitSuperr(self, ctx:MT22Parser.SuperrContext):
        name = 'super'
        exprlist = self.visit(ctx.exprlist())
        return CallStmt(name, exprlist)


    # Visit a parse tree produced by MT22Parser#preventDefault.
    # preventDefault: 'preventDefault' LB RB SEMI;
    def visitPreventDefault(self, ctx:MT22Parser.PreventDefaultContext):
        name = 'preventDefault'
        return CallStmt(name, [])


    # Visit a parse tree produced by MT22Parser#intVal.
    # intVal: ID | INTLIT | expr;
    def visitIntVal(self, ctx:MT22Parser.IntValContext):
        if ctx.ID():
            return [ctx.ID().getText()]
        elif ctx.INTLIT():
            return [IntegerLit(int(ctx.INTLIT().getText()))]
        elif ctx.expr():
            return [self.visit(ctx.expr())]


    # Visit a parse tree produced by MT22Parser#floatVal.
    # floatVal: ID | FLOATLIT | expr;
    def visitFloatVal(self, ctx:MT22Parser.FloatValContext):
        if ctx.ID():
            return [ctx.ID().getText()]
        elif ctx.FLOATLIT():
            return [FloatLit(float(ctx.FLOATLIT().getText()))]
        elif ctx.expr():
            return [self.visit(ctx.expr())]


    # Visit a parse tree produced by MT22Parser#stringVal.
    # stringVal: ID | STRINGLIT | expr;
    def visitStringVal(self, ctx:MT22Parser.StringValContext):
        if ctx.ID():
            return [ctx.ID().getText()]
        elif ctx.STRINGLIT():
            return [StringLit(ctx.STRINGLIT().getText())]
        elif ctx.expr():
            return [self.visit(ctx.expr())]

    # Visit a parse tree produced by MT22Parser#boolVal.
    # boolVal: ID | boollit | expr;
    def visitBoolVal(self, ctx:MT22Parser.BoolValContext):
        if ctx.ID():
            return [ctx.ID().getText()]
        elif ctx.boollit():
            return [self.visit(ctx.boollit())]
        elif ctx.expr():
            return [self.visit(ctx.expr())]


    # Visit a parse tree produced by MT22Parser#vardecl.
    # vardecl: idlist COLON var_typ (ASSIGN exprlist)? SEMI
    # def visitVardecl(self, ctx:MT22Parser.VardeclContext):
    #     # name: str, typ: Type, init: Expr or None = None
    #     names = self.visit(ctx.idlist())
    #     typ = self.visit(ctx.var_typ())
    #     if ctx.exprlist():
    #         inits = self.visit(ctx.exprlist())
    #         return [VarDecl(names[i], typ, inits[i]) for i in range(len(names))]
    #     else:
    #         inits = None
    #         return [VarDecl(names[i], typ, inits) for i in range(len(names))]
    
    # Visit a parse tree produced by MT22Parser#vardecl.
    # vardecl: (helper | notassign) SEMI;
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        if ctx.notassign():
            return self.visit(ctx.notassign())
        else:
            list_vardecl = self.visit(ctx.helper())
            assert len(list_vardecl) % 2 != 0
            typ = list_vardecl[-1]
            list_vardecl = list_vardecl[:-1]
            list_name = list_vardecl[::2]
            list_expr = list_vardecl[1::2]
            list_expr.reverse()
            
            return [VarDecl(list_name[i], typ, list_expr[i]) for i in range(len(list_name))]


    # Visit a parse tree produced by MT22Parser#helper.
    # helper: ID COMMA helper COMMA expr | basecase; 
    def visitHelper(self, ctx:MT22Parser.HelperContext):
        if ctx.basecase():
            typ, pair = self.visit(ctx.basecase())  # typ, [name, expr]
            return pair + [typ]
        else:
            name = ctx.ID().getText()
            expr = self.visit(ctx.expr())
            return [name, expr] + self.visit(ctx.helper())


    # Visit a parse tree produced by MT22Parser#basecase.
    # basecase: ID COLON var_typ ASSIGN expr;
    def visitBasecase(self, ctx:MT22Parser.BasecaseContext):
        name = ctx.ID().getText()
        typ = self.visit(ctx.var_typ())
        expr = self.visit(ctx.expr())
        return typ, [name, expr]


    # Visit a parse tree produced by MT22Parser#notassign.
    # notassign: idlist COLON var_typ;
    def visitNotassign(self, ctx:MT22Parser.NotassignContext):
        names = self.visit(ctx.idlist())
        typ = self.visit(ctx.var_typ())
        return [VarDecl(names[i], typ) for i in range(len(names))]

    # Visit a parse tree produced by MT22Parser#scalar_var.
    # scalar_var: ID | ID idx_op;
    def visitScalar_var(self, ctx:MT22Parser.Scalar_varContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        else:
            return ArrayCell(ctx.ID().getText(), self.visit(ctx.idx_op()))


    # Visit a parse tree produced by MT22Parser#exprlist.
    # exprlist: expr COMMA exprlist | expr;
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.exprlist())


    # Visit a parse tree produced by MT22Parser#expr.
    # expr: expr1 CONCAT expr1 | expr1;
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if ctx.getChildCount() > 1:
            op = ctx.CONCAT().getText()
            return BinExpr(op, self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        return self.visit(ctx.expr1(0))

    # Visit a parse tree produced by MT22Parser#expr1.
    # expr1: expr2 op_relational expr2 | expr2;
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        if ctx.getChildCount() > 1:
            op = self.visit(ctx.op_relational())
            return BinExpr(op, self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        return self.visit(ctx.expr2(0))


    # Visit a parse tree produced by MT22Parser#expr2.
    # expr2: expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        if ctx.expr2():
            op = ctx.AND().getText() if ctx.AND() else ctx.OR().getText()
            return BinExpr(op, self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        return self.visit(ctx.expr3())


    # Visit a parse tree produced by MT22Parser#expr3.
    # expr3: expr3 (ADD | SUB) expr4 | expr4;
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        if ctx.expr3():
            op = ctx.ADD().getText() if ctx.ADD() else ctx.SUB().getText()
            return BinExpr(op, self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        return self.visit(ctx.expr4())


    # Visit a parse tree produced by MT22Parser#expr4.
    # expr4: expr4 op_mul expr5 | expr5;
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        if ctx.expr4():
            op = self.visit(ctx.op_mul())
            return BinExpr(op, self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        return self.visit(ctx.expr5())


    # Visit a parse tree produced by MT22Parser#expr5.
    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        if ctx.expr6(): return self.visit(ctx.expr6())
        return UnExpr(ctx.NOT().getText(), self.visit(ctx.expr5()))


    # Visit a parse tree produced by MT22Parser#expr6.
    # expr6: SUB expr6 | expr7;
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        if ctx.expr7(): return self.visit(ctx.expr7())
        else: return UnExpr(ctx.SUB().getText(), self.visit(ctx.expr6()))


    # Visit a parse tree produced by MT22Parser#expr7.
    # expr7: expr8 idx_op | expr8;
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        if ctx.idx_op(): return ArrayCell(self.visit(ctx.expr8()), self.visit(ctx.idx_op()))
        else: return self.visit(ctx.expr8())


    # Visit a parse tree produced by MT22Parser#expr8.
    # expr8: subexpr | ID | INTLIT | FLOATLIT | boollit | STRINGLIT | callexpr | arraylit;
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        if ctx.subexpr(): return self.visit(ctx.subexpr())
        elif ctx.ID(): return Id(ctx.ID().getText())
        elif ctx.INTLIT(): return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT(): return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT(): return StringLit(ctx.STRINGLIT().getText())
        elif ctx.boollit(): return self.visit(ctx.boollit())
        elif ctx.callexpr(): return self.visit(ctx.callexpr())
        elif ctx.arraylit(): return self.visit(ctx.arraylit())


    # Visit a parse tree produced by MT22Parser#subexpr.
    # subexpr: LB expr RB;
    def visitSubexpr(self, ctx:MT22Parser.SubexprContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by MT22Parser#idx_op.
    # idx_op: LS exprlist RS;
    def visitIdx_op(self, ctx:MT22Parser.Idx_opContext):
        return self.visit(ctx.exprlist())


    # Visit a parse tree produced by MT22Parser#callexpr.
    # callexpr: ID LB arglist RB;
    def visitCallexpr(self, ctx:MT22Parser.CallexprContext):
        name = ctx.ID().getText()
        arglist = self.visit(ctx.arglist())
        return FuncCall(name, arglist)


    # Visit a parse tree produced by MT22Parser#arglist.
    # arglist: arglistprime | ;
    def visitArglist(self, ctx:MT22Parser.ArglistContext):
        if ctx.arglistprime():
            return self.visit(ctx.arglistprime())
        else:
            return []

    # Visit a parse tree produced by MT22Parser#arglistprime.
    # arglistprime: expr COMMA arglistprime | expr;
    def visitArglistprime(self, ctx:MT22Parser.ArglistprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.arglistprime())

    # Visit a parse tree produced by MT22Parser#idlist.
    # idlist: ID COMMA idlist | ID;
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        else:
            return [ctx.ID().getText()] + self.visit(ctx.idlist())

    # Visit a parse tree produced by MT22Parser#arraylit.
    # arraylit: LP subarrayitem RP;
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        exprlist = self.visit(ctx.subarrayitem())
        return ArrayLit(exprlist)


    # Visit a parse tree produced by MT22Parser#subarrayitem.
    # subarrayitem: arritems | ;
    def visitSubarrayitem(self, ctx:MT22Parser.SubarrayitemContext):
        if ctx.arritems():
            return self.visit(ctx.arritems())
        else:
            return []

    # Visit a parse tree produced by MT22Parser#arritems.
    # arritems: expr COMMA arritems | expr;
    def visitArritems(self, ctx:MT22Parser.ArritemsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.arritems())


    # Visit a parse tree produced by MT22Parser#func_typ.
    # func_typ: typ | VOID | arraydecl;
    def visitFunc_typ(self, ctx:MT22Parser.Func_typContext):
        if ctx.typ(): return self.visit(ctx.typ())
        elif ctx.VOID(): return VoidType()
        elif ctx.arraydecl(): return self.visit(ctx.arraydecl())

    # Visit a parse tree produced by MT22Parser#var_typ.
    # var_typ: typ | arraydecl;
    def visitVar_typ(self, ctx:MT22Parser.Var_typContext):
        if ctx.typ(): return self.visit(ctx.typ())
        elif ctx.arraydecl(): return self.visit(ctx.arraydecl())

    # Visit a parse tree produced by MT22Parser#arraydecl.
    # arraydecl: ARRAY LS intlist RS OF typ;
    def visitArraydecl(self, ctx:MT22Parser.ArraydeclContext):
        dimensions = self.visit(ctx.intlist())
        typ = self.visit(ctx.typ())
        return ArrayType(dimensions, typ)


    # Visit a parse tree produced by MT22Parser#intlist.
    # intlist: INTLIT COMMA intlist | INTLIT;
    def visitIntlist(self, ctx:MT22Parser.IntlistContext):
        if ctx.getChildCount() == 1:
            return [int(ctx.INTLIT().getText())]
        else:
            return [int(ctx.INTLIT().getText())] + self.visit(ctx.intlist())


    # Visit a parse tree produced by MT22Parser#typ.
    # typ: FLOAT | INTEGER | BOOLEAN | STRING | AUTO;	// one of 4 atomic types
    def visitTyp(self, ctx:MT22Parser.TypContext):
        if ctx.FLOAT(): return FloatType()
        elif ctx.INTEGER(): return IntegerType()
        elif ctx.BOOLEAN(): return BooleanType()
        elif ctx.STRING(): return StringType()
        elif ctx.AUTO(): return AutoType()


    # Visit a parse tree produced by MT22Parser#op_relational.
    # op_relational: SMALLER | SMALLER_OR_EQUAL | GREATER | GREATER_OR_EQUAL | EQUAL | DIFF;
    def visitOp_relational(self, ctx:MT22Parser.Op_relationalContext):
        if ctx.SMALLER(): return ctx.SMALLER().getText()
        elif ctx.SMALLER_OR_EQUAL(): return ctx.SMALLER_OR_EQUAL().getText()
        elif ctx.GREATER(): return ctx.GREATER().getText()
        elif ctx.GREATER_OR_EQUAL(): return ctx.GREATER_OR_EQUAL().getText()
        elif ctx.EQUAL(): return ctx.EQUAL().getText()
        elif ctx.DIFF(): return ctx.DIFF().getText()


    # Visit a parse tree produced by MT22Parser#op_mul.
    # op_mul: MUL | DIV | MOD;
    def visitOp_mul(self, ctx:MT22Parser.Op_mulContext):
        if ctx.MUL(): return ctx.MUL().getText()
        elif ctx.DIV(): return ctx.DIV().getText()
        elif ctx.MOD(): return ctx.MOD().getText()


    # Visit a parse tree produced by MT22Parser#boollit.
    # boollit: TRUE | FALSE;
    def visitBoollit(self, ctx:MT22Parser.BoollitContext):
        val = True if ctx.TRUE() else False
        return BooleanLit(val)