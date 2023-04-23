import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    
    def test_decl_order(self):
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
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_decl_order_2(self):
        input = """
        main: function void() {
            res : auto = readString();
            b: integer = a;
        }
        foo : function auto (){}
        a : integer = 1;
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    
    def test_name_simple_1(self):
        input = """
        main: function void(){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_name_simple_2(self):
        input = """
        a,b,c,a: integer;
        main: function void(){
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_name_simple_3(self):
        input = """
        a: integer;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_name_simple_5(self):
        input = """
        main: function integer(){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))
        
    def test_name_simple_6(self):
        input = """
        main: function void(a: integer){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_name_simple_7(self):
        input = """
        foo: function integer (){}
        main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_name_simple_8(self):
        input = """
        foo: function integer (){}
        main: function void(){}
        height, weight : integer;
        foo : integer;
        """
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_name_simple_9(self):
        input = """
        main: function void() {
        }
        main: function void() {
        }
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_name_simple_10(self):
        input = """
        main: function void(){}
        height, weight : integer;
        readInteger : integer;
        """
        expect = "Redeclared Variable: readInteger"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_vardecl_1(self):
        input = """
        main: function void() {}
        a: auto;
        """
        expect = "Invalid Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_vardecl_2(self):
        input = """
        main: function void(){}
        a, b, c, d: auto = 1, 2.5, "My name is Hoa", true;
        e : integer = 2.5;
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(e, IntegerType, FloatLit(2.5))"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_vardecl_3(self):
        input = """
        area : float = 2.5;
        an : float = 1 ;
        x : float = true;
        main: function void(){}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(x, FloatType, BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_array_1(self):
        input = """
        arr : array [3] of integer = {1,2,3.3};
        main: function void(){}
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), FloatLit(3.3)])"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_array_2(self):
        input = """
        arr : array [3] of integer = {1.0,2.2,3.3};
        main: function void(){}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([3], IntegerType), ArrayLit([FloatLit(1.0), FloatLit(2.2), FloatLit(3.3)]))"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_array_3(self):
        input = """
        arr : array [2,3,4,5] of integer;
        main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_array_7(self):
        input = """
        arr : array [2] of integer = {1,2};
        a : float = 1.0;
        element : integer = arr[a];
        main: function void(){
            
        }
        """
        expect = "Type mismatch in expression: ArrayCell(arr, [Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_array_8(self):
        input = """
        a : float = 1.0;
        element : integer = a[1.0];
        main: function void(){
        }
        """
        expect = "Type mismatch in expression: ArrayCell(a, [FloatLit(1.0)])"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_array_9(self):
        input = """
        element : string = arr[10];
        main: function void(){
        }
        """
        expect = "Undeclared Identifier: arr"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_array_10(self):
        input = """
        arr : array [5] of integer = {0,1,2,3,4};
        element : integer = arr[arr[0]];
        main: function void(){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,400))