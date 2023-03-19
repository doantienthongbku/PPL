import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
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
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(3)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [Id(i)]), BinExpr(+, Id(b), Id(c))), BlockStmt([CallStmt(printString, StringLit(a[i] = b + c))]), CallStmt(printString, StringLit(a[i] != b + c)))])), ReturnStmt()]))
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
	FuncDecl(foo, VoidType, [Param(x, IntegerType)], None, BlockStmt([AssignStmt(Id(x), IntegerLit(3)), WhileStmt(BinExpr(<, Id(x), IntegerLit(10)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))])), IfStmt(BinExpr(==, Id(x), IntegerLit(10)), BlockStmt([ContinueStmt()])), CallStmt(printString, Id(x)), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))
        
    def test13(self):
        input = """
                    main : function void () {
                        a = 3 + 2 - b[1] * 2 / 3;
                        return;
                    }
                """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, BinExpr(+, IntegerLit(3), IntegerLit(2)), BinExpr(/, BinExpr(*, ArrayCell(b, [IntegerLit(1)]), IntegerLit(2)), IntegerLit(3)))), ReturnStmt()]))
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
        expect= """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, StringLit(hello)), VarDecl(b, StringType, StringLit( world)), VarDecl(c, StringType, BinExpr(::, Id(a), Id(b))), CallStmt(printString, Id(c)), ReturnStmt()]))
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
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4)])])), CallStmt(printInteger, ArrayCell(a, [IntegerLit(1), IntegerLit(1)])), VarDecl(b, IntegerType, IntegerLit(3)), VarDecl(c, IntegerType, BinExpr(+, Id(b), ArrayCell(a, [IntegerLit(1), IntegerLit(1)]))), CallStmt(printInteger, Id(c)), ReturnStmt()]))
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
	FuncDecl(foo, StringType, [Param(x, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), Id(i)))])), ReturnStmt(Id(x))]))
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
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), AssignStmt(ArrayCell(a, [IntegerLit(2)]), BinExpr(*, UnExpr(-, ArrayCell(a, [IntegerLit(1)])), IntegerLit(2))), VarDecl(c, BooleanType, UnExpr(!, BinExpr(>, ArrayCell(a, [IntegerLit(2)]), IntegerLit(0)))), CallStmt(printBoolean, Id(c)), ReturnStmt()]))
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
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), AssignStmt(ArrayCell(a, [IntegerLit(2)]), BinExpr(+, BinExpr(*, UnExpr(-, ArrayCell(a, [IntegerLit(1)])), IntegerLit(2)), FuncCall(foo, [IntegerLit(3)]))), VarDecl(c, BooleanType, UnExpr(!, BinExpr(>, ArrayCell(a, [IntegerLit(2)]), FuncCall(foo, [IntegerLit(3)])))), CallStmt(printBoolean, Id(c)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))
        

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
        
    def test21(self):
        input = """main: function void () {
            do {
                printString("chao cau");
                a = a + 1;
            } while (i < 1);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printString, StringLit(chao cau)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))
    
    def test22(self):
        input = """main: function void () {
            for (i = 0, i < 10, i + 1) {
                if (i == 0) continue;
                else break;
            }
            
            return;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(0)), ContinueStmt(), BreakStmt())])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))
        
    def test23(self):
        input = """
                    main : function void () {
                        a[1+1,a>b,2,3,4] = 0;
                        if (a[1+1,a>b,2,3,4] == 0) {
                            continue;
                        }
                        
                        return;
                    }
                """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(>, Id(a), Id(b)), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), IntegerLit(0)), IfStmt(BinExpr(==, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(>, Id(a), Id(b)), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), IntegerLit(0)), BlockStmt([ContinueStmt()])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))
        
    def test24(self):
        input = """
                    main : function void () {
                        a[1+1,a>b,2,3,4] = 0;
                        for (a[1+1,a>b,2,3,4] = 0, i < 10, a[1+1,a>b,2,3,4] + 1) {
                            break;
                        }
                        
                        return;
                    }
                """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(>, Id(a), Id(b)), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), IntegerLit(0)), ForStmt(AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(>, Id(a), Id(b)), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(>, Id(a), Id(b)), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), IntegerLit(1)), BlockStmt([BreakStmt()])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
    
    def test25(self):
        input = """
                    main : function void () {
                        a[1+1,a>b,2,3,4] = 0;
                        do {
                            continue;
                        } while (a[1+1,a>b,2,3,4] <= 10);
                        
                        return;
                    }
                """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(>, Id(a), Id(b)), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), IntegerLit(0)), DoWhileStmt(BinExpr(<=, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(>, Id(a), Id(b)), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), IntegerLit(10)), BlockStmt([ContinueStmt()])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
        
    def test26(self):
        input = """
                    foo: function string (x : string) {
                        x = x :: "abc";
                        return x;
                    }
                    main : function void () {
                        a: string = foo("abcd");
                        return;
                    }
                """
        expect = """Program([
	FuncDecl(foo, StringType, [Param(x, StringType)], None, BlockStmt([AssignStmt(Id(x), BinExpr(::, Id(x), StringLit(abc))), ReturnStmt(Id(x))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, FuncCall(foo, [StringLit(abcd)])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))


    def test27(self):
        input = """
                    main : function void () {
                        a: integer = readInteger();
                        b =  readInteger();
                        printInteger(a + 10 - 5 * 2 / 2);
                        return;
                    }
                """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, FuncCall(readInteger, [])), AssignStmt(Id(b), FuncCall(readInteger, [])), CallStmt(printInteger, BinExpr(-, BinExpr(+, Id(a), IntegerLit(10)), BinExpr(/, BinExpr(*, IntegerLit(5), IntegerLit(2)), IntegerLit(2)))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))
        
    def test28(self):
        input = """
                    bubbleSort : function array [3] of integer (arr: array [3] of integer) {
                        for (i = 0, i < n, i + 1) {
                            for (j = 0, j < n - i - 1, j + 1) {
                                if (arr[j] > arr[j + 1]) {
                                    swap(arr[j], arr[j + 1]);
                                }
                            }
                        }
                    }
                """
        expect = """Program([
	FuncDecl(bubbleSort, ArrayType([3], IntegerType), [Param(arr, ArrayType([3], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), BinExpr(-, BinExpr(-, Id(n), Id(i)), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), BlockStmt([CallStmt(swap, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
        
    def test29(self):
        input = """
                a : float = 2 + 2%2/2*-2 ;
                b : float = 1*1--1+1/1 ;
                c : float = a + b / (2*1.0+1) ;
        """
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(+, IntegerLit(2), BinExpr(*, BinExpr(/, BinExpr(%, IntegerLit(2), IntegerLit(2)), IntegerLit(2)), UnExpr(-, IntegerLit(2)))))
	VarDecl(b, FloatType, BinExpr(+, BinExpr(-, BinExpr(*, IntegerLit(1), IntegerLit(1)), UnExpr(-, IntegerLit(1))), BinExpr(/, IntegerLit(1), IntegerLit(1))))
	VarDecl(c, FloatType, BinExpr(+, Id(a), BinExpr(/, Id(b), BinExpr(+, BinExpr(*, IntegerLit(2), FloatLit(1.0)), IntegerLit(1)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
        
    def test30(self):
        input = """
        a : boolean = true ;
        b : boolean = !a && false || (false && true || true) ;  
        c : boolean = !!b || false ;
        """
        expect = """Program([
	VarDecl(a, BooleanType, BooleanLit(True))
	VarDecl(b, BooleanType, BinExpr(||, BinExpr(&&, UnExpr(!, Id(a)), BooleanLit(False)), BinExpr(||, BinExpr(&&, BooleanLit(False), BooleanLit(True)), BooleanLit(True))))
	VarDecl(c, BooleanType, BinExpr(||, UnExpr(!, UnExpr(!, Id(b))), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
        
    def test31(self):
        input = """
        a1, a2 : string = "Hello ", "World!" ;
        a: string = a1 :: a2 ;            
        a: string = (a :: ( a :: "a" ) ) :: a;        
        """
        expect = """Program([
	VarDecl(a1, StringType, StringLit(Hello ))
	VarDecl(a2, StringType, StringLit(World!))
	VarDecl(a, StringType, BinExpr(::, Id(a1), Id(a2)))
	VarDecl(a, StringType, BinExpr(::, BinExpr(::, Id(a), BinExpr(::, Id(a), StringLit(a))), Id(a)))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
        
    def test32(self):
        input = """               
        a : boolean = (3 > 2 ) || (7/2 <= 4+3) && !(1.0e1+1 >= 0) ;     
        """
        expect = """Program([
	VarDecl(a, BooleanType, BinExpr(&&, BinExpr(||, BinExpr(>, IntegerLit(3), IntegerLit(2)), BinExpr(<=, BinExpr(/, IntegerLit(7), IntegerLit(2)), BinExpr(+, IntegerLit(4), IntegerLit(3)))), UnExpr(!, BinExpr(>=, BinExpr(+, FloatLit(10.0), IntegerLit(1)), IntegerLit(0)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))
        
    def test33(self):
        input = """               
            arr : array [1_0] of float = {1,2,3,4,5,6,7,8,9,10};
        """
        expect = """Program([
	VarDecl(arr, ArrayType([10], FloatType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))
        
    def test34(self):
        input = """               
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
        """
        expect = """Program([
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))
        
    def test35(self):
        input = """
        average : float = 0.0;
        beginString : string = "";
        main: function void () {
                beginString = "hello world";
                average = sum/number;
        }"""
        expect = """Program([
	VarDecl(average, FloatType, FloatLit(0.0))
	VarDecl(beginString, StringType, StringLit())
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(beginString), StringLit(hello world)), AssignStmt(Id(average), BinExpr(/, Id(sum), Id(number)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))
        
    def test36(self):
        input = """
        main: function void () {
              if (a>b) {a = b;}
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))
        
    def test37(self):
        input = """
        main: function void () {
              if (a>b) {}
              else a = "This is 'else' ";                
              
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), AssignStmt(Id(a), StringLit(This is 'else' )))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))
    
    def test38(self):
        input = """
        main: function void () {
              if (a>b) {}
              else if (true) a = b;
                  else a = 0;           
              
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), IfStmt(BooleanLit(True), AssignStmt(Id(a), Id(b)), AssignStmt(Id(a), IntegerLit(0))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))
        
    def test39(self):
        input = """
        modArray: function array[3] of integer (inherit a: array[3] of integer,out n: integer){
            a[0] = a[0] + n;
            if(a[1] < n) a[1] = a[1] + n; 
            if(a[2] > 0) return a;
            else a[2] = -a[2];
            return a;
        }
        """
        expect = """Program([
	FuncDecl(modArray, ArrayType([3], IntegerType), [InheritParam(a, ArrayType([3], IntegerType)), OutParam(n, IntegerType)], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(0)]), BinExpr(+, ArrayCell(a, [IntegerLit(0)]), Id(n))), IfStmt(BinExpr(<, ArrayCell(a, [IntegerLit(1)]), Id(n)), AssignStmt(ArrayCell(a, [IntegerLit(1)]), BinExpr(+, ArrayCell(a, [IntegerLit(1)]), Id(n)))), IfStmt(BinExpr(>, ArrayCell(a, [IntegerLit(2)]), IntegerLit(0)), ReturnStmt(Id(a)), AssignStmt(ArrayCell(a, [IntegerLit(2)]), UnExpr(-, ArrayCell(a, [IntegerLit(2)])))), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))
        
    def test40(self):
        input = """
        a : integer = round(1.23-1.496, b);
        """
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(round, [BinExpr(-, FloatLit(1.23), FloatLit(1.496)), Id(b)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))
        
    def test41(self):
        input = """               
        a : integer = toInt(bc_, 2, 10) + randomInt() ;
        """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(+, FuncCall(toInt, [Id(bc_), IntegerLit(2), IntegerLit(10)]), FuncCall(randomInt, [])))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))
        
    def test42(self):
        input = """               
                main : function void(){
                    arrB[0,0,arrB[0,0,arrB[i,i,0]]] = arrayA[10-1,8+1];
                }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(arrB, [IntegerLit(0), IntegerLit(0), ArrayCell(arrB, [IntegerLit(0), IntegerLit(0), ArrayCell(arrB, [Id(i), Id(i), IntegerLit(0)])])]), ArrayCell(arrayA, [BinExpr(-, IntegerLit(10), IntegerLit(1)), BinExpr(+, IntegerLit(8), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))
        
    def test43(self):
        input = """
        main: function void () {
              r : float = _callR(-1,2.0,a);
              area = pi * r * r;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, FloatType, FuncCall(_callR, [UnExpr(-, IntegerLit(1)), FloatLit(2.0), Id(a)])), AssignStmt(Id(area), BinExpr(*, BinExpr(*, Id(pi), Id(r)), Id(r)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))
        
    def test44(self):
        input = """x , y : boolean = true , false ;
                    a1, a2 : auto = b1, b2 ;"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	VarDecl(y, BooleanType, BooleanLit(False))
	VarDecl(a1, AutoType, Id(b1))
	VarDecl(a2, AutoType, Id(b2))
])""" 
        self.assertTrue(TestAST.test(input, expect, 343))
        
    def test45(self):
        input = """Rectangle: function void (a: float, b: integer, out c:float) {
        }
        Square: function void(inherit b: integer) inherit Rectangle{
            
        }
        """
        expect = """Program([
	FuncDecl(Rectangle, VoidType, [Param(a, FloatType), Param(b, IntegerType), OutParam(c, FloatType)], None, BlockStmt([]))
	FuncDecl(Square, VoidType, [InheritParam(b, IntegerType)], Rectangle, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))
        
    def test46(self):
        input = """main: function void () {
                b = a + a1;
                c = b*a/2.0;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(b), BinExpr(+, Id(a), Id(a1))), AssignStmt(Id(c), BinExpr(/, BinExpr(*, Id(b), Id(a)), FloatLit(2.0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))
    
    def test47(self):
        input = """
        a : integer = round(1.23-1.496, b);
        """
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(round, [BinExpr(-, FloatLit(1.23), FloatLit(1.496)), Id(b)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))
    
    def test48(self):
        input = """
        main: function void () {
                printInteger(a);    
                printFloat(b);
                printString("string");
                printBoolean(true);
                super(a,b);
                preventDefault();
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, Id(a)), CallStmt(printFloat, Id(b)), CallStmt(printString, StringLit(string)), CallStmt(printBoolean, BooleanLit(True)), CallStmt(super, Id(a), Id(b)), CallStmt(preventDefault, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))
        
    def test49(self):
        input = """
        main: function void () {
                a = readInteger();
                b = readFloat();
                c = readBoolean();
                d = readString();
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), FuncCall(readInteger, [])), AssignStmt(Id(b), FuncCall(readFloat, [])), AssignStmt(Id(c), FuncCall(readBoolean, [])), AssignStmt(Id(d), FuncCall(readString, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))
        
    def test50(self):
        input = """
        average : float = 0.0;
        beginString : string = "";
        main: function void () {
                beginString = "hello world";
                average = sum/number;
        }"""
        expect = """Program([
	VarDecl(average, FloatType, FloatLit(0.0))
	VarDecl(beginString, StringType, StringLit())
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(beginString), StringLit(hello world)), AssignStmt(Id(average), BinExpr(/, Id(sum), Id(number)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))
        
    def test51(self):
        input = """
        main: function void () {
                a = b + c;
                b = a - c;
                c = a * b;
                d = a / b;
                e = a % b;
                f = a && b;
                g = a || b;
                h = a == b;
                i = a != b;
                j = a < b;
                k = a <= b;
                l = a > b;
                m = a >= b;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(b), Id(c))), AssignStmt(Id(b), BinExpr(-, Id(a), Id(c))), AssignStmt(Id(c), BinExpr(*, Id(a), Id(b))), AssignStmt(Id(d), BinExpr(/, Id(a), Id(b))), AssignStmt(Id(e), BinExpr(%, Id(a), Id(b))), AssignStmt(Id(f), BinExpr(&&, Id(a), Id(b))), AssignStmt(Id(g), BinExpr(||, Id(a), Id(b))), AssignStmt(Id(h), BinExpr(==, Id(a), Id(b))), AssignStmt(Id(i), BinExpr(!=, Id(a), Id(b))), AssignStmt(Id(j), BinExpr(<, Id(a), Id(b))), AssignStmt(Id(k), BinExpr(<=, Id(a), Id(b))), AssignStmt(Id(l), BinExpr(>, Id(a), Id(b))), AssignStmt(Id(m), BinExpr(>=, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
        
    def test52(self):
        input = """
        count : auto = 0;
        main: function void () {
                
        }"""
        expect = """Program([
	VarDecl(count, AutoType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))
        
    def test53(self):
        input = """
        main: function void () {
              r : float = _callR(-1,2.0,a);
              area = pi * r * r;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, FloatType, FuncCall(_callR, [UnExpr(-, IntegerLit(1)), FloatLit(2.0), Id(a)])), AssignStmt(Id(area), BinExpr(*, BinExpr(*, Id(pi), Id(r)), Id(r)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))
        
    def test54(self):
        input = """
        main: function void () {
                if (true)
                a = a + 1;
                b = b - 2;         
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))), AssignStmt(Id(b), BinExpr(-, Id(b), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))
        
    def test55(self):
        input = """
        main: function void () {
        if (true)
                if (a == true)
                    if (b == false)
                        if (1)
                            a = 2;
                        else
                            b = 5;
                    else
                        a = 5;      
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), IfStmt(BinExpr(==, Id(a), BooleanLit(True)), IfStmt(BinExpr(==, Id(b), BooleanLit(False)), IfStmt(IntegerLit(1), AssignStmt(Id(a), IntegerLit(2)), AssignStmt(Id(b), IntegerLit(5))), AssignStmt(Id(a), IntegerLit(5)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))
        
    def test56(self):
        input = """
        main: function void () {
        if (a){
                b = a;
                c = a; 
                if (c != a){
                    c = a;
                    b = c;
                }
                else{
                    if (c == a){
                        d : boolean;
                        d = e;
                        d = b;
                    }
                    else{
                        if (!d){
                            y: float;
                        }
                    }
                }
            }
            else{
                if (!a){
                    d : string;
                    d = a;
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(a), BlockStmt([AssignStmt(Id(b), Id(a)), AssignStmt(Id(c), Id(a)), IfStmt(BinExpr(!=, Id(c), Id(a)), BlockStmt([AssignStmt(Id(c), Id(a)), AssignStmt(Id(b), Id(c))]), BlockStmt([IfStmt(BinExpr(==, Id(c), Id(a)), BlockStmt([VarDecl(d, BooleanType), AssignStmt(Id(d), Id(e)), AssignStmt(Id(d), Id(b))]), BlockStmt([IfStmt(UnExpr(!, Id(d)), BlockStmt([VarDecl(y, FloatType)]))]))]))]), BlockStmt([IfStmt(UnExpr(!, Id(a)), BlockStmt([VarDecl(d, StringType), AssignStmt(Id(d), Id(a))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))
        
    def test57(self):
        input = """
        main: function void () {
                if (a==c)
                        if (b==d)
                            if(lv==2) 
                                continue;
                            else c = a[c+1];
                        else return;
                else break;     
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(c)), IfStmt(BinExpr(==, Id(b), Id(d)), IfStmt(BinExpr(==, Id(lv), IntegerLit(2)), ContinueStmt(), AssignStmt(Id(c), ArrayCell(a, [BinExpr(+, Id(c), IntegerLit(1))]))), ReturnStmt()), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
        
    def test58(self):
        input = """
        main: function void () {  
                for (i = n-1, i > 0, i-1) {
                    r : float = a[i] ;                    
                    s = r * r * myPI;
                    printFloat(s);
                }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(>, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([VarDecl(r, FloatType, ArrayCell(a, [Id(i)])), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), CallStmt(printFloat, Id(s))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))
        
    def test59(self):
        input = """
        main: function void () {  
                for(i=1+2+3+4-1*2, i<=arr[2], i+arr[i]-1)
                {
                    printString(hello);
                    add(_);
                    move(___);
                }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)), BinExpr(*, IntegerLit(1), IntegerLit(2)))), BinExpr(<=, Id(i), ArrayCell(arr, [IntegerLit(2)])), BinExpr(-, BinExpr(+, Id(i), ArrayCell(arr, [Id(i)])), IntegerLit(1)), BlockStmt([CallStmt(printString, Id(hello)), CallStmt(add, Id(_)), CallStmt(move, Id(___))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))
        
        
    def test60(self):
        input = """
        main: function void () {  
                for(i=10, i>0, i-1)
                {
                }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(10)), BinExpr(>, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))
        
    def test61(self):
        input = """
        main: function void () {  
                for (i = 1, i <10, i+1) 
                        if (i % 2 == 0) continue;
                        else 
                                for(j = 0, j < 10, j + 1)
                                        print(arr[i,j]);
                a = 1;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), ContinueStmt(), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(10)), BinExpr(+, Id(j), IntegerLit(1)), CallStmt(print, ArrayCell(arr, [Id(i), Id(j)]))))), AssignStmt(Id(a), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))
        
    def test62(self):
        input = """
        main: function void () {  
                while (!true && !!false) {}
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(&&, UnExpr(!, BooleanLit(True)), UnExpr(!, UnExpr(!, BooleanLit(False)))), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))
        
    def test63(self):
        input = """
        main: function void () {  
                while (arr[a,b] == "Cat"){
                        while (a > 0) {
                                if (x) break;
                                a = a - 2; 
                                while (false) printFloat(3.2e2);
                        }
                        update(arr);
                }  
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, ArrayCell(arr, [Id(a), Id(b)]), StringLit(Cat)), BlockStmt([WhileStmt(BinExpr(>, Id(a), IntegerLit(0)), BlockStmt([IfStmt(Id(x), BreakStmt()), AssignStmt(Id(a), BinExpr(-, Id(a), IntegerLit(2))), WhileStmt(BooleanLit(False), CallStmt(printFloat, FloatLit(320.0)))])), CallStmt(update, Id(arr))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))
        
    def test64(self):
        input = """
        main: function void () {  
                do {
                    x,delta : integer = 1, readInteger();
                    a = toInt( a -x/delta );                    
                }
                while(a);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(Id(a), BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), VarDecl(delta, IntegerType, FuncCall(readInteger, [])), AssignStmt(Id(a), FuncCall(toInt, [BinExpr(-, Id(a), BinExpr(/, Id(x), Id(delta)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))
        
    def test65(self):
        input = """
        main: function void () {
        do{
                do {
                        i=0;  
                        do
                        {
                                {}
                                increase(count);
                        }
                        while(c==true);
                }while(i<=10);
                i=count/n;
                calc(i, random());
        }while(i < 5); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(i), IntegerLit(5)), BlockStmt([DoWhileStmt(BinExpr(<=, Id(i), IntegerLit(10)), BlockStmt([AssignStmt(Id(i), IntegerLit(0)), DoWhileStmt(BinExpr(==, Id(c), BooleanLit(True)), BlockStmt([BlockStmt([]), CallStmt(increase, Id(count))]))])), AssignStmt(Id(i), BinExpr(/, Id(count), Id(n))), CallStmt(calc, Id(i), FuncCall(random, []))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))
        
    def test66(self):
        input = """
        main: function void () {  
        do {
            do { print(1);
                do {print(2);
                    do {print(3);
                        do {print(4);
                            do { print(5);
                                do {
                                } while(_value_new__==true);
                            } while(length10 <=10);
                        } while(number_of_s>=9);
                    } while(abc==x%100 && width);
                } while(x && y || z);
            } while(0 || 1);
        } while((sum ==88 )&& 3 == 2);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, BinExpr(&&, BinExpr(==, Id(sum), IntegerLit(88)), IntegerLit(3)), IntegerLit(2)), BlockStmt([DoWhileStmt(BinExpr(||, IntegerLit(0), IntegerLit(1)), BlockStmt([CallStmt(print, IntegerLit(1)), DoWhileStmt(BinExpr(||, BinExpr(&&, Id(x), Id(y)), Id(z)), BlockStmt([CallStmt(print, IntegerLit(2)), DoWhileStmt(BinExpr(==, Id(abc), BinExpr(&&, BinExpr(%, Id(x), IntegerLit(100)), Id(width))), BlockStmt([CallStmt(print, IntegerLit(3)), DoWhileStmt(BinExpr(>=, Id(number_of_s), IntegerLit(9)), BlockStmt([CallStmt(print, IntegerLit(4)), DoWhileStmt(BinExpr(<=, Id(length10), IntegerLit(10)), BlockStmt([CallStmt(print, IntegerLit(5)), DoWhileStmt(BinExpr(==, Id(_value_new__), BooleanLit(True)), BlockStmt([]))]))]))]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))
        
    def test67(self):
        input = """
        main: function void () {  
                do {
                    while(a%2 == 1) 
                        if (i < 0) break;
                        else continue;
                    {
                        {  
                        }
                    }
                }
                while(a);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(Id(a), BlockStmt([WhileStmt(BinExpr(==, BinExpr(%, Id(a), IntegerLit(2)), IntegerLit(1)), IfStmt(BinExpr(<, Id(i), IntegerLit(0)), BreakStmt(), ContinueStmt())), BlockStmt([BlockStmt([])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))
        
    def test68(self):
        input = """
        main: function void () {  
            i: integer = 0;
            for(i= i,i<=arr[1_0, i],arr[i]-2)
                {
                    if(true)
                        continue;
                    else
                        break;
                    continue;
                }
            __remove__(____variable____);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), Id(i)), BinExpr(<=, Id(i), ArrayCell(arr, [IntegerLit(10), Id(i)])), BinExpr(-, ArrayCell(arr, [Id(i)]), IntegerLit(2)), BlockStmt([IfStmt(BooleanLit(True), ContinueStmt(), BreakStmt()), ContinueStmt()])), CallStmt(__remove__, Id(____variable____))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))
        
    def test69(self):
        input = """
        main: function void () {  
            do
                {
                    if(true)
                        {
                            printString("true");
                            continue;
                        }
                    else
                    {
                        if(false)
                            break;
                        else
                            return false;
                    }
                        
                }
            while(_in_range_1_10_(i)!=1);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, FuncCall(_in_range_1_10_, [Id(i)]), IntegerLit(1)), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([CallStmt(printString, StringLit(true)), ContinueStmt()]), BlockStmt([IfStmt(BooleanLit(False), BreakStmt(), ReturnStmt(BooleanLit(False)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test70(self):
        input = """
        main: function void () {  
            if(1) {
                do {
                    arr[i]=i*i;
                } while(i < 0);
                continue;
            }
            else {
                if(false) break;
                else
                    do {
                        print("Hello");
                        if(i==false) {
                            str = str :: "#";
                            continue;
                        }
                    } while(i==true);
                break;
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(IntegerLit(1), BlockStmt([DoWhileStmt(BinExpr(<, Id(i), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(i)]), BinExpr(*, Id(i), Id(i)))])), ContinueStmt()]), BlockStmt([IfStmt(BooleanLit(False), BreakStmt(), DoWhileStmt(BinExpr(==, Id(i), BooleanLit(True)), BlockStmt([CallStmt(print, StringLit(Hello)), IfStmt(BinExpr(==, Id(i), BooleanLit(False)), BlockStmt([AssignStmt(Id(str), BinExpr(::, Id(str), StringLit(#))), ContinueStmt()]))]))), BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))
        
    def test71(self):
        input = """
        main: function void () {  
            a : string = "Hello world";
            return ((a::"!")::a)::"end";
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, StringLit(Hello world)), ReturnStmt(BinExpr(::, BinExpr(::, BinExpr(::, Id(a), StringLit(!)), Id(a)), StringLit(end)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test72(self):
        input = """
        UPDATE: function integer(Date: integer, n: integer){
            calc(Date,n);
            return Date;
        }
        """
        expect = """Program([
	FuncDecl(UPDATE, IntegerType, [Param(Date, IntegerType), Param(n, IntegerType)], None, BlockStmt([CallStmt(calc, Id(Date), Id(n)), ReturnStmt(Id(Date))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))
        
    def test73(self):
        input = """
        main : function void() {
            foo(2 + x, 4.0 / y);
            goo();
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y))), CallStmt(goo, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test74(self):
        input = """
        main : function void() {
            a, b : integer = round(123.0e2), randomInt();
            sum : integer = a + b + arr[0,0];
            print(a, sum);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, FuncCall(round, [FloatLit(12300.0)])), VarDecl(b, IntegerType, FuncCall(randomInt, [])), VarDecl(sum, IntegerType, BinExpr(+, BinExpr(+, Id(a), Id(b)), ArrayCell(arr, [IntegerLit(0), IntegerLit(0)]))), CallStmt(print, Id(a), Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))
        
    def test75(self):
        input = """
        main : function void() {
            a,b : string = readString(), readString();
            if (length(a) == length(b)) return;
            else update();
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, FuncCall(readString, [])), VarDecl(b, StringType, FuncCall(readString, [])), IfStmt(BinExpr(==, FuncCall(length, [Id(a)]), FuncCall(length, [Id(b)])), ReturnStmt(), CallStmt(update, ))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))
        
    def test76(self):
        input = """
        main : function void() {
            {
                {
                     {
                          printString("Hello World;");
                     }
                }
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([BlockStmt([BlockStmt([CallStmt(printString, StringLit(Hello World;))])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))
        
    def test77(self):
        input = """
        main : function void() {
            {
                r, s: integer;
                r = 2.0;
                a, b: array [5] of integer;
                s = r * r * myPI;
                a[0] = s;
            }
            return ;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))]), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))
    
    def test78(self):
        input = """
            printAnimal : function void(out animal: string, num: integer) {                
            }
            printBird : function void(bird : string) inherit printAnimal {
            }
            main: function void() {
                birds : array[2,3] of string = {{"birdA", "birdB", "birdC"},{"birdX", "birdY", "birdZ"}};
                printBird(bird[a[i], 2]);
                return ;
            }
        """
        expect = """Program([
	FuncDecl(printAnimal, VoidType, [OutParam(animal, StringType), Param(num, IntegerType)], None, BlockStmt([]))
	FuncDecl(printBird, VoidType, [Param(bird, StringType)], printAnimal, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(birds, ArrayType([2, 3], StringType), ArrayLit([ArrayLit([StringLit(birdA), StringLit(birdB), StringLit(birdC)]), ArrayLit([StringLit(birdX), StringLit(birdY), StringLit(birdZ)])])), CallStmt(printBird, ArrayCell(bird, [ArrayCell(a, [Id(i)]), IntegerLit(2)])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))
        
    def test79(self):
        input = """
            func : function void(){
                ans = 0;
                for (i = 1, i <= n  , i + 1) 
                    for ( j = n, j <i , j -1){
                        ans = ans + (i*j*arrayA[i]);
                    }
                    print(ans);
            }
            main: function void(){
                func();
                return;
            }
        """
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([AssignStmt(Id(ans), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), Id(n)), BinExpr(<, Id(j), Id(i)), BinExpr(-, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(ans), BinExpr(+, Id(ans), BinExpr(*, BinExpr(*, Id(i), Id(j)), ArrayCell(arrayA, [Id(i)]))))]))), CallStmt(print, Id(ans))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(func, ), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))
        
    def test80(self):
        input = """
            /*Test associative */
            a : float = x * x /2 % 2 +(c% 10)*3.0;
            main : function void() {
                arr[i, 0] = a[b[x+y[1,2,2,0,0]-h[g[5%2]*t[0,t[1]]] * 8+1--1]] + 3;
                b : boolean = (5!=6) && ( (4+5 > 7) || !(false && (false || true)));
            }
        """
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(+, BinExpr(%, BinExpr(/, BinExpr(*, Id(x), Id(x)), IntegerLit(2)), IntegerLit(2)), BinExpr(*, BinExpr(%, Id(c), IntegerLit(10)), FloatLit(3.0))))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(arr, [Id(i), IntegerLit(0)]), BinExpr(+, ArrayCell(a, [ArrayCell(b, [BinExpr(-, BinExpr(+, BinExpr(-, BinExpr(+, Id(x), ArrayCell(y, [IntegerLit(1), IntegerLit(2), IntegerLit(2), IntegerLit(0), IntegerLit(0)])), BinExpr(*, ArrayCell(h, [BinExpr(*, ArrayCell(g, [BinExpr(%, IntegerLit(5), IntegerLit(2))]), ArrayCell(t, [IntegerLit(0), ArrayCell(t, [IntegerLit(1)])]))]), IntegerLit(8))), IntegerLit(1)), UnExpr(-, IntegerLit(1)))])]), IntegerLit(3))), VarDecl(b, BooleanType, BinExpr(&&, BinExpr(!=, IntegerLit(5), IntegerLit(6)), BinExpr(||, BinExpr(>, BinExpr(+, IntegerLit(4), IntegerLit(5)), IntegerLit(7)), UnExpr(!, BinExpr(&&, BooleanLit(False), BinExpr(||, BooleanLit(False), BooleanLit(True)))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))
        
    def test81(self):
        input = """
            /*Test associative */
            a : float = x * x /2 % 2 +(c% 10)*3.0;
            main : function void() {
                arr[i, 0] = a[b[x+y[1,2,2,0,0]-h[g[5%2]*t[0,t[1]]] * 8+1--1]] + 3;
                b : boolean = (5!=6) && ( (4+5 > 7) || !(false && (false || true)));
            }
        """
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(+, BinExpr(%, BinExpr(/, BinExpr(*, Id(x), Id(x)), IntegerLit(2)), IntegerLit(2)), BinExpr(*, BinExpr(%, Id(c), IntegerLit(10)), FloatLit(3.0))))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(arr, [Id(i), IntegerLit(0)]), BinExpr(+, ArrayCell(a, [ArrayCell(b, [BinExpr(-, BinExpr(+, BinExpr(-, BinExpr(+, Id(x), ArrayCell(y, [IntegerLit(1), IntegerLit(2), IntegerLit(2), IntegerLit(0), IntegerLit(0)])), BinExpr(*, ArrayCell(h, [BinExpr(*, ArrayCell(g, [BinExpr(%, IntegerLit(5), IntegerLit(2))]), ArrayCell(t, [IntegerLit(0), ArrayCell(t, [IntegerLit(1)])]))]), IntegerLit(8))), IntegerLit(1)), UnExpr(-, IntegerLit(1)))])]), IntegerLit(3))), VarDecl(b, BooleanType, BinExpr(&&, BinExpr(!=, IntegerLit(5), IntegerLit(6)), BinExpr(||, BinExpr(>, BinExpr(+, IntegerLit(4), IntegerLit(5)), IntegerLit(7)), UnExpr(!, BinExpr(&&, BooleanLit(False), BinExpr(||, BooleanLit(False), BooleanLit(True)))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test82(self):
        input = """
            main : function void() {
                x = a() + b()*c(d);
                if (x < a(arr[0,i])) return;
                x = x / max(x,y+sub(x-y));
                for (i = 1, i < n , i/2) {
                    {
                        k : integer = 0;
                        k = i;
                        if (k < 10 ) break;
                    }
                }
                print("The result is ",x);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, FuncCall(a, []), BinExpr(*, FuncCall(b, []), FuncCall(c, [Id(d)])))), IfStmt(BinExpr(<, Id(x), FuncCall(a, [ArrayCell(arr, [IntegerLit(0), Id(i)])])), ReturnStmt()), AssignStmt(Id(x), BinExpr(/, Id(x), FuncCall(max, [Id(x), BinExpr(+, Id(y), FuncCall(sub, [BinExpr(-, Id(x), Id(y))]))]))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([BlockStmt([VarDecl(k, IntegerType, IntegerLit(0)), AssignStmt(Id(k), Id(i)), IfStmt(BinExpr(<, Id(k), IntegerLit(10)), BreakStmt())])])), CallStmt(print, StringLit(The result is ), Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))
        
    def test83(self):
        input = """
            x, y, i : integer;
            main: function void(){
                for(i=0,i<10,i+1)
                    arr[i]=i;
                for(i=0,i<10,i+1)
                    if(arr[i]%2==0)
                        x = x + arr[i];
                    else
                        return y + arr[i];
                print(x,y);
                }  
            }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(i, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(arr, [Id(i)]), Id(i))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, BinExpr(%, ArrayCell(arr, [Id(i)]), IntegerLit(2)), IntegerLit(0)), AssignStmt(Id(x), BinExpr(+, Id(x), ArrayCell(arr, [Id(i)]))), ReturnStmt(BinExpr(+, Id(y), ArrayCell(arr, [Id(i)]))))), CallStmt(print, Id(x), Id(y))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))
        
    def test84(self):
        input = """
            func : function void(){
                ans = 0;
                for (i = 1, i <= n  , i + 1) 
                    for ( j = n, j <i , j -1){
                        ans = ans + (i*j*arrayA[i]);
                    }
                    print(ans);
            }
            main: function void(){
                func();
                return;
            }
        """
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([AssignStmt(Id(ans), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), Id(n)), BinExpr(<, Id(j), Id(i)), BinExpr(-, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(ans), BinExpr(+, Id(ans), BinExpr(*, BinExpr(*, Id(i), Id(j)), ArrayCell(arrayA, [Id(i)]))))]))), CallStmt(print, Id(ans))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(func, ), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))
        
    def test85(self):
        input = """
            main : function void() {
                arr : array[7] of integer = {5, 4, 9, 1, 4, 6, 3 };
                n : integer = sizeof(arr)/sizeof(arr[0]);
                pair1, pair2 : integer;
                if (findPairs(arr, n, pair1, pair2)) {
                    if (checkAnswer(arr, n, pair1, pair2)){
                        printString("Your answer is correct.");                    
                    }
                    else printString("Your answer is incorrect.");
                }
                else printString("No pair found.");
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([7], IntegerType), ArrayLit([IntegerLit(5), IntegerLit(4), IntegerLit(9), IntegerLit(1), IntegerLit(4), IntegerLit(6), IntegerLit(3)])), VarDecl(n, IntegerType, BinExpr(/, FuncCall(sizeof, [Id(arr)]), FuncCall(sizeof, [ArrayCell(arr, [IntegerLit(0)])]))), VarDecl(pair1, IntegerType), VarDecl(pair2, IntegerType), IfStmt(FuncCall(findPairs, [Id(arr), Id(n), Id(pair1), Id(pair2)]), BlockStmt([IfStmt(FuncCall(checkAnswer, [Id(arr), Id(n), Id(pair1), Id(pair2)]), BlockStmt([CallStmt(printString, StringLit(Your answer is correct.))]), CallStmt(printString, StringLit(Your answer is incorrect.)))]), CallStmt(printString, StringLit(No pair found.)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test86(self):
        input = """
            n : float = a+1;
            a, b, c: boolean;
            p, q : integer = 1, 2;
            arrayA : array[4] of integer = {1, 2, 3, 4};
            arr2 : array[2, 3] of float = {{.3E-34, 2, 1.52}, {.123e-10, 5.E-2, 6.22}};
            empty_function123_263827 : function void(test : boolean, test_array : array[4,7,8] of integer) {}
            main : function void() {
                x = a() + b()*c(d);
                if (x < a(arr[0,i])) return;
                x = x / max(x,y+sub(x-y));
                for (i = 1, i < n , i/2) {
                    {
                        k : integer = 0;
                        k = i;
                        if (k < 10 ) break;
                    }
                }
                print("The result is ",x);
            }
            func : function float(out animal: string, num: integer){
                animal = "this is a string";
                i, j, ans, n : integer;
                n = 10;
                for (i = 1, i <= n, i + 1) 
                    for ( j = n, j <i , j -1){
                        ans = ans + (i*j*arrayA[i]);
                    }
                return ans;
            }
            Car: function void (a: float, b: integer, out c:float) {
                for (i = 1, i <= n, i + 1) 
                    if (i==2)
                        continue;
                    else c = a[c+1];
                    while (false) {
                        if (j>=5) break;
                        s = add(2,3,4,5);
                        printInteger(s);
                    }
                return ans;
            }
            Vinfast: function void(inherit b: integer) inherit Car{
                runStraight(number, vecl, auto_stmt);
                do {
                    a = a - 1; 
                    printInteger(a);
                }
                while(a > 0);
            }
        """
        expect = """Program([
	VarDecl(n, FloatType, BinExpr(+, Id(a), IntegerLit(1)))
	VarDecl(a, BooleanType)
	VarDecl(b, BooleanType)
	VarDecl(c, BooleanType)
	VarDecl(p, IntegerType, IntegerLit(1))
	VarDecl(q, IntegerType, IntegerLit(2))
	VarDecl(arrayA, ArrayType([4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
	VarDecl(arr2, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(3e-35), IntegerLit(2), FloatLit(1.52)]), ArrayLit([FloatLit(1.23e-11), FloatLit(0.05), FloatLit(6.22)])]))
	FuncDecl(empty_function123_263827, VoidType, [Param(test, BooleanType), Param(test_array, ArrayType([4, 7, 8], IntegerType))], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, FuncCall(a, []), BinExpr(*, FuncCall(b, []), FuncCall(c, [Id(d)])))), IfStmt(BinExpr(<, Id(x), FuncCall(a, [ArrayCell(arr, [IntegerLit(0), Id(i)])])), ReturnStmt()), AssignStmt(Id(x), BinExpr(/, Id(x), FuncCall(max, [Id(x), BinExpr(+, Id(y), FuncCall(sub, [BinExpr(-, Id(x), Id(y))]))]))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([BlockStmt([VarDecl(k, IntegerType, IntegerLit(0)), AssignStmt(Id(k), Id(i)), IfStmt(BinExpr(<, Id(k), IntegerLit(10)), BreakStmt())])])), CallStmt(print, StringLit(The result is ), Id(x))]))
	FuncDecl(func, FloatType, [OutParam(animal, StringType), Param(num, IntegerType)], None, BlockStmt([AssignStmt(Id(animal), StringLit(this is a string)), VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(ans, IntegerType), VarDecl(n, IntegerType), AssignStmt(Id(n), IntegerLit(10)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), Id(n)), BinExpr(<, Id(j), Id(i)), BinExpr(-, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(ans), BinExpr(+, Id(ans), BinExpr(*, BinExpr(*, Id(i), Id(j)), ArrayCell(arrayA, [Id(i)]))))]))), ReturnStmt(Id(ans))]))
	FuncDecl(Car, VoidType, [Param(a, FloatType), Param(b, IntegerType), OutParam(c, FloatType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(i), IntegerLit(2)), ContinueStmt(), AssignStmt(Id(c), ArrayCell(a, [BinExpr(+, Id(c), IntegerLit(1))])))), WhileStmt(BooleanLit(False), BlockStmt([IfStmt(BinExpr(>=, Id(j), IntegerLit(5)), BreakStmt()), AssignStmt(Id(s), FuncCall(add, [IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), CallStmt(printInteger, Id(s))])), ReturnStmt(Id(ans))]))
	FuncDecl(Vinfast, VoidType, [InheritParam(b, IntegerType)], Car, BlockStmt([CallStmt(runStraight, Id(number), Id(vecl), Id(auto_stmt)), DoWhileStmt(BinExpr(>, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BinExpr(-, Id(a), IntegerLit(1))), CallStmt(printInteger, Id(a))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,385))

    def test87(self):
        input = """
            main : function void() {
                for (i = n,  i >= 0 , i - 1 ){
                    printString("Enter value of line "::tostring(i));
                    for ( j = 0, j < n, j +1) {
                        Print("Enter value of a[",i,",",j,"] : ");
                        arr[i,j] = readString();
                    }                    
                }
                print("Length of array arr is ", len(arr));
                return;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), Id(n)), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printString, BinExpr(::, StringLit(Enter value of line ), FuncCall(tostring, [Id(i)]))), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(n)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(Print, StringLit(Enter value of a[), Id(i), StringLit(,), Id(j), StringLit(] : )), AssignStmt(ArrayCell(arr, [Id(i), Id(j)]), FuncCall(readString, []))]))])), CallStmt(print, StringLit(Length of array arr is ), FuncCall(len, [Id(arr)])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input,expect,386))

    def test88(self):
        input = """
        main : function void() {
            for (i = 1, j < 10, i + 1) {
            }
            printInteger(x+1);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(j), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([])), CallStmt(printInteger, BinExpr(+, Id(x), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,387))
        
    def test89(self):
        input = """
        printArray: function void (inherit a: array[3] of integer,n: integer){
            a = a - a;
            a = a - (-a);

        }
        """
        expect = """Program([
	FuncDecl(printArray, VoidType, [InheritParam(a, ArrayType([3], IntegerType)), Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, Id(a), Id(a))), AssignStmt(Id(a), BinExpr(-, Id(a), UnExpr(-, Id(a))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,388))
    
    def test90(self):
        input = """
        main : function void() {
            if(true){
                for (i = 1, i < 10, i+1) {
                    
            }
            }else{
                
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,389))
        
    def test91(self):
        input = """
        main : function void() {
            if(true){
                for (i = 1, i < 10, i+1) {
                    writeInt(i);
            }
            }else{
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))]))]), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,390))
        
    def test92(self):
        input = """
        main : function void() {
            if(true){
                for (i = 1, i < 10, i+1) {
                    writeInt(i);
            }
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,391))
        
    def test93(self):
        input = """
        fact : function integer(n: integer) {
            if(n==0) return 3;
            else return n*fact(m-1);
        }
        """
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(3)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(m), IntegerLit(1))]))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,392))

    def test94(self):
        input = """
        x : array [2, 3, 4, 5] of integer;
        """
        expect = """Program([
	VarDecl(x, ArrayType([2, 3, 4, 5], IntegerType))
])"""
        self.assertTrue(TestAST.test(input,expect,393))
    
    def test95(self):
        input = """
        x,y,z,y,t,n : auto = 1,2,3,4,5,8;
        """
        expect = """Program([
	VarDecl(x, AutoType, IntegerLit(1))
	VarDecl(y, AutoType, IntegerLit(2))
	VarDecl(z, AutoType, IntegerLit(3))
	VarDecl(y, AutoType, IntegerLit(4))
	VarDecl(t, AutoType, IntegerLit(5))
	VarDecl(n, AutoType, IntegerLit(8))
])"""
        self.assertTrue(TestAST.test(input,expect,394))
        
    def test96(self):
        input = """
        arr2 : array[2, 3] of float = {{.3E-34, 2, 1.52}, {.123e-10, 5.E-2, 6.22}};
        floatTest: function void (){
                a = .e52;

                a = .0e52;
                a = 0.e52;
                a = 0.0e52;

                a = .5e52;
                a = 5.e52;
                a = 5.5e52;
                
                a = 5_236_7387.e52;
                a = 5_236_7387.1323e52;
        }
        """
        expect = """Program([
	VarDecl(arr2, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(3e-35), IntegerLit(2), FloatLit(1.52)]), ArrayLit([FloatLit(1.23e-11), FloatLit(0.05), FloatLit(6.22)])]))
	FuncDecl(floatTest, VoidType, [], None, BlockStmt([AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(5e+51)), AssignStmt(Id(a), FloatLit(5e+52)), AssignStmt(Id(a), FloatLit(5.5e+52)), AssignStmt(Id(a), FloatLit(5.2367387e+59)), AssignStmt(Id(a), FloatLit(5.23673871323e+59))]))
])"""
        self.assertTrue(TestAST.test(input,expect,395))
        
    def test97(self):
        input = """
        main: function void () {
            x : integer = 1;
            if (x == 1) {
                continue;
                break;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), IfStmt(BinExpr(==, Id(x), IntegerLit(1)), BlockStmt([ContinueStmt(), BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,396))
        
    def test98(self):
        input = """
        x : boolean = true == false;
        a : boolean = true > false;
        c : boolean = true >= false;
        """
        expect = """Program([
	VarDecl(x, BooleanType, BinExpr(==, BooleanLit(True), BooleanLit(False)))
	VarDecl(a, BooleanType, BinExpr(>, BooleanLit(True), BooleanLit(False)))
	VarDecl(c, BooleanType, BinExpr(>=, BooleanLit(True), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input,expect,397))
        
    def test99(self):
        input = '''
            main: function void () {
                a, b: array [5] of integer;
                printInteger(b[1]);
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), CallStmt(printInteger, ArrayCell(b, [IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,398))
        
    def test100(self):
        input = '''
            voidA: function integer(n: integer){
                
            }
            main: function void () {
                delta: integer = voidA(voidA(34));
                
            }
        '''
        expect = """Program([
	FuncDecl(voidA, IntegerType, [Param(n, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(voidA, [FuncCall(voidA, [IntegerLit(34)])]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,399))
        