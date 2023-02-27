import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    
    def test1(self):
        # "test comment line"
        input = '//you are the apple in my eyes'
        output = '<EOF>'
        self.assertTrue(TestLexer.test(input, output, 101))

    def test2(self):
        # "test comment block"
        input = '/* you are the apple \n of my eyes */'
        output = "<EOF>"
        self.assertTrue(TestLexer.test(input, output, 102))

    def test3(self):
        # "test identifier"
        input = 'Abc_01_oFR'
        output = "Abc_01_oFR,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 103))

    def test4(self):
        # "test integer"
        input = '123_4_567'
        output = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 104))

    def test5(self):
        # "test float"
        input = '.01'
        output = ".,0,1,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 105))

    def test6(self):
        # "test float"
        input = "1."
        output = "1.,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 106))

    def test7(self):
        # "test float"
        input = '1_23.7e-4'
        output = "123.7e-4,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 107))

    def test8(self):
        # "test string"
        input = """ "hello world" """
        output = "hello world,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 108))

    def test9(self):
        # "test string"
        input = """ "He asked me: Where is " """
        output = "He asked me: Where is ,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 109))
    
    def test10(self):
        # "test string"
        input = """ "He asked me: Where is John?"""
        output = "Unclosed String: He asked me: Where is John?"
        self.assertTrue(TestLexer.test(input, output, 110))
    
    def test11(self):
        # "test string"
        input = """ "He asked me" """
        output = "He asked me,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 111))
    
    def test12(self):
        # "test string"
        input = """ "He asked me\n"" """
        output = """Unclosed String: He asked me"""
        self.assertTrue(TestLexer.test(input, output, 112))

    def test13(self):
        # "test boolean"
        input = "true"
        output = "true,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 113))

    def test14(self):
        input = "{1,2,3}"
        output = "{,1,,,2,,,3,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 114))

    def test15(self):
        input = "a := 1"
        output = "a,:,=,1,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 115))

    def test16(self):
        input = "integer: integer = 5;"
        output = "integer,:,integer,=,5,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 116))

    def test17(self):
        input = "a : boolean = true;"
        output = "a,:,boolean,=,true,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 117))

    def test18(self):
        input = "123_45_?"
        output = "12345,_,Error Token ?"
        self.assertTrue(TestLexer.test(input, output, 118))

    def test19(self):
        input = "_.123_45"
        output = "_,.,12345,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 119))

    def test20(self):
        input = "?abcdefghijklmnopqrstuvw"
        output = "Error Token ?"
        self.assertTrue(TestLexer.test(input, output, 120))

    def test21(self):
        input = "&&"
        output = "&&,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 121))

    def test22(self):
        input = "a || b || c"
        output = "a,||,b,||,c,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 122))

    def test23(self):
        input = ">>"
        output = ">,>,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 123))

    def test24(self):
        input = "@#$%^&*()_+"
        output = "Error Token @"
        self.assertTrue(TestLexer.test(input, output, 124))

    def test25(self):
        input = "a & b | c"
        output = "a,Error Token &"
        self.assertTrue(TestLexer.test(input, output, 125))

    def test26(self):
        input = "b*c"
        output = "b,*,c,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 126))

    def test27(self):
        input = "b$%^*c"
        output = "b,Error Token $"
        self.assertTrue(TestLexer.test(input, output, 127))

    def test28(self):
        input = "123_.456E12"
        output = "123,_,.456E12,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 128))

    def test29(self):
        input = ".hdmqk"
        output = ".,hdmqk,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 129))

    def test30(self):
        input = "123_abc*456"
        output = "123,_abc,*,456,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 130))

    def test31(self):
        input = "a : function foo(a,b:integer) {};"
        output = "a,:,function,foo,(,a,,,b,:,integer,),{,},;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 131))

    def test32(self):
        input = "mYfUnCtIoN(a,b:integer) {};"
        output = "mYfUnCtIoN,(,a,,,b,:,integer,),{,},;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 132))

    def test33(self):
        input = "variable a: INTEGER := 1;"
        output = "variable,a,:,INTEGER,:,=,1,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 133))

    def test34(self):
        input = "wHy iS tHiS nOt WoRkInG?"
        output = "wHy,iS,tHiS,nOt,WoRkInG,Error Token ?"
        self.assertTrue(TestLexer.test(input, output, 134))

    def test35(self):
        input = "a = 1.0E-12;"
        output = "a,=,1.0E-12,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 135))

    def test36(self):
        input = """ a = "abc"; """
        output = "a,=,abc,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 136))

    def test37(self):
        input = "Error Token on line 1, col 1: Illegal Escape In String:"
        output = "Error,Token,on,line,1,,,col,1,:,Illegal,Escape,In,String,:,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 137))

    def test38(self):
        input = "a : array [1,2] of integer = {1,3,4};"
        output = "a,:,array,[,1,,,2,],of,integer,=,{,1,,,3,,,4,},;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 138))

    def test39(self):
        input = "a == b ? c : d"
        output = "a,==,b,Error Token ?"
        self.assertTrue(TestLexer.test(input, output, 139))

    def test40(self):
        input = ""
        output = "<EOF>"
        self.assertTrue(TestLexer.test(input, output, 140))

    def test41(self):
        input = "if (a > b) a = b; else c = 1;"
        output = "if,(,a,>,b,),a,=,b,;,else,c,=,1,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 141))

    def test42(self):
        input = "do {a = b+c;} while (a < b);"
        output = "do,{,a,=,b,+,c,;,},while,(,a,<,b,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 142))

    def test43(self):
        input = "for (i = 0; i < 10; i = i + 1) {}"
        output = "for,(,i,=,0,;,i,<,10,;,i,=,i,+,1,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 143))

    def test44(self):
        input = "while do for if else out"
        output = "while,do,for,if,else,out,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 144))

    def test45(self):
        input = "||^&%$#@!~`"
        output = "||,Error Token ^"
        self.assertTrue(TestLexer.test(input, output, 145))

    def test46(self):
        input = "_123*456.789E-10"
        output = "_123,*,456.789E-10,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 146))

    def test47(self):
        input = """ abc+def"zyz" """
        output = "abc,+,def,zyz,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 147))

    def test48(self):
        input = "readInteger()"
        output = "readInteger,(,),<EOF>"
        self.assertTrue(TestLexer.test(input, output, 148))

    def test49(self):
        input = "printFloat(1.0E+12)"
        output = "printFloat,(,1.0E+12,),<EOF>"
        self.assertTrue(TestLexer.test(input, output, 149))

    def test50(self):
        input = """ printString("Hello World") """
        output = "printString,(,Hello World,),<EOF>"
        self.assertTrue(TestLexer.test(input, output, 150))

    def test51(self):
        input = "delta.super()"
        output = "delta,.,super,(,),<EOF>"
        self.assertTrue(TestLexer.test(input, output, 151))

    def test52(self):
        input = "Principles of Programming Languages"
        output = "Principles,of,Programming,Languages,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 152))

    def test53(self):
        input = "________________________"
        output = "________________________,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 153))

    def test54(self):
        input = "a = b - c"
        output = "a,=,b,-,c,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 154))

    def test55(self):
        input = "a::b"
        output = "a,::,b,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 155))

    def test56(self):
        input = """ "This is a string containing tab \\" """
        expect = """Unclosed String: This is a string containing tab \\\" """
        self.assertTrue(TestLexer.test(input, expect, 156))

    def test57(self):
        input = """ "This is a string containing tab \t" """
        expect = """This is a string containing tab 	,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 157))

    def test58(self):
        input = """ "This is a string containing tab \\y" """
        expect = """Illegal Escape In String: This is a string containing tab \y"""
        self.assertTrue(TestLexer.test(input, expect, 158))

    def test59(self):
        input = """ "This is a string\n containing tab" """
        expect = """Unclosed String: This is a string"""
        self.assertTrue(TestLexer.test(input, expect, 159))

    def test60(self):
        input = """ "This is a string containing tab \t" """
        expect = """This is a string containing tab 	,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 160))
        
    def test61(self):
        input = "123"
        expect = "123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 161))
        
    def test62(self):
        input = "123_45"
        expect = "12345,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 162))
        
    def test63(self):
        input = "123_345_33"
        expect = "12334533,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 163))
        
    def test64(self):
        input = "1_234.567"
        expect = "1234.567,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 164))

    def test65(self):
        input = "1_234.56789"
        expect = "1234.56789,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 165))
        
    def test66(self):
        input = "123.33"
        expect = "123.33,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 166))
        
    def test67(self):
        input = "123.33e-3"
        expect = "123.33e-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 167))
        
    def test68(self):
        input = "123.33e-34"
        expect = "123.33e-34,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 168))
        
    def test69(self):
        input = "1_234.56789e-34"
        expect = "1234.56789e-34,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 169))
        
    def test70(self):
        input = ""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 170))
        
    def test71(self):
        input = "123."
        expect = "123.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 171))
        
    def test72(self):
        input = "1_234.e-34"
        expect = "1234.e-34,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 172))
        
    def test73(self):
        input = """ "he hh sjsk" """
        expect = "he hh sjsk,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 173))
        
    def test74(self):
        input = "123_"
        expect = "123,_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 174))
        
    def test75(self):
        input = """ "This is a string containing tab \t" """
        expect = "This is a string containing tab \t,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 175))
        
    def test76(self):
        input = """ "This is a string containing tab \'" """
        expect = "This is a string containing tab \',<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 176))
        
    def test77(self):
        input = """ "This is a string containing tab \t" """
        expect = """This is a string containing tab 	,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 177))

    def test78(self):
        input = "123.456E12"
        expect = "123.456E12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 178))
        
    def test79(self):
        input = """ "This is a string containing tab \\y hehe" """
        expect = "Illegal Escape In String: This is a string containing tab \y"
        self.assertTrue(TestLexer.test(input, expect, 179))
        
    def test80(self):
        input = """ "This is a string containing tab \\ hehe" """
        expect = "Illegal Escape In String: This is a string containing tab \ "
        self.assertTrue(TestLexer.test(input, expect, 180))
        
    def test81(self):
        input = """ "This is a unclosed string hehe"""
        expect = "Unclosed String: This is a unclosed string hehe"
        self.assertTrue(TestLexer.test(input, expect, 181))
    
    def test82(self):
        input = """
/* This is another way to do it, also in C.
 ** It is easier to do in editors that do not automatically indent the second
 ** through last lines of the comment one space from the first.
 ** It is also used in Holub's book, in rule 31.
 */
            """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 182))
        
    def test83(self):
        input = """
/* This is a block comment */
// This is a line comment
/* Comment with multiple lines
    Hello comments
*/
/*
    Comment multiple lines
*/
/* nest comments
    // inline comment 
// inline comment
*/
            """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 183))
    
    def test84(self):
        input = """1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42 1e-12 143e1"""
        expect = "1.2,1.,.,1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,1e-12,143e1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 184))
        
    def test185(self):
        input = """ "abc""def" """
        expect = """abc,def,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 185))
    def test186(self):
        input = """ if a == b: return c;"""
        expect = """if,a,==,b,:,return,c,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 186))
    def test187(self):
        input = """ 1__2 """
        expect = """1,__2,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 187))
    def test188(self):
        input = """ _1__2 """
        expect = """_1__2,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 188))
    def test189(self):
        input = """ 1__2 """
        expect = """1,__2,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 189))
    def test190(self):
        input = """ / """
        expect = """/,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 190))
    def test191(self):
        input = """ "\'" """
        expect = """\',<EOF>"""""
        self.assertTrue(TestLexer.test(input, expect, 191))
    def test192(self):
        input = """ "\\'" """
        expect = """\\',<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 192))
    def test193(self):
        input = """ a = {{1,2,3}, {{}}}; """
        expect = """a,=,{,{,1,,,2,,,3,},,,{,{,},},},;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 193))
    def test194(self):
        input = """ <<==>> """
        expect = """<,<=,=,>,>,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 194))
    def test195(self):
        input = """ ::::: """
        expect = """::,::,:,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 195))
    def test196(self):
        input = """ <<=>=>> """
        expect = """<,<=,>=,>,>,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 196))
    def test197(self):
        input = """ dout """
        expect = """dout,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 197))
    def test198(self):
        input = """ writeInt(i); """
        expect = """writeInt,(,i,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 198))
    def test199(self):
        input = """ func : function integer (out a : auto) {}"""
        expect = "func,:,function,integer,(,out,a,:,auto,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 199))
    def test200(self):
        input = """printFloat(a); """
        expect = """printFloat,(,a,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 200))