# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("\u00b4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3<\n\3\3")
        buf.write("\4\3\4\5\4@\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\5\bQ\n\b\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\5\nY\n\n\3\13\3\13\3\13\3\13\3\13\5\13`\n\13\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16m\n\16")
        buf.write("\3\17\3\17\3\17\3\17\5\17s\n\17\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\5\23\u0086\n\23\3\24\3\24\3\24\3\24\3\24\5")
        buf.write("\24\u008d\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u0094\n\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\5\26\u009b\n\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\5\27\u00a2\n\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u00a9\n\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\2\2\33\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\2\4\3\2\17\20\3\2\f\r\2\u00ac\2")
        buf.write("\64\3\2\2\2\4;\3\2\2\2\6?\3\2\2\2\bA\3\2\2\2\nE\3\2\2")
        buf.write("\2\fJ\3\2\2\2\16P\3\2\2\2\20R\3\2\2\2\22X\3\2\2\2\24_")
        buf.write("\3\2\2\2\26a\3\2\2\2\30d\3\2\2\2\32l\3\2\2\2\34r\3\2\2")
        buf.write("\2\36t\3\2\2\2 y\3\2\2\2\"}\3\2\2\2$\u0085\3\2\2\2&\u008c")
        buf.write("\3\2\2\2(\u0093\3\2\2\2*\u009a\3\2\2\2,\u00a1\3\2\2\2")
        buf.write(".\u00a8\3\2\2\2\60\u00aa\3\2\2\2\62\u00ae\3\2\2\2\64\65")
        buf.write("\5\4\3\2\65\66\7\2\2\3\66\3\3\2\2\2\678\5\6\4\289\5\4")
        buf.write("\3\29<\3\2\2\2:<\5\6\4\2;\67\3\2\2\2;:\3\2\2\2<\5\3\2")
        buf.write("\2\2=@\5\b\5\2>@\5\n\6\2?=\3\2\2\2?>\3\2\2\2@\7\3\2\2")
        buf.write("\2AB\5\f\7\2BC\5\16\b\2CD\7\4\2\2D\t\3\2\2\2EF\5\f\7\2")
        buf.write("FG\7\23\2\2GH\5\20\t\2HI\5\30\r\2I\13\3\2\2\2JK\t\2\2")
        buf.write("\2K\r\3\2\2\2LM\7\23\2\2MN\7\3\2\2NQ\5\16\b\2OQ\7\23\2")
        buf.write("\2PL\3\2\2\2PO\3\2\2\2Q\17\3\2\2\2RS\7\5\2\2ST\5\22\n")
        buf.write("\2TU\7\6\2\2U\21\3\2\2\2VY\5\24\13\2WY\3\2\2\2XV\3\2\2")
        buf.write("\2XW\3\2\2\2Y\23\3\2\2\2Z[\5\26\f\2[\\\7\4\2\2\\]\5\24")
        buf.write("\13\2]`\3\2\2\2^`\5\26\f\2_Z\3\2\2\2_^\3\2\2\2`\25\3\2")
        buf.write("\2\2ab\5\f\7\2bc\5\16\b\2c\27\3\2\2\2de\7\7\2\2ef\5\32")
        buf.write("\16\2fg\7\b\2\2g\31\3\2\2\2hi\5\34\17\2ij\5\32\16\2jm")
        buf.write("\3\2\2\2km\3\2\2\2lh\3\2\2\2lk\3\2\2\2m\33\3\2\2\2ns\5")
        buf.write("\b\5\2os\5\36\20\2ps\5\"\22\2qs\5 \21\2rn\3\2\2\2ro\3")
        buf.write("\2\2\2rp\3\2\2\2rq\3\2\2\2s\35\3\2\2\2tu\7\23\2\2uv\7")
        buf.write("\t\2\2vw\5(\25\2wx\7\4\2\2x\37\3\2\2\2yz\7\16\2\2z{\5")
        buf.write("(\25\2{|\7\4\2\2|!\3\2\2\2}~\7\23\2\2~\177\7\5\2\2\177")
        buf.write("\u0080\5$\23\2\u0080\u0081\7\6\2\2\u0081\u0082\7\4\2\2")
        buf.write("\u0082#\3\2\2\2\u0083\u0086\5&\24\2\u0084\u0086\3\2\2")
        buf.write("\2\u0085\u0083\3\2\2\2\u0085\u0084\3\2\2\2\u0086%\3\2")
        buf.write("\2\2\u0087\u0088\5(\25\2\u0088\u0089\7\3\2\2\u0089\u008a")
        buf.write("\5&\24\2\u008a\u008d\3\2\2\2\u008b\u008d\5(\25\2\u008c")
        buf.write("\u0087\3\2\2\2\u008c\u008b\3\2\2\2\u008d\'\3\2\2\2\u008e")
        buf.write("\u008f\5*\26\2\u008f\u0090\7\n\2\2\u0090\u0091\5(\25\2")
        buf.write("\u0091\u0094\3\2\2\2\u0092\u0094\5*\26\2\u0093\u008e\3")
        buf.write("\2\2\2\u0093\u0092\3\2\2\2\u0094)\3\2\2\2\u0095\u0096")
        buf.write("\5,\27\2\u0096\u0097\7\13\2\2\u0097\u0098\5*\26\2\u0098")
        buf.write("\u009b\3\2\2\2\u0099\u009b\5,\27\2\u009a\u0095\3\2\2\2")
        buf.write("\u009a\u0099\3\2\2\2\u009b+\3\2\2\2\u009c\u009d\5.\30")
        buf.write("\2\u009d\u009e\t\3\2\2\u009e\u009f\5,\27\2\u009f\u00a2")
        buf.write("\3\2\2\2\u00a0\u00a2\5.\30\2\u00a1\u009c\3\2\2\2\u00a1")
        buf.write("\u00a0\3\2\2\2\u00a2-\3\2\2\2\u00a3\u00a9\5\60\31\2\u00a4")
        buf.write("\u00a9\7\23\2\2\u00a5\u00a9\7\21\2\2\u00a6\u00a9\7\22")
        buf.write("\2\2\u00a7\u00a9\5\62\32\2\u00a8\u00a3\3\2\2\2\u00a8\u00a4")
        buf.write("\3\2\2\2\u00a8\u00a5\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8")
        buf.write("\u00a7\3\2\2\2\u00a9/\3\2\2\2\u00aa\u00ab\7\5\2\2\u00ab")
        buf.write("\u00ac\5(\25\2\u00ac\u00ad\7\6\2\2\u00ad\61\3\2\2\2\u00ae")
        buf.write("\u00af\7\23\2\2\u00af\u00b0\7\5\2\2\u00b0\u00b1\5$\23")
        buf.write("\2\u00b1\u00b2\7\6\2\2\u00b2\63\3\2\2\2\17;?PX_lr\u0085")
        buf.write("\u008c\u0093\u009a\u00a1\u00a8")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "';'", "'('", "')'", "'{'", "'}'", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'return'", "'float'", 
                     "'int'" ]

    symbolicNames = [ "<INVALID>", "COMMA", "SEMI", "LB", "RB", "LP", "RP", 
                      "ASSIGN", "ADD", "SUB", "MUL", "DIV", "RETURN_TEXT", 
                      "FLOAT", "INT", "INTLIT", "FLOATLIT", "ID", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_funcdecl = 4
    RULE_typ = 5
    RULE_idlist = 6
    RULE_paramdecl = 7
    RULE_paramlist = 8
    RULE_paramprime = 9
    RULE_param = 10
    RULE_body = 11
    RULE_stmtlist = 12
    RULE_stmt = 13
    RULE_assignstmt = 14
    RULE_returnstmt = 15
    RULE_callstmt = 16
    RULE_arglist = 17
    RULE_arglistprime = 18
    RULE_expr = 19
    RULE_expr1 = 20
    RULE_expr2 = 21
    RULE_expr3 = 22
    RULE_subexpr = 23
    RULE_callexpr = 24

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "funcdecl", 
                   "typ", "idlist", "paramdecl", "paramlist", "paramprime", 
                   "param", "body", "stmtlist", "stmt", "assignstmt", "returnstmt", 
                   "callstmt", "arglist", "arglistprime", "expr", "expr1", 
                   "expr2", "expr3", "subexpr", "callexpr" ]

    EOF = Token.EOF
    COMMA=1
    SEMI=2
    LB=3
    RB=4
    LP=5
    RP=6
    ASSIGN=7
    ADD=8
    SUB=9
    MUL=10
    DIV=11
    RETURN_TEXT=12
    FLOAT=13
    INT=14
    INTLIT=15
    FLOATLIT=16
    ID=17
    WS=18
    ERROR_CHAR=19
    UNCLOSE_STRING=20
    ILLEGAL_ESCAPE=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllist(self):
            return self.getTypedRuleContext(BKOOLParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.decllist()
            self.state = 51
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(BKOOLParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(BKOOLParser.DecllistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = BKOOLParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.decl()
                self.state = 54
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(BKOOLParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = BKOOLParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.typ()
            self.state = 64
            self.idlist()
            self.state = 65
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def paramdecl(self):
            return self.getTypedRuleContext(BKOOLParser.ParamdeclContext,0)


        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = BKOOLParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.typ()
            self.state = 68
            self.match(BKOOLParser.ID)
            self.state = 69
            self.paramdecl()
            self.state = 70
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.FLOAT or _la==BKOOLParser.INT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_idlist)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(BKOOLParser.ID)
                self.state = 75
                self.match(BKOOLParser.COMMA)
                self.state = 76
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_paramdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamdecl" ):
                return visitor.visitParamdecl(self)
            else:
                return visitor.visitChildren(self)




    def paramdecl(self):

        localctx = BKOOLParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(BKOOLParser.LB)
            self.state = 81
            self.paramlist()
            self.state = 82
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(BKOOLParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = BKOOLParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramlist)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FLOAT, BKOOLParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.paramprime()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def paramprime(self):
            return self.getTypedRuleContext(BKOOLParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




    def paramprime(self):

        localctx = BKOOLParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramprime)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.param()
                self.state = 89
                self.match(BKOOLParser.SEMI)
                self.state = 90
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.typ()
            self.state = 96
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(BKOOLParser.StmtlistContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(BKOOLParser.LP)
            self.state = 99
            self.stmtlist()
            self.state = 100
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(BKOOLParser.StmtlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = BKOOLParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stmtlist)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.RETURN_TEXT, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.stmt()
                self.state = 103
                self.stmtlist()
                pass
            elif token in [BKOOLParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(BKOOLParser.AssignstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(BKOOLParser.CallstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnstmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt)
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.callstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 111
                self.returnstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = BKOOLParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(BKOOLParser.ID)
            self.state = 115
            self.match(BKOOLParser.ASSIGN)
            self.state = 116
            self.expr()
            self.state = 117
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_TEXT(self):
            return self.getToken(BKOOLParser.RETURN_TEXT, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = BKOOLParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(BKOOLParser.RETURN_TEXT)
            self.state = 120
            self.expr()
            self.state = 121
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def arglist(self):
            return self.getTypedRuleContext(BKOOLParser.ArglistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = BKOOLParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(BKOOLParser.ID)
            self.state = 124
            self.match(BKOOLParser.LB)
            self.state = 125
            self.arglist()
            self.state = 126
            self.match(BKOOLParser.RB)
            self.state = 127
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arglistprime(self):
            return self.getTypedRuleContext(BKOOLParser.ArglistprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arglist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = BKOOLParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arglist)
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.arglistprime()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def arglistprime(self):
            return self.getTypedRuleContext(BKOOLParser.ArglistprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arglistprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglistprime" ):
                return visitor.visitArglistprime(self)
            else:
                return visitor.visitChildren(self)




    def arglistprime(self):

        localctx = BKOOLParser.ArglistprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arglistprime)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.expr()
                self.state = 134
                self.match(BKOOLParser.COMMA)
                self.state = 135
                self.arglistprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(BKOOLParser.Expr1Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.expr1()
                self.state = 141
                self.match(BKOOLParser.ADD)
                self.state = 142
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def expr1(self):
            return self.getTypedRuleContext(BKOOLParser.Expr1Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = BKOOLParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr1)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.expr2()
                self.state = 148
                self.match(BKOOLParser.SUB)
                self.state = 149
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.expr2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKOOLParser.DIV, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)




    def expr2(self):

        localctx = BKOOLParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr2)
        self._la = 0 # Token type
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.expr3()
                self.state = 155
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.MUL or _la==BKOOLParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 156
                self.expr2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.expr3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subexpr(self):
            return self.getTypedRuleContext(BKOOLParser.SubexprContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def callexpr(self):
            return self.getTypedRuleContext(BKOOLParser.CallexprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)




    def expr3(self):

        localctx = BKOOLParser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr3)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.subexpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 163
                self.match(BKOOLParser.INTLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 164
                self.match(BKOOLParser.FLOATLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 165
                self.callexpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_subexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




    def subexpr(self):

        localctx = BKOOLParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(BKOOLParser.LB)
            self.state = 169
            self.expr()
            self.state = 170
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def arglist(self):
            return self.getTypedRuleContext(BKOOLParser.ArglistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_callexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallexpr" ):
                return visitor.visitCallexpr(self)
            else:
                return visitor.visitChildren(self)




    def callexpr(self):

        localctx = BKOOLParser.CallexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_callexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(BKOOLParser.ID)
            self.state = 173
            self.match(BKOOLParser.LB)
            self.state = 174
            self.arglist()
            self.state = 175
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





