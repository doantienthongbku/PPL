# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2K")
        buf.write("\u028b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u011b\n\f")
        buf.write("\3\r\3\r\3\r\5\r\u0120\n\r\3\16\3\16\3\16\3\16\7\16\u0126")
        buf.write("\n\16\f\16\16\16\u0129\13\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\7\17\u0134\n\17\f\17\16\17\u0137")
        buf.write("\13\17\3\17\7\17\u013a\n\17\f\17\16\17\u013d\13\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("$\3$\3$\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3")
        buf.write("*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\5\64\u01e6\n\64\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u01f3\n\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u01ff")
        buf.write("\n\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3")
        buf.write(">\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3C\7C\u021c\nC\fC\16")
        buf.write("C\u021f\13C\3C\3C\6C\u0223\nC\rC\16C\u0224\7C\u0227\n")
        buf.write("C\fC\16C\u022a\13C\3C\5C\u022d\nC\3D\3D\3D\5D\u0232\n")
        buf.write("D\5D\u0234\nD\3D\3D\3D\3D\3D\3D\5D\u023c\nD\3D\3D\5D\u0240")
        buf.write("\nD\3E\3E\5E\u0244\nE\3E\3E\3F\6F\u0249\nF\rF\16F\u024a")
        buf.write("\3G\3G\7G\u024f\nG\fG\16G\u0252\13G\3G\3G\3G\3H\3H\5H")
        buf.write("\u0259\nH\3I\3I\3I\3J\3J\3J\5J\u0261\nJ\3K\3K\3L\3L\7")
        buf.write("L\u0267\nL\fL\16L\u026a\13L\3M\6M\u026d\nM\rM\16M\u026e")
        buf.write("\3M\3M\3N\3N\3N\3O\3O\7O\u0278\nO\fO\16O\u027b\13O\3O")
        buf.write("\5O\u027e\nO\3O\3O\3P\3P\7P\u0284\nP\fP\16P\u0287\13P")
        buf.write("\3P\3P\3P\4\u0127\u0135\2Q\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C")
        buf.write("\u0085D\u0087E\u0089\2\u008b\2\u008dF\u008f\2\u0091\2")
        buf.write("\u0093\2\u0095\2\u0097G\u0099H\u009bI\u009dJ\u009fK\3")
        buf.write("\2\r\4\2\f\f\17\17\3\2\63;\3\2\62;\4\2GGgg\4\2--//\6\2")
        buf.write("\f\f\16\17$$^^\n\2$$))^^ddhhppttvv\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\5\2\n\f\16\17\"\"\6\3\f\f\16\17$$^^\2\u02b6\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\3\u00a1\3\2\2\2\5\u00ad\3\2\2")
        buf.write("\2\7\u00ba\3\2\2\2\t\u00c4\3\2\2\2\13\u00cf\3\2\2\2\r")
        buf.write("\u00db\3\2\2\2\17\u00e8\3\2\2\2\21\u00f3\3\2\2\2\23\u00ff")
        buf.write("\3\2\2\2\25\u0105\3\2\2\2\27\u011a\3\2\2\2\31\u011f\3")
        buf.write("\2\2\2\33\u0121\3\2\2\2\35\u012f\3\2\2\2\37\u0140\3\2")
        buf.write("\2\2!\u0145\3\2\2\2#\u014b\3\2\2\2%\u0153\3\2\2\2\'\u0156")
        buf.write("\3\2\2\2)\u015b\3\2\2\2+\u0161\3\2\2\2-\u0167\3\2\2\2")
        buf.write("/\u016b\3\2\2\2\61\u0174\3\2\2\2\63\u0177\3\2\2\2\65\u017f")
        buf.write("\3\2\2\2\67\u0186\3\2\2\29\u018d\3\2\2\2;\u0192\3\2\2")
        buf.write("\2=\u0198\3\2\2\2?\u019d\3\2\2\2A\u01a1\3\2\2\2C\u01aa")
        buf.write("\3\2\2\2E\u01ad\3\2\2\2G\u01b5\3\2\2\2I\u01bb\3\2\2\2")
        buf.write("K\u01bd\3\2\2\2M\u01bf\3\2\2\2O\u01c1\3\2\2\2Q\u01c3\3")
        buf.write("\2\2\2S\u01c5\3\2\2\2U\u01c7\3\2\2\2W\u01ca\3\2\2\2Y\u01cd")
        buf.write("\3\2\2\2[\u01d0\3\2\2\2]\u01d3\3\2\2\2_\u01d5\3\2\2\2")
        buf.write("a\u01d8\3\2\2\2c\u01da\3\2\2\2e\u01dd\3\2\2\2g\u01e5\3")
        buf.write("\2\2\2i\u01f2\3\2\2\2k\u01fe\3\2\2\2m\u0200\3\2\2\2o\u0202")
        buf.write("\3\2\2\2q\u0204\3\2\2\2s\u0206\3\2\2\2u\u0208\3\2\2\2")
        buf.write("w\u020a\3\2\2\2y\u020c\3\2\2\2{\u020e\3\2\2\2}\u0210\3")
        buf.write("\2\2\2\177\u0212\3\2\2\2\u0081\u0214\3\2\2\2\u0083\u0216")
        buf.write("\3\2\2\2\u0085\u022c\3\2\2\2\u0087\u023f\3\2\2\2\u0089")
        buf.write("\u0241\3\2\2\2\u008b\u0248\3\2\2\2\u008d\u024c\3\2\2\2")
        buf.write("\u008f\u0258\3\2\2\2\u0091\u025a\3\2\2\2\u0093\u0260\3")
        buf.write("\2\2\2\u0095\u0262\3\2\2\2\u0097\u0264\3\2\2\2\u0099\u026c")
        buf.write("\3\2\2\2\u009b\u0272\3\2\2\2\u009d\u0275\3\2\2\2\u009f")
        buf.write("\u0281\3\2\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3\7g\2\2\u00a3")
        buf.write("\u00a4\7c\2\2\u00a4\u00a5\7f\2\2\u00a5\u00a6\7K\2\2\u00a6")
        buf.write("\u00a7\7p\2\2\u00a7\u00a8\7v\2\2\u00a8\u00a9\7g\2\2\u00a9")
        buf.write("\u00aa\7i\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7t\2\2\u00ac")
        buf.write("\4\3\2\2\2\u00ad\u00ae\7r\2\2\u00ae\u00af\7t\2\2\u00af")
        buf.write("\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2\7v\2\2\u00b2")
        buf.write("\u00b3\7K\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5\7v\2\2\u00b5")
        buf.write("\u00b6\7g\2\2\u00b6\u00b7\7i\2\2\u00b7\u00b8\7g\2\2\u00b8")
        buf.write("\u00b9\7t\2\2\u00b9\6\3\2\2\2\u00ba\u00bb\7t\2\2\u00bb")
        buf.write("\u00bc\7g\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be\7f\2\2\u00be")
        buf.write("\u00bf\7H\2\2\u00bf\u00c0\7n\2\2\u00c0\u00c1\7q\2\2\u00c1")
        buf.write("\u00c2\7c\2\2\u00c2\u00c3\7v\2\2\u00c3\b\3\2\2\2\u00c4")
        buf.write("\u00c5\7r\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7k\2\2\u00c7")
        buf.write("\u00c8\7p\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca\7H\2\2\u00ca")
        buf.write("\u00cb\7n\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd\7c\2\2\u00cd")
        buf.write("\u00ce\7v\2\2\u00ce\n\3\2\2\2\u00cf\u00d0\7t\2\2\u00d0")
        buf.write("\u00d1\7g\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3\7f\2\2\u00d3")
        buf.write("\u00d4\7D\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7q\2\2\u00d6")
        buf.write("\u00d7\7n\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9\7c\2\2\u00d9")
        buf.write("\u00da\7p\2\2\u00da\f\3\2\2\2\u00db\u00dc\7r\2\2\u00dc")
        buf.write("\u00dd\7t\2\2\u00dd\u00de\7k\2\2\u00de\u00df\7p\2\2\u00df")
        buf.write("\u00e0\7v\2\2\u00e0\u00e1\7D\2\2\u00e1\u00e2\7q\2\2\u00e2")
        buf.write("\u00e3\7q\2\2\u00e3\u00e4\7n\2\2\u00e4\u00e5\7g\2\2\u00e5")
        buf.write("\u00e6\7c\2\2\u00e6\u00e7\7p\2\2\u00e7\16\3\2\2\2\u00e8")
        buf.write("\u00e9\7t\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb\7c\2\2\u00eb")
        buf.write("\u00ec\7f\2\2\u00ec\u00ed\7U\2\2\u00ed\u00ee\7v\2\2\u00ee")
        buf.write("\u00ef\7t\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7p\2\2\u00f1")
        buf.write("\u00f2\7i\2\2\u00f2\20\3\2\2\2\u00f3\u00f4\7r\2\2\u00f4")
        buf.write("\u00f5\7t\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7\7p\2\2\u00f7")
        buf.write("\u00f8\7v\2\2\u00f8\u00f9\7U\2\2\u00f9\u00fa\7v\2\2\u00fa")
        buf.write("\u00fb\7t\2\2\u00fb\u00fc\7k\2\2\u00fc\u00fd\7p\2\2\u00fd")
        buf.write("\u00fe\7i\2\2\u00fe\22\3\2\2\2\u00ff\u0100\7u\2\2\u0100")
        buf.write("\u0101\7w\2\2\u0101\u0102\7r\2\2\u0102\u0103\7g\2\2\u0103")
        buf.write("\u0104\7t\2\2\u0104\24\3\2\2\2\u0105\u0106\7r\2\2\u0106")
        buf.write("\u0107\7t\2\2\u0107\u0108\7g\2\2\u0108\u0109\7x\2\2\u0109")
        buf.write("\u010a\7g\2\2\u010a\u010b\7p\2\2\u010b\u010c\7v\2\2\u010c")
        buf.write("\u010d\7F\2\2\u010d\u010e\7g\2\2\u010e\u010f\7h\2\2\u010f")
        buf.write("\u0110\7c\2\2\u0110\u0111\7w\2\2\u0111\u0112\7n\2\2\u0112")
        buf.write("\u0113\7v\2\2\u0113\26\3\2\2\2\u0114\u011b\5]/\2\u0115")
        buf.write("\u011b\5_\60\2\u0116\u011b\5a\61\2\u0117\u011b\5c\62\2")
        buf.write("\u0118\u011b\5Y-\2\u0119\u011b\5[.\2\u011a\u0114\3\2\2")
        buf.write("\2\u011a\u0115\3\2\2\2\u011a\u0116\3\2\2\2\u011a\u0117")
        buf.write("\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u0119\3\2\2\2\u011b")
        buf.write("\30\3\2\2\2\u011c\u0120\5M\'\2\u011d\u0120\5O(\2\u011e")
        buf.write("\u0120\5Q)\2\u011f\u011c\3\2\2\2\u011f\u011d\3\2\2\2\u011f")
        buf.write("\u011e\3\2\2\2\u0120\32\3\2\2\2\u0121\u0122\7\61\2\2\u0122")
        buf.write("\u0123\7,\2\2\u0123\u0127\3\2\2\2\u0124\u0126\13\2\2\2")
        buf.write("\u0125\u0124\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0128\3")
        buf.write("\2\2\2\u0127\u0125\3\2\2\2\u0128\u012a\3\2\2\2\u0129\u0127")
        buf.write("\3\2\2\2\u012a\u012b\7,\2\2\u012b\u012c\7\61\2\2\u012c")
        buf.write("\u012d\3\2\2\2\u012d\u012e\b\16\2\2\u012e\34\3\2\2\2\u012f")
        buf.write("\u0130\7\61\2\2\u0130\u0131\7\61\2\2\u0131\u0135\3\2\2")
        buf.write("\2\u0132\u0134\13\2\2\2\u0133\u0132\3\2\2\2\u0134\u0137")
        buf.write("\3\2\2\2\u0135\u0136\3\2\2\2\u0135\u0133\3\2\2\2\u0136")
        buf.write("\u013b\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u013a\n\2\2\2")
        buf.write("\u0139\u0138\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3")
        buf.write("\2\2\2\u013b\u013c\3\2\2\2\u013c\u013e\3\2\2\2\u013d\u013b")
        buf.write("\3\2\2\2\u013e\u013f\b\17\2\2\u013f\36\3\2\2\2\u0140\u0141")
        buf.write("\7c\2\2\u0141\u0142\7w\2\2\u0142\u0143\7v\2\2\u0143\u0144")
        buf.write("\7q\2\2\u0144 \3\2\2\2\u0145\u0146\7d\2\2\u0146\u0147")
        buf.write("\7t\2\2\u0147\u0148\7g\2\2\u0148\u0149\7c\2\2\u0149\u014a")
        buf.write("\7m\2\2\u014a\"\3\2\2\2\u014b\u014c\7d\2\2\u014c\u014d")
        buf.write("\7q\2\2\u014d\u014e\7q\2\2\u014e\u014f\7n\2\2\u014f\u0150")
        buf.write("\7g\2\2\u0150\u0151\7c\2\2\u0151\u0152\7p\2\2\u0152$\3")
        buf.write("\2\2\2\u0153\u0154\7f\2\2\u0154\u0155\7q\2\2\u0155&\3")
        buf.write("\2\2\2\u0156\u0157\7g\2\2\u0157\u0158\7n\2\2\u0158\u0159")
        buf.write("\7u\2\2\u0159\u015a\7g\2\2\u015a(\3\2\2\2\u015b\u015c")
        buf.write("\7h\2\2\u015c\u015d\7c\2\2\u015d\u015e\7n\2\2\u015e\u015f")
        buf.write("\7u\2\2\u015f\u0160\7g\2\2\u0160*\3\2\2\2\u0161\u0162")
        buf.write("\7h\2\2\u0162\u0163\7n\2\2\u0163\u0164\7q\2\2\u0164\u0165")
        buf.write("\7c\2\2\u0165\u0166\7v\2\2\u0166,\3\2\2\2\u0167\u0168")
        buf.write("\7h\2\2\u0168\u0169\7q\2\2\u0169\u016a\7t\2\2\u016a.\3")
        buf.write("\2\2\2\u016b\u016c\7h\2\2\u016c\u016d\7w\2\2\u016d\u016e")
        buf.write("\7p\2\2\u016e\u016f\7e\2\2\u016f\u0170\7v\2\2\u0170\u0171")
        buf.write("\7k\2\2\u0171\u0172\7q\2\2\u0172\u0173\7p\2\2\u0173\60")
        buf.write("\3\2\2\2\u0174\u0175\7k\2\2\u0175\u0176\7h\2\2\u0176\62")
        buf.write("\3\2\2\2\u0177\u0178\7k\2\2\u0178\u0179\7p\2\2\u0179\u017a")
        buf.write("\7v\2\2\u017a\u017b\7g\2\2\u017b\u017c\7i\2\2\u017c\u017d")
        buf.write("\7g\2\2\u017d\u017e\7t\2\2\u017e\64\3\2\2\2\u017f\u0180")
        buf.write("\7t\2\2\u0180\u0181\7g\2\2\u0181\u0182\7v\2\2\u0182\u0183")
        buf.write("\7w\2\2\u0183\u0184\7t\2\2\u0184\u0185\7p\2\2\u0185\66")
        buf.write("\3\2\2\2\u0186\u0187\7u\2\2\u0187\u0188\7v\2\2\u0188\u0189")
        buf.write("\7t\2\2\u0189\u018a\7k\2\2\u018a\u018b\7p\2\2\u018b\u018c")
        buf.write("\7i\2\2\u018c8\3\2\2\2\u018d\u018e\7v\2\2\u018e\u018f")
        buf.write("\7t\2\2\u018f\u0190\7w\2\2\u0190\u0191\7g\2\2\u0191:\3")
        buf.write("\2\2\2\u0192\u0193\7y\2\2\u0193\u0194\7j\2\2\u0194\u0195")
        buf.write("\7k\2\2\u0195\u0196\7n\2\2\u0196\u0197\7g\2\2\u0197<\3")
        buf.write("\2\2\2\u0198\u0199\7x\2\2\u0199\u019a\7q\2\2\u019a\u019b")
        buf.write("\7k\2\2\u019b\u019c\7f\2\2\u019c>\3\2\2\2\u019d\u019e")
        buf.write("\7q\2\2\u019e\u019f\7w\2\2\u019f\u01a0\7v\2\2\u01a0@\3")
        buf.write("\2\2\2\u01a1\u01a2\7e\2\2\u01a2\u01a3\7q\2\2\u01a3\u01a4")
        buf.write("\7p\2\2\u01a4\u01a5\7v\2\2\u01a5\u01a6\7k\2\2\u01a6\u01a7")
        buf.write("\7p\2\2\u01a7\u01a8\7w\2\2\u01a8\u01a9\7g\2\2\u01a9B\3")
        buf.write("\2\2\2\u01aa\u01ab\7q\2\2\u01ab\u01ac\7h\2\2\u01acD\3")
        buf.write("\2\2\2\u01ad\u01ae\7k\2\2\u01ae\u01af\7p\2\2\u01af\u01b0")
        buf.write("\7j\2\2\u01b0\u01b1\7g\2\2\u01b1\u01b2\7t\2\2\u01b2\u01b3")
        buf.write("\7k\2\2\u01b3\u01b4\7v\2\2\u01b4F\3\2\2\2\u01b5\u01b6")
        buf.write("\7c\2\2\u01b6\u01b7\7t\2\2\u01b7\u01b8\7t\2\2\u01b8\u01b9")
        buf.write("\7c\2\2\u01b9\u01ba\7{\2\2\u01baH\3\2\2\2\u01bb\u01bc")
        buf.write("\7-\2\2\u01bcJ\3\2\2\2\u01bd\u01be\7/\2\2\u01beL\3\2\2")
        buf.write("\2\u01bf\u01c0\7,\2\2\u01c0N\3\2\2\2\u01c1\u01c2\7\61")
        buf.write("\2\2\u01c2P\3\2\2\2\u01c3\u01c4\7\'\2\2\u01c4R\3\2\2\2")
        buf.write("\u01c5\u01c6\7#\2\2\u01c6T\3\2\2\2\u01c7\u01c8\7(\2\2")
        buf.write("\u01c8\u01c9\7(\2\2\u01c9V\3\2\2\2\u01ca\u01cb\7~\2\2")
        buf.write("\u01cb\u01cc\7~\2\2\u01ccX\3\2\2\2\u01cd\u01ce\7?\2\2")
        buf.write("\u01ce\u01cf\7?\2\2\u01cfZ\3\2\2\2\u01d0\u01d1\7#\2\2")
        buf.write("\u01d1\u01d2\7?\2\2\u01d2\\\3\2\2\2\u01d3\u01d4\7>\2\2")
        buf.write("\u01d4^\3\2\2\2\u01d5\u01d6\7>\2\2\u01d6\u01d7\7?\2\2")
        buf.write("\u01d7`\3\2\2\2\u01d8\u01d9\7@\2\2\u01d9b\3\2\2\2\u01da")
        buf.write("\u01db\7@\2\2\u01db\u01dc\7?\2\2\u01dcd\3\2\2\2\u01dd")
        buf.write("\u01de\7<\2\2\u01de\u01df\7<\2\2\u01dff\3\2\2\2\u01e0")
        buf.write("\u01e6\5S*\2\u01e1\u01e6\5U+\2\u01e2\u01e6\5W,\2\u01e3")
        buf.write("\u01e6\5Y-\2\u01e4\u01e6\5[.\2\u01e5\u01e0\3\2\2\2\u01e5")
        buf.write("\u01e1\3\2\2\2\u01e5\u01e2\3\2\2\2\u01e5\u01e3\3\2\2\2")
        buf.write("\u01e5\u01e4\3\2\2\2\u01e6h\3\2\2\2\u01e7\u01f3\5I%\2")
        buf.write("\u01e8\u01f3\5K&\2\u01e9\u01f3\5M\'\2\u01ea\u01f3\5O(")
        buf.write("\2\u01eb\u01f3\5Q)\2\u01ec\u01f3\5Y-\2\u01ed\u01f3\5[")
        buf.write(".\2\u01ee\u01f3\5]/\2\u01ef\u01f3\5_\60\2\u01f0\u01f3")
        buf.write("\5a\61\2\u01f1\u01f3\5c\62\2\u01f2\u01e7\3\2\2\2\u01f2")
        buf.write("\u01e8\3\2\2\2\u01f2\u01e9\3\2\2\2\u01f2\u01ea\3\2\2\2")
        buf.write("\u01f2\u01eb\3\2\2\2\u01f2\u01ec\3\2\2\2\u01f2\u01ed\3")
        buf.write("\2\2\2\u01f2\u01ee\3\2\2\2\u01f2\u01ef\3\2\2\2\u01f2\u01f0")
        buf.write("\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3j\3\2\2\2\u01f4\u01ff")
        buf.write("\5I%\2\u01f5\u01ff\5K&\2\u01f6\u01ff\5M\'\2\u01f7\u01ff")
        buf.write("\5O(\2\u01f8\u01ff\5Y-\2\u01f9\u01ff\5[.\2\u01fa\u01ff")
        buf.write("\5]/\2\u01fb\u01ff\5_\60\2\u01fc\u01ff\5a\61\2\u01fd\u01ff")
        buf.write("\5c\62\2\u01fe\u01f4\3\2\2\2\u01fe\u01f5\3\2\2\2\u01fe")
        buf.write("\u01f6\3\2\2\2\u01fe\u01f7\3\2\2\2\u01fe\u01f8\3\2\2\2")
        buf.write("\u01fe\u01f9\3\2\2\2\u01fe\u01fa\3\2\2\2\u01fe\u01fb\3")
        buf.write("\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01fd\3\2\2\2\u01ffl")
        buf.write("\3\2\2\2\u0200\u0201\5e\63\2\u0201n\3\2\2\2\u0202\u0203")
        buf.write("\7.\2\2\u0203p\3\2\2\2\u0204\u0205\7\60\2\2\u0205r\3\2")
        buf.write("\2\2\u0206\u0207\7=\2\2\u0207t\3\2\2\2\u0208\u0209\7?")
        buf.write("\2\2\u0209v\3\2\2\2\u020a\u020b\7<\2\2\u020bx\3\2\2\2")
        buf.write("\u020c\u020d\7*\2\2\u020dz\3\2\2\2\u020e\u020f\7+\2\2")
        buf.write("\u020f|\3\2\2\2\u0210\u0211\7}\2\2\u0211~\3\2\2\2\u0212")
        buf.write("\u0213\7\177\2\2\u0213\u0080\3\2\2\2\u0214\u0215\7]\2")
        buf.write("\2\u0215\u0082\3\2\2\2\u0216\u0217\7_\2\2\u0217\u0084")
        buf.write("\3\2\2\2\u0218\u022d\7\62\2\2\u0219\u021d\t\3\2\2\u021a")
        buf.write("\u021c\t\4\2\2\u021b\u021a\3\2\2\2\u021c\u021f\3\2\2\2")
        buf.write("\u021d\u021b\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u0228\3")
        buf.write("\2\2\2\u021f\u021d\3\2\2\2\u0220\u0222\7a\2\2\u0221\u0223")
        buf.write("\t\4\2\2\u0222\u0221\3\2\2\2\u0223\u0224\3\2\2\2\u0224")
        buf.write("\u0222\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u0227\3\2\2\2")
        buf.write("\u0226\u0220\3\2\2\2\u0227\u022a\3\2\2\2\u0228\u0226\3")
        buf.write("\2\2\2\u0228\u0229\3\2\2\2\u0229\u022b\3\2\2\2\u022a\u0228")
        buf.write("\3\2\2\2\u022b\u022d\bC\3\2\u022c\u0218\3\2\2\2\u022c")
        buf.write("\u0219\3\2\2\2\u022d\u0086\3\2\2\2\u022e\u0233\5\u0085")
        buf.write("C\2\u022f\u0231\5q9\2\u0230\u0232\5\u0085C\2\u0231\u0230")
        buf.write("\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0234\3\2\2\2\u0233")
        buf.write("\u022f\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0235\3\2\2\2")
        buf.write("\u0235\u0236\5\u0089E\2\u0236\u0237\bD\4\2\u0237\u0240")
        buf.write("\3\2\2\2\u0238\u0239\5\u0085C\2\u0239\u023b\5q9\2\u023a")
        buf.write("\u023c\5\u0085C\2\u023b\u023a\3\2\2\2\u023b\u023c\3\2")
        buf.write("\2\2\u023c\u023d\3\2\2\2\u023d\u023e\bD\5\2\u023e\u0240")
        buf.write("\3\2\2\2\u023f\u022e\3\2\2\2\u023f\u0238\3\2\2\2\u0240")
        buf.write("\u0088\3\2\2\2\u0241\u0243\t\5\2\2\u0242\u0244\t\6\2\2")
        buf.write("\u0243\u0242\3\2\2\2\u0243\u0244\3\2\2\2\u0244\u0245\3")
        buf.write("\2\2\2\u0245\u0246\5\u008bF\2\u0246\u008a\3\2\2\2\u0247")
        buf.write("\u0249\t\4\2\2\u0248\u0247\3\2\2\2\u0249\u024a\3\2\2\2")
        buf.write("\u024a\u0248\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u008c\3")
        buf.write("\2\2\2\u024c\u0250\5\u0095K\2\u024d\u024f\5\u008fH\2\u024e")
        buf.write("\u024d\3\2\2\2\u024f\u0252\3\2\2\2\u0250\u024e\3\2\2\2")
        buf.write("\u0250\u0251\3\2\2\2\u0251\u0253\3\2\2\2\u0252\u0250\3")
        buf.write("\2\2\2\u0253\u0254\5\u0095K\2\u0254\u0255\bG\6\2\u0255")
        buf.write("\u008e\3\2\2\2\u0256\u0259\n\7\2\2\u0257\u0259\5\u0091")
        buf.write("I\2\u0258\u0256\3\2\2\2\u0258\u0257\3\2\2\2\u0259\u0090")
        buf.write("\3\2\2\2\u025a\u025b\7^\2\2\u025b\u025c\t\b\2\2\u025c")
        buf.write("\u0092\3\2\2\2\u025d\u025e\7^\2\2\u025e\u0261\n\b\2\2")
        buf.write("\u025f\u0261\7^\2\2\u0260\u025d\3\2\2\2\u0260\u025f\3")
        buf.write("\2\2\2\u0261\u0094\3\2\2\2\u0262\u0263\7$\2\2\u0263\u0096")
        buf.write("\3\2\2\2\u0264\u0268\t\t\2\2\u0265\u0267\t\n\2\2\u0266")
        buf.write("\u0265\3\2\2\2\u0267\u026a\3\2\2\2\u0268\u0266\3\2\2\2")
        buf.write("\u0268\u0269\3\2\2\2\u0269\u0098\3\2\2\2\u026a\u0268\3")
        buf.write("\2\2\2\u026b\u026d\t\13\2\2\u026c\u026b\3\2\2\2\u026d")
        buf.write("\u026e\3\2\2\2\u026e\u026c\3\2\2\2\u026e\u026f\3\2\2\2")
        buf.write("\u026f\u0270\3\2\2\2\u0270\u0271\bM\2\2\u0271\u009a\3")
        buf.write("\2\2\2\u0272\u0273\13\2\2\2\u0273\u0274\bN\7\2\u0274\u009c")
        buf.write("\3\2\2\2\u0275\u0279\5\u0095K\2\u0276\u0278\5\u008fH\2")
        buf.write("\u0277\u0276\3\2\2\2\u0278\u027b\3\2\2\2\u0279\u0277\3")
        buf.write("\2\2\2\u0279\u027a\3\2\2\2\u027a\u027d\3\2\2\2\u027b\u0279")
        buf.write("\3\2\2\2\u027c\u027e\t\f\2\2\u027d\u027c\3\2\2\2\u027e")
        buf.write("\u027f\3\2\2\2\u027f\u0280\bO\b\2\u0280\u009e\3\2\2\2")
        buf.write("\u0281\u0285\5\u0095K\2\u0282\u0284\5\u008fH\2\u0283\u0282")
        buf.write("\3\2\2\2\u0284\u0287\3\2\2\2\u0285\u0283\3\2\2\2\u0285")
        buf.write("\u0286\3\2\2\2\u0286\u0288\3\2\2\2\u0287\u0285\3\2\2\2")
        buf.write("\u0288\u0289\5\u0093J\2\u0289\u028a\bP\t\2\u028a\u00a0")
        buf.write("\3\2\2\2\35\2\u011a\u011f\u0127\u0135\u013b\u01e5\u01f2")
        buf.write("\u01fe\u021d\u0224\u0228\u022c\u0231\u0233\u023b\u023f")
        buf.write("\u0243\u024a\u0250\u0258\u0260\u0268\u026e\u0279\u027d")
        buf.write("\u0285\n\b\2\2\3C\2\3D\3\3D\4\3G\5\3N\6\3O\7\3P\b")
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
    ID = 69
    WS = 70
    ERROR_CHAR = 71
    UNCLOSE_STRING = 72
    ILLEGAL_ESCAPE = 73

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger'", "'printInteger'", "'readFloat'", "'printFloat'", 
            "'readBoolean'", "'printBoolean'", "'readString'", "'printString'", 
            "'super'", "'preventDefault'", "'auto'", "'break'", "'boolean'", 
            "'do'", "'else'", "'false'", "'float'", "'for'", "'function'", 
            "'if'", "'integer'", "'return'", "'string'", "'true'", "'while'", 
            "'void'", "'out'", "'continue'", "'of'", "'inherit'", "'array'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "','", "'.'", 
            "';'", "'='", "':'", "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "OP_RELATIONAL", "OP_MUL", "BLOCK_COMMENT", "LINE_COMMENT", 
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
            "DIFF", "SMALLER", "SMALLER_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
            "CONCAT", "OP_BOOL", "OP_INT", "OP_FLOAT", "OP_STRING", "COMMA", 
            "DOT", "SEMI", "ASSIGN", "COLON", "LB", "RB", "LP", "RP", "LS", 
            "RS", "INTLIT", "FLOATLIT", "STRINGLIT", "ID", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
                  "LS", "RS", "INTLIT", "FLOATLIT", "SCIENTIFIC", "DIGIT", 
                  "STRINGLIT", "StringChar", "EscapeSequence", "IllegalString", 
                  "DoubleQuote", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[76] = self.ERROR_CHAR_action 
            actions[77] = self.UNCLOSE_STRING_action 
            actions[78] = self.ILLEGAL_ESCAPE_action 
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
             
            	result = str(self.text)
            	self.text = self.text[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
             raise ErrorToken(self.text) 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	unclose_str = str(self.text)
            	possible = ['\f', '\n', '\r', '"', '\\']
            	if unclose_str[-1] in possible:
            		raise UncloseString(unclose_str[1:-1])
            	else:
            		raise UncloseString(unclose_str[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            	illegal_str = str(self.text)
            	raise IllegalEscape(illegal_str[1:]) 

     


