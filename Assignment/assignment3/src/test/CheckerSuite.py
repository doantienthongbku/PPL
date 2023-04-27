import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_1(self):
        input = """a : integer;
        c: float;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    def test_2(self):
        input = """a: integer = 5;
        c: auto;"""
        expect = "Invalid Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    # test_decl_order
    def test_3(self):
        input = """
        main: function void(){
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,403))
        
    def test_4(self):
        input = """
        a,b,c,a: integer;
        main: function void(){
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))
    
    def test_5(self):
        input = """
        main: function integer(){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,405))
        
    def test_6(self):
        input = """
        main: function void(a: integer){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,406))
        
    def test_7(self):
        input = """
        foo: function integer (){}
        main: function void(){}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_8(self):
        input = """
        foo: function integer (){}
        main: function void(){}
        height, weight : integer;
        foo : integer;
        """
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input,expect,408))
        
    def test_9(self):
        input = """
        main: function void() {
        }
        main: function void() {
        }
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_10(self):
        input = """
        main: function void() {}
        a: auto;
        """
        expect = "Invalid Variable: a"
        self.assertTrue(TestChecker.test(input,expect,410))
    
    def test_11(self):
        input = """
        main: function void(){}
        a, b, c, d: auto = 1, 2.5, "My name is Hoa", true;
        e : integer = 2.5;
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(e, IntegerType, FloatLit(2.5))"
        self.assertTrue(TestChecker.test(input,expect,411))
        
    def test_12(self):
        input = """
        area : float = 2.5;
        an : float = 1 ;
        x : float = true;
        main: function void(){}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(x, FloatType, BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,412))
        
    def test_13(self):
        input = """
        main: function void() {
            res : auto = readString();
            b: integer = a;
        }
        foo : function auto (){}
        a : integer = 1;
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,413))
    
    def test_14(self):
        input = """
        a : integer = 1;
        a : integer = 2;
        main: function void() {
            b: integer = 3;
            b: integer = 4;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,414))
    
    def test_15(self):
        input = """
        a : integer = 1;
        foo : function auto (){}
        main: function void() {
            res : auto = readString();
            b: integer = a;
            res = foo() + foo(2); 
        }
        """
        expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input,expect,415))
    
    def test_16(self):
        input = """a : integer = 12;
        b: integer = 13;
        c: string = "abc";
        foo : function string (d: integer, d: string) {
            d: integer = 12;
        }
        main : function void () {}"""
        expect = "Redeclared Parameter: d"
        self.assertTrue(TestChecker.test(input, expect, 416))
        
    def test_17(self):
        input = """a : integer = 12;
        b: integer = 13;
        c: string = "abc";
        main : function void () {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 417))
        
    def test_18(self):
        input = """foo: function string (a: integer, b: string) {
            a = b;
        }
        main: function void () {

        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
    def test_19(self):
        input = """c: integer = 3;
        foo: function string (a: integer, b: integer) {
            a = b;
            b = c;
        }
        main: function void () {

        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 419))
        
    def test_20(self):
        input = """a: integer = "string";
        foo: function string(b: integer) {}
        main: function void() {
            a = 3;
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 420))
    
    def test_21(self):
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
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_22(self):
        input = """a: auto = readString();
        main: function void() {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test_23(self):
        input = """
        a : integer = 1;
        b : integer = 2;
        main: function void() {
            b: integer = 3;
            a: integer = 4;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,423))
    
    def test_24(self):
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
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input,expect,424))
    
    def test_25(self):
        input = """foo: function integer(){}
        main: function void(){
            m: integer;
            m = foo + 1;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,425))
    
    def test_26(self):
        input = """m: string;
        foo: function integer(a: integer){
            m, n: string;
            m = n;
        }
        main: function void(){
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,426))
    
    def test_27(self):
        input = """m: integer;
        foo: function integer(a: integer){
            for (m = 0, m > 3, m + 1) {
                break;
            }
        }
        main: function void(){
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(m), IntegerLit(0))"
        self.assertTrue(TestChecker.test(input,expect,427))
    
    def test_28(self):
        input = """
        arr : array [3] of integer = {1,2,3.3};
        main: function void(){}
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), FloatLit(3.3)])"
        self.assertTrue(TestChecker.test(input,expect,428))
        
    def test_29(self):
        input = """
        arr : array [3] of integer = {1.0,2.2,3.3};
        main: function void(){}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([3], IntegerType), ArrayLit([FloatLit(1.0), FloatLit(2.2), FloatLit(3.3)]))"
        self.assertTrue(TestChecker.test(input,expect,429))
    
    def test_30(self):
        input = """
        arr : array [2,3,4,5] of integer;
        main: function void(){}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))
    
    def test_31(self):
        input = """
        arr : array [2] of integer = {1,2};
        a : float = 1.0;
        element : integer = arr[a];
        main: function void(){
            
        }
        """
        expect = "Type mismatch in expression: ArrayCell(arr, [Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,431))
    
    def test_32(self):
        input = """
        a : float = 1.0;
        element : integer = a[1.0];
        main: function void(){
        }
        """
        expect = "Type mismatch in expression: ArrayCell(a, [FloatLit(1.0)])"
        self.assertTrue(TestChecker.test(input,expect,432))
    
    def test_33(self):
        input = """
        element : string = arr[10];
        main: function void(){
        }
        """
        expect = "Undeclared Identifier: arr"
        self.assertTrue(TestChecker.test(input,expect,433))
    
    def test_34(self):
        input = """
        arr : array [5] of integer = {0,1,2,3,4};
        element : integer = arr[arr[0]];
        main: function void(){
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,434))
        
    def test_35(self):
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
        self.assertTrue(TestChecker.test(input,expect,435))
        
    def test_36(self):
        input = """
        i:auto = 0;
        a: array [5] of integer;
        main: function void(){
            a:integer = 1;
        }
        sum : function auto(c: auto) inherit sum1{
           super(1,2,3);
            
        }
        sum1 : function integer(inherit a:integer, inherit b:integer){
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test_37(self):
        input = """
        a: array [5] of integer;
        main: function void(){
            hehe:integer = 1;
        }
        foo: function void (inherit a: integer, a: float) inherit bar {
            
        }
        """
        expect = """Undeclared Function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 437))
    
    def test_38(self):
        input = """
        a: array [5] of integer;
        main: function void(){
        }
        x: function auto(){
            
        } 

        foo:function void() {
            a1: auto = x() + x();
        }
        """
        expect = """Type mismatch in expression: BinExpr(+, FuncCall(x, []), FuncCall(x, []))"""
        self.assertTrue(TestChecker.test(input, expect, 438))
    
    def test_39(self):
        input = """
        main: function void(){
            hehe:integer = 1;
            bar(1);
        }
        bar: function void (inherit c: integer){

        }
        foo: function void (a: integer) inherit bar {
            preventDefault();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 439))
    
    def test_40(self):
        input = """
        main: function void(){
        }
        foo: function void (a: auto, c: auto){
            a: float = 1;
            foo(1.2, 1.2);
            foo(1.2, 1);
        }
        """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 440))
    
    def test9(self):
        input = """
        main: function void(c: integer) inherit func{
            super(1,2);
            super(1,2);
        }
        func :function auto (inherit a: auto, inherit b :auto){
            
        }
        """
        expect = """Invalid statement in function: main"""
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test10(self):
        input = """
        main: function void(c: integer) inherit func{
            preventDefault();
            func(1,2);
            d:integer = func(1,2);
        }
        func :function auto (inherit a: auto, inherit b :auto){
            
        
        }
        func1 :function auto (inherit a: auto, inherit b :auto){
            func("1",2);
        }
        
        """
        expect = """Type mismatch in statement: CallStmt(func, StringLit(1), IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 410))
    