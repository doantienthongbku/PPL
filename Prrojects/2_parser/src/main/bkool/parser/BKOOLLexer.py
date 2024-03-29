# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("K\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\2\3\3\3\3\5\3%\n\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\6\6\62\n\6\r\6\16\6\63")
        buf.write("\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\6\13?\n\13\r\13")
        buf.write("\16\13@\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\2\2\17")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\3\2\4\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2M\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\3\35\3\2\2\2\5$\3\2\2\2\7&\3\2\2\2\t,\3\2\2\2\13\61")
        buf.write("\3\2\2\2\r\65\3\2\2\2\17\67\3\2\2\2\219\3\2\2\2\23;\3")
        buf.write("\2\2\2\25>\3\2\2\2\27D\3\2\2\2\31G\3\2\2\2\33I\3\2\2\2")
        buf.write("\35\36\7d\2\2\36\37\7q\2\2\37 \7f\2\2 !\7{\2\2!\4\3\2")
        buf.write("\2\2\"%\5\t\5\2#%\5\7\4\2$\"\3\2\2\2$#\3\2\2\2%\6\3\2")
        buf.write("\2\2&\'\7h\2\2\'(\7n\2\2()\7q\2\2)*\7c\2\2*+\7v\2\2+\b")
        buf.write("\3\2\2\2,-\7k\2\2-.\7p\2\2./\7v\2\2/\n\3\2\2\2\60\62\t")
        buf.write("\2\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2\2\2\63\64")
        buf.write("\3\2\2\2\64\f\3\2\2\2\65\66\7.\2\2\66\16\3\2\2\2\678\7")
        buf.write("\60\2\28\20\3\2\2\29:\7*\2\2:\22\3\2\2\2;<\7+\2\2<\24")
        buf.write("\3\2\2\2=?\t\3\2\2>=\3\2\2\2?@\3\2\2\2@>\3\2\2\2@A\3\2")
        buf.write("\2\2AB\3\2\2\2BC\b\13\2\2C\26\3\2\2\2DE\13\2\2\2EF\b\f")
        buf.write("\3\2F\30\3\2\2\2GH\13\2\2\2H\32\3\2\2\2IJ\13\2\2\2J\34")
        buf.write("\3\2\2\2\6\2$\63@\4\b\2\2\3\f\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    TYP = 2
    FLOAT = 3
    INT = 4
    ID = 5
    COMMA = 6
    SEMI = 7
    LP = 8
    RP = 9
    WS = 10
    ERROR_CHAR = 11
    UNCLOSE_STRING = 12
    ILLEGAL_ESCAPE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'body'", "'float'", "'int'", "','", "'.'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "TYP", "FLOAT", "INT", "ID", "COMMA", "SEMI", "LP", "RP", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "TYP", "FLOAT", "INT", "ID", "COMMA", "SEMI", 
                  "LP", "RP", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[10] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


