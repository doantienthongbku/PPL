import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # def test1(self):
    #     input = "123"
    #     expect = "123,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 101))
        
    # def test2(self):
    #     input = "123_45"
    #     expect = "12345,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 102))
        
    # def test3(self):
    #     input = "123_345_33"
    #     expect = "12334533,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 103))
        
    # def test4(self):
    #     input = "1_234.567"
    #     expect = "1234.567,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 104))

    # def test5(self):
    #     input = "1_234.567_89"
    #     expect = "1234.56789,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 105))
        
    # def test6(self):
    #     input = "123.33"
    #     expect = "123.33,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 106))
        
    # def test7(self):
    #     input = "123.33e-3"
    #     expect = "123.33e-3,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 107))
        
    # def test8(self):
    #     input = "123.33e-3_4"
    #     expect = "123.33e-34,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 108))
        
    # def test9(self):
    #     input = "1_234.567_89e-3_4"
    #     expect = "1234.56789e-34,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 109))
        
    # def test10(self):
    #     input = ""
    #     expect = "<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 110))
        
    # def test11(self):
    #     input = "123."
    #     expect = "123.,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 111))
        
    # def test12(self):
    #     input = "1_234.e-3_4"
    #     expect = "1234.e-34,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 112))
        
    # def test13(self):
    #     input = """ "he hh sjsk" """
    #     expect = "he hh sjsk,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 113))
        
    # def test14(self):
    #     input = "123_"
    #     expect = "123,_,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 114))
        
    # def test15(self):
    #     input = """ "This is a string containing tab \t" """
    #     expect = "This is a string containing tab \t,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 115))
        
    # def test16(self):
    #     input = """ "This is a string containing tab \'" """
    #     expect = "This is a string containing tab \',<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 116))
        
    # def test17(self):
    #     input = """ "This is a string containing tab \t" """
    #     expect = """This is a string containing tab 	,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 117))

    # def test18(self):
    #     input = "123.456E12"
    #     expect = "123.456E12,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 118))
        
    # def test19(self):
    #     input = """ "This is a string containing tab \\y hehe" """
    #     expect = "Illegal Escape In String: This is a string containing tab \y"
    #     self.assertTrue(TestLexer.test(input, expect, 119))
        
    # def test20(self):
    #     input = """ "This is a string containing tab \\ hehe" """
    #     expect = "Illegal Escape In String: This is a string containing tab \ "
    #     self.assertTrue(TestLexer.test(input, expect, 120))
        
    # def test21(self):
    #     input = """ "This is a unclosed string hehe"""
    #     expect = "Unclosed String: This is a unclosed string hehe"
    #     self.assertTrue(TestLexer.test(input, expect, 121))
    
    def testcase_1(self):
        # "test comment line"
        input = '//you are the apple in my eyes'
        output = '<EOF>'
        self.assertTrue(TestLexer.test(input, output, 101))

    def testcase_2(self):
        # "test comment block"
        input = '/* you are the apple \n of my eyes */'
        output = "<EOF>"
        self.assertTrue(TestLexer.test(input, output, 102))

    def testcase_3(self):
        # "test identifier"
        input = 'Abc_01_oFR'
        output = "Abc_01_oFR,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 103))

    def testcase_4(self):
        # "test integer"
        input = '123_4_567'
        output = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 104))

    def testcase_5(self):
        # "test float"
        input = '.01'
        output = ".,0,1,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 105))

    def testcase_6(self):
        # "test float"
        input = "1."
        output = "1.,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 106))

    def testcase_7(self):
        # "test float"
        input = '1_23.7e-4'
        output = "123.7e-4,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 107))

    def testcase_8(self):
        # "test string"
        input = """ "hello world" """
        output = "hello world,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 108))

    # def testcase_9(self):
    #     # "test string"
    #     input = """ "He asked me: \\"Where is John?\\"" """
    #     output = "He asked me: \"Where is John?\",<EOF>"
    #     self.assertTrue(TestLexer.test(input, output, 109))
    #
    # def testcase_10(self):
    #     # "test string"
    #     input = """ "He asked me: \\"Where is John?\\" """
    #     output = " Unclosed String: He asked me: \"Where is John?\" "
    #     self.assertTrue(TestLexer.test(input, output, 110))
    #
    # def testcase_11(self):
    #     # "test string"
    #     input = """ "He asked me: \\"Where is John?\\"\n" """
    #     output = """ He asked me: \"Where is John?\"" """
    #     self.assertTrue(TestLexer.test(input, output, 111))
    #
    # def testcase_12(self):
    #     # "test string"
    #     input = """ "He asked me: \\"Where is \fJohn?\\"" """
    #     output = """ He asked me: \"Where is John?\"" """
    #     self.assertTrue(TestLexer.test(input, output, 112))

    def testcase_13(self):
        # "test boolean"
        input = "true"
        output = "true,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 113))

    def testcase_14(self):
        input = "{1,2,3}"
        output = "{,1,,,2,,,3,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 114))

    def testcase_15(self):
        input = "a := 1"
        output = "a,:,=,1,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 115))

    def testcase_16(self):
        input = "integer: integer = 5;"
        output = "integer,:,integer,=,5,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 116))

    def testcase_17(self):
        input = "a : boolean = true;"
        output = "a,:,boolean,=,true,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 117))

    def testcase_18(self):
        input = "123_45_?"
        output = "12345,_,Error Token ?"
        self.assertTrue(TestLexer.test(input, output, 118))

    def testcase_19(self):
        input = "_.123_45"
        output = "_,.,12345,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 119))

    def testcase_20(self):
        input = "?abcdefghijklmnopqrstuvw"
        output = "Error Token ?"
        self.assertTrue(TestLexer.test(input, output, 120))

    def testcase_21(self):
        input = "&&"
        output = "&&,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 121))

    def testcase_22(self):
        input = "a || b || c"
        output = "a,||,b,||,c,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 122))

    def testcase_23(self):
        input = ">>"
        output = ">,>,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 123))

    def testcase_24(self):
        input = "@#$%^&*()_+"
        output = "Error Token @"
        self.assertTrue(TestLexer.test(input, output, 124))

    def testcase_25(self):
        input = "a & b | c"
        output = "a,Error Token &"
        self.assertTrue(TestLexer.test(input, output, 125))

    def testcase_26(self):
        input = "b*c"
        output = "b,*,c,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 126))

    def testcase_27(self):
        input = "b$%^*c"
        output = "b,Error Token $"
        self.assertTrue(TestLexer.test(input, output, 127))

    def testcase_28(self):
        input = "123_.456E12"
        output = "123,_,.,456E12,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 128))

    def testcase_29(self):
        input = ".hdmqk"
        output = ".,hdmqk,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 129))

    def testcase_30(self):
        input = "123_abc*456"
        output = "123,_abc,*,456,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 130))

    def testcase_31(self):
        input = "a : function foo(a,b:integer) {};"
        output = "a,:,function,foo,(,a,,,b,:,integer,),{,},;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 131))

    def testcase_32(self):
        input = "mYfUnCtIoN(a,b:integer) {};"
        output = "mYfUnCtIoN,(,a,,,b,:,integer,),{,},;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 132))

    def testcase_33(self):
        input = "variable a: INTEGER := 1;"
        output = "variable,a,:,INTEGER,:,=,1,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 133))

    def testcase_34(self):
        input = "wHy iS tHiS nOt WoRkInG?"
        output = "wHy,iS,tHiS,nOt,WoRkInG,Error Token ?"
        self.assertTrue(TestLexer.test(input, output, 134))

    def testcase_35(self):
        input = "a = 1.0E-12;"
        output = "a,=,1.0E-12,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 135))

    def testcase_36(self):
        input = """ a = "abc"; """
        output = "a,=,abc,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 136))

    def testcase_37(self):
        input = "Error Token on line 1, col 1: Illegal Escape In String:"
        output = "Error,Token,on,line,1,,,col,1,:,Illegal,Escape,In,String,:,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 137))

    def testcase_38(self):
        input = "a : array [1,2] of integer = {1,3,4};"
        output = "a,:,array,[,1,,,2,],of,integer,=,{,1,,,3,,,4,},;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 138))

    def testcase_39(self):
        input = "a == b ? c : d"
        output = "a,==,b,Error Token ?"
        self.assertTrue(TestLexer.test(input, output, 139))

    def testcase_40(self):
        input = ""
        output = "<EOF>"
        self.assertTrue(TestLexer.test(input, output, 140))

    def testcase_41(self):
        input = "if (a > b) a = b; else c = 1;"
        output = "if,(,a,>,b,),a,=,b,;,else,c,=,1,;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 141))

    def testcase_42(self):
        input = "do {a = b+c;} while (a < b);"
        output = "do,{,a,=,b,+,c,;,},while,(,a,<,b,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 142))

    def testcase_43(self):
        input = "for (i = 0; i < 10; i = i + 1) {}"
        output = "for,(,i,=,0,;,i,<,10,;,i,=,i,+,1,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 143))

    def testcase_44(self):
        input = "while do for if else out"
        output = "while,do,for,if,else,out,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 144))

    def testcase_45(self):
        input = "||^&%$#@!~`"
        output = "||,Error Token ^"
        self.assertTrue(TestLexer.test(input, output, 145))

    def testcase_46(self):
        input = "_123*456.789E-10"
        output = "_123,*,456.789E-10,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 146))

    def testcase_47(self):
        input = """ abc+def"zyz" """
        output = "abc,+,def,zyz,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 147))

    def testcase_48(self):
        input = "readInteger()"
        output = "readInteger,(,),<EOF>"
        self.assertTrue(TestLexer.test(input, output, 148))

    def testcase_49(self):
        input = "printFloat(1.0E+12)"
        output = "printFloat,(,1.0E+12,),<EOF>"
        self.assertTrue(TestLexer.test(input, output, 149))

    def testcase_50(self):
        input = """ printString("Hello World") """
        output = "printString,(,Hello World,),<EOF>"
        self.assertTrue(TestLexer.test(input, output, 150))

    def testcase_51(self):
        input = "delta.super()"
        output = "delta,.,super,(,),<EOF>"
        self.assertTrue(TestLexer.test(input, output, 151))

    def testcase_52(self):
        input = "Principles of Programming Languages"
        output = "Principles,of,Programming,Languages,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 152))

    def testcase_53(self):
        input = "________________________"
        output = "________________________,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 153))

    def testcase_54(self):
        input = "a = b - c"
        output = "a,=,b,-,c,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 154))

    def testcase_55(self):
        input = "a::b"
        output = "a,::,b,<EOF>"
        self.assertTrue(TestLexer.test(input, output, 155))

    # def testcase_56(self):
    #     input = """ "This is a string containing tab \\" """
    #     expect = """Unclosed String: This is a string containing tab \""""
    #     self.assertTrue(TestLexer.test(input, expect, 156))

    def testcase_57(self):
        input = """ "This is a string containing tab \t" """
        expect = """This is a string containing tab 	,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 157))

    def testcase_58(self):
        input = """ "This is a string containing tab \\y" """
        expect = """Illegal Escape In String: This is a string containing tab \y"""
        self.assertTrue(TestLexer.test(input, expect, 158))

    def testcase_59(self):
        input = """ "This is a string\n containing tab" """
        expect = """Unclosed String: This is a string"""
        self.assertTrue(TestLexer.test(input, expect, 159))

    def testcase_60(self):
        input = """ "This is a string containing tab \t" """
        expect = """This is a string containing tab 	,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 160))