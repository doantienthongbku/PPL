import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    # =================================================================================
    # test general
    # =================================================================================
    def test1(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test2(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test3(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test4(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test5(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test6(self):
        input = """
foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

main: function void () {
     printInteger(4);
}"""
        expect = """Program([
\tFuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
\tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))
        
    def test7(self):
        input = """
foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

main: function void () {
     printInteger(4);
     x, y, z: integer = 1, 2, 3;
     x = y + z;
     sum: integer = x + y + z;
}"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4)), VarDecl(x, IntegerType, IntegerLit(1)), VarDecl(y, IntegerType, IntegerLit(2)), VarDecl(z, IntegerType, IntegerLit(3)), AssignStmt(Id(x), BinExpr(+, Id(y), Id(z))), VarDecl(sum, IntegerType, BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
        
    def test8(self):
        input = """a: array[3] of integer;
        c: float = 4;
        b: array[3] of integer = {1, 2, 3};"""
        expect = """Program([
	VarDecl(a, ArrayType([3], IntegerType))
	VarDecl(c, FloatType, IntegerLit(4))
	VarDecl(b, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
        
    def test9(self):
        input = """b,c: integer = 4,5;
        i: integer;
        main: function void () {
            a: array[3] of integer = {1, 2, 4};
            while (i < 3) printString("hehe");
            
            while (i < 3) {
                a[1] = 3;
                printString("hehe");
            }
            
            return;
        }"""
        expect = """Program([
	VarDecl(b, IntegerType, IntegerLit(4))
	VarDecl(c, IntegerType, IntegerLit(5))
	VarDecl(i, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(4)])), WhileStmt(BinExpr(<, Id(i), IntegerLit(3)), CallStmt(printString, StringLit(hehe))), WhileStmt(BinExpr(<, Id(i), IntegerLit(3)), BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1)]), IntegerLit(3)), CallStmt(printString, StringLit(hehe))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
        
    def test10(self):
        input = """b,c: integer = 4,5;
                i: integer;
                main: function void () {
                    a: array[3] of integer = {3};
                    for (i = 0, i < 3, i + 1) {
                        if (a[i] == b + c) {
                            printString("a[i] = b + c");
                        } else
                            printString("a[i] != b + c");
                    }
                    return;
                }"""
        expect = """Program([
	VarDecl(b, IntegerType, IntegerLit(4))
	VarDecl(c, IntegerType, IntegerLit(5))
	VarDecl(i, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(3)])), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(Id(a), [Id(i)]), BinExpr(+, Id(b), Id(c))), BlockStmt([CallStmt(printString, StringLit(a[i] = b + c))]), CallStmt(printString, StringLit(a[i] != b + c)))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))
        
    def test11(self):
        input = """delta : integer = a;
                foo : function integer (inherit out a: integer, out b: boolean) {
                    a, b, c: string = 3, "hello", true;
                    if (a == 3)
                        return a + b;
                    else
                        return a > b;
                }"""
        expect = """Program([
	VarDecl(delta, IntegerType, Id(a))
	FuncDecl(foo, IntegerType, [InheritOutParam(a, IntegerType), OutParam(b, BooleanType)], None, BlockStmt([VarDecl(a, StringType, IntegerLit(3)), VarDecl(b, StringType, StringLit(hello)), VarDecl(c, StringType, BooleanLit(True)), IfStmt(BinExpr(==, Id(a), IntegerLit(3)), ReturnStmt(BinExpr(+, Id(a), Id(b))), ReturnStmt(BinExpr(>, Id(a), Id(b))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
        
    def test12(self):
        input = """
                    foo : function void (x : integer) {
                        x = 3;
                        while (x < 10) {
                            x = x + 1;
                        }
                        if (x == 10) {
                            continue;
                        }
                        printString(x);
                        return true;
                    }
                """
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(x, IntegerType)], None, BlockStmt([AssignStmt(Id(x), IntegerLit(3)), WhileStmt(BinExpr(<, Id(x), IntegerLit(10)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))])), IfStmt(BinExpr(==, Id(x), IntegerLit(10)), BlockStmt([ContinueStmt()])), CallStmt(printString, x), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))
        
    # =================================================================================
    # test expression
    # =================================================================================
    def test13(self):
        input = """
                    main : function void () {
                        a = 3 + 2 - b[1] * 2 / 3;
                        return;
                    }
                """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, BinExpr(+, IntegerLit(3), IntegerLit(2)), BinExpr(/, BinExpr(*, ArrayCell(Id(b), [IntegerLit(1)]), IntegerLit(2)), IntegerLit(3)))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
        
    def test14(self):
        input = """
                    main : function void () {
                        a: string = "hello";
                        b: string = " world";
                        
                        c: string = a :: b;
                        printString(c);
                        
                        return;
                    }
                """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, StringLit(hello)), VarDecl(b, StringType, StringLit( world)), VarDecl(c, StringType, BinExpr(::, Id(a), Id(b))), CallStmt(printString, c), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))
        
    def test15(self):
        # test relational operator
        input = """
                    main : function integer () {
                        a: boolean = true;
                        b: boolean = false;
                        c: integer = 3;
                        d: integer = 4;
                        
                        if ((a == b) && (c > d)) {
                            printString("a == b and c > d");
                            return a;
                        } else
                            return b;
                        
                        return 0;
                    }
                """
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(a, BooleanType, BooleanLit(True)), VarDecl(b, BooleanType, BooleanLit(False)), VarDecl(c, IntegerType, IntegerLit(3)), VarDecl(d, IntegerType, IntegerLit(4)), IfStmt(BinExpr(&&, BinExpr(==, Id(a), Id(b)), BinExpr(>, Id(c), Id(d))), BlockStmt([CallStmt(printString, StringLit(a == b and c > d)), ReturnStmt(Id(a))]), ReturnStmt(Id(b))), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))
        
    def test16(self):
        input = """main : function void () {
                        a: array[2, 2] of integer = {{1, 2}, {3, 4}};
                        printInteger(a[1, 1]);
                        b: integer = 3;
                        c: integer = b + a[1, 1];
                        printInteger(c);
                        
                        return;
                    }
                """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4)])])), CallStmt(printInteger, ArrayCell(Id(a), [IntegerLit(1), IntegerLit(1)])), VarDecl(b, IntegerType, IntegerLit(3)), VarDecl(c, IntegerType, BinExpr(+, Id(b), ArrayCell(Id(a), [IntegerLit(1), IntegerLit(1)]))), CallStmt(printInteger, c), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
    
            
    def test17(self):
        input = """
                    foo : function string (x : integer) {
                        i: integer = 0;
                        for (i = 0, i < 10, i + 1) {
                            x = x + i;
                        }
                        return x;
                    }
                    goo : function integer (x : integer) {
                        if ((x % 2) == 0)
                            return x;
                        else {
                            return x + 1;
                        }
                    }
                    main : function void () {
                        a: array [3] of integer = {1,2,3};
                        a[0] = foo(4) + 5;
                        b: array [3] of integer = {goo(1), goo(2), goo(3)};
                        
                        return;
                    }    
                """
        expect = """Program([
	FuncDecl(foo, StringType, [Param(x, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), Id(i)))])), ReturnStmt(Id(x))]))
	FuncDecl(goo, IntegerType, [Param(x, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(x), IntegerLit(2)), IntegerLit(0)), ReturnStmt(Id(x)), BlockStmt([ReturnStmt(BinExpr(+, Id(x), IntegerLit(1)))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), AssignStmt(ArrayCell(a, [IntegerLit(0)]), BinExpr(+, FuncCall(foo, [IntegerLit(4)]), IntegerLit(5))), VarDecl(b, ArrayType([3], IntegerType), ArrayLit([FuncCall(goo, [IntegerLit(1)]), FuncCall(goo, [IntegerLit(2)]), FuncCall(goo, [IntegerLit(3)])])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))
        
    def test18(self):
        input = """
                    main : function void () {
                        a: array [3] of integer = {1,2,3};
                        
                        a[2] = -a[1] * 2;
                        c: boolean = !(a[2] > 0);
                        printBoolean(c);
                        
                        return;
                    }    
                """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), AssignStmt(ArrayCell(a, [IntegerLit(2)]), BinExpr(*, UnExpr(-, ArrayCell(Id(a), [IntegerLit(1)])), IntegerLit(2))), VarDecl(c, BooleanType, UnExpr(!, BinExpr(>, ArrayCell(Id(a), [IntegerLit(2)]), IntegerLit(0)))), CallStmt(printBoolean, c), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
        
    def test19(self):
        input = """foo: function integer (x: integer) {
            return x + 1;
        }
        main : function void () {
                        a: array [3] of integer = {1,2,3};
                        
                        a[2] = -a[1] * 2 + foo(3);
                        c: boolean = !(a[2] > foo(3));
                        printBoolean(c);
                        
                        return;
                    }    
        """
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(x), IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), AssignStmt(ArrayCell(a, [IntegerLit(2)]), BinExpr(+, BinExpr(*, UnExpr(-, ArrayCell(Id(a), [IntegerLit(1)])), IntegerLit(2)), FuncCall(foo, [IntegerLit(3)]))), VarDecl(c, BooleanType, UnExpr(!, BinExpr(>, ArrayCell(Id(a), [IntegerLit(2)]), FuncCall(foo, [IntegerLit(3)])))), CallStmt(printBoolean, c), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))
        

    # =================================================================================
    # test statement
    # =================================================================================
    def test20(self):
        input = """
                    main : function void () {
                        a: array [3] of integer = {1,2,3};
                        foo(4);
                    }    
                    foo : function string (x : integer) {
                        foo(3);
                        main();
                    }
                    goo : function integer (x : integer) {
                        goo(3);
                        main();
                    }
                    hoo : function float (x : integer) {
                        hoo(3);
                        main();
                    }
                """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), CallStmt(foo, IntegerLit(4))]))
	FuncDecl(foo, StringType, [Param(x, IntegerType)], None, BlockStmt([CallStmt(foo, IntegerLit(3)), CallStmt(main, )]))
	FuncDecl(goo, IntegerType, [Param(x, IntegerType)], None, BlockStmt([CallStmt(goo, IntegerLit(3)), CallStmt(main, )]))
	FuncDecl(hoo, FloatType, [Param(x, IntegerType)], None, BlockStmt([CallStmt(hoo, IntegerLit(3)), CallStmt(main, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))