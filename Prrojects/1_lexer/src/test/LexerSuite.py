import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
        
    def test1(self):
        input = "21A"
        expect = "21A,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 101))