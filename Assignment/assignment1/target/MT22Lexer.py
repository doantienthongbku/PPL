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
        buf.write("\u02a4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u011d")
        buf.write("\n\f\3\r\3\r\3\r\5\r\u0122\n\r\3\16\3\16\3\16\3\16\7\16")
        buf.write("\u0128\n\16\f\16\16\16\u012b\13\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\7\17\u0136\n\17\f\17\16\17\u0139")
        buf.write("\13\17\3\17\7\17\u013c\n\17\f\17\16\17\u013f\13\17\3\17")
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
        buf.write("\3\64\3\64\3\64\5\64\u01e8\n\64\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u01f5\n\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u0201")
        buf.write("\n\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3")
        buf.write(">\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3C\7C\u021e\nC\fC\16")
        buf.write("C\u0221\13C\3C\3C\6C\u0225\nC\rC\16C\u0226\7C\u0229\n")
        buf.write("C\fC\16C\u022c\13C\3C\5C\u022f\nC\3D\3D\5D\u0233\nD\3")
        buf.write("D\3D\3D\3D\3D\5D\u023a\nD\3D\5D\u023d\nD\3D\3D\3D\5D\u0242")
        buf.write("\nD\3D\3D\3E\6E\u0247\nE\rE\16E\u0248\3E\3E\6E\u024d\n")
        buf.write("E\rE\16E\u024e\7E\u0251\nE\fE\16E\u0254\13E\3F\3F\5F\u0258")
        buf.write("\nF\3F\6F\u025b\nF\rF\16F\u025c\3G\3G\7G\u0261\nG\fG\16")
        buf.write("G\u0264\13G\3H\3H\7H\u0268\nH\fH\16H\u026b\13H\3H\3H\3")
        buf.write("H\3I\3I\5I\u0272\nI\3J\3J\3J\3K\3K\3K\5K\u027a\nK\3L\3")
        buf.write("L\3M\3M\7M\u0280\nM\fM\16M\u0283\13M\3N\6N\u0286\nN\r")
        buf.write("N\16N\u0287\3N\3N\3O\3O\3O\3P\3P\7P\u0291\nP\fP\16P\u0294")
        buf.write("\13P\3P\5P\u0297\nP\3P\3P\3Q\3Q\7Q\u029d\nQ\fQ\16Q\u02a0")
        buf.write("\13Q\3Q\3Q\3Q\4\u0129\u0137\2R\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089\2\u008b\2\u008d\2\u008fF")
        buf.write("\u0091\2\u0093\2\u0095\2\u0097\2\u0099G\u009bH\u009dI")
        buf.write("\u009fJ\u00a1K\3\2\r\4\2\f\f\17\17\3\2\63;\3\2\62;\4\2")
        buf.write("GGgg\4\2--//\6\2\f\f\16\17$$^^\n\2$$))^^ddhhppttvv\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\5\2\n\f\16\17\"\"\6\3\f\f\16\17")
        buf.write("$$^^\2\u02d3\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\3\u00a3\3\2\2")
        buf.write("\2\5\u00af\3\2\2\2\7\u00bc\3\2\2\2\t\u00c6\3\2\2\2\13")
        buf.write("\u00d1\3\2\2\2\r\u00dd\3\2\2\2\17\u00ea\3\2\2\2\21\u00f5")
        buf.write("\3\2\2\2\23\u0101\3\2\2\2\25\u0107\3\2\2\2\27\u011c\3")
        buf.write("\2\2\2\31\u0121\3\2\2\2\33\u0123\3\2\2\2\35\u0131\3\2")
        buf.write("\2\2\37\u0142\3\2\2\2!\u0147\3\2\2\2#\u014d\3\2\2\2%\u0155")
        buf.write("\3\2\2\2\'\u0158\3\2\2\2)\u015d\3\2\2\2+\u0163\3\2\2\2")
        buf.write("-\u0169\3\2\2\2/\u016d\3\2\2\2\61\u0176\3\2\2\2\63\u0179")
        buf.write("\3\2\2\2\65\u0181\3\2\2\2\67\u0188\3\2\2\29\u018f\3\2")
        buf.write("\2\2;\u0194\3\2\2\2=\u019a\3\2\2\2?\u019f\3\2\2\2A\u01a3")
        buf.write("\3\2\2\2C\u01ac\3\2\2\2E\u01af\3\2\2\2G\u01b7\3\2\2\2")
        buf.write("I\u01bd\3\2\2\2K\u01bf\3\2\2\2M\u01c1\3\2\2\2O\u01c3\3")
        buf.write("\2\2\2Q\u01c5\3\2\2\2S\u01c7\3\2\2\2U\u01c9\3\2\2\2W\u01cc")
        buf.write("\3\2\2\2Y\u01cf\3\2\2\2[\u01d2\3\2\2\2]\u01d5\3\2\2\2")
        buf.write("_\u01d7\3\2\2\2a\u01da\3\2\2\2c\u01dc\3\2\2\2e\u01df\3")
        buf.write("\2\2\2g\u01e7\3\2\2\2i\u01f4\3\2\2\2k\u0200\3\2\2\2m\u0202")
        buf.write("\3\2\2\2o\u0204\3\2\2\2q\u0206\3\2\2\2s\u0208\3\2\2\2")
        buf.write("u\u020a\3\2\2\2w\u020c\3\2\2\2y\u020e\3\2\2\2{\u0210\3")
        buf.write("\2\2\2}\u0212\3\2\2\2\177\u0214\3\2\2\2\u0081\u0216\3")
        buf.write("\2\2\2\u0083\u0218\3\2\2\2\u0085\u022e\3\2\2\2\u0087\u0241")
        buf.write("\3\2\2\2\u0089\u0246\3\2\2\2\u008b\u0255\3\2\2\2\u008d")
        buf.write("\u025e\3\2\2\2\u008f\u0265\3\2\2\2\u0091\u0271\3\2\2\2")
        buf.write("\u0093\u0273\3\2\2\2\u0095\u0279\3\2\2\2\u0097\u027b\3")
        buf.write("\2\2\2\u0099\u027d\3\2\2\2\u009b\u0285\3\2\2\2\u009d\u028b")
        buf.write("\3\2\2\2\u009f\u028e\3\2\2\2\u00a1\u029a\3\2\2\2\u00a3")
        buf.write("\u00a4\7t\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6\7c\2\2\u00a6")
        buf.write("\u00a7\7f\2\2\u00a7\u00a8\7K\2\2\u00a8\u00a9\7p\2\2\u00a9")
        buf.write("\u00aa\7v\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7i\2\2\u00ac")
        buf.write("\u00ad\7g\2\2\u00ad\u00ae\7t\2\2\u00ae\4\3\2\2\2\u00af")
        buf.write("\u00b0\7r\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2\7k\2\2\u00b2")
        buf.write("\u00b3\7p\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5\7K\2\2\u00b5")
        buf.write("\u00b6\7p\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8\7g\2\2\u00b8")
        buf.write("\u00b9\7i\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb\7t\2\2\u00bb")
        buf.write("\6\3\2\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be\7g\2\2\u00be")
        buf.write("\u00bf\7c\2\2\u00bf\u00c0\7f\2\2\u00c0\u00c1\7H\2\2\u00c1")
        buf.write("\u00c2\7n\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4\7c\2\2\u00c4")
        buf.write("\u00c5\7v\2\2\u00c5\b\3\2\2\2\u00c6\u00c7\7r\2\2\u00c7")
        buf.write("\u00c8\7t\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7p\2\2\u00ca")
        buf.write("\u00cb\7v\2\2\u00cb\u00cc\7H\2\2\u00cc\u00cd\7n\2\2\u00cd")
        buf.write("\u00ce\7q\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0\7v\2\2\u00d0")
        buf.write("\n\3\2\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3\7g\2\2\u00d3")
        buf.write("\u00d4\7c\2\2\u00d4\u00d5\7f\2\2\u00d5\u00d6\7D\2\2\u00d6")
        buf.write("\u00d7\7q\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7n\2\2\u00d9")
        buf.write("\u00da\7g\2\2\u00da\u00db\7c\2\2\u00db\u00dc\7p\2\2\u00dc")
        buf.write("\f\3\2\2\2\u00dd\u00de\7r\2\2\u00de\u00df\7t\2\2\u00df")
        buf.write("\u00e0\7k\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7v\2\2\u00e2")
        buf.write("\u00e3\7D\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7q\2\2\u00e5")
        buf.write("\u00e6\7n\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8\7c\2\2\u00e8")
        buf.write("\u00e9\7p\2\2\u00e9\16\3\2\2\2\u00ea\u00eb\7t\2\2\u00eb")
        buf.write("\u00ec\7g\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee\7f\2\2\u00ee")
        buf.write("\u00ef\7U\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1\7t\2\2\u00f1")
        buf.write("\u00f2\7k\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4\7i\2\2\u00f4")
        buf.write("\20\3\2\2\2\u00f5\u00f6\7r\2\2\u00f6\u00f7\7t\2\2\u00f7")
        buf.write("\u00f8\7k\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa\7v\2\2\u00fa")
        buf.write("\u00fb\7U\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7t\2\2\u00fd")
        buf.write("\u00fe\7k\2\2\u00fe\u00ff\7p\2\2\u00ff\u0100\7i\2\2\u0100")
        buf.write("\22\3\2\2\2\u0101\u0102\7u\2\2\u0102\u0103\7w\2\2\u0103")
        buf.write("\u0104\7r\2\2\u0104\u0105\7g\2\2\u0105\u0106\7t\2\2\u0106")
        buf.write("\24\3\2\2\2\u0107\u0108\7r\2\2\u0108\u0109\7t\2\2\u0109")
        buf.write("\u010a\7g\2\2\u010a\u010b\7x\2\2\u010b\u010c\7g\2\2\u010c")
        buf.write("\u010d\7p\2\2\u010d\u010e\7v\2\2\u010e\u010f\7F\2\2\u010f")
        buf.write("\u0110\7g\2\2\u0110\u0111\7h\2\2\u0111\u0112\7c\2\2\u0112")
        buf.write("\u0113\7w\2\2\u0113\u0114\7n\2\2\u0114\u0115\7v\2\2\u0115")
        buf.write("\26\3\2\2\2\u0116\u011d\5]/\2\u0117\u011d\5_\60\2\u0118")
        buf.write("\u011d\5a\61\2\u0119\u011d\5c\62\2\u011a\u011d\5Y-\2\u011b")
        buf.write("\u011d\5[.\2\u011c\u0116\3\2\2\2\u011c\u0117\3\2\2\2\u011c")
        buf.write("\u0118\3\2\2\2\u011c\u0119\3\2\2\2\u011c\u011a\3\2\2\2")
        buf.write("\u011c\u011b\3\2\2\2\u011d\30\3\2\2\2\u011e\u0122\5M\'")
        buf.write("\2\u011f\u0122\5O(\2\u0120\u0122\5Q)\2\u0121\u011e\3\2")
        buf.write("\2\2\u0121\u011f\3\2\2\2\u0121\u0120\3\2\2\2\u0122\32")
        buf.write("\3\2\2\2\u0123\u0124\7\61\2\2\u0124\u0125\7,\2\2\u0125")
        buf.write("\u0129\3\2\2\2\u0126\u0128\13\2\2\2\u0127\u0126\3\2\2")
        buf.write("\2\u0128\u012b\3\2\2\2\u0129\u012a\3\2\2\2\u0129\u0127")
        buf.write("\3\2\2\2\u012a\u012c\3\2\2\2\u012b\u0129\3\2\2\2\u012c")
        buf.write("\u012d\7,\2\2\u012d\u012e\7\61\2\2\u012e\u012f\3\2\2\2")
        buf.write("\u012f\u0130\b\16\2\2\u0130\34\3\2\2\2\u0131\u0132\7\61")
        buf.write("\2\2\u0132\u0133\7\61\2\2\u0133\u0137\3\2\2\2\u0134\u0136")
        buf.write("\13\2\2\2\u0135\u0134\3\2\2\2\u0136\u0139\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u013d\3\2\2\2")
        buf.write("\u0139\u0137\3\2\2\2\u013a\u013c\n\2\2\2\u013b\u013a\3")
        buf.write("\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e")
        buf.write("\3\2\2\2\u013e\u0140\3\2\2\2\u013f\u013d\3\2\2\2\u0140")
        buf.write("\u0141\b\17\2\2\u0141\36\3\2\2\2\u0142\u0143\7c\2\2\u0143")
        buf.write("\u0144\7w\2\2\u0144\u0145\7v\2\2\u0145\u0146\7q\2\2\u0146")
        buf.write(" \3\2\2\2\u0147\u0148\7d\2\2\u0148\u0149\7t\2\2\u0149")
        buf.write("\u014a\7g\2\2\u014a\u014b\7c\2\2\u014b\u014c\7m\2\2\u014c")
        buf.write("\"\3\2\2\2\u014d\u014e\7d\2\2\u014e\u014f\7q\2\2\u014f")
        buf.write("\u0150\7q\2\2\u0150\u0151\7n\2\2\u0151\u0152\7g\2\2\u0152")
        buf.write("\u0153\7c\2\2\u0153\u0154\7p\2\2\u0154$\3\2\2\2\u0155")
        buf.write("\u0156\7f\2\2\u0156\u0157\7q\2\2\u0157&\3\2\2\2\u0158")
        buf.write("\u0159\7g\2\2\u0159\u015a\7n\2\2\u015a\u015b\7u\2\2\u015b")
        buf.write("\u015c\7g\2\2\u015c(\3\2\2\2\u015d\u015e\7h\2\2\u015e")
        buf.write("\u015f\7c\2\2\u015f\u0160\7n\2\2\u0160\u0161\7u\2\2\u0161")
        buf.write("\u0162\7g\2\2\u0162*\3\2\2\2\u0163\u0164\7h\2\2\u0164")
        buf.write("\u0165\7n\2\2\u0165\u0166\7q\2\2\u0166\u0167\7c\2\2\u0167")
        buf.write("\u0168\7v\2\2\u0168,\3\2\2\2\u0169\u016a\7h\2\2\u016a")
        buf.write("\u016b\7q\2\2\u016b\u016c\7t\2\2\u016c.\3\2\2\2\u016d")
        buf.write("\u016e\7h\2\2\u016e\u016f\7w\2\2\u016f\u0170\7p\2\2\u0170")
        buf.write("\u0171\7e\2\2\u0171\u0172\7v\2\2\u0172\u0173\7k\2\2\u0173")
        buf.write("\u0174\7q\2\2\u0174\u0175\7p\2\2\u0175\60\3\2\2\2\u0176")
        buf.write("\u0177\7k\2\2\u0177\u0178\7h\2\2\u0178\62\3\2\2\2\u0179")
        buf.write("\u017a\7k\2\2\u017a\u017b\7p\2\2\u017b\u017c\7v\2\2\u017c")
        buf.write("\u017d\7g\2\2\u017d\u017e\7i\2\2\u017e\u017f\7g\2\2\u017f")
        buf.write("\u0180\7t\2\2\u0180\64\3\2\2\2\u0181\u0182\7t\2\2\u0182")
        buf.write("\u0183\7g\2\2\u0183\u0184\7v\2\2\u0184\u0185\7w\2\2\u0185")
        buf.write("\u0186\7t\2\2\u0186\u0187\7p\2\2\u0187\66\3\2\2\2\u0188")
        buf.write("\u0189\7u\2\2\u0189\u018a\7v\2\2\u018a\u018b\7t\2\2\u018b")
        buf.write("\u018c\7k\2\2\u018c\u018d\7p\2\2\u018d\u018e\7i\2\2\u018e")
        buf.write("8\3\2\2\2\u018f\u0190\7v\2\2\u0190\u0191\7t\2\2\u0191")
        buf.write("\u0192\7w\2\2\u0192\u0193\7g\2\2\u0193:\3\2\2\2\u0194")
        buf.write("\u0195\7y\2\2\u0195\u0196\7j\2\2\u0196\u0197\7k\2\2\u0197")
        buf.write("\u0198\7n\2\2\u0198\u0199\7g\2\2\u0199<\3\2\2\2\u019a")
        buf.write("\u019b\7x\2\2\u019b\u019c\7q\2\2\u019c\u019d\7k\2\2\u019d")
        buf.write("\u019e\7f\2\2\u019e>\3\2\2\2\u019f\u01a0\7q\2\2\u01a0")
        buf.write("\u01a1\7w\2\2\u01a1\u01a2\7v\2\2\u01a2@\3\2\2\2\u01a3")
        buf.write("\u01a4\7e\2\2\u01a4\u01a5\7q\2\2\u01a5\u01a6\7p\2\2\u01a6")
        buf.write("\u01a7\7v\2\2\u01a7\u01a8\7k\2\2\u01a8\u01a9\7p\2\2\u01a9")
        buf.write("\u01aa\7w\2\2\u01aa\u01ab\7g\2\2\u01abB\3\2\2\2\u01ac")
        buf.write("\u01ad\7q\2\2\u01ad\u01ae\7h\2\2\u01aeD\3\2\2\2\u01af")
        buf.write("\u01b0\7k\2\2\u01b0\u01b1\7p\2\2\u01b1\u01b2\7j\2\2\u01b2")
        buf.write("\u01b3\7g\2\2\u01b3\u01b4\7t\2\2\u01b4\u01b5\7k\2\2\u01b5")
        buf.write("\u01b6\7v\2\2\u01b6F\3\2\2\2\u01b7\u01b8\7c\2\2\u01b8")
        buf.write("\u01b9\7t\2\2\u01b9\u01ba\7t\2\2\u01ba\u01bb\7c\2\2\u01bb")
        buf.write("\u01bc\7{\2\2\u01bcH\3\2\2\2\u01bd\u01be\7-\2\2\u01be")
        buf.write("J\3\2\2\2\u01bf\u01c0\7/\2\2\u01c0L\3\2\2\2\u01c1\u01c2")
        buf.write("\7,\2\2\u01c2N\3\2\2\2\u01c3\u01c4\7\61\2\2\u01c4P\3\2")
        buf.write("\2\2\u01c5\u01c6\7\'\2\2\u01c6R\3\2\2\2\u01c7\u01c8\7")
        buf.write("#\2\2\u01c8T\3\2\2\2\u01c9\u01ca\7(\2\2\u01ca\u01cb\7")
        buf.write("(\2\2\u01cbV\3\2\2\2\u01cc\u01cd\7~\2\2\u01cd\u01ce\7")
        buf.write("~\2\2\u01ceX\3\2\2\2\u01cf\u01d0\7?\2\2\u01d0\u01d1\7")
        buf.write("?\2\2\u01d1Z\3\2\2\2\u01d2\u01d3\7#\2\2\u01d3\u01d4\7")
        buf.write("?\2\2\u01d4\\\3\2\2\2\u01d5\u01d6\7>\2\2\u01d6^\3\2\2")
        buf.write("\2\u01d7\u01d8\7>\2\2\u01d8\u01d9\7?\2\2\u01d9`\3\2\2")
        buf.write("\2\u01da\u01db\7@\2\2\u01dbb\3\2\2\2\u01dc\u01dd\7@\2")
        buf.write("\2\u01dd\u01de\7?\2\2\u01ded\3\2\2\2\u01df\u01e0\7<\2")
        buf.write("\2\u01e0\u01e1\7<\2\2\u01e1f\3\2\2\2\u01e2\u01e8\5S*\2")
        buf.write("\u01e3\u01e8\5U+\2\u01e4\u01e8\5W,\2\u01e5\u01e8\5Y-\2")
        buf.write("\u01e6\u01e8\5[.\2\u01e7\u01e2\3\2\2\2\u01e7\u01e3\3\2")
        buf.write("\2\2\u01e7\u01e4\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7\u01e6")
        buf.write("\3\2\2\2\u01e8h\3\2\2\2\u01e9\u01f5\5I%\2\u01ea\u01f5")
        buf.write("\5K&\2\u01eb\u01f5\5M\'\2\u01ec\u01f5\5O(\2\u01ed\u01f5")
        buf.write("\5Q)\2\u01ee\u01f5\5Y-\2\u01ef\u01f5\5[.\2\u01f0\u01f5")
        buf.write("\5]/\2\u01f1\u01f5\5_\60\2\u01f2\u01f5\5a\61\2\u01f3\u01f5")
        buf.write("\5c\62\2\u01f4\u01e9\3\2\2\2\u01f4\u01ea\3\2\2\2\u01f4")
        buf.write("\u01eb\3\2\2\2\u01f4\u01ec\3\2\2\2\u01f4\u01ed\3\2\2\2")
        buf.write("\u01f4\u01ee\3\2\2\2\u01f4\u01ef\3\2\2\2\u01f4\u01f0\3")
        buf.write("\2\2\2\u01f4\u01f1\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f3")
        buf.write("\3\2\2\2\u01f5j\3\2\2\2\u01f6\u0201\5I%\2\u01f7\u0201")
        buf.write("\5K&\2\u01f8\u0201\5M\'\2\u01f9\u0201\5O(\2\u01fa\u0201")
        buf.write("\5Y-\2\u01fb\u0201\5[.\2\u01fc\u0201\5]/\2\u01fd\u0201")
        buf.write("\5_\60\2\u01fe\u0201\5a\61\2\u01ff\u0201\5c\62\2\u0200")
        buf.write("\u01f6\3\2\2\2\u0200\u01f7\3\2\2\2\u0200\u01f8\3\2\2\2")
        buf.write("\u0200\u01f9\3\2\2\2\u0200\u01fa\3\2\2\2\u0200\u01fb\3")
        buf.write("\2\2\2\u0200\u01fc\3\2\2\2\u0200\u01fd\3\2\2\2\u0200\u01fe")
        buf.write("\3\2\2\2\u0200\u01ff\3\2\2\2\u0201l\3\2\2\2\u0202\u0203")
        buf.write("\5e\63\2\u0203n\3\2\2\2\u0204\u0205\7.\2\2\u0205p\3\2")
        buf.write("\2\2\u0206\u0207\7=\2\2\u0207r\3\2\2\2\u0208\u0209\7?")
        buf.write("\2\2\u0209t\3\2\2\2\u020a\u020b\7<\2\2\u020bv\3\2\2\2")
        buf.write("\u020c\u020d\7\60\2\2\u020dx\3\2\2\2\u020e\u020f\7*\2")
        buf.write("\2\u020fz\3\2\2\2\u0210\u0211\7+\2\2\u0211|\3\2\2\2\u0212")
        buf.write("\u0213\7}\2\2\u0213~\3\2\2\2\u0214\u0215\7\177\2\2\u0215")
        buf.write("\u0080\3\2\2\2\u0216\u0217\7]\2\2\u0217\u0082\3\2\2\2")
        buf.write("\u0218\u0219\7_\2\2\u0219\u0084\3\2\2\2\u021a\u022f\7")
        buf.write("\62\2\2\u021b\u021f\t\3\2\2\u021c\u021e\t\4\2\2\u021d")
        buf.write("\u021c\3\2\2\2\u021e\u0221\3\2\2\2\u021f\u021d\3\2\2\2")
        buf.write("\u021f\u0220\3\2\2\2\u0220\u022a\3\2\2\2\u0221\u021f\3")
        buf.write("\2\2\2\u0222\u0224\7a\2\2\u0223\u0225\t\4\2\2\u0224\u0223")
        buf.write("\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0224\3\2\2\2\u0226")
        buf.write("\u0227\3\2\2\2\u0227\u0229\3\2\2\2\u0228\u0222\3\2\2\2")
        buf.write("\u0229\u022c\3\2\2\2\u022a\u0228\3\2\2\2\u022a\u022b\3")
        buf.write("\2\2\2\u022b\u022d\3\2\2\2\u022c\u022a\3\2\2\2\u022d\u022f")
        buf.write("\bC\3\2\u022e\u021a\3\2\2\2\u022e\u021b\3\2\2\2\u022f")
        buf.write("\u0086\3\2\2\2\u0230\u0232\5\u0089E\2\u0231\u0233\5\u008d")
        buf.write("G\2\u0232\u0231\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u0234")
        buf.write("\3\2\2\2\u0234\u0235\5\u008bF\2\u0235\u0242\3\2\2\2\u0236")
        buf.write("\u0237\5\u0089E\2\u0237\u0239\5\u008dG\2\u0238\u023a\5")
        buf.write("\u008bF\2\u0239\u0238\3\2\2\2\u0239\u023a\3\2\2\2\u023a")
        buf.write("\u0242\3\2\2\2\u023b\u023d\5\u0089E\2\u023c\u023b\3\2")
        buf.write("\2\2\u023c\u023d\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u023f")
        buf.write("\5\u008dG\2\u023f\u0240\5\u008bF\2\u0240\u0242\3\2\2\2")
        buf.write("\u0241\u0230\3\2\2\2\u0241\u0236\3\2\2\2\u0241\u023c\3")
        buf.write("\2\2\2\u0242\u0243\3\2\2\2\u0243\u0244\bD\4\2\u0244\u0088")
        buf.write("\3\2\2\2\u0245\u0247\t\4\2\2\u0246\u0245\3\2\2\2\u0247")
        buf.write("\u0248\3\2\2\2\u0248\u0246\3\2\2\2\u0248\u0249\3\2\2\2")
        buf.write("\u0249\u0252\3\2\2\2\u024a\u024c\7a\2\2\u024b\u024d\t")
        buf.write("\4\2\2\u024c\u024b\3\2\2\2\u024d\u024e\3\2\2\2\u024e\u024c")
        buf.write("\3\2\2\2\u024e\u024f\3\2\2\2\u024f\u0251\3\2\2\2\u0250")
        buf.write("\u024a\3\2\2\2\u0251\u0254\3\2\2\2\u0252\u0250\3\2\2\2")
        buf.write("\u0252\u0253\3\2\2\2\u0253\u008a\3\2\2\2\u0254\u0252\3")
        buf.write("\2\2\2\u0255\u0257\t\5\2\2\u0256\u0258\t\6\2\2\u0257\u0256")
        buf.write("\3\2\2\2\u0257\u0258\3\2\2\2\u0258\u025a\3\2\2\2\u0259")
        buf.write("\u025b\t\4\2\2\u025a\u0259\3\2\2\2\u025b\u025c\3\2\2\2")
        buf.write("\u025c\u025a\3\2\2\2\u025c\u025d\3\2\2\2\u025d\u008c\3")
        buf.write("\2\2\2\u025e\u0262\7\60\2\2\u025f\u0261\t\4\2\2\u0260")
        buf.write("\u025f\3\2\2\2\u0261\u0264\3\2\2\2\u0262\u0260\3\2\2\2")
        buf.write("\u0262\u0263\3\2\2\2\u0263\u008e\3\2\2\2\u0264\u0262\3")
        buf.write("\2\2\2\u0265\u0269\5\u0097L\2\u0266\u0268\5\u0091I\2\u0267")
        buf.write("\u0266\3\2\2\2\u0268\u026b\3\2\2\2\u0269\u0267\3\2\2\2")
        buf.write("\u0269\u026a\3\2\2\2\u026a\u026c\3\2\2\2\u026b\u0269\3")
        buf.write("\2\2\2\u026c\u026d\5\u0097L\2\u026d\u026e\bH\5\2\u026e")
        buf.write("\u0090\3\2\2\2\u026f\u0272\n\7\2\2\u0270\u0272\5\u0093")
        buf.write("J\2\u0271\u026f\3\2\2\2\u0271\u0270\3\2\2\2\u0272\u0092")
        buf.write("\3\2\2\2\u0273\u0274\7^\2\2\u0274\u0275\t\b\2\2\u0275")
        buf.write("\u0094\3\2\2\2\u0276\u0277\7^\2\2\u0277\u027a\n\b\2\2")
        buf.write("\u0278\u027a\7^\2\2\u0279\u0276\3\2\2\2\u0279\u0278\3")
        buf.write("\2\2\2\u027a\u0096\3\2\2\2\u027b\u027c\7$\2\2\u027c\u0098")
        buf.write("\3\2\2\2\u027d\u0281\t\t\2\2\u027e\u0280\t\n\2\2\u027f")
        buf.write("\u027e\3\2\2\2\u0280\u0283\3\2\2\2\u0281\u027f\3\2\2\2")
        buf.write("\u0281\u0282\3\2\2\2\u0282\u009a\3\2\2\2\u0283\u0281\3")
        buf.write("\2\2\2\u0284\u0286\t\13\2\2\u0285\u0284\3\2\2\2\u0286")
        buf.write("\u0287\3\2\2\2\u0287\u0285\3\2\2\2\u0287\u0288\3\2\2\2")
        buf.write("\u0288\u0289\3\2\2\2\u0289\u028a\bN\2\2\u028a\u009c\3")
        buf.write("\2\2\2\u028b\u028c\13\2\2\2\u028c\u028d\bO\6\2\u028d\u009e")
        buf.write("\3\2\2\2\u028e\u0292\5\u0097L\2\u028f\u0291\5\u0091I\2")
        buf.write("\u0290\u028f\3\2\2\2\u0291\u0294\3\2\2\2\u0292\u0290\3")
        buf.write("\2\2\2\u0292\u0293\3\2\2\2\u0293\u0296\3\2\2\2\u0294\u0292")
        buf.write("\3\2\2\2\u0295\u0297\t\f\2\2\u0296\u0295\3\2\2\2\u0297")
        buf.write("\u0298\3\2\2\2\u0298\u0299\bP\7\2\u0299\u00a0\3\2\2\2")
        buf.write("\u029a\u029e\5\u0097L\2\u029b\u029d\5\u0091I\2\u029c\u029b")
        buf.write("\3\2\2\2\u029d\u02a0\3\2\2\2\u029e\u029c\3\2\2\2\u029e")
        buf.write("\u029f\3\2\2\2\u029f\u02a1\3\2\2\2\u02a0\u029e\3\2\2\2")
        buf.write("\u02a1\u02a2\5\u0095K\2\u02a2\u02a3\bQ\b\2\u02a3\u00a2")
        buf.write("\3\2\2\2!\2\u011c\u0121\u0129\u0137\u013d\u01e7\u01f4")
        buf.write("\u0200\u021f\u0226\u022a\u022e\u0232\u0239\u023c\u0241")
        buf.write("\u0248\u024e\u0252\u0257\u025c\u0262\u0269\u0271\u0279")
        buf.write("\u0281\u0287\u0292\u0296\u029e\t\b\2\2\3C\2\3D\3\3H\4")
        buf.write("\3O\5\3P\6\3Q\7")
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
    SEMI = 56
    ASSIGN = 57
    COLON = 58
    DOT = 59
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
            "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "','", "';'", 
            "'='", "':'", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "OP_RELATIONAL", "OP_MUL", "BLOCK_COMMENT", "LINE_COMMENT", 
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
            "DIFF", "SMALLER", "SMALLER_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
            "CONCAT", "OP_BOOL", "OP_INT", "OP_FLOAT", "OP_STRING", "COMMA", 
            "SEMI", "ASSIGN", "COLON", "DOT", "LB", "RB", "LP", "RP", "LS", 
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
                  "SEMI", "ASSIGN", "COLON", "DOT", "LB", "RB", "LP", "RP", 
                  "LS", "RS", "INTLIT", "FLOATLIT", "DIGIT_UNDERSCORE", 
                  "SCIENTIFIC", "DECIMAL", "STRINGLIT", "StringChar", "EscapeSequence", 
                  "IllegalString", "DoubleQuote", "ID", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[70] = self.STRINGLIT_action 
            actions[77] = self.ERROR_CHAR_action 
            actions[78] = self.UNCLOSE_STRING_action 
            actions[79] = self.ILLEGAL_ESCAPE_action 
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
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             
            	result = str(self.text)
            	self.text = result[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise ErrorToken(self.text) 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	unclose_str = str(self.text)
            	possible = ['\f', '\n', '\r', '"', '\\']
            	if unclose_str[-1] in possible:
            		raise UncloseString(unclose_str[1:-1])
            	else:
            		raise UncloseString(unclose_str[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	illegal_str = str(self.text)
            	raise IllegalEscape(illegal_str[1:]) 

     


