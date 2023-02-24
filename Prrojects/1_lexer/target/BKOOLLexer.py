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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("\60\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\3\2\6\2\23\n\2\r\2\16\2\24\3\2\7\2\30\n\2\f")
        buf.write("\2\16\2\33\13\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\6\5$\n\5\r")
        buf.write("\5\16\5%\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\b\3\b\2\2\t\3\3")
        buf.write("\5\2\7\2\t\4\13\5\r\6\17\7\3\2\5\3\2\62;\4\2C\\c|\5\2")
        buf.write("\13\f\17\17\"\"\2\60\2\3\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3\22\3\2\2\2\5\36\3\2\2")
        buf.write("\2\7 \3\2\2\2\t#\3\2\2\2\13)\3\2\2\2\r,\3\2\2\2\17.\3")
        buf.write("\2\2\2\21\23\5\5\3\2\22\21\3\2\2\2\23\24\3\2\2\2\24\22")
        buf.write("\3\2\2\2\24\25\3\2\2\2\25\31\3\2\2\2\26\30\5\7\4\2\27")
        buf.write("\26\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2")
        buf.write("\32\34\3\2\2\2\33\31\3\2\2\2\34\35\6\2\2\2\35\4\3\2\2")
        buf.write("\2\36\37\t\2\2\2\37\6\3\2\2\2 !\t\3\2\2!\b\3\2\2\2\"$")
        buf.write("\t\4\2\2#\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\'\3")
        buf.write("\2\2\2\'(\b\5\2\2(\n\3\2\2\2)*\13\2\2\2*+\b\6\3\2+\f\3")
        buf.write("\2\2\2,-\13\2\2\2-\16\3\2\2\2./\13\2\2\2/\20\3\2\2\2\6")
        buf.write("\2\24\31%\4\b\2\2\3\6\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SHEXA = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "SHEXA", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "SHEXA", "DIGIT", "LETTER", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[4] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[0] = self.SHEXA_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def SHEXA_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return int(self.text, 16) % 2 == 0
         


