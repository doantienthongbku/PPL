import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test_1(self):
    #     input = """a : integer;
    #     c: float;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 401))
        
    # def test_2(self):
    #     input = """a: integer = 5;
    #     c: auto;"""
    #     expect = "Invalid Variable: c"
    #     self.assertTrue(TestChecker.test(input, expect, 402))
    
    # # test_decl_order
    # def test_3(self):
    #     input = """
    #     main: function void(){
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,403))
        
    # def test_4(self):
    #     input = """
    #     a,b,c,a: integer;
    #     main: function void(){
    #     }
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,404))
    
    # def test_5(self):
    #     input = """
    #     main: function integer(){}
    #     """
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input,expect,405))
        
    # def test_6(self):
    #     input = """
    #     main: function void(a: integer){}
    #     """
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input,expect,406))
        
    # def test_7(self):
    #     input = """
    #     foo: function integer (){}
    #     main: function void(){}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,407))

    # def test_8(self):
    #     input = """
    #     foo: function integer (){}
    #     main: function void(){}
    #     height, weight : integer;
    #     foo : integer;
    #     """
    #     expect = "Redeclared Variable: foo"
    #     self.assertTrue(TestChecker.test(input,expect,408))
        
    # def test_9(self):
    #     input = """
    #     main: function void() {
    #     }
    #     main: function void() {
    #     }
    #     """
    #     expect = "Redeclared Function: main"
    #     self.assertTrue(TestChecker.test(input,expect,409))

    # def test_10(self):
    #     input = """
    #     main: function void() {}
    #     a: auto;
    #     """
    #     expect = "Invalid Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,410))
    
    # def test_11(self):
    #     input = """
    #     main: function void(){}
    #     a, b, c, d: auto = 1, 2.5, "My name is Hoa", true;
    #     e : integer = 2.5;
    #     """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(e, IntegerType, FloatLit(2.5))"
    #     self.assertTrue(TestChecker.test(input,expect,411))
        
    # def test_12(self):
    #     input = """
    #     area : float = 2.5;
    #     an : float = 1 ;
    #     x : float = true;
    #     main: function void(){}
    #     """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(x, FloatType, BooleanLit(True))"
    #     self.assertTrue(TestChecker.test(input,expect,412))
        
    # def test_13(self):
    #     input = """
    #     main: function void() {
    #         res : auto = readString();
    #         b: integer = a;
    #     }
    #     foo : function auto (){}
    #     a : integer = 1;
    #     """
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input,expect,413))
    
    # def test_14(self):
    #     input = """
    #     a : integer = 1;
    #     a : integer = 2;
    #     main: function void() {
    #         b: integer = 3;
    #         b: integer = 4;
    #     }
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,414))
    
    def test_15(self):
        input = """
        a : integer = 1;
        main: function void() {
            res : auto = readString();
            b: integer = a;
            res = foo() + foo(2); 
        }
        foo : function auto (){}
        """
        expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input,expect,415))