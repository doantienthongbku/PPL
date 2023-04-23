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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2I")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u0117\n\f\f\f\16\f\u011a")
        buf.write("\13\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\7\r\u0125\n")
        buf.write("\r\f\r\16\r\u0128\13\r\3\r\7\r\u012b\n\r\f\r\16\r\u012e")
        buf.write("\13\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*")
        buf.write("\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\5\62\u01d7")
        buf.write("\n\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\5\63\u01e4\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\64\5\64\u01f0\n\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3")
        buf.write("?\3?\3@\3@\3A\3A\3A\7A\u020d\nA\fA\16A\u0210\13A\3A\3")
        buf.write("A\6A\u0214\nA\rA\16A\u0215\7A\u0218\nA\fA\16A\u021b\13")
        buf.write("A\3A\5A\u021e\nA\3B\3B\5B\u0222\nB\3B\3B\3B\3B\3B\5B\u0229")
        buf.write("\nB\3B\5B\u022c\nB\3B\3B\3B\5B\u0231\nB\3B\3B\3C\6C\u0236")
        buf.write("\nC\rC\16C\u0237\3C\3C\6C\u023c\nC\rC\16C\u023d\7C\u0240")
        buf.write("\nC\fC\16C\u0243\13C\3D\3D\5D\u0247\nD\3D\6D\u024a\nD")
        buf.write("\rD\16D\u024b\3E\3E\7E\u0250\nE\fE\16E\u0253\13E\3F\3")
        buf.write("F\7F\u0257\nF\fF\16F\u025a\13F\3F\3F\3F\3G\3G\5G\u0261")
        buf.write("\nG\3H\3H\3H\3I\3I\3I\5I\u0269\nI\3J\3J\3K\3K\7K\u026f")
        buf.write("\nK\fK\16K\u0272\13K\3L\6L\u0275\nL\rL\16L\u0276\3L\3")
        buf.write("L\3M\3M\3M\3N\3N\7N\u0280\nN\fN\16N\u0283\13N\3N\5N\u0286")
        buf.write("\nN\3N\3N\3O\3O\7O\u028c\nO\fO\16O\u028f\13O\3O\3O\3O")
        buf.write("\4\u0118\u0126\2P\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085\2")
        buf.write("\u0087\2\u0089\2\u008bD\u008d\2\u008f\2\u0091\2\u0093")
        buf.write("\2\u0095E\u0097F\u0099G\u009bH\u009dI\3\2\r\4\2\f\f\17")
        buf.write("\17\3\2\63;\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\16\17$$^^")
        buf.write("\n\2$$))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\f")
        buf.write("\16\17\"\"\6\3\f\f\16\17$$^^\2\u02bb\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2")
        buf.write("\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\3\u009f\3\2\2\2\5\u00ab")
        buf.write("\3\2\2\2\7\u00b8\3\2\2\2\t\u00c2\3\2\2\2\13\u00cd\3\2")
        buf.write("\2\2\r\u00d9\3\2\2\2\17\u00e6\3\2\2\2\21\u00f1\3\2\2\2")
        buf.write("\23\u00fd\3\2\2\2\25\u0103\3\2\2\2\27\u0112\3\2\2\2\31")
        buf.write("\u0120\3\2\2\2\33\u0131\3\2\2\2\35\u0136\3\2\2\2\37\u013c")
        buf.write("\3\2\2\2!\u0144\3\2\2\2#\u0147\3\2\2\2%\u014c\3\2\2\2")
        buf.write("\'\u0152\3\2\2\2)\u0158\3\2\2\2+\u015c\3\2\2\2-\u0165")
        buf.write("\3\2\2\2/\u0168\3\2\2\2\61\u0170\3\2\2\2\63\u0177\3\2")
        buf.write("\2\2\65\u017e\3\2\2\2\67\u0183\3\2\2\29\u0189\3\2\2\2")
        buf.write(";\u018e\3\2\2\2=\u0192\3\2\2\2?\u019b\3\2\2\2A\u019e\3")
        buf.write("\2\2\2C\u01a6\3\2\2\2E\u01ac\3\2\2\2G\u01ae\3\2\2\2I\u01b0")
        buf.write("\3\2\2\2K\u01b2\3\2\2\2M\u01b4\3\2\2\2O\u01b6\3\2\2\2")
        buf.write("Q\u01b8\3\2\2\2S\u01bb\3\2\2\2U\u01be\3\2\2\2W\u01c1\3")
        buf.write("\2\2\2Y\u01c4\3\2\2\2[\u01c6\3\2\2\2]\u01c9\3\2\2\2_\u01cb")
        buf.write("\3\2\2\2a\u01ce\3\2\2\2c\u01d6\3\2\2\2e\u01e3\3\2\2\2")
        buf.write("g\u01ef\3\2\2\2i\u01f1\3\2\2\2k\u01f3\3\2\2\2m\u01f5\3")
        buf.write("\2\2\2o\u01f7\3\2\2\2q\u01f9\3\2\2\2s\u01fb\3\2\2\2u\u01fd")
        buf.write("\3\2\2\2w\u01ff\3\2\2\2y\u0201\3\2\2\2{\u0203\3\2\2\2")
        buf.write("}\u0205\3\2\2\2\177\u0207\3\2\2\2\u0081\u021d\3\2\2\2")
        buf.write("\u0083\u0230\3\2\2\2\u0085\u0235\3\2\2\2\u0087\u0244\3")
        buf.write("\2\2\2\u0089\u024d\3\2\2\2\u008b\u0254\3\2\2\2\u008d\u0260")
        buf.write("\3\2\2\2\u008f\u0262\3\2\2\2\u0091\u0268\3\2\2\2\u0093")
        buf.write("\u026a\3\2\2\2\u0095\u026c\3\2\2\2\u0097\u0274\3\2\2\2")
        buf.write("\u0099\u027a\3\2\2\2\u009b\u027d\3\2\2\2\u009d\u0289\3")
        buf.write("\2\2\2\u009f\u00a0\7t\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2")
        buf.write("\7c\2\2\u00a2\u00a3\7f\2\2\u00a3\u00a4\7K\2\2\u00a4\u00a5")
        buf.write("\7p\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8")
        buf.write("\7i\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7t\2\2\u00aa\4")
        buf.write("\3\2\2\2\u00ab\u00ac\7r\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae")
        buf.write("\7k\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1")
        buf.write("\7K\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4")
        buf.write("\7g\2\2\u00b4\u00b5\7i\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7")
        buf.write("\7t\2\2\u00b7\6\3\2\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7f\2\2\u00bc\u00bd")
        buf.write("\7H\2\2\u00bd\u00be\7n\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0")
        buf.write("\7c\2\2\u00c0\u00c1\7v\2\2\u00c1\b\3\2\2\2\u00c2\u00c3")
        buf.write("\7r\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6")
        buf.write("\7p\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8\7H\2\2\u00c8\u00c9")
        buf.write("\7n\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc")
        buf.write("\7v\2\2\u00cc\n\3\2\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf")
        buf.write("\7g\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7f\2\2\u00d1\u00d2")
        buf.write("\7D\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5")
        buf.write("\7n\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8")
        buf.write("\7p\2\2\u00d8\f\3\2\2\2\u00d9\u00da\7r\2\2\u00da\u00db")
        buf.write("\7t\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de")
        buf.write("\7v\2\2\u00de\u00df\7D\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1")
        buf.write("\7q\2\2\u00e1\u00e2\7n\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4")
        buf.write("\7c\2\2\u00e4\u00e5\7p\2\2\u00e5\16\3\2\2\2\u00e6\u00e7")
        buf.write("\7t\2\2\u00e7\u00e8\7g\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea")
        buf.write("\7f\2\2\u00ea\u00eb\7U\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed")
        buf.write("\7t\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0")
        buf.write("\7i\2\2\u00f0\20\3\2\2\2\u00f1\u00f2\7r\2\2\u00f2\u00f3")
        buf.write("\7t\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6")
        buf.write("\7v\2\2\u00f6\u00f7\7U\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9")
        buf.write("\7t\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc")
        buf.write("\7i\2\2\u00fc\22\3\2\2\2\u00fd\u00fe\7u\2\2\u00fe\u00ff")
        buf.write("\7w\2\2\u00ff\u0100\7r\2\2\u0100\u0101\7g\2\2\u0101\u0102")
        buf.write("\7t\2\2\u0102\24\3\2\2\2\u0103\u0104\7r\2\2\u0104\u0105")
        buf.write("\7t\2\2\u0105\u0106\7g\2\2\u0106\u0107\7x\2\2\u0107\u0108")
        buf.write("\7g\2\2\u0108\u0109\7p\2\2\u0109\u010a\7v\2\2\u010a\u010b")
        buf.write("\7F\2\2\u010b\u010c\7g\2\2\u010c\u010d\7h\2\2\u010d\u010e")
        buf.write("\7c\2\2\u010e\u010f\7w\2\2\u010f\u0110\7n\2\2\u0110\u0111")
        buf.write("\7v\2\2\u0111\26\3\2\2\2\u0112\u0113\7\61\2\2\u0113\u0114")
        buf.write("\7,\2\2\u0114\u0118\3\2\2\2\u0115\u0117\13\2\2\2\u0116")
        buf.write("\u0115\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0119\3\2\2\2")
        buf.write("\u0118\u0116\3\2\2\2\u0119\u011b\3\2\2\2\u011a\u0118\3")
        buf.write("\2\2\2\u011b\u011c\7,\2\2\u011c\u011d\7\61\2\2\u011d\u011e")
        buf.write("\3\2\2\2\u011e\u011f\b\f\2\2\u011f\30\3\2\2\2\u0120\u0121")
        buf.write("\7\61\2\2\u0121\u0122\7\61\2\2\u0122\u0126\3\2\2\2\u0123")
        buf.write("\u0125\13\2\2\2\u0124\u0123\3\2\2\2\u0125\u0128\3\2\2")
        buf.write("\2\u0126\u0127\3\2\2\2\u0126\u0124\3\2\2\2\u0127\u012c")
        buf.write("\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u012b\n\2\2\2\u012a")
        buf.write("\u0129\3\2\2\2\u012b\u012e\3\2\2\2\u012c\u012a\3\2\2\2")
        buf.write("\u012c\u012d\3\2\2\2\u012d\u012f\3\2\2\2\u012e\u012c\3")
        buf.write("\2\2\2\u012f\u0130\b\r\2\2\u0130\32\3\2\2\2\u0131\u0132")
        buf.write("\7c\2\2\u0132\u0133\7w\2\2\u0133\u0134\7v\2\2\u0134\u0135")
        buf.write("\7q\2\2\u0135\34\3\2\2\2\u0136\u0137\7d\2\2\u0137\u0138")
        buf.write("\7t\2\2\u0138\u0139\7g\2\2\u0139\u013a\7c\2\2\u013a\u013b")
        buf.write("\7m\2\2\u013b\36\3\2\2\2\u013c\u013d\7d\2\2\u013d\u013e")
        buf.write("\7q\2\2\u013e\u013f\7q\2\2\u013f\u0140\7n\2\2\u0140\u0141")
        buf.write("\7g\2\2\u0141\u0142\7c\2\2\u0142\u0143\7p\2\2\u0143 \3")
        buf.write("\2\2\2\u0144\u0145\7f\2\2\u0145\u0146\7q\2\2\u0146\"\3")
        buf.write("\2\2\2\u0147\u0148\7g\2\2\u0148\u0149\7n\2\2\u0149\u014a")
        buf.write("\7u\2\2\u014a\u014b\7g\2\2\u014b$\3\2\2\2\u014c\u014d")
        buf.write("\7h\2\2\u014d\u014e\7c\2\2\u014e\u014f\7n\2\2\u014f\u0150")
        buf.write("\7u\2\2\u0150\u0151\7g\2\2\u0151&\3\2\2\2\u0152\u0153")
        buf.write("\7h\2\2\u0153\u0154\7n\2\2\u0154\u0155\7q\2\2\u0155\u0156")
        buf.write("\7c\2\2\u0156\u0157\7v\2\2\u0157(\3\2\2\2\u0158\u0159")
        buf.write("\7h\2\2\u0159\u015a\7q\2\2\u015a\u015b\7t\2\2\u015b*\3")
        buf.write("\2\2\2\u015c\u015d\7h\2\2\u015d\u015e\7w\2\2\u015e\u015f")
        buf.write("\7p\2\2\u015f\u0160\7e\2\2\u0160\u0161\7v\2\2\u0161\u0162")
        buf.write("\7k\2\2\u0162\u0163\7q\2\2\u0163\u0164\7p\2\2\u0164,\3")
        buf.write("\2\2\2\u0165\u0166\7k\2\2\u0166\u0167\7h\2\2\u0167.\3")
        buf.write("\2\2\2\u0168\u0169\7k\2\2\u0169\u016a\7p\2\2\u016a\u016b")
        buf.write("\7v\2\2\u016b\u016c\7g\2\2\u016c\u016d\7i\2\2\u016d\u016e")
        buf.write("\7g\2\2\u016e\u016f\7t\2\2\u016f\60\3\2\2\2\u0170\u0171")
        buf.write("\7t\2\2\u0171\u0172\7g\2\2\u0172\u0173\7v\2\2\u0173\u0174")
        buf.write("\7w\2\2\u0174\u0175\7t\2\2\u0175\u0176\7p\2\2\u0176\62")
        buf.write("\3\2\2\2\u0177\u0178\7u\2\2\u0178\u0179\7v\2\2\u0179\u017a")
        buf.write("\7t\2\2\u017a\u017b\7k\2\2\u017b\u017c\7p\2\2\u017c\u017d")
        buf.write("\7i\2\2\u017d\64\3\2\2\2\u017e\u017f\7v\2\2\u017f\u0180")
        buf.write("\7t\2\2\u0180\u0181\7w\2\2\u0181\u0182\7g\2\2\u0182\66")
        buf.write("\3\2\2\2\u0183\u0184\7y\2\2\u0184\u0185\7j\2\2\u0185\u0186")
        buf.write("\7k\2\2\u0186\u0187\7n\2\2\u0187\u0188\7g\2\2\u01888\3")
        buf.write("\2\2\2\u0189\u018a\7x\2\2\u018a\u018b\7q\2\2\u018b\u018c")
        buf.write("\7k\2\2\u018c\u018d\7f\2\2\u018d:\3\2\2\2\u018e\u018f")
        buf.write("\7q\2\2\u018f\u0190\7w\2\2\u0190\u0191\7v\2\2\u0191<\3")
        buf.write("\2\2\2\u0192\u0193\7e\2\2\u0193\u0194\7q\2\2\u0194\u0195")
        buf.write("\7p\2\2\u0195\u0196\7v\2\2\u0196\u0197\7k\2\2\u0197\u0198")
        buf.write("\7p\2\2\u0198\u0199\7w\2\2\u0199\u019a\7g\2\2\u019a>\3")
        buf.write("\2\2\2\u019b\u019c\7q\2\2\u019c\u019d\7h\2\2\u019d@\3")
        buf.write("\2\2\2\u019e\u019f\7k\2\2\u019f\u01a0\7p\2\2\u01a0\u01a1")
        buf.write("\7j\2\2\u01a1\u01a2\7g\2\2\u01a2\u01a3\7t\2\2\u01a3\u01a4")
        buf.write("\7k\2\2\u01a4\u01a5\7v\2\2\u01a5B\3\2\2\2\u01a6\u01a7")
        buf.write("\7c\2\2\u01a7\u01a8\7t\2\2\u01a8\u01a9\7t\2\2\u01a9\u01aa")
        buf.write("\7c\2\2\u01aa\u01ab\7{\2\2\u01abD\3\2\2\2\u01ac\u01ad")
        buf.write("\7-\2\2\u01adF\3\2\2\2\u01ae\u01af\7/\2\2\u01afH\3\2\2")
        buf.write("\2\u01b0\u01b1\7,\2\2\u01b1J\3\2\2\2\u01b2\u01b3\7\61")
        buf.write("\2\2\u01b3L\3\2\2\2\u01b4\u01b5\7\'\2\2\u01b5N\3\2\2\2")
        buf.write("\u01b6\u01b7\7#\2\2\u01b7P\3\2\2\2\u01b8\u01b9\7(\2\2")
        buf.write("\u01b9\u01ba\7(\2\2\u01baR\3\2\2\2\u01bb\u01bc\7~\2\2")
        buf.write("\u01bc\u01bd\7~\2\2\u01bdT\3\2\2\2\u01be\u01bf\7?\2\2")
        buf.write("\u01bf\u01c0\7?\2\2\u01c0V\3\2\2\2\u01c1\u01c2\7#\2\2")
        buf.write("\u01c2\u01c3\7?\2\2\u01c3X\3\2\2\2\u01c4\u01c5\7>\2\2")
        buf.write("\u01c5Z\3\2\2\2\u01c6\u01c7\7>\2\2\u01c7\u01c8\7?\2\2")
        buf.write("\u01c8\\\3\2\2\2\u01c9\u01ca\7@\2\2\u01ca^\3\2\2\2\u01cb")
        buf.write("\u01cc\7@\2\2\u01cc\u01cd\7?\2\2\u01cd`\3\2\2\2\u01ce")
        buf.write("\u01cf\7<\2\2\u01cf\u01d0\7<\2\2\u01d0b\3\2\2\2\u01d1")
        buf.write("\u01d7\5O(\2\u01d2\u01d7\5Q)\2\u01d3\u01d7\5S*\2\u01d4")
        buf.write("\u01d7\5U+\2\u01d5\u01d7\5W,\2\u01d6\u01d1\3\2\2\2\u01d6")
        buf.write("\u01d2\3\2\2\2\u01d6\u01d3\3\2\2\2\u01d6\u01d4\3\2\2\2")
        buf.write("\u01d6\u01d5\3\2\2\2\u01d7d\3\2\2\2\u01d8\u01e4\5E#\2")
        buf.write("\u01d9\u01e4\5G$\2\u01da\u01e4\5I%\2\u01db\u01e4\5K&\2")
        buf.write("\u01dc\u01e4\5M\'\2\u01dd\u01e4\5U+\2\u01de\u01e4\5W,")
        buf.write("\2\u01df\u01e4\5Y-\2\u01e0\u01e4\5[.\2\u01e1\u01e4\5]")
        buf.write("/\2\u01e2\u01e4\5_\60\2\u01e3\u01d8\3\2\2\2\u01e3\u01d9")
        buf.write("\3\2\2\2\u01e3\u01da\3\2\2\2\u01e3\u01db\3\2\2\2\u01e3")
        buf.write("\u01dc\3\2\2\2\u01e3\u01dd\3\2\2\2\u01e3\u01de\3\2\2\2")
        buf.write("\u01e3\u01df\3\2\2\2\u01e3\u01e0\3\2\2\2\u01e3\u01e1\3")
        buf.write("\2\2\2\u01e3\u01e2\3\2\2\2\u01e4f\3\2\2\2\u01e5\u01f0")
        buf.write("\5E#\2\u01e6\u01f0\5G$\2\u01e7\u01f0\5I%\2\u01e8\u01f0")
        buf.write("\5K&\2\u01e9\u01f0\5U+\2\u01ea\u01f0\5W,\2\u01eb\u01f0")
        buf.write("\5Y-\2\u01ec\u01f0\5[.\2\u01ed\u01f0\5]/\2\u01ee\u01f0")
        buf.write("\5_\60\2\u01ef\u01e5\3\2\2\2\u01ef\u01e6\3\2\2\2\u01ef")
        buf.write("\u01e7\3\2\2\2\u01ef\u01e8\3\2\2\2\u01ef\u01e9\3\2\2\2")
        buf.write("\u01ef\u01ea\3\2\2\2\u01ef\u01eb\3\2\2\2\u01ef\u01ec\3")
        buf.write("\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0h")
        buf.write("\3\2\2\2\u01f1\u01f2\5a\61\2\u01f2j\3\2\2\2\u01f3\u01f4")
        buf.write("\7.\2\2\u01f4l\3\2\2\2\u01f5\u01f6\7=\2\2\u01f6n\3\2\2")
        buf.write("\2\u01f7\u01f8\7?\2\2\u01f8p\3\2\2\2\u01f9\u01fa\7<\2")
        buf.write("\2\u01far\3\2\2\2\u01fb\u01fc\7\60\2\2\u01fct\3\2\2\2")
        buf.write("\u01fd\u01fe\7*\2\2\u01fev\3\2\2\2\u01ff\u0200\7+\2\2")
        buf.write("\u0200x\3\2\2\2\u0201\u0202\7}\2\2\u0202z\3\2\2\2\u0203")
        buf.write("\u0204\7\177\2\2\u0204|\3\2\2\2\u0205\u0206\7]\2\2\u0206")
        buf.write("~\3\2\2\2\u0207\u0208\7_\2\2\u0208\u0080\3\2\2\2\u0209")
        buf.write("\u021e\7\62\2\2\u020a\u020e\t\3\2\2\u020b\u020d\t\4\2")
        buf.write("\2\u020c\u020b\3\2\2\2\u020d\u0210\3\2\2\2\u020e\u020c")
        buf.write("\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0219\3\2\2\2\u0210")
        buf.write("\u020e\3\2\2\2\u0211\u0213\7a\2\2\u0212\u0214\t\4\2\2")
        buf.write("\u0213\u0212\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0213\3")
        buf.write("\2\2\2\u0215\u0216\3\2\2\2\u0216\u0218\3\2\2\2\u0217\u0211")
        buf.write("\3\2\2\2\u0218\u021b\3\2\2\2\u0219\u0217\3\2\2\2\u0219")
        buf.write("\u021a\3\2\2\2\u021a\u021c\3\2\2\2\u021b\u0219\3\2\2\2")
        buf.write("\u021c\u021e\bA\3\2\u021d\u0209\3\2\2\2\u021d\u020a\3")
        buf.write("\2\2\2\u021e\u0082\3\2\2\2\u021f\u0221\5\u0085C\2\u0220")
        buf.write("\u0222\5\u0089E\2\u0221\u0220\3\2\2\2\u0221\u0222\3\2")
        buf.write("\2\2\u0222\u0223\3\2\2\2\u0223\u0224\5\u0087D\2\u0224")
        buf.write("\u0231\3\2\2\2\u0225\u0226\5\u0085C\2\u0226\u0228\5\u0089")
        buf.write("E\2\u0227\u0229\5\u0087D\2\u0228\u0227\3\2\2\2\u0228\u0229")
        buf.write("\3\2\2\2\u0229\u0231\3\2\2\2\u022a\u022c\5\u0085C\2\u022b")
        buf.write("\u022a\3\2\2\2\u022b\u022c\3\2\2\2\u022c\u022d\3\2\2\2")
        buf.write("\u022d\u022e\5\u0089E\2\u022e\u022f\5\u0087D\2\u022f\u0231")
        buf.write("\3\2\2\2\u0230\u021f\3\2\2\2\u0230\u0225\3\2\2\2\u0230")
        buf.write("\u022b\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0233\bB\4\2")
        buf.write("\u0233\u0084\3\2\2\2\u0234\u0236\t\4\2\2\u0235\u0234\3")
        buf.write("\2\2\2\u0236\u0237\3\2\2\2\u0237\u0235\3\2\2\2\u0237\u0238")
        buf.write("\3\2\2\2\u0238\u0241\3\2\2\2\u0239\u023b\7a\2\2\u023a")
        buf.write("\u023c\t\4\2\2\u023b\u023a\3\2\2\2\u023c\u023d\3\2\2\2")
        buf.write("\u023d\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u0240\3")
        buf.write("\2\2\2\u023f\u0239\3\2\2\2\u0240\u0243\3\2\2\2\u0241\u023f")
        buf.write("\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0086\3\2\2\2\u0243")
        buf.write("\u0241\3\2\2\2\u0244\u0246\t\5\2\2\u0245\u0247\t\6\2\2")
        buf.write("\u0246\u0245\3\2\2\2\u0246\u0247\3\2\2\2\u0247\u0249\3")
        buf.write("\2\2\2\u0248\u024a\t\4\2\2\u0249\u0248\3\2\2\2\u024a\u024b")
        buf.write("\3\2\2\2\u024b\u0249\3\2\2\2\u024b\u024c\3\2\2\2\u024c")
        buf.write("\u0088\3\2\2\2\u024d\u0251\7\60\2\2\u024e\u0250\t\4\2")
        buf.write("\2\u024f\u024e\3\2\2\2\u0250\u0253\3\2\2\2\u0251\u024f")
        buf.write("\3\2\2\2\u0251\u0252\3\2\2\2\u0252\u008a\3\2\2\2\u0253")
        buf.write("\u0251\3\2\2\2\u0254\u0258\5\u0093J\2\u0255\u0257\5\u008d")
        buf.write("G\2\u0256\u0255\3\2\2\2\u0257\u025a\3\2\2\2\u0258\u0256")
        buf.write("\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u025b\3\2\2\2\u025a")
        buf.write("\u0258\3\2\2\2\u025b\u025c\5\u0093J\2\u025c\u025d\bF\5")
        buf.write("\2\u025d\u008c\3\2\2\2\u025e\u0261\n\7\2\2\u025f\u0261")
        buf.write("\5\u008fH\2\u0260\u025e\3\2\2\2\u0260\u025f\3\2\2\2\u0261")
        buf.write("\u008e\3\2\2\2\u0262\u0263\7^\2\2\u0263\u0264\t\b\2\2")
        buf.write("\u0264\u0090\3\2\2\2\u0265\u0266\7^\2\2\u0266\u0269\n")
        buf.write("\b\2\2\u0267\u0269\7^\2\2\u0268\u0265\3\2\2\2\u0268\u0267")
        buf.write("\3\2\2\2\u0269\u0092\3\2\2\2\u026a\u026b\7$\2\2\u026b")
        buf.write("\u0094\3\2\2\2\u026c\u0270\t\t\2\2\u026d\u026f\t\n\2\2")
        buf.write("\u026e\u026d\3\2\2\2\u026f\u0272\3\2\2\2\u0270\u026e\3")
        buf.write("\2\2\2\u0270\u0271\3\2\2\2\u0271\u0096\3\2\2\2\u0272\u0270")
        buf.write("\3\2\2\2\u0273\u0275\t\13\2\2\u0274\u0273\3\2\2\2\u0275")
        buf.write("\u0276\3\2\2\2\u0276\u0274\3\2\2\2\u0276\u0277\3\2\2\2")
        buf.write("\u0277\u0278\3\2\2\2\u0278\u0279\bL\2\2\u0279\u0098\3")
        buf.write("\2\2\2\u027a\u027b\13\2\2\2\u027b\u027c\bM\6\2\u027c\u009a")
        buf.write("\3\2\2\2\u027d\u0281\5\u0093J\2\u027e\u0280\5\u008dG\2")
        buf.write("\u027f\u027e\3\2\2\2\u0280\u0283\3\2\2\2\u0281\u027f\3")
        buf.write("\2\2\2\u0281\u0282\3\2\2\2\u0282\u0285\3\2\2\2\u0283\u0281")
        buf.write("\3\2\2\2\u0284\u0286\t\f\2\2\u0285\u0284\3\2\2\2\u0286")
        buf.write("\u0287\3\2\2\2\u0287\u0288\bN\7\2\u0288\u009c\3\2\2\2")
        buf.write("\u0289\u028d\5\u0093J\2\u028a\u028c\5\u008dG\2\u028b\u028a")
        buf.write("\3\2\2\2\u028c\u028f\3\2\2\2\u028d\u028b\3\2\2\2\u028d")
        buf.write("\u028e\3\2\2\2\u028e\u0290\3\2\2\2\u028f\u028d\3\2\2\2")
        buf.write("\u0290\u0291\5\u0091I\2\u0291\u0292\bO\b\2\u0292\u009e")
        buf.write("\3\2\2\2\37\2\u0118\u0126\u012c\u01d6\u01e3\u01ef\u020e")
        buf.write("\u0215\u0219\u021d\u0221\u0228\u022b\u0230\u0237\u023d")
        buf.write("\u0241\u0246\u024b\u0251\u0258\u0260\u0268\u0270\u0276")
        buf.write("\u0281\u0285\u028d\t\b\2\2\3A\2\3B\3\3F\4\3M\5\3N\6\3")
        buf.write("O\7")
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
    BLOCK_COMMENT = 11
    LINE_COMMENT = 12
    AUTO = 13
    BREAK = 14
    BOOLEAN = 15
    DO = 16
    ELSE = 17
    FALSE = 18
    FLOAT = 19
    FOR = 20
    FUNCTION = 21
    IF = 22
    INTEGER = 23
    RETURN = 24
    STRING = 25
    TRUE = 26
    WHILE = 27
    VOID = 28
    OUT = 29
    CONTINUE = 30
    OF = 31
    INHERIT = 32
    ARRAY = 33
    ADD = 34
    SUB = 35
    MUL = 36
    DIV = 37
    MOD = 38
    NOT = 39
    AND = 40
    OR = 41
    EQUAL = 42
    DIFF = 43
    SMALLER = 44
    SMALLER_OR_EQUAL = 45
    GREATER = 46
    GREATER_OR_EQUAL = 47
    CONCAT = 48
    OP_BOOL = 49
    OP_INT = 50
    OP_FLOAT = 51
    OP_STRING = 52
    COMMA = 53
    SEMI = 54
    ASSIGN = 55
    COLON = 56
    DOT = 57
    LB = 58
    RB = 59
    LP = 60
    RP = 61
    LS = 62
    RS = 63
    INTLIT = 64
    FLOATLIT = 65
    STRINGLIT = 66
    ID = 67
    WS = 68
    ERROR_CHAR = 69
    UNCLOSE_STRING = 70
    ILLEGAL_ESCAPE = 71

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
            "BLOCK_COMMENT", "LINE_COMMENT", "AUTO", "BREAK", "BOOLEAN", 
            "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
            "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
            "OF", "INHERIT", "ARRAY", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "NOT", "AND", "OR", "EQUAL", "DIFF", "SMALLER", "SMALLER_OR_EQUAL", 
            "GREATER", "GREATER_OR_EQUAL", "CONCAT", "OP_BOOL", "OP_INT", 
            "OP_FLOAT", "OP_STRING", "COMMA", "SEMI", "ASSIGN", "COLON", 
            "DOT", "LB", "RB", "LP", "RP", "LS", "RS", "INTLIT", "FLOATLIT", 
            "STRINGLIT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "BLOCK_COMMENT", "LINE_COMMENT", 
                  "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", 
                  "OR", "EQUAL", "DIFF", "SMALLER", "SMALLER_OR_EQUAL", 
                  "GREATER", "GREATER_OR_EQUAL", "CONCAT", "OP_BOOL", "OP_INT", 
                  "OP_FLOAT", "OP_STRING", "COMMA", "SEMI", "ASSIGN", "COLON", 
                  "DOT", "LB", "RB", "LP", "RP", "LS", "RS", "INTLIT", "FLOATLIT", 
                  "DIGIT_UNDERSCORE", "SCIENTIFIC", "DECIMAL", "STRINGLIT", 
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
            actions[63] = self.INTLIT_action 
            actions[64] = self.FLOATLIT_action 
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

     


