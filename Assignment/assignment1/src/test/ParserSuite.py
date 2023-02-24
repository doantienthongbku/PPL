import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test1(self):
        input = """delta: integer = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
        
    def test2(self):
        input = """delta: boolean;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
        
    def test3(self):
        input = """delta: integer = 3, 4;"""
        expect = "Error on line 1 col 21: ;"
        self.assertTrue(TestParser.test(input, expect, 203))
        
    def test4(self):
        input = """delta: boolean = true;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
        
    # def test4(self):
    #     input = """a, b, c: float = 2.2, 2e-1, 2.;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 204))
        
    # def test1(self):
    #     input = """delta: integer = 3;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 201))