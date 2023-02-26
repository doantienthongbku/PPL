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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2K")
        buf.write("\u028a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\5\f\u0123\n\f\3\r\3\r\3\r\5\r\u0128")
        buf.write("\n\r\3\16\3\16\3\16\3\16\7\16\u012e\n\16\f\16\16\16\u0131")
        buf.write("\13\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\7")
        buf.write("\17\u013c\n\17\f\17\16\17\u013f\13\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
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
        buf.write("\3\64\3\64\3\64\5\64\u01ea\n\64\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u01f7\n\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u0203")
        buf.write("\n\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3")
        buf.write(">\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3C\7C\u0220\nC\fC\16")
        buf.write("C\u0223\13C\3C\3C\6C\u0227\nC\rC\16C\u0228\7C\u022b\n")
        buf.write("C\fC\16C\u022e\13C\3C\5C\u0231\nC\3D\3D\3D\5D\u0236\n")
        buf.write("D\5D\u0238\nD\3D\3D\3D\3D\3D\3D\5D\u0240\nD\3D\3D\5D\u0244")
        buf.write("\nD\3E\3E\5E\u0248\nE\3E\3E\3F\3F\7F\u024e\nF\fF\16F\u0251")
        buf.write("\13F\3F\3F\3F\3G\3G\5G\u0258\nG\3H\3H\3H\3I\3I\3I\5I\u0260")
        buf.write("\nI\3J\3J\3K\3K\7K\u0266\nK\fK\16K\u0269\13K\3L\6L\u026c")
        buf.write("\nL\rL\16L\u026d\3L\3L\3M\3M\3M\3N\3N\7N\u0277\nN\fN\16")
        buf.write("N\u027a\13N\3N\5N\u027d\nN\3N\3N\3O\3O\7O\u0283\nO\fO")
        buf.write("\16O\u0286\13O\3O\3O\3O\4\u012f\u013d\2P\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089\2\u008bF\u008d\2\u008f\2")
        buf.write("\u0091\2\u0093\2\u0095G\u0097H\u0099I\u009bJ\u009dK\3")
        buf.write("\2\r\4\2\f\f\17\17\3\2\63;\3\2\62;\4\2GGgg\4\2--//\6\2")
        buf.write("\f\f\16\17$$^^\n\2$$))^^ddhhppttvv\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\5\2\n\f\16\17\"\"\6\3\f\f\16\17$$^^\2\u02b4\2")
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
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\3\u009f\3\2\2\2\5\u00ad\3\2\2")
        buf.write("\2\7\u00ba\3\2\2\2\t\u00c6\3\2\2\2\13\u00d1\3\2\2\2\r")
        buf.write("\u00df\3\2\2\2\17\u00ec\3\2\2\2\21\u00f9\3\2\2\2\23\u0105")
        buf.write("\3\2\2\2\25\u010b\3\2\2\2\27\u0122\3\2\2\2\31\u0127\3")
        buf.write("\2\2\2\33\u0129\3\2\2\2\35\u0137\3\2\2\2\37\u0144\3\2")
        buf.write("\2\2!\u0149\3\2\2\2#\u014f\3\2\2\2%\u0157\3\2\2\2\'\u015a")
        buf.write("\3\2\2\2)\u015f\3\2\2\2+\u0165\3\2\2\2-\u016b\3\2\2\2")
        buf.write("/\u016f\3\2\2\2\61\u0178\3\2\2\2\63\u017b\3\2\2\2\65\u0183")
        buf.write("\3\2\2\2\67\u018a\3\2\2\29\u0191\3\2\2\2;\u0196\3\2\2")
        buf.write("\2=\u019c\3\2\2\2?\u01a1\3\2\2\2A\u01a5\3\2\2\2C\u01ae")
        buf.write("\3\2\2\2E\u01b1\3\2\2\2G\u01b9\3\2\2\2I\u01bf\3\2\2\2")
        buf.write("K\u01c1\3\2\2\2M\u01c3\3\2\2\2O\u01c5\3\2\2\2Q\u01c7\3")
        buf.write("\2\2\2S\u01c9\3\2\2\2U\u01cb\3\2\2\2W\u01ce\3\2\2\2Y\u01d1")
        buf.write("\3\2\2\2[\u01d4\3\2\2\2]\u01d7\3\2\2\2_\u01d9\3\2\2\2")
        buf.write("a\u01dc\3\2\2\2c\u01de\3\2\2\2e\u01e1\3\2\2\2g\u01e9\3")
        buf.write("\2\2\2i\u01f6\3\2\2\2k\u0202\3\2\2\2m\u0204\3\2\2\2o\u0206")
        buf.write("\3\2\2\2q\u0208\3\2\2\2s\u020a\3\2\2\2u\u020c\3\2\2\2")
        buf.write("w\u020e\3\2\2\2y\u0210\3\2\2\2{\u0212\3\2\2\2}\u0214\3")
        buf.write("\2\2\2\177\u0216\3\2\2\2\u0081\u0218\3\2\2\2\u0083\u021a")
        buf.write("\3\2\2\2\u0085\u0230\3\2\2\2\u0087\u0243\3\2\2\2\u0089")
        buf.write("\u0245\3\2\2\2\u008b\u024b\3\2\2\2\u008d\u0257\3\2\2\2")
        buf.write("\u008f\u0259\3\2\2\2\u0091\u025f\3\2\2\2\u0093\u0261\3")
        buf.write("\2\2\2\u0095\u0263\3\2\2\2\u0097\u026b\3\2\2\2\u0099\u0271")
        buf.write("\3\2\2\2\u009b\u0274\3\2\2\2\u009d\u0280\3\2\2\2\u009f")
        buf.write("\u00a0\7t\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7c\2\2\u00a2")
        buf.write("\u00a3\7f\2\2\u00a3\u00a4\7K\2\2\u00a4\u00a5\7p\2\2\u00a5")
        buf.write("\u00a6\7v\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8\7i\2\2\u00a8")
        buf.write("\u00a9\7g\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab\7*\2\2\u00ab")
        buf.write("\u00ac\7+\2\2\u00ac\4\3\2\2\2\u00ad\u00ae\7r\2\2\u00ae")
        buf.write("\u00af\7t\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1")
        buf.write("\u00b2\7v\2\2\u00b2\u00b3\7K\2\2\u00b3\u00b4\7p\2\2\u00b4")
        buf.write("\u00b5\7v\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7i\2\2\u00b7")
        buf.write("\u00b8\7g\2\2\u00b8\u00b9\7t\2\2\u00b9\6\3\2\2\2\u00ba")
        buf.write("\u00bb\7t\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd\7c\2\2\u00bd")
        buf.write("\u00be\7f\2\2\u00be\u00bf\7H\2\2\u00bf\u00c0\7n\2\2\u00c0")
        buf.write("\u00c1\7q\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3\7v\2\2\u00c3")
        buf.write("\u00c4\7*\2\2\u00c4\u00c5\7+\2\2\u00c5\b\3\2\2\2\u00c6")
        buf.write("\u00c7\7r\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7k\2\2\u00c9")
        buf.write("\u00ca\7p\2\2\u00ca\u00cb\7v\2\2\u00cb\u00cc\7H\2\2\u00cc")
        buf.write("\u00cd\7n\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7c\2\2\u00cf")
        buf.write("\u00d0\7v\2\2\u00d0\n\3\2\2\2\u00d1\u00d2\7t\2\2\u00d2")
        buf.write("\u00d3\7g\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7f\2\2\u00d5")
        buf.write("\u00d6\7D\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7q\2\2\u00d8")
        buf.write("\u00d9\7n\2\2\u00d9\u00da\7g\2\2\u00da\u00db\7c\2\2\u00db")
        buf.write("\u00dc\7p\2\2\u00dc\u00dd\7*\2\2\u00dd\u00de\7+\2\2\u00de")
        buf.write("\f\3\2\2\2\u00df\u00e0\7r\2\2\u00e0\u00e1\7t\2\2\u00e1")
        buf.write("\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7v\2\2\u00e4")
        buf.write("\u00e5\7D\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7q\2\2\u00e7")
        buf.write("\u00e8\7n\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea\7c\2\2\u00ea")
        buf.write("\u00eb\7p\2\2\u00eb\16\3\2\2\2\u00ec\u00ed\7t\2\2\u00ed")
        buf.write("\u00ee\7g\2\2\u00ee\u00ef\7c\2\2\u00ef\u00f0\7f\2\2\u00f0")
        buf.write("\u00f1\7U\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7t\2\2\u00f3")
        buf.write("\u00f4\7k\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6\7i\2\2\u00f6")
        buf.write("\u00f7\7*\2\2\u00f7\u00f8\7+\2\2\u00f8\20\3\2\2\2\u00f9")
        buf.write("\u00fa\7r\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc\7k\2\2\u00fc")
        buf.write("\u00fd\7p\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7U\2\2\u00ff")
        buf.write("\u0100\7v\2\2\u0100\u0101\7t\2\2\u0101\u0102\7k\2\2\u0102")
        buf.write("\u0103\7p\2\2\u0103\u0104\7i\2\2\u0104\22\3\2\2\2\u0105")
        buf.write("\u0106\7u\2\2\u0106\u0107\7w\2\2\u0107\u0108\7r\2\2\u0108")
        buf.write("\u0109\7g\2\2\u0109\u010a\7t\2\2\u010a\24\3\2\2\2\u010b")
        buf.write("\u010c\7r\2\2\u010c\u010d\7t\2\2\u010d\u010e\7g\2\2\u010e")
        buf.write("\u010f\7x\2\2\u010f\u0110\7g\2\2\u0110\u0111\7p\2\2\u0111")
        buf.write("\u0112\7v\2\2\u0112\u0113\7F\2\2\u0113\u0114\7g\2\2\u0114")
        buf.write("\u0115\7h\2\2\u0115\u0116\7c\2\2\u0116\u0117\7w\2\2\u0117")
        buf.write("\u0118\7n\2\2\u0118\u0119\7v\2\2\u0119\u011a\7*\2\2\u011a")
        buf.write("\u011b\7+\2\2\u011b\26\3\2\2\2\u011c\u0123\5]/\2\u011d")
        buf.write("\u0123\5_\60\2\u011e\u0123\5a\61\2\u011f\u0123\5c\62\2")
        buf.write("\u0120\u0123\5Y-\2\u0121\u0123\5[.\2\u0122\u011c\3\2\2")
        buf.write("\2\u0122\u011d\3\2\2\2\u0122\u011e\3\2\2\2\u0122\u011f")
        buf.write("\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0121\3\2\2\2\u0123")
        buf.write("\30\3\2\2\2\u0124\u0128\5M\'\2\u0125\u0128\5O(\2\u0126")
        buf.write("\u0128\5Q)\2\u0127\u0124\3\2\2\2\u0127\u0125\3\2\2\2\u0127")
        buf.write("\u0126\3\2\2\2\u0128\32\3\2\2\2\u0129\u012a\7\61\2\2\u012a")
        buf.write("\u012b\7,\2\2\u012b\u012f\3\2\2\2\u012c\u012e\13\2\2\2")
        buf.write("\u012d\u012c\3\2\2\2\u012e\u0131\3\2\2\2\u012f\u0130\3")
        buf.write("\2\2\2\u012f\u012d\3\2\2\2\u0130\u0132\3\2\2\2\u0131\u012f")
        buf.write("\3\2\2\2\u0132\u0133\7,\2\2\u0133\u0134\7\61\2\2\u0134")
        buf.write("\u0135\3\2\2\2\u0135\u0136\b\16\2\2\u0136\34\3\2\2\2\u0137")
        buf.write("\u0138\7\61\2\2\u0138\u0139\7\61\2\2\u0139\u013d\3\2\2")
        buf.write("\2\u013a\u013c\13\2\2\2\u013b\u013a\3\2\2\2\u013c\u013f")
        buf.write("\3\2\2\2\u013d\u013e\3\2\2\2\u013d\u013b\3\2\2\2\u013e")
        buf.write("\u0140\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0141\t\2\2\2")
        buf.write("\u0141\u0142\3\2\2\2\u0142\u0143\b\17\2\2\u0143\36\3\2")
        buf.write("\2\2\u0144\u0145\7c\2\2\u0145\u0146\7w\2\2\u0146\u0147")
        buf.write("\7v\2\2\u0147\u0148\7q\2\2\u0148 \3\2\2\2\u0149\u014a")
        buf.write("\7d\2\2\u014a\u014b\7t\2\2\u014b\u014c\7g\2\2\u014c\u014d")
        buf.write("\7c\2\2\u014d\u014e\7m\2\2\u014e\"\3\2\2\2\u014f\u0150")
        buf.write("\7d\2\2\u0150\u0151\7q\2\2\u0151\u0152\7q\2\2\u0152\u0153")
        buf.write("\7n\2\2\u0153\u0154\7g\2\2\u0154\u0155\7c\2\2\u0155\u0156")
        buf.write("\7p\2\2\u0156$\3\2\2\2\u0157\u0158\7f\2\2\u0158\u0159")
        buf.write("\7q\2\2\u0159&\3\2\2\2\u015a\u015b\7g\2\2\u015b\u015c")
        buf.write("\7n\2\2\u015c\u015d\7u\2\2\u015d\u015e\7g\2\2\u015e(\3")
        buf.write("\2\2\2\u015f\u0160\7h\2\2\u0160\u0161\7c\2\2\u0161\u0162")
        buf.write("\7n\2\2\u0162\u0163\7u\2\2\u0163\u0164\7g\2\2\u0164*\3")
        buf.write("\2\2\2\u0165\u0166\7h\2\2\u0166\u0167\7n\2\2\u0167\u0168")
        buf.write("\7q\2\2\u0168\u0169\7c\2\2\u0169\u016a\7v\2\2\u016a,\3")
        buf.write("\2\2\2\u016b\u016c\7h\2\2\u016c\u016d\7q\2\2\u016d\u016e")
        buf.write("\7t\2\2\u016e.\3\2\2\2\u016f\u0170\7h\2\2\u0170\u0171")
        buf.write("\7w\2\2\u0171\u0172\7p\2\2\u0172\u0173\7e\2\2\u0173\u0174")
        buf.write("\7v\2\2\u0174\u0175\7k\2\2\u0175\u0176\7q\2\2\u0176\u0177")
        buf.write("\7p\2\2\u0177\60\3\2\2\2\u0178\u0179\7k\2\2\u0179\u017a")
        buf.write("\7h\2\2\u017a\62\3\2\2\2\u017b\u017c\7k\2\2\u017c\u017d")
        buf.write("\7p\2\2\u017d\u017e\7v\2\2\u017e\u017f\7g\2\2\u017f\u0180")
        buf.write("\7i\2\2\u0180\u0181\7g\2\2\u0181\u0182\7t\2\2\u0182\64")
        buf.write("\3\2\2\2\u0183\u0184\7t\2\2\u0184\u0185\7g\2\2\u0185\u0186")
        buf.write("\7v\2\2\u0186\u0187\7w\2\2\u0187\u0188\7t\2\2\u0188\u0189")
        buf.write("\7p\2\2\u0189\66\3\2\2\2\u018a\u018b\7u\2\2\u018b\u018c")
        buf.write("\7v\2\2\u018c\u018d\7t\2\2\u018d\u018e\7k\2\2\u018e\u018f")
        buf.write("\7p\2\2\u018f\u0190\7i\2\2\u01908\3\2\2\2\u0191\u0192")
        buf.write("\7v\2\2\u0192\u0193\7t\2\2\u0193\u0194\7w\2\2\u0194\u0195")
        buf.write("\7g\2\2\u0195:\3\2\2\2\u0196\u0197\7y\2\2\u0197\u0198")
        buf.write("\7j\2\2\u0198\u0199\7k\2\2\u0199\u019a\7n\2\2\u019a\u019b")
        buf.write("\7g\2\2\u019b<\3\2\2\2\u019c\u019d\7x\2\2\u019d\u019e")
        buf.write("\7q\2\2\u019e\u019f\7k\2\2\u019f\u01a0\7f\2\2\u01a0>\3")
        buf.write("\2\2\2\u01a1\u01a2\7q\2\2\u01a2\u01a3\7w\2\2\u01a3\u01a4")
        buf.write("\7v\2\2\u01a4@\3\2\2\2\u01a5\u01a6\7e\2\2\u01a6\u01a7")
        buf.write("\7q\2\2\u01a7\u01a8\7p\2\2\u01a8\u01a9\7v\2\2\u01a9\u01aa")
        buf.write("\7k\2\2\u01aa\u01ab\7p\2\2\u01ab\u01ac\7w\2\2\u01ac\u01ad")
        buf.write("\7g\2\2\u01adB\3\2\2\2\u01ae\u01af\7q\2\2\u01af\u01b0")
        buf.write("\7h\2\2\u01b0D\3\2\2\2\u01b1\u01b2\7k\2\2\u01b2\u01b3")
        buf.write("\7p\2\2\u01b3\u01b4\7j\2\2\u01b4\u01b5\7g\2\2\u01b5\u01b6")
        buf.write("\7t\2\2\u01b6\u01b7\7k\2\2\u01b7\u01b8\7v\2\2\u01b8F\3")
        buf.write("\2\2\2\u01b9\u01ba\7c\2\2\u01ba\u01bb\7t\2\2\u01bb\u01bc")
        buf.write("\7t\2\2\u01bc\u01bd\7c\2\2\u01bd\u01be\7{\2\2\u01beH\3")
        buf.write("\2\2\2\u01bf\u01c0\7-\2\2\u01c0J\3\2\2\2\u01c1\u01c2\7")
        buf.write("/\2\2\u01c2L\3\2\2\2\u01c3\u01c4\7,\2\2\u01c4N\3\2\2\2")
        buf.write("\u01c5\u01c6\7\61\2\2\u01c6P\3\2\2\2\u01c7\u01c8\7\'\2")
        buf.write("\2\u01c8R\3\2\2\2\u01c9\u01ca\7#\2\2\u01caT\3\2\2\2\u01cb")
        buf.write("\u01cc\7(\2\2\u01cc\u01cd\7(\2\2\u01cdV\3\2\2\2\u01ce")
        buf.write("\u01cf\7~\2\2\u01cf\u01d0\7~\2\2\u01d0X\3\2\2\2\u01d1")
        buf.write("\u01d2\7?\2\2\u01d2\u01d3\7?\2\2\u01d3Z\3\2\2\2\u01d4")
        buf.write("\u01d5\7#\2\2\u01d5\u01d6\7?\2\2\u01d6\\\3\2\2\2\u01d7")
        buf.write("\u01d8\7>\2\2\u01d8^\3\2\2\2\u01d9\u01da\7>\2\2\u01da")
        buf.write("\u01db\7?\2\2\u01db`\3\2\2\2\u01dc\u01dd\7@\2\2\u01dd")
        buf.write("b\3\2\2\2\u01de\u01df\7@\2\2\u01df\u01e0\7?\2\2\u01e0")
        buf.write("d\3\2\2\2\u01e1\u01e2\7<\2\2\u01e2\u01e3\7<\2\2\u01e3")
        buf.write("f\3\2\2\2\u01e4\u01ea\5S*\2\u01e5\u01ea\5U+\2\u01e6\u01ea")
        buf.write("\5W,\2\u01e7\u01ea\5Y-\2\u01e8\u01ea\5[.\2\u01e9\u01e4")
        buf.write("\3\2\2\2\u01e9\u01e5\3\2\2\2\u01e9\u01e6\3\2\2\2\u01e9")
        buf.write("\u01e7\3\2\2\2\u01e9\u01e8\3\2\2\2\u01eah\3\2\2\2\u01eb")
        buf.write("\u01f7\5I%\2\u01ec\u01f7\5K&\2\u01ed\u01f7\5M\'\2\u01ee")
        buf.write("\u01f7\5O(\2\u01ef\u01f7\5Q)\2\u01f0\u01f7\5Y-\2\u01f1")
        buf.write("\u01f7\5[.\2\u01f2\u01f7\5]/\2\u01f3\u01f7\5_\60\2\u01f4")
        buf.write("\u01f7\5a\61\2\u01f5\u01f7\5c\62\2\u01f6\u01eb\3\2\2\2")
        buf.write("\u01f6\u01ec\3\2\2\2\u01f6\u01ed\3\2\2\2\u01f6\u01ee\3")
        buf.write("\2\2\2\u01f6\u01ef\3\2\2\2\u01f6\u01f0\3\2\2\2\u01f6\u01f1")
        buf.write("\3\2\2\2\u01f6\u01f2\3\2\2\2\u01f6\u01f3\3\2\2\2\u01f6")
        buf.write("\u01f4\3\2\2\2\u01f6\u01f5\3\2\2\2\u01f7j\3\2\2\2\u01f8")
        buf.write("\u0203\5I%\2\u01f9\u0203\5K&\2\u01fa\u0203\5M\'\2\u01fb")
        buf.write("\u0203\5O(\2\u01fc\u0203\5Y-\2\u01fd\u0203\5[.\2\u01fe")
        buf.write("\u0203\5]/\2\u01ff\u0203\5_\60\2\u0200\u0203\5a\61\2\u0201")
        buf.write("\u0203\5c\62\2\u0202\u01f8\3\2\2\2\u0202\u01f9\3\2\2\2")
        buf.write("\u0202\u01fa\3\2\2\2\u0202\u01fb\3\2\2\2\u0202\u01fc\3")
        buf.write("\2\2\2\u0202\u01fd\3\2\2\2\u0202\u01fe\3\2\2\2\u0202\u01ff")
        buf.write("\3\2\2\2\u0202\u0200\3\2\2\2\u0202\u0201\3\2\2\2\u0203")
        buf.write("l\3\2\2\2\u0204\u0205\5e\63\2\u0205n\3\2\2\2\u0206\u0207")
        buf.write("\7.\2\2\u0207p\3\2\2\2\u0208\u0209\7\60\2\2\u0209r\3\2")
        buf.write("\2\2\u020a\u020b\7=\2\2\u020bt\3\2\2\2\u020c\u020d\7?")
        buf.write("\2\2\u020dv\3\2\2\2\u020e\u020f\7<\2\2\u020fx\3\2\2\2")
        buf.write("\u0210\u0211\7*\2\2\u0211z\3\2\2\2\u0212\u0213\7+\2\2")
        buf.write("\u0213|\3\2\2\2\u0214\u0215\7}\2\2\u0215~\3\2\2\2\u0216")
        buf.write("\u0217\7\177\2\2\u0217\u0080\3\2\2\2\u0218\u0219\7]\2")
        buf.write("\2\u0219\u0082\3\2\2\2\u021a\u021b\7_\2\2\u021b\u0084")
        buf.write("\3\2\2\2\u021c\u0231\7\62\2\2\u021d\u0221\t\3\2\2\u021e")
        buf.write("\u0220\t\4\2\2\u021f\u021e\3\2\2\2\u0220\u0223\3\2\2\2")
        buf.write("\u0221\u021f\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u022c\3")
        buf.write("\2\2\2\u0223\u0221\3\2\2\2\u0224\u0226\7a\2\2\u0225\u0227")
        buf.write("\t\4\2\2\u0226\u0225\3\2\2\2\u0227\u0228\3\2\2\2\u0228")
        buf.write("\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u022b\3\2\2\2")
        buf.write("\u022a\u0224\3\2\2\2\u022b\u022e\3\2\2\2\u022c\u022a\3")
        buf.write("\2\2\2\u022c\u022d\3\2\2\2\u022d\u022f\3\2\2\2\u022e\u022c")
        buf.write("\3\2\2\2\u022f\u0231\bC\3\2\u0230\u021c\3\2\2\2\u0230")
        buf.write("\u021d\3\2\2\2\u0231\u0086\3\2\2\2\u0232\u0237\5\u0085")
        buf.write("C\2\u0233\u0235\5q9\2\u0234\u0236\5\u0085C\2\u0235\u0234")
        buf.write("\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0238\3\2\2\2\u0237")
        buf.write("\u0233\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u0239\3\2\2\2")
        buf.write("\u0239\u023a\5\u0089E\2\u023a\u023b\bD\4\2\u023b\u0244")
        buf.write("\3\2\2\2\u023c\u023d\5\u0085C\2\u023d\u023f\5q9\2\u023e")
        buf.write("\u0240\5\u0085C\2\u023f\u023e\3\2\2\2\u023f\u0240\3\2")
        buf.write("\2\2\u0240\u0241\3\2\2\2\u0241\u0242\bD\5\2\u0242\u0244")
        buf.write("\3\2\2\2\u0243\u0232\3\2\2\2\u0243\u023c\3\2\2\2\u0244")
        buf.write("\u0088\3\2\2\2\u0245\u0247\t\5\2\2\u0246\u0248\t\6\2\2")
        buf.write("\u0247\u0246\3\2\2\2\u0247\u0248\3\2\2\2\u0248\u0249\3")
        buf.write("\2\2\2\u0249\u024a\5\u0085C\2\u024a\u008a\3\2\2\2\u024b")
        buf.write("\u024f\5\u0093J\2\u024c\u024e\5\u008dG\2\u024d\u024c\3")
        buf.write("\2\2\2\u024e\u0251\3\2\2\2\u024f\u024d\3\2\2\2\u024f\u0250")
        buf.write("\3\2\2\2\u0250\u0252\3\2\2\2\u0251\u024f\3\2\2\2\u0252")
        buf.write("\u0253\5\u0093J\2\u0253\u0254\bF\6\2\u0254\u008c\3\2\2")
        buf.write("\2\u0255\u0258\n\7\2\2\u0256\u0258\5\u008fH\2\u0257\u0255")
        buf.write("\3\2\2\2\u0257\u0256\3\2\2\2\u0258\u008e\3\2\2\2\u0259")
        buf.write("\u025a\7^\2\2\u025a\u025b\t\b\2\2\u025b\u0090\3\2\2\2")
        buf.write("\u025c\u025d\7^\2\2\u025d\u0260\n\b\2\2\u025e\u0260\7")
        buf.write("^\2\2\u025f\u025c\3\2\2\2\u025f\u025e\3\2\2\2\u0260\u0092")
        buf.write("\3\2\2\2\u0261\u0262\7$\2\2\u0262\u0094\3\2\2\2\u0263")
        buf.write("\u0267\t\t\2\2\u0264\u0266\t\n\2\2\u0265\u0264\3\2\2\2")
        buf.write("\u0266\u0269\3\2\2\2\u0267\u0265\3\2\2\2\u0267\u0268\3")
        buf.write("\2\2\2\u0268\u0096\3\2\2\2\u0269\u0267\3\2\2\2\u026a\u026c")
        buf.write("\t\13\2\2\u026b\u026a\3\2\2\2\u026c\u026d\3\2\2\2\u026d")
        buf.write("\u026b\3\2\2\2\u026d\u026e\3\2\2\2\u026e\u026f\3\2\2\2")
        buf.write("\u026f\u0270\bL\2\2\u0270\u0098\3\2\2\2\u0271\u0272\13")
        buf.write("\2\2\2\u0272\u0273\bM\7\2\u0273\u009a\3\2\2\2\u0274\u0278")
        buf.write("\5\u0093J\2\u0275\u0277\5\u008dG\2\u0276\u0275\3\2\2\2")
        buf.write("\u0277\u027a\3\2\2\2\u0278\u0276\3\2\2\2\u0278\u0279\3")
        buf.write("\2\2\2\u0279\u027c\3\2\2\2\u027a\u0278\3\2\2\2\u027b\u027d")
        buf.write("\t\f\2\2\u027c\u027b\3\2\2\2\u027d\u027e\3\2\2\2\u027e")
        buf.write("\u027f\bN\b\2\u027f\u009c\3\2\2\2\u0280\u0284\5\u0093")
        buf.write("J\2\u0281\u0283\5\u008dG\2\u0282\u0281\3\2\2\2\u0283\u0286")
        buf.write("\3\2\2\2\u0284\u0282\3\2\2\2\u0284\u0285\3\2\2\2\u0285")
        buf.write("\u0287\3\2\2\2\u0286\u0284\3\2\2\2\u0287\u0288\5\u0091")
        buf.write("I\2\u0288\u0289\bO\t\2\u0289\u009e\3\2\2\2\33\2\u0122")
        buf.write("\u0127\u012f\u013d\u01e9\u01f6\u0202\u0221\u0228\u022c")
        buf.write("\u0230\u0235\u0237\u023f\u0243\u0247\u024f\u0257\u025f")
        buf.write("\u0267\u026d\u0278\u027c\u0284\n\b\2\2\3C\2\3D\3\3D\4")
        buf.write("\3F\5\3M\6\3N\7\3O\b")
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
            "'readInteger()'", "'printInteger'", "'readFloat()'", "'printFloat'", 
            "'readBoolean()'", "'printBoolean'", "'readString()'", "'printString'", 
            "'super'", "'preventDefault()'", "'auto'", "'break'", "'boolean'", 
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
                  "LS", "RS", "INTLIT", "FLOATLIT", "SCIENTIFIC", "STRINGLIT", 
                  "StringChar", "EscapeSequence", "IllegalString", "DoubleQuote", 
                  "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[68] = self.STRINGLIT_action 
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

     


