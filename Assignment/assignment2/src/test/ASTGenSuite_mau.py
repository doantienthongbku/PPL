import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))



    def test_vardecl(self):
        input = """
        x, y, z: integer;
        a: float = 1.2;
        b,c: boolean = true, false;
        d: array[1,2] of boolean;
        e,f: array[2,3] of string;
        g: array[1] of float = {a+1.2};
        h,i: array[1,2] of string = {"D96","MT22"}, {{}, "BKOOL"};
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(z, IntegerType)
	VarDecl(a, FloatType, FloatLit(1.2))
	VarDecl(b, BooleanType, BooleanLit(True))
	VarDecl(c, BooleanType, BooleanLit(False))
	VarDecl(d, ArrayType([1, 2], BooleanType))
	VarDecl(e, ArrayType([2, 3], StringType))
	VarDecl(f, ArrayType([2, 3], StringType))
	VarDecl(g, ArrayType([1], FloatType), ArrayLit([BinExpr(+, Id(a), FloatLit(1.2))]))
	VarDecl(h, ArrayType([1, 2], StringType), ArrayLit([StringLit(D96), StringLit(MT22)]))
	VarDecl(i, ArrayType([1, 2], StringType), ArrayLit([ArrayLit([]), StringLit(BKOOL)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_funcdecl(self):
        input = """
        main: function void (){}
        abc: function integer(){}
        def: function integer() inherit abc{}
        ghi: function array[1,2] of boolean () {}
        klm: function array[1,2] of string () inherit ghi {}
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(abc, IntegerType, [], None, BlockStmt([]))
	FuncDecl(def, IntegerType, [], abc, BlockStmt([]))
	FuncDecl(ghi, ArrayType([1, 2], BooleanType), [], None, BlockStmt([]))
	FuncDecl(klm, ArrayType([1, 2], StringType), [], ghi, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))


    def test_param(self):
        input = """
        abc: function integer(a: integer){}
        def: function integer(a: array[3] of integer) inherit abc{}
        ghi: function array[1,2] of boolean (out n: integer) {}
        klm: function array[1,2] of string (inherit out a: array[3] of integer, n: integer) inherit ghi {}
        """
        expect = """Program([
	FuncDecl(abc, IntegerType, [Param(a, IntegerType)], None, BlockStmt([]))
	FuncDecl(def, IntegerType, [Param(a, ArrayType([3], IntegerType))], abc, BlockStmt([]))
	FuncDecl(ghi, ArrayType([1, 2], BooleanType), [OutParam(n, IntegerType)], None, BlockStmt([]))
	FuncDecl(klm, ArrayType([1, 2], StringType), [InheritOutParam(a, ArrayType([3], IntegerType)), Param(n, IntegerType)], ghi, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_stmt_1(self):
        input = """
        abs: function integer() {
            return 0;
        }
        main: function void() {
            return;
        }
        """
        expect = """Program([
	FuncDecl(abs, IntegerType, [], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl2(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_vardecls2(self):
        input = """x , y : boolean = true , false ;
                    a1, a2 : auto = b1, b2 ;"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	VarDecl(y, BooleanType, BooleanLit(False))
	VarDecl(a1, AutoType, Id(b1))
	VarDecl(a2, AutoType, Id(b2))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))


    def test_stmt_2(self):
        input = """
        plus: function integer(b: integer) {
            a: integer = 2;
            return a + b;
        }
        abs: function integer() inherit plus {
            c: integer = a + plus(5);
            return c;
        }
        """
        expect = """Program([
	FuncDecl(plus, IntegerType, [Param(b, IntegerType)], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(2)), ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(abs, IntegerType, [], plus, BlockStmt([VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_short_vardecl(self):
        input = """x: integer;
        """
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_short_vardecl2(self):
        input = """x,y,z: integer;
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(z, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_full_vardecl(self):
        input = """x: integer = 1;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    

    def test_vardecls(self):
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



################################################



    def test_stmt_2(self):
        input = """
        plus: function integer(b: integer) {
        a: integer = 2;
        return a + b;
        }
        abs: function integer() inherit plus {
        c: integer = a + plus(5);
        return c;
        }
        """
        expect = """Program([
	FuncDecl(plus, IntegerType, [Param(b, IntegerType)], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(2)), ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(abs, IntegerType, [], plus, BlockStmt([VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_4(self):
        input = """
        printArray: function void (inherit a: array[3] of integer,n: integer){
            for(i = 1, i<length(a), i+1) print(a[i]);
            while(a[1]<n) {
                print(a[1]);
                a[1] = a[1] - 1;
            }
            do {
                a[2] = a[2] - n;
            } while(a[2] > 0);
        }
        """
        expect = """Program([
	FuncDecl(printArray, VoidType, [InheritParam(a, ArrayType([3], IntegerType)), Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(length, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(print, ArrayCell(a, [Id(i)]))), WhileStmt(BinExpr(<, ArrayCell(a, [IntegerLit(1)]), Id(n)), BlockStmt([CallStmt(print, ArrayCell(a, [IntegerLit(1)])), AssignStmt(ArrayCell(a, [IntegerLit(1)]), BinExpr(-, ArrayCell(a, [IntegerLit(1)]), IntegerLit(1)))])), DoWhileStmt(BinExpr(>, ArrayCell(a, [IntegerLit(2)]), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(2)]), BinExpr(-, ArrayCell(a, [IntegerLit(2)]), Id(n)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_5(self):
        input = """
        printArray: function void (a: array[3,1] of integer,n: integer){
            while(a[1,1]<n) {
                print(a[1,1]);
                if(n > 1) n = n-1;
                else break;
            }
            {
                m: integer = 5;
                for(i = 1, i<length(a), i+1) {
                    if(a[max(i,2),1]>m) {continue;}
                    else {m = m-1;}
                    m = m + 2;
                }
            }
        }
        """
        expect = """Program([
	FuncDecl(printArray, VoidType, [Param(a, ArrayType([3, 1], IntegerType)), Param(n, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(<, ArrayCell(a, [IntegerLit(1), IntegerLit(1)]), Id(n)), BlockStmt([CallStmt(print, ArrayCell(a, [IntegerLit(1), IntegerLit(1)])), IfStmt(BinExpr(>, Id(n), IntegerLit(1)), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1))), BreakStmt())])), BlockStmt([VarDecl(m, IntegerType, IntegerLit(5)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(length, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(a, [FuncCall(max, [Id(i), IntegerLit(2)]), IntegerLit(1)]), Id(m)), BlockStmt([ContinueStmt()]), BlockStmt([AssignStmt(Id(m), BinExpr(-, Id(m), IntegerLit(1)))])), AssignStmt(Id(m), BinExpr(+, Id(m), IntegerLit(2)))]))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_spec_func(self):
        input = """
        printArray: function void (a: array[3,1] of integer,n: integer){
            a: integer = readInteger();
            printInteger(a + 10);
        }
        """
        expect = """Program([
	FuncDecl(printArray, VoidType, [Param(a, ArrayType([3, 1], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(a, IntegerType, FuncCall(readInteger, [])), CallStmt(printInteger, BinExpr(+, Id(a), IntegerLit(10)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))



## Test function declaration

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

        
    
    def test_simple_program_4(self):
        """Simple program"""
        input = """Rectangle: function void (a: float, b: integer, out c:float) {
        }
        Square: function void(inherit b: integer) inherit Rectangle{
            
        }
        """
        expect = """Program([
	FuncDecl(Rectangle, VoidType, [Param(a, FloatType), Param(b, IntegerType), OutParam(c, FloatType)], None, BlockStmt([]))
	FuncDecl(Square, VoidType, [InheritParam(b, IntegerType)], Rectangle, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    # Test expression
    def test_expr_1(self):
        input = """main: function void () {
                a1, b2 : integer = a + 1, 0 ;
                a  = 3;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a1, IntegerType, BinExpr(+, Id(a), IntegerLit(1))), VarDecl(b2, IntegerType, IntegerLit(0)), AssignStmt(Id(a), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    
    def test_simple_program_6(self):
        """Simple program"""
        input = """toString : function string () {
        }
        toInteger : function integer () {
        }"""
        expect = """Program([
	FuncDecl(toString, StringType, [], None, BlockStmt([]))
	FuncDecl(toInteger, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_expr_2(self):
        input = """main: function void () {
                b = a + a1;
                c = b*a/2.0;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(b), BinExpr(+, Id(a), Id(a1))), AssignStmt(Id(c), BinExpr(/, BinExpr(*, Id(b), Id(a)), FloatLit(2.0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))
    def test_expr_4(self):
        input = """
        a : float = 12 - 2*3/4 + 1 +1 / 5;
        """
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(+, BinExpr(+, BinExpr(-, IntegerLit(12), BinExpr(/, BinExpr(*, IntegerLit(2), IntegerLit(3)), IntegerLit(4))), IntegerLit(1)), BinExpr(/, IntegerLit(1), IntegerLit(5))))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    
    
    def test_expr_5(self):
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
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_expr_6(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_expr_7(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))


    def test_expr_8(self):
        input = """               
        b: boolean = 1!= 2 || (0==0.1) ;       
        """
        expect = """Program([
	VarDecl(b, BooleanType, BinExpr(!=, IntegerLit(1), BinExpr(||, IntegerLit(2), BinExpr(==, IntegerLit(0), FloatLit(0.1)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_expr_9(self):
        input = """               
        a : boolean = (3 > 2 ) || (7/2 <= 4+3) && !(1.0e1+1 >= 0) ;     
        """
        expect = """Program([
	VarDecl(a, BooleanType, BinExpr(&&, BinExpr(||, BinExpr(>, IntegerLit(3), IntegerLit(2)), BinExpr(<=, BinExpr(/, IntegerLit(7), IntegerLit(2)), BinExpr(+, IntegerLit(4), IntegerLit(3)))), UnExpr(!, BinExpr(>=, BinExpr(+, FloatLit(10.0), IntegerLit(1)), IntegerLit(0)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 3))

    def test_array_no(self):
        input = """               
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
        """
        expect = """Program([
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))
    def test_array_1(self):
        input = """               
            a : array [2] of integer;
            arr : array [1,2,3] of string;
        """
        expect = """Program([
	VarDecl(a, ArrayType([2], IntegerType))
	VarDecl(arr, ArrayType([1, 2, 3], StringType))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_array_2(self):
        input = """               
            arr : array [1_0] of float = {1,2,3,4,5,6,7,8,9,10};
        """
        expect = """Program([
	VarDecl(arr, ArrayType([10], FloatType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_array_3(self):
        input = """               
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
        """
        expect = """Program([
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_array_4(self):
        input = """               
            printArr: function void(out arr:array[5] of string) 
                { return (arr[0]);}
            myPets : array[5] of string = {"Cat", "Dog", "Parot", "Pig", "Ducky"} ;    
        """
        expect = """Program([
	FuncDecl(printArr, VoidType, [OutParam(arr, ArrayType([5], StringType))], None, BlockStmt([ReturnStmt(ArrayCell(Id(arr), [IntegerLit(0)]))]))
	VarDecl(myPets, ArrayType([5], StringType), ArrayLit([StringLit(Cat), StringLit(Dog), StringLit(Parot), StringLit(Pig), StringLit(Ducky)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    # ## Test statement
# # --------- Assignment
    def test_stmt_assign_1(self):
        input = """
        main: function void () {
                count = 1;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_assign_2(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_assign_3(self):
        input = """
        count : auto = 0;
        main: function void () {
                
        }"""
        expect = """Program([
	VarDecl(count, AutoType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_assign_4(self):
        input = """
        main: function void () {
                count = 1;
                str = "";
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1)), AssignStmt(Id(str), StringLit())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    ##---------- If
    def test_stmt_if_1(self):
        input = """
        main: function void () {
              if (a>b) a = b;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), AssignStmt(Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_stmt_if_2(self):
        input = """
        main: function void () {
              if (a>b) {a = b;}
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_if_3(self):
        input = """
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_if_4(self):
        input = """
        main: function void () {
              if (a>b) {}
              else a = "This is 'else' ";                
              
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), AssignStmt(Id(a), StringLit(This is 'else' )))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_if_5(self):
        input = """
        main: function void () {
              if (a>b) {}
              else if (true) a = b;
                  else a = 0;           
              
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), IfStmt(BooleanLit(True), AssignStmt(Id(a), Id(b)), AssignStmt(Id(a), IntegerLit(0))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

# # ## Test full

    def test_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    
    def test_simple_program_2(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))    
    
    


    def test_simple_program_3(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
##############################################################    
    def test_stmt_3(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))


    def test_expr_3(self):
        input = """
        a : integer = round(1.23-1.496, b);
        """
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(round, [BinExpr(-, FloatLit(1.23), FloatLit(1.496)), Id(b)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

##### CÒN SAI - LỖI ##########################################

    def test_expr_10(self):
        input = """               
        a : integer = toInt(bc_, 2, 10) + randomInt() ;
        """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(+, FuncCall(toInt, [Id(bc_), IntegerLit(2), IntegerLit(10)]), FuncCall(randomInt, [])))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_array_5(self):
        input = """               
                main : function void(){
                    arrB[0,0,arrB[0,0,arrB[i,i,0]]] = arrayA[10-1,8+1];
                }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(arrB, [IntegerLit(0), IntegerLit(0), ArrayCell(arrB, [IntegerLit(0), IntegerLit(0), ArrayCell(arrB, [Id(i), Id(i), IntegerLit(0)])])]), ArrayCell(arrayA, [BinExpr(-, IntegerLit(10), IntegerLit(1)), BinExpr(+, IntegerLit(8), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))



    def test_stmt_assign_5(self):
        input = """
        main: function void () {
              r : float = _callR(-1,2.0,a);
              area = pi * r * r;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, FloatType, FuncCall(_callR, [UnExpr(-, IntegerLit(1)), FloatLit(2.0), Id(a)])), AssignStmt(Id(area), BinExpr(*, BinExpr(*, Id(pi), Id(r)), Id(r)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))
##########################################

    def test_short_vardecl(self):
        input = """x: integer;
        """
        expect = """Program([
	VarDecl(x, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 305))
    def test_short_vardecl2(self):
        input = """x,y,z: integer;
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(z, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl(self):
        input = """x: integer = 1;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl2(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_vardecls(self):
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

    def test_vardecls2(self):
        input = """x , y : boolean = true , false ;
                    a1, a2 : auto = b1, b2 ;"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	VarDecl(y, BooleanType, BooleanLit(False))
	VarDecl(a1, AutoType, Id(b1))
	VarDecl(a2, AutoType, Id(b2))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

## Test function declaration

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_simple_program_2(self):
        """Simple program"""
        input = """abc: function integer (a : float) {
        }"""
        expect = """Program([
	FuncDecl(abc, IntegerType, [Param(a, FloatType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_simple_program_3(self):
        """Simple program"""
        input = """abc: function string (out a : string) {
        }"""
        expect = """Program([
	FuncDecl(abc, StringType, [OutParam(a, StringType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_simple_program_4(self):
        """Simple program"""
        input = """Rectangle: function void (a: float, b: integer, out c:float) {
        }
        Square: function void(inherit b: integer) inherit Rectangle{
            
        }
        """
        expect = """Program([
	FuncDecl(Rectangle, VoidType, [Param(a, FloatType), Param(b, IntegerType), OutParam(c, FloatType)], None, BlockStmt([]))
	FuncDecl(Square, VoidType, [InheritParam(b, IntegerType)], Rectangle, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_simple_program_6(self):
        """Simple program"""
        input = """toString : function string () {
        }
        toInteger : function integer () {
        }"""
        expect = """Program([
	FuncDecl(toString, StringType, [], None, BlockStmt([]))
	FuncDecl(toInteger, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))


# Test expression
    def test_expr_1(self):
        input = """main: function void () {
                a1, b2 : integer = a + 1, 0 ;
                a  = 3;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a1, IntegerType, BinExpr(+, Id(a), IntegerLit(1))), VarDecl(b2, IntegerType, IntegerLit(0)), AssignStmt(Id(a), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_expr_2(self):
        input = """main: function void () {
                b = a + a1;
                c = b*a/2.0;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(b), BinExpr(+, Id(a), Id(a1))), AssignStmt(Id(c), BinExpr(/, BinExpr(*, Id(b), Id(a)), FloatLit(2.0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))


    def test_expr_3(self):
        input = """
        a : integer = round(1.23-1.496, b);
        """
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(round, [BinExpr(-, FloatLit(1.23), FloatLit(1.496)), Id(b)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))


    def test_expr_4(self):
        input = """
        a : float = 12 - 2*3/4 + 1 +1 / 5;
        """
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(+, BinExpr(+, BinExpr(-, IntegerLit(12), BinExpr(/, BinExpr(*, IntegerLit(2), IntegerLit(3)), IntegerLit(4))), IntegerLit(1)), BinExpr(/, IntegerLit(1), IntegerLit(5))))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))


    def test_expr_5(self):
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
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_expr_6(self):
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
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_expr_7(self):
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
        self.assertTrue(TestAST.test(input, expect, 320))


    def test_expr_8(self):
        input = """               
        b: boolean = 1!= 2 || (0==0.1) ;       
        """
        expect = """Program([
	VarDecl(b, BooleanType, BinExpr(!=, IntegerLit(1), BinExpr(||, IntegerLit(2), BinExpr(==, IntegerLit(0), FloatLit(0.1)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_expr_9(self):
        input = """               
        a : boolean = (3 > 2 ) || (7/2 <= 4+3) && !(1.0e1+1 >= 0) ;     
        """
        expect = """Program([
	VarDecl(a, BooleanType, BinExpr(&&, BinExpr(||, BinExpr(>, IntegerLit(3), IntegerLit(2)), BinExpr(<=, BinExpr(/, IntegerLit(7), IntegerLit(2)), BinExpr(+, IntegerLit(4), IntegerLit(3)))), UnExpr(!, BinExpr(>=, BinExpr(+, FloatLit(10.0), IntegerLit(1)), IntegerLit(0)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))


    def test_expr_10(self):
        input = """               
        a : integer = toInt(bc_, 2, 10) + randomInt() ;
        """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(+, FuncCall(toInt, [Id(bc_), IntegerLit(2), IntegerLit(10)]), FuncCall(randomInt, [])))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

# # --------- Test array

    def test_array_1(self):
        input = """               
            a : array [2] of integer;
            newarr, arr : array [1,2,3] of string;
        """
        expect = """Program([
	VarDecl(a, ArrayType([2], IntegerType))
	VarDecl(newarr, ArrayType([1, 2, 3], StringType))
	VarDecl(arr, ArrayType([1, 2, 3], StringType))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_array_2(self):
        input = """               
            arr : array [1_0] of float = {1,2,3,4,5,6,7,8,9,10};
        """
        expect = """Program([
	VarDecl(arr, ArrayType([10], FloatType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_array_3(self):
        input = """               
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
        """
        expect = """Program([
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_array_4(self):
        input = """               
            printArr: function void(out arr:array[5] of string) 
                { return (arr[0]);}
            myPets : array[5] of string = {"Cat", "Dog", "Parot", "Pig", "Ducky"} ;    
        """
        expect = """Program([
	FuncDecl(printArr, VoidType, [OutParam(arr, ArrayType([5], StringType))], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(0)]))]))
	VarDecl(myPets, ArrayType([5], StringType), ArrayLit([StringLit(Cat), StringLit(Dog), StringLit(Parot), StringLit(Pig), StringLit(Ducky)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_array_5(self):
        input = """               
                main : function void(){
                    arrB[0,0,arrB[0,0,arrB[i,i,0]]] = arrayA[10-1,8+1];
                }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(arrB, [IntegerLit(0), IntegerLit(0), ArrayCell(arrB, [IntegerLit(0), IntegerLit(0), ArrayCell(arrB, [Id(i), Id(i), IntegerLit(0)])])]), ArrayCell(arrayA, [BinExpr(-, IntegerLit(10), IntegerLit(1)), BinExpr(+, IntegerLit(8), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))


    def test_array_no(self):
        input = """               
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
        """
        expect = """Program([
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))



## Test statement
## --------- Built in function
    def test_built_in_function_1(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_built_in_function_2(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))



# --------- Assignment
    def test_stmt_assign_1(self):
        input = """
        main: function void () {
                count = 1;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_assign_2(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_assign_3(self):
        input = """
        count : auto = 0;
        main: function void () {
                
        }"""
        expect = """Program([
	VarDecl(count, AutoType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_assign_4(self):
        input = """
        main: function void () {
                count = 1;
                str = "";
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1)), AssignStmt(Id(str), StringLit())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_assign_5(self):
        input = """
        main: function void () {
              r : float = _callR(-1,2.0,a);
              area = pi * r * r;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, FloatType, FuncCall(_callR, [UnExpr(-, IntegerLit(1)), FloatLit(2.0), Id(a)])), AssignStmt(Id(area), BinExpr(*, BinExpr(*, Id(pi), Id(r)), Id(r)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

#---------- If
    def test_stmt_if_1(self):
        input = """
        main: function void () {
              if (a>b) a = b;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), AssignStmt(Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_stmt_if_2(self):
        input = """
        main: function void () {
              if (a>b) {a = b;}
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_if_3(self):
        input = """
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_if_4(self):
        input = """
        main: function void () {
              if (a>b) {}
              else a = "This is 'else' ";                
              
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), AssignStmt(Id(a), StringLit(This is 'else' )))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_if_5(self):
        input = """
        main: function void () {
              if (a>b) {}
              else if (true) a = b;
                        else a = 0;           
              
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), IfStmt(BooleanLit(True), AssignStmt(Id(a), Id(b)), AssignStmt(Id(a), IntegerLit(0))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_if_6(self):
        input = """
        main: function void () {
              if (a%2 == 0) {
                      b : integer = a;
                      return b;
              }
              else {}           
              
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(a), IntegerLit(2)), IntegerLit(0)), BlockStmt([VarDecl(b, IntegerType, Id(a)), ReturnStmt(Id(b))]), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

##--nested if
    def test_stmt_if_7(self):
        input = """
        main: function void () {
                if (isEmpty(listA)) if (true) print("true"); else print("false");
                else print(b);             
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(FuncCall(isEmpty, [Id(listA)]), IfStmt(BooleanLit(True), CallStmt(print, StringLit(true)), CallStmt(print, StringLit(false))), CallStmt(print, Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_stmt_if_8(self):
        input = """
        main: function void () {
                if (a>b) 
                    if (true) print(1);
                    else if (a <= 0) print(2);
                         else a = -a;
                else print(3);            
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), IfStmt(BooleanLit(True), CallStmt(print, IntegerLit(1)), IfStmt(BinExpr(<=, Id(a), IntegerLit(0)), CallStmt(print, IntegerLit(2)), AssignStmt(Id(a), UnExpr(-, Id(a))))), CallStmt(print, IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_stmt_if_9(self):
        input = """
        main: function void () {
                if (a>b) {
                        temp : integer = a;
                        a = b;
                        b = temp ;
                }                   
                else {
                        x,y : integer = b,a;
                        return ;
                }           
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([VarDecl(temp, IntegerType, Id(a)), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(temp))]), BlockStmt([VarDecl(x, IntegerType, Id(b)), VarDecl(y, IntegerType, Id(a)), ReturnStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_stmt_if_10(self):
        input = """
        main: function void () {
                if (true)
                a = a + 1;
                b = b - 2;         
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))), AssignStmt(Id(b), BinExpr(-, Id(b), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_stmt_if_11(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))
      
    def test_stmt_if_12(self):
        input = """
        main: function void () {
        if (true)
                if (a == 0) print(a);
                if (false) {
                        if (true) {}
                        if (0) {} else {}
                }
                else print(1)   ;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), IfStmt(BinExpr(==, Id(a), IntegerLit(0)), CallStmt(print, Id(a)))), IfStmt(BooleanLit(False), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([])), IfStmt(IntegerLit(0), BlockStmt([]), BlockStmt([]))]), CallStmt(print, IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
     
    def test_stmt_if_13(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))
  
    def test_stmt_if_14(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))
      
#-----ForStmt
##--- single
    def test_stmt_for_1(self):
        input = """
        main: function void () {  
                for (i = 1, i <10, i+1)  print(i);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(print, Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_stmt_for_2(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))
  
    def test_stmt_for_3(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_for_4(self):
        input = """
        main: function void () {  
                for(i=10, i>0, i-1)
                {
                }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(10)), BinExpr(>, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
       

###---- nested for
    def test_stmt_for_5(self):
        input = """
        main: function void () {  
                for (i = 1, i <10, i+1) 
                        for(j = 1, j < i, j+arr[0])
                                printInteger(i*j);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<, Id(j), Id(i)), BinExpr(+, Id(j), ArrayCell(arr, [IntegerLit(0)])), CallStmt(printInteger, BinExpr(*, Id(i), Id(j)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_stmt_for_6(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

#-------- while

    def test_stmt_while_1(self):
        input = """
        main: function void () {  
                while (false) {
                    s = add(2,3,4,5);
                    printInteger(s);
                }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(False), BlockStmt([AssignStmt(Id(s), FuncCall(add, [IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), CallStmt(printInteger, Id(s))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_while_2(self):
        input = """
        main: function void () {  
                while (a > 0 || (b -c < 1)) print("False expr");
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(>, Id(a), BinExpr(||, IntegerLit(0), BinExpr(<, BinExpr(-, Id(b), Id(c)), IntegerLit(1)))), CallStmt(print, StringLit(False expr)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_while_3(self):
        input = """
        main: function void () {  
                while (!true && !!false) {}
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(&&, UnExpr(!, BooleanLit(True)), UnExpr(!, UnExpr(!, BooleanLit(False)))), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

##----nested while
    def test_stmt_while_4(self):
        input = """
        main: function void () {  
                while (arr[a,b] == "Cat")
                        while (x) print(x);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, ArrayCell(arr, [Id(a), Id(b)]), StringLit(Cat)), WhileStmt(Id(x), CallStmt(print, Id(x))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_stmt_while_5(self):
        input = """
        main: function void () {  
                while (arr[a,b] == "Cat")
                        if (a == 1)
                                while (x == y) x = update(x);
                        else while(false) {}
                
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, ArrayCell(arr, [Id(a), Id(b)]), StringLit(Cat)), IfStmt(BinExpr(==, Id(a), IntegerLit(1)), WhileStmt(BinExpr(==, Id(x), Id(y)), AssignStmt(Id(x), FuncCall(update, [Id(x)]))), WhileStmt(BooleanLit(False), BlockStmt([]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
 
    def test_stmt_while_6(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

##-------- do while

    def test_stmt_dowhile_1(self):
        input = """
        main: function void () {  
                do {
                    a = a - 1; 
                    printInteger(a);
                }
                while(a > 0);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BinExpr(-, Id(a), IntegerLit(1))), CallStmt(printInteger, Id(a))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_stmt_dowhile_2(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_dowhile_3(self):
        input = """
        main: function void () {  
                do {
                        do {
                        }
                        while(a);
                } while(b);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(Id(b), BlockStmt([DoWhileStmt(Id(a), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_dowhile_4(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_dowhile_5(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))
 
    def test_stmt_dowhile_6(self):
        input = """
        main: function void () {  
                do {
                    if (a == 5) break;
                    while (b != a) update(b,a);                   
                }
                while(a);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(Id(a), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), BreakStmt()), WhileStmt(BinExpr(!=, Id(b), Id(a)), CallStmt(update, Id(b), Id(a)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_dowhile_7(self):
        input = """
        main: function void () {  
                do {
                    while(b) do {
                            printString("My name is Hoa");
                    }   while (c);
                }
                while(a);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(Id(a), BlockStmt([WhileStmt(Id(b), DoWhileStmt(Id(c), BlockStmt([CallStmt(printString, StringLit(My name is Hoa))])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_dowhile_8(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

# --------- break and continue

    def test_stmt_break_continue_1(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_break_continue_2(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_break_continue_2(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

# --------- return statements

    def test_stmt_return_1(self):
        input = """
        main: function void () {  
            a : string = "Hello world";
            return ((a::"!")::a)::"end";
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, StringLit(Hello world)), ReturnStmt(BinExpr(::, BinExpr(::, BinExpr(::, Id(a), StringLit(!)), Id(a)), StringLit(end)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_return_2(self):
        input = """
        main: function void () {  
            return a[2,2]*1-b[0]/c;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(BinExpr(-, BinExpr(*, ArrayCell(a, [IntegerLit(2), IntegerLit(2)]), IntegerLit(1)), BinExpr(/, ArrayCell(b, [IntegerLit(0)]), Id(c))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_return_3(self):
        input = """
        main: function void () {  
            return result+foo(1,2);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(BinExpr(+, Id(result), FuncCall(foo, [IntegerLit(1), IntegerLit(2)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_return_4(self):
        input = """
        main: function void () {  
            return;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_return_5(self):
        input = """
        UPDATE: function integer(Date: integer, n: integer){
            calc(Date,n);
            return Date;
        }
        """
        expect = """Program([
	FuncDecl(UPDATE, IntegerType, [Param(Date, IntegerType), Param(n, IntegerType)], None, BlockStmt([CallStmt(calc, Id(Date), Id(n)), ReturnStmt(Id(Date))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

# --------- call statements

    def test_stmt_call_1(self):
        input = """
        main : function void() {
            foo(2 + x, 4.0 / y);
            goo();
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y))), CallStmt(goo, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_call_2(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_call_3(self):
        input = """
        main : function void() {
            a : integer = callA() +  1;
            b = _writeInt();
            c : integer = toInteger(sum(a+b)) - min(a,b);
            print(a,b,c);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(+, FuncCall(callA, []), IntegerLit(1))), AssignStmt(Id(b), FuncCall(_writeInt, [])), VarDecl(c, IntegerType, BinExpr(-, FuncCall(toInteger, [FuncCall(sum, [BinExpr(+, Id(a), Id(b))])]), FuncCall(min, [Id(a), Id(b)]))), CallStmt(print, Id(a), Id(b), Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_call_4(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

# --------- block statements

    def test_stmt_block_1(self):
        input = """
        main : function void() {
            {
                {
                    
                }
                if (a == 0) printBoolean(b);
            }
            return ;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([BlockStmt([]), IfStmt(BinExpr(==, Id(a), IntegerLit(0)), CallStmt(printBoolean, Id(b)))]), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_stmt_block_2(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

## Test full

    def test_full_1(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_2(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_3(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_4(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_5(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_6(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_8(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_9(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_10(self):
        input = """
            main: function void() {
                printString("");
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_full_7(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_all(self):
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
        self.assertTrue(TestAST.test(input, expect, 307))



    def test_full_10(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))
## Nó cũng ok mà bị gì đó lạ lắm


#############################################
#           VÕ THỊ NA                      ##
#
########################################
    def test_201(self):
        input = """
        main : function void() {
            for (i = 1, j < 10, i + 1) {
                writeInt(5);
            }
            
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(j), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, IntegerLit(5))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))


    def test_203(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_204(self):
        input = """
        main : function void() {
            for (i = 1, j < 10, i + 1) {
               
            }
            printInteger(x);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(j), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([])), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_205(self):
        input = """
        main : function void() {
            for (i = 1, j < 10, i + 1) {
                printInteger(i);
            }
            
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(j), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))


   
    def test_207(self):
        input = """
        main : function void() {
            for (i = 1,i < 10, i + 1) {
                writeInt(1);
            }
            printInteger(x);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, IntegerLit(1))])), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))


    def test(self):
        input = """
        printArray: function void (inherit a: array[3] of integer,n: integer){
            a = a - a;
            a = a - (-a);

        }
        """
        expect = """Program([
	FuncDecl(printArray, VoidType, [InheritParam(a, ArrayType([3], IntegerType)), Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, Id(a), Id(a))), AssignStmt(Id(a), BinExpr(-, Id(a), UnExpr(-, Id(a))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

   
    """test if statement"""
    def test_211(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_212(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_213(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_214(self):
        input = """
        main : function void() {
            if(true){
            }else{
                printInteger(0);
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([]), BlockStmt([CallStmt(printInteger, IntegerLit(0))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_215(self):
        input = """
        fact : function integer(n: integer) {
            if(n==0) return 3;
            else return n*fact(m-1);
        }
        """
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(3)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(m), IntegerLit(1))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    """test Variable declarations"""
    def test_216(self):
        input = """
        beta: integer = 36;
        """
        expect = """Program([
	VarDecl(beta, IntegerType, IntegerLit(36))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
   
    
    def test_220(self):
        input = """
        x : array [2, 3] of integer;
        """
        expect = """Program([
	VarDecl(x, ArrayType([2, 3], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_1000(self):
            input = """a : float = false;"""
            expect = r"""Program([
	VarDecl(a, FloatType, BooleanLit(False))
])"""
            self.assertTrue(TestAST.test(input, expect, 1000))
    def test_221(self):
        input = """
        x : array [2, 3, 4, 5] of integer;
        """
        expect = """Program([
	VarDecl(x, ArrayType([2, 3, 4, 5], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_222(self):
        input = """
        x : auto = 0.08;
        """
        expect = """Program([
	VarDecl(x, AutoType, FloatLit(0.08))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_223(self):
        input = """
        x : auto = 0.09;
        y : auto = true;
        """
        expect = """Program([
	VarDecl(x, AutoType, FloatLit(0.09))
	VarDecl(y, AutoType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_224(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))
    
    def test(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))
  
    def test(self):
        input = """
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
	FuncDecl(floatTest, VoidType, [], None, BlockStmt([AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(5e+51)), AssignStmt(Id(a), FloatLit(5e+52)), AssignStmt(Id(a), FloatLit(5.5e+52)), AssignStmt(Id(a), FloatLit(5.2367387e+59)), AssignStmt(Id(a), FloatLit(5.23673871323e+59))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_227(self):
        input = """
        main: function void () {
            x : integer = 1;
            if (x == 1) {
                break;
                return false;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), IfStmt(BinExpr(==, Id(x), IntegerLit(1)), BlockStmt([BreakStmt(), ReturnStmt(BooleanLit(False))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_228(self):
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
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_229(self):
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
        self.assertTrue(TestAST.test(input, expect, 301))
    def test_230(self):
        input = """
        x : integer = a[0, 2];
        """
        expect = """Program([
	VarDecl(x, IntegerType, ArrayCell(a, [IntegerLit(0), IntegerLit(2)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))
        
    # """test assignment statement"""
    def test_231(self):
        input = """
        main: function void () {
            x : integer;
            x = 1 + 2 + 3 + 7 +9;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(x), BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(7)), IntegerLit(9)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))
    def test_232(self):
        input = """
        x : array [2, 3] of integer; 
        main: function void () {
            x[1, 2] = 1;
            x[0 ,3] = 3;
        }
        """
        expect = """Program([
	VarDecl(x, ArrayType([2, 3], IntegerType))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(x, [IntegerLit(1), IntegerLit(2)]), IntegerLit(1)), AssignStmt(ArrayCell(x, [IntegerLit(0), IntegerLit(3)]), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))
    def test_233(self):
        input = """
        x : integer = 1;
        main: function void () {
            z = x * y * z;
        }
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(z), BinExpr(*, BinExpr(*, Id(x), Id(y)), Id(z)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))
   
   
   
    
    def test_235(self):
        input = """
        fact : function integer(n: integer) {
            if(n==0) return 3;
            else return n*fact(n-1);
        }
        main: function void () {
            beta = fact(5)*fact(4)*fact(3);
        }
        """
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(3)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(beta), BinExpr(*, BinExpr(*, FuncCall(fact, [IntegerLit(5)]), FuncCall(fact, [IntegerLit(4)])), FuncCall(fact, [IntegerLit(3)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 3001))
    def test_236(self):
        input = """
        fact : function integer(n: integer) {
            if(n==0) return 1;
            else return n*fact(n-1);
        }
        main: function void () {
            
        }
        """
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 3001))
    
    # """test for statement"""
    def test_241(self):
        input = """
        inc : function void (out n : integer, delta : integer){
            n = n + delta;
            for(i = 1, i < 10, i+1){
                writeInt(i);
            } 
        }
        """
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 3100))
    
    def test_245(self):
        input = """
        inc : function void (out n : integer, delta : integer){
            n = n + delta;
            i : integer;
            a : boolean;
            for(i = 1, i < n, i+1){
            } 
        }
        """
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), VarDecl(i, IntegerType), VarDecl(a, BooleanType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 3010))
    def test_246(self):
        input = """
        inc : function void (out n : integer, delta : integer){
            n = n + delta;
            i : integer;
            var : float;
            for(i = 1, i < n, i+1) writeInt(i);
        }
        """
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), VarDecl(i, IntegerType), VarDecl(var, FloatType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(writeInt, Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 3010))
    def test_247(self):
        input = """
        inc : function void (out n : integer, delta : integer){
            n = n + delta;
            abc : boolean;
            i : integer;
            for(i = 1, i < n, i+1){
                delta : integer = 0;
                writeInt(i+delta);
            }
        }
        """
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), VarDecl(abc, BooleanType), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(delta, IntegerType, IntegerLit(0)), CallStmt(writeInt, BinExpr(+, Id(i), Id(delta)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 31100))
    
    def test_249(self):
        input = """
        inc : function void (out n : integer, delta : integer){
            n = n + delta;
            b : float;
            a : integer;
            for(i = 1, i < n, i+1){
                return 0;
            }
        }
        """
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), VarDecl(b, FloatType), VarDecl(a, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(0))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 3001))
    def test_250(self):
        input = """
        inc : function void (out n : integer, delta : integer){
            n = n + delta;
            for(i = 1, i < n, i+1){
                return 0;
                break;
                continue;
            }
        }
        """
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(0)), BreakStmt(), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 30011))
        
    # """test error"""
   
    def test_252(self):
        input = """
            main: function void () {
                a1, a2 : string = "Hello ", "World!" ;
                mn: string = "Good";          
            } """ 
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a1, StringType, StringLit(Hello )), VarDecl(a2, StringType, StringLit(World!)), VarDecl(mn, StringType, StringLit(Good))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 30110))  
    
   
    def test_256(self):
        input = '''
            x: integer = 65;
            mess: function integer(n: integer){
                return n/50 * 2;
            }
        '''
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(mess, IntegerType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, BinExpr(/, Id(n), IntegerLit(50)), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 31100))

    def test_257(self):
        input = '''
            add: function integer(n: integer){
                sum: integer = 0;
                for (i = 0, i<=n, i+1){
                    sum = sum + i;
                    delta: integer = add(10);
                    printInteger(delta);
                }
                return sum;
            }
        '''
        expect = """Program([
	FuncDecl(add, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i))), VarDecl(delta, IntegerType, FuncCall(add, [IntegerLit(10)])), CallStmt(printInteger, Id(delta))])), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 11300))

    def test_258(self):
        input = '''
            x: integer = 65;
            fact: function integer(n: integer){
                if (n == 0) return 1;
                else return n * fact(n-1);
            }
            inc: function void (out n: integer, delta: integer){
                n = n + delta;
            }
        '''
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 111300))


    
    def test_262(self):
        input = '''
            main: function void () {
                i: integer = 10;
                {
                    i = i - 1;
                }
                return  i;
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(10)), BlockStmt([AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))]), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 30210))
    
   
   

    def test_269(self):
        input = '''
            
            main: function void () {
                delta: integer = 5;
                voidB(x,delta);
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, IntegerLit(5)), CallStmt(voidB, Id(x), Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311100))

    def test_270(self):
        input = '''
            main: function void () {
                printBoolean(delta);
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolean, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 30011))



    def test_276(self):
        input = '''
            main: function void () {
                a,c: string = "true","det\tse";
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, StringLit(true)), VarDecl(c, StringType, StringLit(det	se))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 12300))

    def test_277(self):
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
        self.assertTrue(TestAST.test(input, expect,3002))

    def test_292(self):
        input = '''
            s: float = 5.5e4;
            main: function void () {
                s = s/7;
                printFloat(s);
            }
        '''
        expect = """Program([
	VarDecl(s, FloatType, FloatLit(55000.0))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), BinExpr(/, Id(s), IntegerLit(7))), CallStmt(printFloat, Id(s))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 3200))

    def test_295(self):
        input = '''
            main: function void () {
                s: boolean;
                
                }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(s, BooleanType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 3050))

    def test_300(self):
        input = '''
            main: function void () {
                a, b: array [5] of integer;
                printInteger(b[1]);
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), CallStmt(printInteger, ArrayCell(b, [IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
        