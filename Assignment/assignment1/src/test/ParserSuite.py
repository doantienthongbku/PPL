import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    # Test variable declaration
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
        expect = "Error on line 1 col 18: ,"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test4(self):
        input = """delta: boolean = true;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test5(self):
        input = """a: array[2, 2] of integer = {{1, 2}, {3, 4}};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test6(self):
        input = """a, b, c: string = 3, "hello";"""
        expect = "Error on line 1 col 28: ;"
        self.assertTrue(TestParser.test(input, expect, 206))

    # Test function declaration
    def test7(self):
        input = """foo: function integer () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test8(self):
        input = """foo: function integer (a: integer) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test9(self):
        input = """foo: function integer (a: integer, out b: boolean) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test10(self):
        input = """foo: function integer (inherit a: integer, out b: boolean) [inherit parent] {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test11(self):
        input = """foo: function integer (a: integer, out b: boolean) [inherit parent] {
                a, b, c: string = 3, "hello", true;
                return hehe;
            }"""    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test12(self):
        input = """foo: function integer (a: integer, out b: boolean) [inherit parent] {
                a, b, c: string = 3, "hello", true;
                
                a = b + c;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
    def test13(self):
        # test function declaration with error
        input = """foo: function integer (a: integer, out b: boolean) [inherit parent] {
            a, b, c: string = 3, "hello", true;
            return a;
            """
        expect = "Error on line 4 col 12: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test14(self):
        input = """foo: function integer (a: integer, out b: boolean) [inherit parent] {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
    
    # Test statement
    def test15(self):
        input = """ a: integer = 3;
                    a = b + c;"""
        expect = "Error on line 2 col 22: ="
        self.assertTrue(TestParser.test(input, expect, 215))
    def test16(self):
        input = """ a: integer = 3;
        main: function void () {
            b: integer = 4;
            sum: integer = a + b;
            printInteger(sum);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test17(self):
        input = """ a: integer = 3;
        main: function void () {
            b: integer = 4;
            sum: integer = a + b;
            printInteger(sum);
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test18(self):
        input = """ a: integer = 3;
        main: function void () {
            if (a == 3) 
                printString("a = 3");
            else {
                printString("a != 3");
                printString("you are wrong");
            }
            
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test19(self):
        input = """b,c: integer = 4,5;
        main: function void () {
            a: array[3] of integer = {1, 2, 4};
            a[0] = b + c;
            
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    def test20(self):
        input = """
        main: function void () {
            for (i = 1, i < 10, i + 1) {
                a[i, 0] = a + 1;
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
    def test21(self):
        input = """b,c: integer = 4,5;
        i: integer;
        main: function void () {
            a: array[3] of integer = {1, 2, 4};
            for (i = 0, i < 3, i + 1) {
                if (a[i] == b + c) {
                    printString("a[i] = b + c");
                } else
                    printString("a[i] != b + c");
            }
            
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))  
    def test22(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test23(self):
        input = """main: function void () {
            do {
                printString("chao cau");
                a = a + 1;
            } while (i < 1);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test24(self):
        input = """foo : function string (x : integer) {
                        if (x == 0) return "a";
                        else return foo(x - 1);
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test25(self):
        input = """b,c: integer = 4,5;
        i: integer;
        main: function void () {
            a: array[3] of integer = {1, 2, 4};
            while (i < 3) {
                printString("hehe");
                if (a[1] == 3) continue;
            }
            
            while (i < 3) {
                a[1] = 3;
                printString("hehe");
                if (a[1] == 3) break;
            }
            
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
    def test26(self):
        input = """foo: function integer (a: integer, out b: boolean) [inherit parent] {
                a, b, c: string = 3, "hello", true;
                foo(2 + x, 4.0 / y);
                return a;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test27(self):
        input = """main : function void () {
                        a = 3 > 2 + 1 * 4 / 5 * 6 + 9 + a[3, 4];
                        return;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test28(self):
        input = """main : function void () {
                        
                        return;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test29(self):
        input = """main : function void () {
            a, b: array[3] of integer = {1, 2, 3}, {4, 5, 6};
        
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    def test30(self):
        input = """main : function void () {
            a: array[3] of integer = {1 > 2, 2 + 10, 3};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230)) 
    def test31(self):                                       # TODO: fix this
        input = """main : function void () {
            a,b,c : integer = 1,2,3,4;
        }"""
        expect = "Error on line 2 col 35: ,"
        self.assertTrue(TestParser.test(input, expect, 231))
    def test32(self):
        input = """main : function void () {
            a: array[2, 2] of integer = {{1, 2}, {3, 4}};
            printInteger(a[1, 1]);
            
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
    def test33(self):
        input = """main : function void () {
            a: array[2, 2] of integer = {{1, 2}, {3, 4}};
            printInteger(a[1, 1]);
            
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    
    # Test special function
    
    
    # Test 