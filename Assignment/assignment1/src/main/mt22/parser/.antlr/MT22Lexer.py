# Generated from d:\HOC_TAP_SV\semester_222\PPL\Assignment\assignment1\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2M")
        buf.write("\u0297\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u0125\n\f\3\r\3\r\3")
        buf.write("\r\5\r\u012a\n\r\3\16\3\16\3\16\3\16\7\16\u0130\n\16\f")
        buf.write("\16\16\16\u0133\13\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\7\17\u013e\n\17\f\17\16\17\u0141\13\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3")
        buf.write("(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\5\64\u01ec\n\64\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65")
        buf.write("\u01f9\n\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3")
        buf.write("\66\3\66\5\66\u0205\n\66\3\67\3\67\38\38\39\39\3:\3:\3")
        buf.write(";\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3")
        buf.write("C\7C\u0222\nC\fC\16C\u0225\13C\3C\3C\6C\u0229\nC\rC\16")
        buf.write("C\u022a\7C\u022d\nC\fC\16C\u0230\13C\3C\5C\u0233\nC\3")
        buf.write("D\3D\3D\5D\u0238\nD\5D\u023a\nD\3D\3D\3D\3D\3D\3D\5D\u0242")
        buf.write("\nD\3D\3D\5D\u0246\nD\3E\6E\u0249\nE\rE\16E\u024a\3F\3")
        buf.write("F\5F\u024f\nF\3F\3F\3G\3G\3G\7G\u0256\nG\fG\16G\u0259")
        buf.write("\13G\3G\3G\3G\3H\3H\3H\3I\3I\5I\u0263\nI\3J\3J\3J\3J\3")
        buf.write("J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\5J\u027a")
        buf.write("\nJ\3K\3K\7K\u027e\nK\fK\16K\u0281\13K\3L\6L\u0284\nL")
        buf.write("\rL\16L\u0285\3L\3L\3M\3M\3M\3N\3N\3N\3O\3O\3O\3P\3P\3")
        buf.write("P\5P\u0296\nP\4\u0131\u013f\2Q\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089\2\u008b\2\u008dF\u008f\2")
        buf.write("\u0091G\u0093H\u0095I\u0097J\u0099K\u009bL\u009dM\u009f")
        buf.write("\2\3\2\16\4\2\f\f\17\17\3\2\63;\3\2\62;\4\2\62;aa\4\2")
        buf.write("GGgg\4\2--//\4\2$$^^\n\2$$))^^ddhhppttvv\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\5\2\n\f\16\17\"\"\3\2^^\2\u02d6\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3")
        buf.write("\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u008d\3\2\2\2")
        buf.write("\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\3\u00a1\3\2\2\2\5\u00af\3\2\2\2\7\u00bc\3\2\2\2\t\u00c8")
        buf.write("\3\2\2\2\13\u00d3\3\2\2\2\r\u00e1\3\2\2\2\17\u00ee\3\2")
        buf.write("\2\2\21\u00fb\3\2\2\2\23\u0107\3\2\2\2\25\u010d\3\2\2")
        buf.write("\2\27\u0124\3\2\2\2\31\u0129\3\2\2\2\33\u012b\3\2\2\2")
        buf.write("\35\u0139\3\2\2\2\37\u0146\3\2\2\2!\u014b\3\2\2\2#\u0151")
        buf.write("\3\2\2\2%\u0159\3\2\2\2\'\u015c\3\2\2\2)\u0161\3\2\2\2")
        buf.write("+\u0167\3\2\2\2-\u016d\3\2\2\2/\u0171\3\2\2\2\61\u017a")
        buf.write("\3\2\2\2\63\u017d\3\2\2\2\65\u0185\3\2\2\2\67\u018c\3")
        buf.write("\2\2\29\u0193\3\2\2\2;\u0198\3\2\2\2=\u019e\3\2\2\2?\u01a3")
        buf.write("\3\2\2\2A\u01a7\3\2\2\2C\u01b0\3\2\2\2E\u01b3\3\2\2\2")
        buf.write("G\u01bb\3\2\2\2I\u01c1\3\2\2\2K\u01c3\3\2\2\2M\u01c5\3")
        buf.write("\2\2\2O\u01c7\3\2\2\2Q\u01c9\3\2\2\2S\u01cb\3\2\2\2U\u01cd")
        buf.write("\3\2\2\2W\u01d0\3\2\2\2Y\u01d3\3\2\2\2[\u01d6\3\2\2\2")
        buf.write("]\u01d9\3\2\2\2_\u01db\3\2\2\2a\u01de\3\2\2\2c\u01e0\3")
        buf.write("\2\2\2e\u01e3\3\2\2\2g\u01eb\3\2\2\2i\u01f8\3\2\2\2k\u0204")
        buf.write("\3\2\2\2m\u0206\3\2\2\2o\u0208\3\2\2\2q\u020a\3\2\2\2")
        buf.write("s\u020c\3\2\2\2u\u020e\3\2\2\2w\u0210\3\2\2\2y\u0212\3")
        buf.write("\2\2\2{\u0214\3\2\2\2}\u0216\3\2\2\2\177\u0218\3\2\2\2")
        buf.write("\u0081\u021a\3\2\2\2\u0083\u021c\3\2\2\2\u0085\u0232\3")
        buf.write("\2\2\2\u0087\u0245\3\2\2\2\u0089\u0248\3\2\2\2\u008b\u024c")
        buf.write("\3\2\2\2\u008d\u0252\3\2\2\2\u008f\u025d\3\2\2\2\u0091")
        buf.write("\u0262\3\2\2\2\u0093\u0279\3\2\2\2\u0095\u027b\3\2\2\2")
        buf.write("\u0097\u0283\3\2\2\2\u0099\u0289\3\2\2\2\u009b\u028c\3")
        buf.write("\2\2\2\u009d\u028f\3\2\2\2\u009f\u0295\3\2\2\2\u00a1\u00a2")
        buf.write("\7t\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5")
        buf.write("\7f\2\2\u00a5\u00a6\7K\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8")
        buf.write("\7v\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7i\2\2\u00aa\u00ab")
        buf.write("\7g\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad\7*\2\2\u00ad\u00ae")
        buf.write("\7+\2\2\u00ae\4\3\2\2\2\u00af\u00b0\7r\2\2\u00b0\u00b1")
        buf.write("\7t\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4")
        buf.write("\7v\2\2\u00b4\u00b5\7K\2\2\u00b5\u00b6\7p\2\2\u00b6\u00b7")
        buf.write("\7v\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9\7i\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\u00bb\7t\2\2\u00bb\6\3\2\2\2\u00bc\u00bd")
        buf.write("\7t\2\2\u00bd\u00be\7g\2\2\u00be\u00bf\7c\2\2\u00bf\u00c0")
        buf.write("\7f\2\2\u00c0\u00c1\7H\2\2\u00c1\u00c2\7n\2\2\u00c2\u00c3")
        buf.write("\7q\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6")
        buf.write("\7*\2\2\u00c6\u00c7\7+\2\2\u00c7\b\3\2\2\2\u00c8\u00c9")
        buf.write("\7r\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7H\2\2\u00ce\u00cf")
        buf.write("\7n\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2")
        buf.write("\7v\2\2\u00d2\n\3\2\2\2\u00d3\u00d4\7t\2\2\u00d4\u00d5")
        buf.write("\7g\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7f\2\2\u00d7\u00d8")
        buf.write("\7D\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7n\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de")
        buf.write("\7p\2\2\u00de\u00df\7*\2\2\u00df\u00e0\7+\2\2\u00e0\f")
        buf.write("\3\2\2\2\u00e1\u00e2\7r\2\2\u00e2\u00e3\7t\2\2\u00e3\u00e4")
        buf.write("\7k\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7")
        buf.write("\7D\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea")
        buf.write("\7n\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed")
        buf.write("\7p\2\2\u00ed\16\3\2\2\2\u00ee\u00ef\7t\2\2\u00ef\u00f0")
        buf.write("\7g\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2\7f\2\2\u00f2\u00f3")
        buf.write("\7U\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6")
        buf.write("\7k\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8\7i\2\2\u00f8\u00f9")
        buf.write("\7*\2\2\u00f9\u00fa\7+\2\2\u00fa\20\3\2\2\2\u00fb\u00fc")
        buf.write("\7r\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff")
        buf.write("\7p\2\2\u00ff\u0100\7v\2\2\u0100\u0101\7U\2\2\u0101\u0102")
        buf.write("\7v\2\2\u0102\u0103\7t\2\2\u0103\u0104\7k\2\2\u0104\u0105")
        buf.write("\7p\2\2\u0105\u0106\7i\2\2\u0106\22\3\2\2\2\u0107\u0108")
        buf.write("\7u\2\2\u0108\u0109\7w\2\2\u0109\u010a\7r\2\2\u010a\u010b")
        buf.write("\7g\2\2\u010b\u010c\7t\2\2\u010c\24\3\2\2\2\u010d\u010e")
        buf.write("\7r\2\2\u010e\u010f\7t\2\2\u010f\u0110\7g\2\2\u0110\u0111")
        buf.write("\7x\2\2\u0111\u0112\7g\2\2\u0112\u0113\7p\2\2\u0113\u0114")
        buf.write("\7v\2\2\u0114\u0115\7F\2\2\u0115\u0116\7g\2\2\u0116\u0117")
        buf.write("\7h\2\2\u0117\u0118\7c\2\2\u0118\u0119\7w\2\2\u0119\u011a")
        buf.write("\7n\2\2\u011a\u011b\7v\2\2\u011b\u011c\7*\2\2\u011c\u011d")
        buf.write("\7+\2\2\u011d\26\3\2\2\2\u011e\u0125\5]/\2\u011f\u0125")
        buf.write("\5_\60\2\u0120\u0125\5a\61\2\u0121\u0125\5c\62\2\u0122")
        buf.write("\u0125\5Y-\2\u0123\u0125\5[.\2\u0124\u011e\3\2\2\2\u0124")
        buf.write("\u011f\3\2\2\2\u0124\u0120\3\2\2\2\u0124\u0121\3\2\2\2")
        buf.write("\u0124\u0122\3\2\2\2\u0124\u0123\3\2\2\2\u0125\30\3\2")
        buf.write("\2\2\u0126\u012a\5M\'\2\u0127\u012a\5O(\2\u0128\u012a")
        buf.write("\5Q)\2\u0129\u0126\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u0128")
        buf.write("\3\2\2\2\u012a\32\3\2\2\2\u012b\u012c\7\61\2\2\u012c\u012d")
        buf.write("\7,\2\2\u012d\u0131\3\2\2\2\u012e\u0130\13\2\2\2\u012f")
        buf.write("\u012e\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u0132\3\2\2\2")
        buf.write("\u0131\u012f\3\2\2\2\u0132\u0134\3\2\2\2\u0133\u0131\3")
        buf.write("\2\2\2\u0134\u0135\7,\2\2\u0135\u0136\7\61\2\2\u0136\u0137")
        buf.write("\3\2\2\2\u0137\u0138\b\16\2\2\u0138\34\3\2\2\2\u0139\u013a")
        buf.write("\7\61\2\2\u013a\u013b\7\61\2\2\u013b\u013f\3\2\2\2\u013c")
        buf.write("\u013e\13\2\2\2\u013d\u013c\3\2\2\2\u013e\u0141\3\2\2")
        buf.write("\2\u013f\u0140\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0142")
        buf.write("\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0143\t\2\2\2\u0143")
        buf.write("\u0144\3\2\2\2\u0144\u0145\b\17\2\2\u0145\36\3\2\2\2\u0146")
        buf.write("\u0147\7c\2\2\u0147\u0148\7w\2\2\u0148\u0149\7v\2\2\u0149")
        buf.write("\u014a\7q\2\2\u014a \3\2\2\2\u014b\u014c\7d\2\2\u014c")
        buf.write("\u014d\7t\2\2\u014d\u014e\7g\2\2\u014e\u014f\7c\2\2\u014f")
        buf.write("\u0150\7m\2\2\u0150\"\3\2\2\2\u0151\u0152\7d\2\2\u0152")
        buf.write("\u0153\7q\2\2\u0153\u0154\7q\2\2\u0154\u0155\7n\2\2\u0155")
        buf.write("\u0156\7g\2\2\u0156\u0157\7c\2\2\u0157\u0158\7p\2\2\u0158")
        buf.write("$\3\2\2\2\u0159\u015a\7f\2\2\u015a\u015b\7q\2\2\u015b")
        buf.write("&\3\2\2\2\u015c\u015d\7g\2\2\u015d\u015e\7n\2\2\u015e")
        buf.write("\u015f\7u\2\2\u015f\u0160\7g\2\2\u0160(\3\2\2\2\u0161")
        buf.write("\u0162\7h\2\2\u0162\u0163\7c\2\2\u0163\u0164\7n\2\2\u0164")
        buf.write("\u0165\7u\2\2\u0165\u0166\7g\2\2\u0166*\3\2\2\2\u0167")
        buf.write("\u0168\7h\2\2\u0168\u0169\7n\2\2\u0169\u016a\7q\2\2\u016a")
        buf.write("\u016b\7c\2\2\u016b\u016c\7v\2\2\u016c,\3\2\2\2\u016d")
        buf.write("\u016e\7h\2\2\u016e\u016f\7q\2\2\u016f\u0170\7t\2\2\u0170")
        buf.write(".\3\2\2\2\u0171\u0172\7h\2\2\u0172\u0173\7w\2\2\u0173")
        buf.write("\u0174\7p\2\2\u0174\u0175\7e\2\2\u0175\u0176\7v\2\2\u0176")
        buf.write("\u0177\7k\2\2\u0177\u0178\7q\2\2\u0178\u0179\7p\2\2\u0179")
        buf.write("\60\3\2\2\2\u017a\u017b\7k\2\2\u017b\u017c\7h\2\2\u017c")
        buf.write("\62\3\2\2\2\u017d\u017e\7k\2\2\u017e\u017f\7p\2\2\u017f")
        buf.write("\u0180\7v\2\2\u0180\u0181\7g\2\2\u0181\u0182\7i\2\2\u0182")
        buf.write("\u0183\7g\2\2\u0183\u0184\7t\2\2\u0184\64\3\2\2\2\u0185")
        buf.write("\u0186\7t\2\2\u0186\u0187\7g\2\2\u0187\u0188\7v\2\2\u0188")
        buf.write("\u0189\7w\2\2\u0189\u018a\7t\2\2\u018a\u018b\7p\2\2\u018b")
        buf.write("\66\3\2\2\2\u018c\u018d\7u\2\2\u018d\u018e\7v\2\2\u018e")
        buf.write("\u018f\7t\2\2\u018f\u0190\7k\2\2\u0190\u0191\7p\2\2\u0191")
        buf.write("\u0192\7i\2\2\u01928\3\2\2\2\u0193\u0194\7v\2\2\u0194")
        buf.write("\u0195\7t\2\2\u0195\u0196\7w\2\2\u0196\u0197\7g\2\2\u0197")
        buf.write(":\3\2\2\2\u0198\u0199\7y\2\2\u0199\u019a\7j\2\2\u019a")
        buf.write("\u019b\7k\2\2\u019b\u019c\7n\2\2\u019c\u019d\7g\2\2\u019d")
        buf.write("<\3\2\2\2\u019e\u019f\7x\2\2\u019f\u01a0\7q\2\2\u01a0")
        buf.write("\u01a1\7k\2\2\u01a1\u01a2\7f\2\2\u01a2>\3\2\2\2\u01a3")
        buf.write("\u01a4\7q\2\2\u01a4\u01a5\7w\2\2\u01a5\u01a6\7v\2\2\u01a6")
        buf.write("@\3\2\2\2\u01a7\u01a8\7e\2\2\u01a8\u01a9\7q\2\2\u01a9")
        buf.write("\u01aa\7p\2\2\u01aa\u01ab\7v\2\2\u01ab\u01ac\7k\2\2\u01ac")
        buf.write("\u01ad\7p\2\2\u01ad\u01ae\7w\2\2\u01ae\u01af\7g\2\2\u01af")
        buf.write("B\3\2\2\2\u01b0\u01b1\7q\2\2\u01b1\u01b2\7h\2\2\u01b2")
        buf.write("D\3\2\2\2\u01b3\u01b4\7k\2\2\u01b4\u01b5\7p\2\2\u01b5")
        buf.write("\u01b6\7j\2\2\u01b6\u01b7\7g\2\2\u01b7\u01b8\7t\2\2\u01b8")
        buf.write("\u01b9\7k\2\2\u01b9\u01ba\7v\2\2\u01baF\3\2\2\2\u01bb")
        buf.write("\u01bc\7c\2\2\u01bc\u01bd\7t\2\2\u01bd\u01be\7t\2\2\u01be")
        buf.write("\u01bf\7c\2\2\u01bf\u01c0\7{\2\2\u01c0H\3\2\2\2\u01c1")
        buf.write("\u01c2\7-\2\2\u01c2J\3\2\2\2\u01c3\u01c4\7/\2\2\u01c4")
        buf.write("L\3\2\2\2\u01c5\u01c6\7,\2\2\u01c6N\3\2\2\2\u01c7\u01c8")
        buf.write("\7\61\2\2\u01c8P\3\2\2\2\u01c9\u01ca\7\'\2\2\u01caR\3")
        buf.write("\2\2\2\u01cb\u01cc\7#\2\2\u01ccT\3\2\2\2\u01cd\u01ce\7")
        buf.write("(\2\2\u01ce\u01cf\7(\2\2\u01cfV\3\2\2\2\u01d0\u01d1\7")
        buf.write("~\2\2\u01d1\u01d2\7~\2\2\u01d2X\3\2\2\2\u01d3\u01d4\7")
        buf.write("?\2\2\u01d4\u01d5\7?\2\2\u01d5Z\3\2\2\2\u01d6\u01d7\7")
        buf.write("#\2\2\u01d7\u01d8\7?\2\2\u01d8\\\3\2\2\2\u01d9\u01da\7")
        buf.write(">\2\2\u01da^\3\2\2\2\u01db\u01dc\7>\2\2\u01dc\u01dd\7")
        buf.write("?\2\2\u01dd`\3\2\2\2\u01de\u01df\7@\2\2\u01dfb\3\2\2\2")
        buf.write("\u01e0\u01e1\7@\2\2\u01e1\u01e2\7?\2\2\u01e2d\3\2\2\2")
        buf.write("\u01e3\u01e4\7<\2\2\u01e4\u01e5\7<\2\2\u01e5f\3\2\2\2")
        buf.write("\u01e6\u01ec\5S*\2\u01e7\u01ec\5U+\2\u01e8\u01ec\5W,\2")
        buf.write("\u01e9\u01ec\5Y-\2\u01ea\u01ec\5[.\2\u01eb\u01e6\3\2\2")
        buf.write("\2\u01eb\u01e7\3\2\2\2\u01eb\u01e8\3\2\2\2\u01eb\u01e9")
        buf.write("\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ech\3\2\2\2\u01ed\u01f9")
        buf.write("\5I%\2\u01ee\u01f9\5K&\2\u01ef\u01f9\5M\'\2\u01f0\u01f9")
        buf.write("\5O(\2\u01f1\u01f9\5Q)\2\u01f2\u01f9\5Y-\2\u01f3\u01f9")
        buf.write("\5[.\2\u01f4\u01f9\5]/\2\u01f5\u01f9\5_\60\2\u01f6\u01f9")
        buf.write("\5a\61\2\u01f7\u01f9\5c\62\2\u01f8\u01ed\3\2\2\2\u01f8")
        buf.write("\u01ee\3\2\2\2\u01f8\u01ef\3\2\2\2\u01f8\u01f0\3\2\2\2")
        buf.write("\u01f8\u01f1\3\2\2\2\u01f8\u01f2\3\2\2\2\u01f8\u01f3\3")
        buf.write("\2\2\2\u01f8\u01f4\3\2\2\2\u01f8\u01f5\3\2\2\2\u01f8\u01f6")
        buf.write("\3\2\2\2\u01f8\u01f7\3\2\2\2\u01f9j\3\2\2\2\u01fa\u0205")
        buf.write("\5I%\2\u01fb\u0205\5K&\2\u01fc\u0205\5M\'\2\u01fd\u0205")
        buf.write("\5O(\2\u01fe\u0205\5Y-\2\u01ff\u0205\5[.\2\u0200\u0205")
        buf.write("\5]/\2\u0201\u0205\5_\60\2\u0202\u0205\5a\61\2\u0203\u0205")
        buf.write("\5c\62\2\u0204\u01fa\3\2\2\2\u0204\u01fb\3\2\2\2\u0204")
        buf.write("\u01fc\3\2\2\2\u0204\u01fd\3\2\2\2\u0204\u01fe\3\2\2\2")
        buf.write("\u0204\u01ff\3\2\2\2\u0204\u0200\3\2\2\2\u0204\u0201\3")
        buf.write("\2\2\2\u0204\u0202\3\2\2\2\u0204\u0203\3\2\2\2\u0205l")
        buf.write("\3\2\2\2\u0206\u0207\5e\63\2\u0207n\3\2\2\2\u0208\u0209")
        buf.write("\7.\2\2\u0209p\3\2\2\2\u020a\u020b\7\60\2\2\u020br\3\2")
        buf.write("\2\2\u020c\u020d\7=\2\2\u020dt\3\2\2\2\u020e\u020f\7?")
        buf.write("\2\2\u020fv\3\2\2\2\u0210\u0211\7<\2\2\u0211x\3\2\2\2")
        buf.write("\u0212\u0213\7*\2\2\u0213z\3\2\2\2\u0214\u0215\7+\2\2")
        buf.write("\u0215|\3\2\2\2\u0216\u0217\7}\2\2\u0217~\3\2\2\2\u0218")
        buf.write("\u0219\7\177\2\2\u0219\u0080\3\2\2\2\u021a\u021b\7]\2")
        buf.write("\2\u021b\u0082\3\2\2\2\u021c\u021d\7_\2\2\u021d\u0084")
        buf.write("\3\2\2\2\u021e\u0233\7\62\2\2\u021f\u0223\t\3\2\2\u0220")
        buf.write("\u0222\t\4\2\2\u0221\u0220\3\2\2\2\u0222\u0225\3\2\2\2")
        buf.write("\u0223\u0221\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u022e\3")
        buf.write("\2\2\2\u0225\u0223\3\2\2\2\u0226\u0228\7a\2\2\u0227\u0229")
        buf.write("\t\4\2\2\u0228\u0227\3\2\2\2\u0229\u022a\3\2\2\2\u022a")
        buf.write("\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022d\3\2\2\2")
        buf.write("\u022c\u0226\3\2\2\2\u022d\u0230\3\2\2\2\u022e\u022c\3")
        buf.write("\2\2\2\u022e\u022f\3\2\2\2\u022f\u0231\3\2\2\2\u0230\u022e")
        buf.write("\3\2\2\2\u0231\u0233\bC\3\2\u0232\u021e\3\2\2\2\u0232")
        buf.write("\u021f\3\2\2\2\u0233\u0086\3\2\2\2\u0234\u0239\5\u0089")
        buf.write("E\2\u0235\u0237\5q9\2\u0236\u0238\5\u0089E\2\u0237\u0236")
        buf.write("\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u023a\3\2\2\2\u0239")
        buf.write("\u0235\3\2\2\2\u0239\u023a\3\2\2\2\u023a\u023b\3\2\2\2")
        buf.write("\u023b\u023c\5\u008bF\2\u023c\u023d\bD\4\2\u023d\u0246")
        buf.write("\3\2\2\2\u023e\u023f\5\u0089E\2\u023f\u0241\5q9\2\u0240")
        buf.write("\u0242\5\u0089E\2\u0241\u0240\3\2\2\2\u0241\u0242\3\2")
        buf.write("\2\2\u0242\u0243\3\2\2\2\u0243\u0244\bD\5\2\u0244\u0246")
        buf.write("\3\2\2\2\u0245\u0234\3\2\2\2\u0245\u023e\3\2\2\2\u0246")
        buf.write("\u0088\3\2\2\2\u0247\u0249\t\5\2\2\u0248\u0247\3\2\2\2")
        buf.write("\u0249\u024a\3\2\2\2\u024a\u0248\3\2\2\2\u024a\u024b\3")
        buf.write("\2\2\2\u024b\u008a\3\2\2\2\u024c\u024e\t\6\2\2\u024d\u024f")
        buf.write("\t\7\2\2\u024e\u024d\3\2\2\2\u024e\u024f\3\2\2\2\u024f")
        buf.write("\u0250\3\2\2\2\u0250\u0251\5\u0089E\2\u0251\u008c\3\2")
        buf.write("\2\2\u0252\u0257\7$\2\2\u0253\u0256\5\u008fH\2\u0254\u0256")
        buf.write("\n\b\2\2\u0255\u0253\3\2\2\2\u0255\u0254\3\2\2\2\u0256")
        buf.write("\u0259\3\2\2\2\u0257\u0255\3\2\2\2\u0257\u0258\3\2\2\2")
        buf.write("\u0258\u025a\3\2\2\2\u0259\u0257\3\2\2\2\u025a\u025b\7")
        buf.write("$\2\2\u025b\u025c\bG\6\2\u025c\u008e\3\2\2\2\u025d\u025e")
        buf.write("\7^\2\2\u025e\u025f\t\t\2\2\u025f\u0090\3\2\2\2\u0260")
        buf.write("\u0263\59\35\2\u0261\u0263\5)\25\2\u0262\u0260\3\2\2\2")
        buf.write("\u0262\u0261\3\2\2\2\u0263\u0092\3\2\2\2\u0264\u027a\5")
        buf.write("\37\20\2\u0265\u027a\5!\21\2\u0266\u027a\5#\22\2\u0267")
        buf.write("\u027a\5%\23\2\u0268\u027a\5\'\24\2\u0269\u027a\5)\25")
        buf.write("\2\u026a\u027a\5+\26\2\u026b\u027a\5-\27\2\u026c\u027a")
        buf.write("\5/\30\2\u026d\u027a\5\61\31\2\u026e\u027a\5\63\32\2\u026f")
        buf.write("\u027a\5\65\33\2\u0270\u027a\5\67\34\2\u0271\u027a\59")
        buf.write("\35\2\u0272\u027a\5;\36\2\u0273\u027a\5=\37\2\u0274\u027a")
        buf.write("\5? \2\u0275\u027a\5A!\2\u0276\u027a\5C\"\2\u0277\u027a")
        buf.write("\5E#\2\u0278\u027a\5G$\2\u0279\u0264\3\2\2\2\u0279\u0265")
        buf.write("\3\2\2\2\u0279\u0266\3\2\2\2\u0279\u0267\3\2\2\2\u0279")
        buf.write("\u0268\3\2\2\2\u0279\u0269\3\2\2\2\u0279\u026a\3\2\2\2")
        buf.write("\u0279\u026b\3\2\2\2\u0279\u026c\3\2\2\2\u0279\u026d\3")
        buf.write("\2\2\2\u0279\u026e\3\2\2\2\u0279\u026f\3\2\2\2\u0279\u0270")
        buf.write("\3\2\2\2\u0279\u0271\3\2\2\2\u0279\u0272\3\2\2\2\u0279")
        buf.write("\u0273\3\2\2\2\u0279\u0274\3\2\2\2\u0279\u0275\3\2\2\2")
        buf.write("\u0279\u0276\3\2\2\2\u0279\u0277\3\2\2\2\u0279\u0278\3")
        buf.write("\2\2\2\u027a\u0094\3\2\2\2\u027b\u027f\t\n\2\2\u027c\u027e")
        buf.write("\t\13\2\2\u027d\u027c\3\2\2\2\u027e\u0281\3\2\2\2\u027f")
        buf.write("\u027d\3\2\2\2\u027f\u0280\3\2\2\2\u0280\u0096\3\2\2\2")
        buf.write("\u0281\u027f\3\2\2\2\u0282\u0284\t\f\2\2\u0283\u0282\3")
        buf.write("\2\2\2\u0284\u0285\3\2\2\2\u0285\u0283\3\2\2\2\u0285\u0286")
        buf.write("\3\2\2\2\u0286\u0287\3\2\2\2\u0287\u0288\bL\2\2\u0288")
        buf.write("\u0098\3\2\2\2\u0289\u028a\13\2\2\2\u028a\u028b\bM\7\2")
        buf.write("\u028b\u009a\3\2\2\2\u028c\u028d\7$\2\2\u028d\u028e\b")
        buf.write("N\b\2\u028e\u009c\3\2\2\2\u028f\u0290\5\u009fP\2\u0290")
        buf.write("\u0291\bO\t\2\u0291\u009e\3\2\2\2\u0292\u0293\7^\2\2\u0293")
        buf.write("\u0296\n\t\2\2\u0294\u0296\n\r\2\2\u0295\u0292\3\2\2\2")
        buf.write("\u0295\u0294\3\2\2\2\u0296\u00a0\3\2\2\2\33\2\u0124\u0129")
        buf.write("\u0131\u013f\u01eb\u01f8\u0204\u0223\u022a\u022e\u0232")
        buf.write("\u0237\u0239\u0241\u0245\u024a\u024e\u0255\u0257\u0262")
        buf.write("\u0279\u027f\u0285\u0295\n\b\2\2\3C\2\3D\3\3D\4\3G\5\3")
        buf.write("M\6\3N\7\3O\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    OP_RELATIONAL = 11
    OP_MUL = 12
    BLOCK_COMMENT = 13
    LINE_COMMENT = 14
    AUTO = 15
    BREAK = 16
    BOOLEAN = 17
    DO = 18
    ELSE = 19
    FALSE = 20
    FLOAT = 21
    FOR = 22
    FUNCTION = 23
    IF = 24
    INTEGER = 25
    RETURN = 26
    STRING = 27
    TRUE = 28
    WHILE = 29
    VOID = 30
    OUT = 31
    CONTINUE = 32
    OF = 33
    INHERIT = 34
    ARRAY = 35
    ADD = 36
    SUB = 37
    MUL = 38
    DIV = 39
    MOD = 40
    NOT = 41
    AND = 42
    OR = 43
    EQUAL = 44
    DIFF = 45
    SMALLER = 46
    SMALLER_OR_EQUAL = 47
    GREATER = 48
    GREATER_OR_EQUAL = 49
    CONCAT = 50
    OP_BOOL = 51
    OP_INT = 52
    OP_FLOAT = 53
    OP_STRING = 54
    COMMA = 55
    DOT = 56
    SEMI = 57
    ASSIGN = 58
    COLON = 59
    LB = 60
    RB = 61
    LP = 62
    RP = 63
    LS = 64
    RS = 65
    INTLIT = 66
    FLOATLIT = 67
    STRINGLIT = 68
    BOOLLIT = 69
    KEYWORD = 70
    ID = 71
    WS = 72
    ERROR_CHAR = 73
    UNCLOSE_STRING = 74
    ILLEGAL_ESCAPE = 75

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger()'", "'printInteger'", "'readFloat()'", "'printFloat'", 
            "'readBoolean()'", "'printBoolean'", "'readString()'", "'printString'", 
            "'super'", "'preventDefault()'", "'auto'", "'break'", "'boolean'", 
            "'do'", "'else'", "'false'", "'float'", "'for'", "'function'", 
            "'if'", "'integer'", "'return'", "'string'", "'true'", "'while'", 
            "'void'", "'out'", "'continue'", "'of'", "'inherit'", "'array'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "','", "'.'", 
            "';'", "'='", "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "OP_RELATIONAL", "OP_MUL", "BLOCK_COMMENT", "LINE_COMMENT", 
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
            "DIFF", "SMALLER", "SMALLER_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
            "CONCAT", "OP_BOOL", "OP_INT", "OP_FLOAT", "OP_STRING", "COMMA", 
            "DOT", "SEMI", "ASSIGN", "COLON", "LB", "RB", "LP", "RP", "LS", 
            "RS", "INTLIT", "FLOATLIT", "STRINGLIT", "BOOLLIT", "KEYWORD", 
            "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "OP_RELATIONAL", "OP_MUL", "BLOCK_COMMENT", 
                  "LINE_COMMENT", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
                  "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                  "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
                  "OF", "INHERIT", "ARRAY", "ADD", "SUB", "MUL", "DIV", 
                  "MOD", "NOT", "AND", "OR", "EQUAL", "DIFF", "SMALLER", 
                  "SMALLER_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", "CONCAT", 
                  "OP_BOOL", "OP_INT", "OP_FLOAT", "OP_STRING", "COMMA", 
                  "DOT", "SEMI", "ASSIGN", "COLON", "LB", "RB", "LP", "RP", 
                  "LS", "RS", "INTLIT", "FLOATLIT", "DIGIT_UNDERSCORE", 
                  "SCIENTIFIC", "STRINGLIT", "EscapeSequence", "BOOLLIT", 
                  "KEYWORD", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ESC_ILLEGAL" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[65] = self.INTLIT_action 
            actions[66] = self.FLOATLIT_action 
            actions[69] = self.STRINGLIT_action 
            actions[75] = self.ERROR_CHAR_action 
            actions[76] = self.UNCLOSE_STRING_action 
            actions[77] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_', '')
     

        if actionIndex == 2:
            self.text = self.text.replace('_', '')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise IllegalEscape(self.text)
     

