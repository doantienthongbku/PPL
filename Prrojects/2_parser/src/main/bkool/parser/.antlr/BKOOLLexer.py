# Generated from d:\HOC_TAP_SV\semester_222\PPL\Prrojects\2_parser\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("E\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\5\6\5,\n\5\r\5\16\5-\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\6\n9\n\n\r\n\16\n:\3\n\3\n\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\3\2\4\6\2\62;C\\aac|\5\2\13\f\17")
        buf.write("\17\"\"\2F\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\3\33\3\2\2\2\5 \3\2\2\2\7&\3\2\2\2\t+\3\2\2\2\13/\3\2")
        buf.write("\2\2\r\61\3\2\2\2\17\63\3\2\2\2\21\65\3\2\2\2\238\3\2")
        buf.write("\2\2\25>\3\2\2\2\27A\3\2\2\2\31C\3\2\2\2\33\34\7d\2\2")
        buf.write("\34\35\7q\2\2\35\36\7f\2\2\36\37\7{\2\2\37\4\3\2\2\2 ")
        buf.write("!\7h\2\2!\"\7n\2\2\"#\7q\2\2#$\7c\2\2$%\7v\2\2%\6\3\2")
        buf.write("\2\2&\'\7k\2\2\'(\7p\2\2()\7v\2\2)\b\3\2\2\2*,\t\2\2\2")
        buf.write("+*\3\2\2\2,-\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\n\3\2\2\2/\60")
        buf.write("\7.\2\2\60\f\3\2\2\2\61\62\7\60\2\2\62\16\3\2\2\2\63\64")
        buf.write("\7*\2\2\64\20\3\2\2\2\65\66\7+\2\2\66\22\3\2\2\2\679\t")
        buf.write("\3\2\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;<\3\2")
        buf.write("\2\2<=\b\n\2\2=\24\3\2\2\2>?\13\2\2\2?@\b\13\3\2@\26\3")
        buf.write("\2\2\2AB\13\2\2\2B\30\3\2\2\2CD\13\2\2\2D\32\3\2\2\2\5")
        buf.write("\2-:\4\b\2\2\3\13\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    FLOAT = 2
    INT = 3
    ID = 4
    COMMA = 5
    SEMI = 6
    LP = 7
    RP = 8
    WS = 9
    ERROR_CHAR = 10
    UNCLOSE_STRING = 11
    ILLEGAL_ESCAPE = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'body'", "'float'", "'int'", "','", "'.'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "FLOAT", "INT", "ID", "COMMA", "SEMI", "LP", "RP", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "FLOAT", "INT", "ID", "COMMA", "SEMI", "LP", "RP", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[9] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


