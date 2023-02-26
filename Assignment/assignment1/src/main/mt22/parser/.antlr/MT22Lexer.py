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
        buf.write("\u0293\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u0121\n\f\3\r\3\r\3\r\5\r\u0126\n")
        buf.write("\r\3\16\3\16\3\16\3\16\7\16\u012c\n\16\f\16\16\16\u012f")
        buf.write("\13\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\7")
        buf.write("\17\u013a\n\17\f\17\16\17\u013d\13\17\3\17\3\17\3\17\3")
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
        buf.write("\3\64\3\64\3\64\5\64\u01e8\n\64\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u01f5\n\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u0201")
        buf.write("\n\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3")
        buf.write(">\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3C\7C\u021e\nC\fC\16")
        buf.write("C\u0221\13C\3C\3C\6C\u0225\nC\rC\16C\u0226\7C\u0229\n")
        buf.write("C\fC\16C\u022c\13C\3C\5C\u022f\nC\3D\3D\3D\5D\u0234\n")
        buf.write("D\5D\u0236\nD\3D\3D\3D\3D\3D\3D\5D\u023e\nD\3D\3D\5D\u0242")
        buf.write("\nD\3E\3E\5E\u0246\nE\3E\3E\3F\3F\3F\3F\7F\u024e\nF\f")
        buf.write("F\16F\u0251\13F\3F\3F\3F\3G\3G\3G\3G\3G\3G\3G\3G\3G\3")
        buf.write("G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\5G\u026b\nG\3H\3H\7")
        buf.write("H\u026f\nH\fH\16H\u0272\13H\3I\6I\u0275\nI\rI\16I\u0276")
        buf.write("\3I\3I\3J\3J\3J\3K\3K\3K\3L\3L\3L\3M\3M\3M\5M\u0287\n")
        buf.write("M\3N\3N\3N\3N\7N\u028d\nN\fN\16N\u0290\13N\3N\3N\5\u012d")
        buf.write("\u013b\u028e\2O\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087")
        buf.write("E\u0089\2\u008bF\u008dG\u008fH\u0091I\u0093J\u0095K\u0097")
        buf.write("L\u0099\2\u009bM\3\2\r\4\2\f\f\17\17\3\2\63;\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\n\2$$))^^ddhhppttvv\6\2\f\f\17\17$$^^\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\5\2\n\f\16\17\"\"\3\2^^\2\u02d3")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
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
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\3\u009d\3\2\2\2\5\u00ab\3\2\2\2\7\u00b8\3\2\2\2\t\u00c4")
        buf.write("\3\2\2\2\13\u00cf\3\2\2\2\r\u00dd\3\2\2\2\17\u00ea\3\2")
        buf.write("\2\2\21\u00f7\3\2\2\2\23\u0103\3\2\2\2\25\u0109\3\2\2")
        buf.write("\2\27\u0120\3\2\2\2\31\u0125\3\2\2\2\33\u0127\3\2\2\2")
        buf.write("\35\u0135\3\2\2\2\37\u0142\3\2\2\2!\u0147\3\2\2\2#\u014d")
        buf.write("\3\2\2\2%\u0155\3\2\2\2\'\u0158\3\2\2\2)\u015d\3\2\2\2")
        buf.write("+\u0163\3\2\2\2-\u0169\3\2\2\2/\u016d\3\2\2\2\61\u0176")
        buf.write("\3\2\2\2\63\u0179\3\2\2\2\65\u0181\3\2\2\2\67\u0188\3")
        buf.write("\2\2\29\u018f\3\2\2\2;\u0194\3\2\2\2=\u019a\3\2\2\2?\u019f")
        buf.write("\3\2\2\2A\u01a3\3\2\2\2C\u01ac\3\2\2\2E\u01af\3\2\2\2")
        buf.write("G\u01b7\3\2\2\2I\u01bd\3\2\2\2K\u01bf\3\2\2\2M\u01c1\3")
        buf.write("\2\2\2O\u01c3\3\2\2\2Q\u01c5\3\2\2\2S\u01c7\3\2\2\2U\u01c9")
        buf.write("\3\2\2\2W\u01cc\3\2\2\2Y\u01cf\3\2\2\2[\u01d2\3\2\2\2")
        buf.write("]\u01d5\3\2\2\2_\u01d7\3\2\2\2a\u01da\3\2\2\2c\u01dc\3")
        buf.write("\2\2\2e\u01df\3\2\2\2g\u01e7\3\2\2\2i\u01f4\3\2\2\2k\u0200")
        buf.write("\3\2\2\2m\u0202\3\2\2\2o\u0204\3\2\2\2q\u0206\3\2\2\2")
        buf.write("s\u0208\3\2\2\2u\u020a\3\2\2\2w\u020c\3\2\2\2y\u020e\3")
        buf.write("\2\2\2{\u0210\3\2\2\2}\u0212\3\2\2\2\177\u0214\3\2\2\2")
        buf.write("\u0081\u0216\3\2\2\2\u0083\u0218\3\2\2\2\u0085\u022e\3")
        buf.write("\2\2\2\u0087\u0241\3\2\2\2\u0089\u0243\3\2\2\2\u008b\u0249")
        buf.write("\3\2\2\2\u008d\u026a\3\2\2\2\u008f\u026c\3\2\2\2\u0091")
        buf.write("\u0274\3\2\2\2\u0093\u027a\3\2\2\2\u0095\u027d\3\2\2\2")
        buf.write("\u0097\u0280\3\2\2\2\u0099\u0286\3\2\2\2\u009b\u0288\3")
        buf.write("\2\2\2\u009d\u009e\7t\2\2\u009e\u009f\7g\2\2\u009f\u00a0")
        buf.write("\7c\2\2\u00a0\u00a1\7f\2\2\u00a1\u00a2\7K\2\2\u00a2\u00a3")
        buf.write("\7p\2\2\u00a3\u00a4\7v\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6")
        buf.write("\7i\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9")
        buf.write("\7*\2\2\u00a9\u00aa\7+\2\2\u00aa\4\3\2\2\2\u00ab\u00ac")
        buf.write("\7r\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7K\2\2\u00b1\u00b2")
        buf.write("\7p\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5")
        buf.write("\7i\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7t\2\2\u00b7\6")
        buf.write("\3\2\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb")
        buf.write("\7c\2\2\u00bb\u00bc\7f\2\2\u00bc\u00bd\7H\2\2\u00bd\u00be")
        buf.write("\7n\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7c\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\u00c2\7*\2\2\u00c2\u00c3\7+\2\2\u00c3\b")
        buf.write("\3\2\2\2\u00c4\u00c5\7r\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7")
        buf.write("\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca")
        buf.write("\7H\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd")
        buf.write("\7c\2\2\u00cd\u00ce\7v\2\2\u00ce\n\3\2\2\2\u00cf\u00d0")
        buf.write("\7t\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3")
        buf.write("\7f\2\2\u00d3\u00d4\7D\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6")
        buf.write("\7q\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9")
        buf.write("\7c\2\2\u00d9\u00da\7p\2\2\u00da\u00db\7*\2\2\u00db\u00dc")
        buf.write("\7+\2\2\u00dc\f\3\2\2\2\u00dd\u00de\7r\2\2\u00de\u00df")
        buf.write("\7t\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2")
        buf.write("\7v\2\2\u00e2\u00e3\7D\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5")
        buf.write("\7q\2\2\u00e5\u00e6\7n\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8")
        buf.write("\7c\2\2\u00e8\u00e9\7p\2\2\u00e9\16\3\2\2\2\u00ea\u00eb")
        buf.write("\7t\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee")
        buf.write("\7f\2\2\u00ee\u00ef\7U\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1")
        buf.write("\7t\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4")
        buf.write("\7i\2\2\u00f4\u00f5\7*\2\2\u00f5\u00f6\7+\2\2\u00f6\20")
        buf.write("\3\2\2\2\u00f7\u00f8\7r\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa")
        buf.write("\7k\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd")
        buf.write("\7U\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100")
        buf.write("\7k\2\2\u0100\u0101\7p\2\2\u0101\u0102\7i\2\2\u0102\22")
        buf.write("\3\2\2\2\u0103\u0104\7u\2\2\u0104\u0105\7w\2\2\u0105\u0106")
        buf.write("\7r\2\2\u0106\u0107\7g\2\2\u0107\u0108\7t\2\2\u0108\24")
        buf.write("\3\2\2\2\u0109\u010a\7r\2\2\u010a\u010b\7t\2\2\u010b\u010c")
        buf.write("\7g\2\2\u010c\u010d\7x\2\2\u010d\u010e\7g\2\2\u010e\u010f")
        buf.write("\7p\2\2\u010f\u0110\7v\2\2\u0110\u0111\7F\2\2\u0111\u0112")
        buf.write("\7g\2\2\u0112\u0113\7h\2\2\u0113\u0114\7c\2\2\u0114\u0115")
        buf.write("\7w\2\2\u0115\u0116\7n\2\2\u0116\u0117\7v\2\2\u0117\u0118")
        buf.write("\7*\2\2\u0118\u0119\7+\2\2\u0119\26\3\2\2\2\u011a\u0121")
        buf.write("\5]/\2\u011b\u0121\5_\60\2\u011c\u0121\5a\61\2\u011d\u0121")
        buf.write("\5c\62\2\u011e\u0121\5Y-\2\u011f\u0121\5[.\2\u0120\u011a")
        buf.write("\3\2\2\2\u0120\u011b\3\2\2\2\u0120\u011c\3\2\2\2\u0120")
        buf.write("\u011d\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u011f\3\2\2\2")
        buf.write("\u0121\30\3\2\2\2\u0122\u0126\5M\'\2\u0123\u0126\5O(\2")
        buf.write("\u0124\u0126\5Q)\2\u0125\u0122\3\2\2\2\u0125\u0123\3\2")
        buf.write("\2\2\u0125\u0124\3\2\2\2\u0126\32\3\2\2\2\u0127\u0128")
        buf.write("\7\61\2\2\u0128\u0129\7,\2\2\u0129\u012d\3\2\2\2\u012a")
        buf.write("\u012c\13\2\2\2\u012b\u012a\3\2\2\2\u012c\u012f\3\2\2")
        buf.write("\2\u012d\u012e\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u0130")
        buf.write("\3\2\2\2\u012f\u012d\3\2\2\2\u0130\u0131\7,\2\2\u0131")
        buf.write("\u0132\7\61\2\2\u0132\u0133\3\2\2\2\u0133\u0134\b\16\2")
        buf.write("\2\u0134\34\3\2\2\2\u0135\u0136\7\61\2\2\u0136\u0137\7")
        buf.write("\61\2\2\u0137\u013b\3\2\2\2\u0138\u013a\13\2\2\2\u0139")
        buf.write("\u0138\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u013c\3\2\2\2")
        buf.write("\u013b\u0139\3\2\2\2\u013c\u013e\3\2\2\2\u013d\u013b\3")
        buf.write("\2\2\2\u013e\u013f\t\2\2\2\u013f\u0140\3\2\2\2\u0140\u0141")
        buf.write("\b\17\2\2\u0141\36\3\2\2\2\u0142\u0143\7c\2\2\u0143\u0144")
        buf.write("\7w\2\2\u0144\u0145\7v\2\2\u0145\u0146\7q\2\2\u0146 \3")
        buf.write("\2\2\2\u0147\u0148\7d\2\2\u0148\u0149\7t\2\2\u0149\u014a")
        buf.write("\7g\2\2\u014a\u014b\7c\2\2\u014b\u014c\7m\2\2\u014c\"")
        buf.write("\3\2\2\2\u014d\u014e\7d\2\2\u014e\u014f\7q\2\2\u014f\u0150")
        buf.write("\7q\2\2\u0150\u0151\7n\2\2\u0151\u0152\7g\2\2\u0152\u0153")
        buf.write("\7c\2\2\u0153\u0154\7p\2\2\u0154$\3\2\2\2\u0155\u0156")
        buf.write("\7f\2\2\u0156\u0157\7q\2\2\u0157&\3\2\2\2\u0158\u0159")
        buf.write("\7g\2\2\u0159\u015a\7n\2\2\u015a\u015b\7u\2\2\u015b\u015c")
        buf.write("\7g\2\2\u015c(\3\2\2\2\u015d\u015e\7h\2\2\u015e\u015f")
        buf.write("\7c\2\2\u015f\u0160\7n\2\2\u0160\u0161\7u\2\2\u0161\u0162")
        buf.write("\7g\2\2\u0162*\3\2\2\2\u0163\u0164\7h\2\2\u0164\u0165")
        buf.write("\7n\2\2\u0165\u0166\7q\2\2\u0166\u0167\7c\2\2\u0167\u0168")
        buf.write("\7v\2\2\u0168,\3\2\2\2\u0169\u016a\7h\2\2\u016a\u016b")
        buf.write("\7q\2\2\u016b\u016c\7t\2\2\u016c.\3\2\2\2\u016d\u016e")
        buf.write("\7h\2\2\u016e\u016f\7w\2\2\u016f\u0170\7p\2\2\u0170\u0171")
        buf.write("\7e\2\2\u0171\u0172\7v\2\2\u0172\u0173\7k\2\2\u0173\u0174")
        buf.write("\7q\2\2\u0174\u0175\7p\2\2\u0175\60\3\2\2\2\u0176\u0177")
        buf.write("\7k\2\2\u0177\u0178\7h\2\2\u0178\62\3\2\2\2\u0179\u017a")
        buf.write("\7k\2\2\u017a\u017b\7p\2\2\u017b\u017c\7v\2\2\u017c\u017d")
        buf.write("\7g\2\2\u017d\u017e\7i\2\2\u017e\u017f\7g\2\2\u017f\u0180")
        buf.write("\7t\2\2\u0180\64\3\2\2\2\u0181\u0182\7t\2\2\u0182\u0183")
        buf.write("\7g\2\2\u0183\u0184\7v\2\2\u0184\u0185\7w\2\2\u0185\u0186")
        buf.write("\7t\2\2\u0186\u0187\7p\2\2\u0187\66\3\2\2\2\u0188\u0189")
        buf.write("\7u\2\2\u0189\u018a\7v\2\2\u018a\u018b\7t\2\2\u018b\u018c")
        buf.write("\7k\2\2\u018c\u018d\7p\2\2\u018d\u018e\7i\2\2\u018e8\3")
        buf.write("\2\2\2\u018f\u0190\7v\2\2\u0190\u0191\7t\2\2\u0191\u0192")
        buf.write("\7w\2\2\u0192\u0193\7g\2\2\u0193:\3\2\2\2\u0194\u0195")
        buf.write("\7y\2\2\u0195\u0196\7j\2\2\u0196\u0197\7k\2\2\u0197\u0198")
        buf.write("\7n\2\2\u0198\u0199\7g\2\2\u0199<\3\2\2\2\u019a\u019b")
        buf.write("\7x\2\2\u019b\u019c\7q\2\2\u019c\u019d\7k\2\2\u019d\u019e")
        buf.write("\7f\2\2\u019e>\3\2\2\2\u019f\u01a0\7q\2\2\u01a0\u01a1")
        buf.write("\7w\2\2\u01a1\u01a2\7v\2\2\u01a2@\3\2\2\2\u01a3\u01a4")
        buf.write("\7e\2\2\u01a4\u01a5\7q\2\2\u01a5\u01a6\7p\2\2\u01a6\u01a7")
        buf.write("\7v\2\2\u01a7\u01a8\7k\2\2\u01a8\u01a9\7p\2\2\u01a9\u01aa")
        buf.write("\7w\2\2\u01aa\u01ab\7g\2\2\u01abB\3\2\2\2\u01ac\u01ad")
        buf.write("\7q\2\2\u01ad\u01ae\7h\2\2\u01aeD\3\2\2\2\u01af\u01b0")
        buf.write("\7k\2\2\u01b0\u01b1\7p\2\2\u01b1\u01b2\7j\2\2\u01b2\u01b3")
        buf.write("\7g\2\2\u01b3\u01b4\7t\2\2\u01b4\u01b5\7k\2\2\u01b5\u01b6")
        buf.write("\7v\2\2\u01b6F\3\2\2\2\u01b7\u01b8\7c\2\2\u01b8\u01b9")
        buf.write("\7t\2\2\u01b9\u01ba\7t\2\2\u01ba\u01bb\7c\2\2\u01bb\u01bc")
        buf.write("\7{\2\2\u01bcH\3\2\2\2\u01bd\u01be\7-\2\2\u01beJ\3\2\2")
        buf.write("\2\u01bf\u01c0\7/\2\2\u01c0L\3\2\2\2\u01c1\u01c2\7,\2")
        buf.write("\2\u01c2N\3\2\2\2\u01c3\u01c4\7\61\2\2\u01c4P\3\2\2\2")
        buf.write("\u01c5\u01c6\7\'\2\2\u01c6R\3\2\2\2\u01c7\u01c8\7#\2\2")
        buf.write("\u01c8T\3\2\2\2\u01c9\u01ca\7(\2\2\u01ca\u01cb\7(\2\2")
        buf.write("\u01cbV\3\2\2\2\u01cc\u01cd\7~\2\2\u01cd\u01ce\7~\2\2")
        buf.write("\u01ceX\3\2\2\2\u01cf\u01d0\7?\2\2\u01d0\u01d1\7?\2\2")
        buf.write("\u01d1Z\3\2\2\2\u01d2\u01d3\7#\2\2\u01d3\u01d4\7?\2\2")
        buf.write("\u01d4\\\3\2\2\2\u01d5\u01d6\7>\2\2\u01d6^\3\2\2\2\u01d7")
        buf.write("\u01d8\7>\2\2\u01d8\u01d9\7?\2\2\u01d9`\3\2\2\2\u01da")
        buf.write("\u01db\7@\2\2\u01dbb\3\2\2\2\u01dc\u01dd\7@\2\2\u01dd")
        buf.write("\u01de\7?\2\2\u01ded\3\2\2\2\u01df\u01e0\7<\2\2\u01e0")
        buf.write("\u01e1\7<\2\2\u01e1f\3\2\2\2\u01e2\u01e8\5S*\2\u01e3\u01e8")
        buf.write("\5U+\2\u01e4\u01e8\5W,\2\u01e5\u01e8\5Y-\2\u01e6\u01e8")
        buf.write("\5[.\2\u01e7\u01e2\3\2\2\2\u01e7\u01e3\3\2\2\2\u01e7\u01e4")
        buf.write("\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8")
        buf.write("h\3\2\2\2\u01e9\u01f5\5I%\2\u01ea\u01f5\5K&\2\u01eb\u01f5")
        buf.write("\5M\'\2\u01ec\u01f5\5O(\2\u01ed\u01f5\5Q)\2\u01ee\u01f5")
        buf.write("\5Y-\2\u01ef\u01f5\5[.\2\u01f0\u01f5\5]/\2\u01f1\u01f5")
        buf.write("\5_\60\2\u01f2\u01f5\5a\61\2\u01f3\u01f5\5c\62\2\u01f4")
        buf.write("\u01e9\3\2\2\2\u01f4\u01ea\3\2\2\2\u01f4\u01eb\3\2\2\2")
        buf.write("\u01f4\u01ec\3\2\2\2\u01f4\u01ed\3\2\2\2\u01f4\u01ee\3")
        buf.write("\2\2\2\u01f4\u01ef\3\2\2\2\u01f4\u01f0\3\2\2\2\u01f4\u01f1")
        buf.write("\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f3\3\2\2\2\u01f5")
        buf.write("j\3\2\2\2\u01f6\u0201\5I%\2\u01f7\u0201\5K&\2\u01f8\u0201")
        buf.write("\5M\'\2\u01f9\u0201\5O(\2\u01fa\u0201\5Y-\2\u01fb\u0201")
        buf.write("\5[.\2\u01fc\u0201\5]/\2\u01fd\u0201\5_\60\2\u01fe\u0201")
        buf.write("\5a\61\2\u01ff\u0201\5c\62\2\u0200\u01f6\3\2\2\2\u0200")
        buf.write("\u01f7\3\2\2\2\u0200\u01f8\3\2\2\2\u0200\u01f9\3\2\2\2")
        buf.write("\u0200\u01fa\3\2\2\2\u0200\u01fb\3\2\2\2\u0200\u01fc\3")
        buf.write("\2\2\2\u0200\u01fd\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u01ff")
        buf.write("\3\2\2\2\u0201l\3\2\2\2\u0202\u0203\5e\63\2\u0203n\3\2")
        buf.write("\2\2\u0204\u0205\7.\2\2\u0205p\3\2\2\2\u0206\u0207\7\60")
        buf.write("\2\2\u0207r\3\2\2\2\u0208\u0209\7=\2\2\u0209t\3\2\2\2")
        buf.write("\u020a\u020b\7?\2\2\u020bv\3\2\2\2\u020c\u020d\7<\2\2")
        buf.write("\u020dx\3\2\2\2\u020e\u020f\7*\2\2\u020fz\3\2\2\2\u0210")
        buf.write("\u0211\7+\2\2\u0211|\3\2\2\2\u0212\u0213\7}\2\2\u0213")
        buf.write("~\3\2\2\2\u0214\u0215\7\177\2\2\u0215\u0080\3\2\2\2\u0216")
        buf.write("\u0217\7]\2\2\u0217\u0082\3\2\2\2\u0218\u0219\7_\2\2\u0219")
        buf.write("\u0084\3\2\2\2\u021a\u022f\7\62\2\2\u021b\u021f\t\3\2")
        buf.write("\2\u021c\u021e\t\4\2\2\u021d\u021c\3\2\2\2\u021e\u0221")
        buf.write("\3\2\2\2\u021f\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220")
        buf.write("\u022a\3\2\2\2\u0221\u021f\3\2\2\2\u0222\u0224\7a\2\2")
        buf.write("\u0223\u0225\t\4\2\2\u0224\u0223\3\2\2\2\u0225\u0226\3")
        buf.write("\2\2\2\u0226\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u0229")
        buf.write("\3\2\2\2\u0228\u0222\3\2\2\2\u0229\u022c\3\2\2\2\u022a")
        buf.write("\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022d\3\2\2\2")
        buf.write("\u022c\u022a\3\2\2\2\u022d\u022f\bC\3\2\u022e\u021a\3")
        buf.write("\2\2\2\u022e\u021b\3\2\2\2\u022f\u0086\3\2\2\2\u0230\u0235")
        buf.write("\5\u0085C\2\u0231\u0233\5q9\2\u0232\u0234\5\u0085C\2\u0233")
        buf.write("\u0232\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0236\3\2\2\2")
        buf.write("\u0235\u0231\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0237\3")
        buf.write("\2\2\2\u0237\u0238\5\u0089E\2\u0238\u0239\bD\4\2\u0239")
        buf.write("\u0242\3\2\2\2\u023a\u023b\5\u0085C\2\u023b\u023d\5q9")
        buf.write("\2\u023c\u023e\5\u0085C\2\u023d\u023c\3\2\2\2\u023d\u023e")
        buf.write("\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u0240\bD\5\2\u0240")
        buf.write("\u0242\3\2\2\2\u0241\u0230\3\2\2\2\u0241\u023a\3\2\2\2")
        buf.write("\u0242\u0088\3\2\2\2\u0243\u0245\t\5\2\2\u0244\u0246\t")
        buf.write("\6\2\2\u0245\u0244\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u0247")
        buf.write("\3\2\2\2\u0247\u0248\5\u0085C\2\u0248\u008a\3\2\2\2\u0249")
        buf.write("\u024f\7$\2\2\u024a\u024b\7^\2\2\u024b\u024e\t\7\2\2\u024c")
        buf.write("\u024e\n\b\2\2\u024d\u024a\3\2\2\2\u024d\u024c\3\2\2\2")
        buf.write("\u024e\u0251\3\2\2\2\u024f\u024d\3\2\2\2\u024f\u0250\3")
        buf.write("\2\2\2\u0250\u0252\3\2\2\2\u0251\u024f\3\2\2\2\u0252\u0253")
        buf.write("\7$\2\2\u0253\u0254\bF\6\2\u0254\u008c\3\2\2\2\u0255\u026b")
        buf.write("\5\37\20\2\u0256\u026b\5!\21\2\u0257\u026b\5#\22\2\u0258")
        buf.write("\u026b\5%\23\2\u0259\u026b\5\'\24\2\u025a\u026b\5)\25")
        buf.write("\2\u025b\u026b\5+\26\2\u025c\u026b\5-\27\2\u025d\u026b")
        buf.write("\5/\30\2\u025e\u026b\5\61\31\2\u025f\u026b\5\63\32\2\u0260")
        buf.write("\u026b\5\65\33\2\u0261\u026b\5\67\34\2\u0262\u026b\59")
        buf.write("\35\2\u0263\u026b\5;\36\2\u0264\u026b\5=\37\2\u0265\u026b")
        buf.write("\5? \2\u0266\u026b\5A!\2\u0267\u026b\5C\"\2\u0268\u026b")
        buf.write("\5E#\2\u0269\u026b\5G$\2\u026a\u0255\3\2\2\2\u026a\u0256")
        buf.write("\3\2\2\2\u026a\u0257\3\2\2\2\u026a\u0258\3\2\2\2\u026a")
        buf.write("\u0259\3\2\2\2\u026a\u025a\3\2\2\2\u026a\u025b\3\2\2\2")
        buf.write("\u026a\u025c\3\2\2\2\u026a\u025d\3\2\2\2\u026a\u025e\3")
        buf.write("\2\2\2\u026a\u025f\3\2\2\2\u026a\u0260\3\2\2\2\u026a\u0261")
        buf.write("\3\2\2\2\u026a\u0262\3\2\2\2\u026a\u0263\3\2\2\2\u026a")
        buf.write("\u0264\3\2\2\2\u026a\u0265\3\2\2\2\u026a\u0266\3\2\2\2")
        buf.write("\u026a\u0267\3\2\2\2\u026a\u0268\3\2\2\2\u026a\u0269\3")
        buf.write("\2\2\2\u026b\u008e\3\2\2\2\u026c\u0270\t\t\2\2\u026d\u026f")
        buf.write("\t\n\2\2\u026e\u026d\3\2\2\2\u026f\u0272\3\2\2\2\u0270")
        buf.write("\u026e\3\2\2\2\u0270\u0271\3\2\2\2\u0271\u0090\3\2\2\2")
        buf.write("\u0272\u0270\3\2\2\2\u0273\u0275\t\13\2\2\u0274\u0273")
        buf.write("\3\2\2\2\u0275\u0276\3\2\2\2\u0276\u0274\3\2\2\2\u0276")
        buf.write("\u0277\3\2\2\2\u0277\u0278\3\2\2\2\u0278\u0279\bI\2\2")
        buf.write("\u0279\u0092\3\2\2\2\u027a\u027b\13\2\2\2\u027b\u027c")
        buf.write("\bJ\7\2\u027c\u0094\3\2\2\2\u027d\u027e\7$\2\2\u027e\u027f")
        buf.write("\bK\b\2\u027f\u0096\3\2\2\2\u0280\u0281\5\u0099M\2\u0281")
        buf.write("\u0282\bL\t\2\u0282\u0098\3\2\2\2\u0283\u0284\7^\2\2\u0284")
        buf.write("\u0287\n\7\2\2\u0285\u0287\n\f\2\2\u0286\u0283\3\2\2\2")
        buf.write("\u0286\u0285\3\2\2\2\u0287\u009a\3\2\2\2\u0288\u0289\7")
        buf.write("\61\2\2\u0289\u028a\7,\2\2\u028a\u028e\3\2\2\2\u028b\u028d")
        buf.write("\13\2\2\2\u028c\u028b\3\2\2\2\u028d\u0290\3\2\2\2\u028e")
        buf.write("\u028f\3\2\2\2\u028e\u028c\3\2\2\2\u028f\u0291\3\2\2\2")
        buf.write("\u0290\u028e\3\2\2\2\u0291\u0292\bN\n\2\u0292\u009c\3")
        buf.write("\2\2\2\32\2\u0120\u0125\u012d\u013b\u01e7\u01f4\u0200")
        buf.write("\u021f\u0226\u022a\u022e\u0233\u0235\u023d\u0241\u0245")
        buf.write("\u024d\u024f\u026a\u0270\u0276\u0286\u028e\13\b\2\2\3")
        buf.write("C\2\3D\3\3D\4\3F\5\3J\6\3K\7\3L\b\3N\t")
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
    KEYWORD = 69
    ID = 70
    WS = 71
    ERROR_CHAR = 72
    UNCLOSE_STRING = 73
    ILLEGAL_ESCAPE = 74
    UNTERMINATED_COMMENT = 75

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
            "RS", "INTLIT", "FLOATLIT", "STRINGLIT", "KEYWORD", "ID", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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
                  "KEYWORD", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ESC_ILLEGAL", "UNTERMINATED_COMMENT" ]

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
            actions[72] = self.ERROR_CHAR_action 
            actions[73] = self.UNCLOSE_STRING_action 
            actions[74] = self.ILLEGAL_ESCAPE_action 
            actions[76] = self.UNTERMINATED_COMMENT_action 
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
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise UnterminatedComment(self.text)
     


