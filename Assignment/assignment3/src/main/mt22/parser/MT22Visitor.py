# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decllist.
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramprime.
    def visitParamprime(self, ctx:MT22Parser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmtlist.
    def visitStmtlist(self, ctx:MT22Parser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignstmt.
    def visitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifstmt.
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forstmt.
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whilestmt.
    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhilestmt.
    def visitDowhilestmt(self, ctx:MT22Parser.DowhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakstmt.
    def visitBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continuestmt.
    def visitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnstmt.
    def visitReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callstmt.
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#spec_func_stmt.
    def visitSpec_func_stmt(self, ctx:MT22Parser.Spec_func_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#spec_func_expr.
    def visitSpec_func_expr(self, ctx:MT22Parser.Spec_func_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readInt.
    def visitReadInt(self, ctx:MT22Parser.ReadIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printInt.
    def visitPrintInt(self, ctx:MT22Parser.PrintIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readFloat.
    def visitReadFloat(self, ctx:MT22Parser.ReadFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printFloat.
    def visitPrintFloat(self, ctx:MT22Parser.PrintFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readBool.
    def visitReadBool(self, ctx:MT22Parser.ReadBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printBool.
    def visitPrintBool(self, ctx:MT22Parser.PrintBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readString.
    def visitReadString(self, ctx:MT22Parser.ReadStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printString.
    def visitPrintString(self, ctx:MT22Parser.PrintStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#superr.
    def visitSuperr(self, ctx:MT22Parser.SuperrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#preventDefault.
    def visitPreventDefault(self, ctx:MT22Parser.PreventDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#helper.
    def visitHelper(self, ctx:MT22Parser.HelperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#basecase.
    def visitBasecase(self, ctx:MT22Parser.BasecaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#notassign.
    def visitNotassign(self, ctx:MT22Parser.NotassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalar_var.
    def visitScalar_var(self, ctx:MT22Parser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subexpr.
    def visitSubexpr(self, ctx:MT22Parser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idx_op.
    def visitIdx_op(self, ctx:MT22Parser.Idx_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callexpr.
    def visitCallexpr(self, ctx:MT22Parser.CallexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arglist.
    def visitArglist(self, ctx:MT22Parser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arglistprime.
    def visitArglistprime(self, ctx:MT22Parser.ArglistprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subarrayitem.
    def visitSubarrayitem(self, ctx:MT22Parser.SubarrayitemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arritems.
    def visitArritems(self, ctx:MT22Parser.ArritemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_typ.
    def visitFunc_typ(self, ctx:MT22Parser.Func_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_typ.
    def visitVar_typ(self, ctx:MT22Parser.Var_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraydecl.
    def visitArraydecl(self, ctx:MT22Parser.ArraydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intlist.
    def visitIntlist(self, ctx:MT22Parser.IntlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#op_relational.
    def visitOp_relational(self, ctx:MT22Parser.Op_relationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#op_mul.
    def visitOp_mul(self, ctx:MT22Parser.Op_mulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boollit.
    def visitBoollit(self, ctx:MT22Parser.BoollitContext):
        return self.visitChildren(ctx)



del MT22Parser