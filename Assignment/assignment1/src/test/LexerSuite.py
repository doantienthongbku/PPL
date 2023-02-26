import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test1(self):
        input = "123"
        expect = "123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 101))
        
    def test2(self):
        input = "123_45"
        expect = "12345,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 102))
        
    def test3(self):
        input = "123_345_33"
        expect = "12334533,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 103))
        
    def test4(self):
        input = "1_234.567"
        expect = "1234.567,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 104))

    def test5(self):
        input = "1_234.567_89"
        expect = "1234.56789,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 105))
        
    def test6(self):
        input = "123.33"
        expect = "123.33,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 106))
        
    def test7(self):
        input = "123.33e-3"
        expect = "123.33e-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 107))
        
    def test8(self):
        input = "123.33e-3_4"
        expect = "123.33e-34,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 108))
        
    def test9(self):
        input = "1_234.567_89e-3_4"
        expect = "1234.56789e-34,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 109))
        
    def test10(self):
        input = ""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 110))
        
    def test11(self):
        input = "123."
        expect = "123.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 111))
        
    def test12(self):
        input = "1_234.e-3_4"
        expect = "1234.e-34,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 112))
        
    def test13(self):
        input = """ "he hh sjsk" """
        expect = "he hh sjsk,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 113))
        
    def test14(self):
        input = "123_"
        expect = "123,_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 114))
        
    def test15(self):
        input = """ "This is a string containing tab \t" """
        expect = "This is a string containing tab \t,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 115))
        
    def test16(self):
        input = """ "This is a string containing tab \'" """
        expect = "This is a string containing tab \',<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 116))
        
    def test17(self):
        input = """ "This is a string containing tab \\" """
        expect = "Error Token \""
        self.assertTrue(TestLexer.test(input, expect, 117))

    def test18(self):
        input = "123.456E12"
        expect = "123.456E12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 118))
        
    def test19(self):
        input = """ "This is a string containing tab \n" """
        expect = ",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 119))
    
    
        

        
    # def test11(self):
    #     input = ""
    #     expect = ",<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 111))
        
    # def test11(self):
    #     input = ""
    #     expect = ",<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 111))
        
    # def test11(self):
    #     input = ""
    #     expect = ",<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 111))
        
    # def test11(self):
    #     input = ""
    #     expect = ",<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 111))
        
    # def test11(self):
    #     input = ""
    #     expect = ",<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 111))
        
    # def test11(self):
    #     input = ""
    #     expect = ",<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 111))