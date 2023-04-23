import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        input = """int a, b,c;
float foo(int a; float c, d) body
float goo (float a, b) body"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
