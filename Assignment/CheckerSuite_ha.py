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
        
        
        
        
## huhuhu

    def test_1(self):
        input = """a : integer = 12;
        b: integer = 13;
        c: string = "abc";
        foo : function string (d: integer, d: string) {
            d: integer = 12;
        }
        main : function void () {}"""
        expect = "Redeclared Parameter: d"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_2(self):
        input = """foo: function string () {
        }
        foo: function string () {
        }
        main: function void () {
        }"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_3(self):
        input = """a : integer = 12;
        b: integer = 13;
        c: string = "abc";
        main : function void () {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_4(self):
        input = """foo: function string (a: integer, b: string) {
            a = b;
        }
        main: function void () {

        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_5(self):
        input = """c: integer = 3;
        foo: function string (a: integer, b: integer) {
            a = b;
            b = c;
        }
        main: function void () {

        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_6(self):
        input = """a: integer = "string";
        foo: function string(b: integer) {}
        main: function void() {
            a = 3;
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_7(self):
        input = """a: auto = 3;
        b: auto = 4;
        foo: function string() {
            b: auto = 3;
            if (a == 3) {
                a = 4;
            }
            else
                a = 5;
        }
        main: function void() {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_8(self):
        input = """a: auto = readString();
        main: function void() {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 408))
    
    def test_9(self):
        input = """
        a : integer = 1;
        b : integer = 2;
        main: function void() {
            b: integer = 3;
            a: integer = 4;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test_10(self):
        input = """
        main: function void() {
            i: integer;
            a: integer = 0;
            while (i < 10) {
                a = a + 1;
                i = i + 1;
                break;
            }
            break;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,410))
    
    def test_11(self):
        input = """foo: function integer(){}
        main: function void(){
            m: integer;
            m = foo + 1;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,411))
    
    def test_12(self):
        input = """m: string;
        foo: function integer(a: integer){
            m, n: string;
            m = n;
        }
        main: function void(){
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,412))
    
    def test_13(self):
        input = """m: integer;
        foo: function integer(a: integer){
            for (m = 0, m > 3, m + 1) {
                break;
            }
        }
        main: function void(){
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,413))    