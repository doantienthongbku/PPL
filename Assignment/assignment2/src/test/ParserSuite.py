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
        input = """foo: function integer (inherit a: integer, out b: boolean) inherit parent {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test11(self):
        input = """foo: function integer (a: integer, out b: boolean) inherit parent {
                a, b, c: string = 3, "hello", true;
                return hehe;
            }"""    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test12(self):
        input = """foo: function integer (a: integer, out b: boolean) inherit parent {
                a, b, c: string = 3, "hello", true;
                
                a = b + c;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
    def test13(self):
        # test function declaration with error
        input = """foo: function integer (a: integer, out b: boolean) inherit parent {
            a, b, c: string = 3, "hello", true;
            return a;
            """
        expect = "Error on line 4 col 12: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test14(self):
        input = """foo: function integer (a: integer, out b: boolean) inherit parent {}"""
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
        input = """foo: function integer (a: integer, out b: boolean) inherit parent {
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
    def test34(self):
        input = """main : function void () {
            a: array[2, 2] of integer = {{1, 2}, {3, 4}};
            printInteger(a[1, 1]);
            
            foo(a[1, 1], a[0, 1] * 5 / 10 + 11);
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
        
    def test35(self):
        input = """main : function void () {
            a: array[2, 2] of integer;
            a[1] = {3 + 4, 5 > 10};
            
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    def test36(self):
        input = """main : function void () {
            a[2] = {2+3, 4/5>6, abc::abc};
            
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
        
    def test37(self):
        """Simple program: int main() {} """
        input = """x: integer = 65;
                fact: function integer (n: integer) {
                    if (n == 0) return 1;
                    else return n * fact(n - 1);
                }
                inc: function void(out n: integer, delta: integer) {
                    n = n + delta;
                }
                main: function void() {
                    delta: integer = fact(3);
                    inc(x, delta);
                    printInteger(x);
                }"""
        # input = "integer_: integer = 5;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test38(self):
        input = "a : boolean = true;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test39(self):
        input = "a?bc : integer = 1;"
        expect = "?"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test40(self):
        input = """foo: function integer (a: integer, out b: boolean) inherit parent {
                    a, b, c: string = 3, "hello", true;
                    return a; """
        expect = "Error on line 3 col 30: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test41(self):
        input = """ main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test42(self):
        input = """a: integer = 3;
                    a = b + c;"""
        expect = "Error on line 2 col 22: ="
        self.assertTrue(TestParser.test(input, expect, 242))

    def test43(self):
        input = """a: array[3] of integer = {1, 2, 3};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test44(self):
        input = """main: function void() {} """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test45(self):
        input = """b,c: integer = 4,5;
                i: integer;
                main: function void () {
                    a: array[3] of integer = 3;
                    for (i = 0, i < 3, i + 1) {
                        if (a[i] == b + c) {
                            printString("a[i] = b + c");
                        } else
                            printString("a[i] != b + c");
                    }
                    return;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test46(self):
        input = """for(i = 0, i < 3, i + 1)
                    a[i] = b + c;"""
        expect = "Error on line 1 col 0: for"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test47(self):
        input = """for : integer = 3;"""
        expect = "Error on line 1 col 0: for"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test48(self):
        input = """delta : integer = a;
                foo : function integer (inherit out a: integer, out b: boolean) {
                    a, b, c: string = 3, "hello", true;
                    if (a == 3)
                        return a + b;
                    else
                        return a > b;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test49(self):
        input = """a, b: integer = 3, 4, 5;"""
        expect = "Error on line 1 col 20: ,"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test50(self):
        input = """a, b, c, d: integer = 3, 4, 5;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test51(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test52(self):
        input = """foo : function string (x : integer) {}
                    main : function void () {
                        return foo(3);
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test53(self):
        input = """foo : function string (x : integer) {}
                    main : function void () {
                        a[3] = 4;
                        do {
                            a[3] = a[3] + 1;
                        }
                        while (a[3] < 10);    
                        return foo(a[3]);
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test54(self):
        input = """foo : function string (x : integer) {}
                    main : function void () {
                        a[0,0] = 4;
                        do {
                            a[0,0] = a[3] + 1;
                        }
                        while (a[0,0] < 10);    
                        return foo();
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test55(self):
        input = """foo : function string (x : integer) {}
                    main : function void () {
                        a[0,0] = 4;
                        do {
                            a[0,0] = a[3] + 1;
                        }
                        while (a[0,0] < 10);    
                        super(a+b);
                        printString("hello");
                        preventDefault();
                        for (i = 0, i < 10, i + 1) {
                            for (j = 0, j < 10, j + 1) {
                                if (a[i,j] == 0) {
                                    continue;
                                }
                            }
                        }            
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test56(self):
        input = """foo : function string (x : integer) {
                        if (x == 0) return "a";
                        else return foo(x - 1);
                   }     
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test57(self):
        input = """foo : function string (x : integer) {
                        else return foo(x - 1);
                   }     
                """
        expect = "Error on line 2 col 24: else"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test58(self):
        input = """
                    foo : function string (x : integer) {}
                    goo : function float (i: integer) {}
                    hoo : function integer (z: integer) {
                        goo(foo(3));
                    }   
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test59(self):
        input = """
                    countInteger : function integer (x: integer) {
                        count : integer = 0;
                        i: integer = 0;
                        for (i = 0, i < 10, i + 1) {
                            count = count + a[i];
                        }
                        return count;
                    }    
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test60(self):
        input = """
                    foo : function string (x : integer) {}
                    goo : function float (i: integer) {}
                    hoo : function integer (z: integer) {
                        goo(foo(hoo(3)));
                    } 
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test61(self):
        input = """
                    main : function void () {
                        a = 3 > 2 + 1 * 4 / 5 <= 6 != 9 + a[3][4];
                        return;
                    }
                """
        expect = "Error on line 3 col 46: <="
        self.assertTrue(TestParser.test(input, expect, 261))

    def test62(self):
        input = """
                    main : function void () {
                        a = a::b;
                        return;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test63(self):
        input = """
                    main : function void () {
                        if (a == 3) {
                            if (b == 4) {
                                if (c == 5) {
                                    for (a[1+1,a>b,2,3,4] = 0, i < 10, i + 1) {
                                        while (a[1+1,a>b,2,3,4] < 10) {}
                                    }
                                    continue;
                                }
                                break;
                            }
                        }    
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test64(self):
        input = """
                    main : function void () {
                        a = 2::"abc";
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test65(self):
        input = """
                    main : function void () {
                        a = 2::"abc"::"def";
                    }
                """
        expect = "Error on line 3 col 36: ::"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test66(self):
        input = """
                    abcdefghijklmnopqrstuvw : function array [3] of integer () {
                        return {1, 2, 3};
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test67(self):
        input = """
                    abcdefghijklmnopqrstuvw : function string (inherit out x: integer) {
                        return "\\n";
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test68(self):
        input = """
                    a : float = .14;
                """
        expect = "Error on line 2 col 32: ."
        self.assertTrue(TestParser.test(input, expect, 268))

    def test69(self):
        input = """
                    main : function void () {
                        a = "abc"::("a"::"b");
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test70(self):
        input = """
                    main : function void () {
                        /* comment */// comment
                        a = (2 >= 3) && (4 < 5);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test71(self):
        input = """
                    main : function boolean (i : integer) {
                        return (!i && (!!!i || !!!!i));
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test72(self):
        input = """
                    a : array [2,2] of integer = {{1,2},{3,4}};
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test73(self):
        input = """
                    main : function void () {
                        a = 7[2,3] + 2;
                        return a;
                    }    
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test74(self):
        input = """
                    main : function void () {
                        a[2] = {2+3, 4/5>6, abc::abc};
                    }    
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test75(self):
        input = """
                    main : function void () {
                        a = _abcbda[2,3,4,5,6,7,8,9] + 2 / 3 :: "abc";
                        return a;
                    }    
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test76(self):
        input = """
                    main : function void () {
                        a: array [3] of integer = {1,2,3}, {4,5,6}, {7,8,9};
                    }    
                """
        expect = "Error on line 3 col 57: ,"
        self.assertTrue(TestParser.test(input, expect, 276))
        
    def test77(self):
        input = """
                    foo : function string (x : integer) {
                        foo(3);
                        main();
                    }
                    main : function void () {
                        a: array [3] of integer = {1,2,3};
                        foo(4);
                    }    
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    
    def test78(self):
        input = """
                    main : function void () {
                        a: array [3] of integer = {1,2,3};
                        foo(4);
                    }    
                    foo : function string (x : integer) {
                        foo(3);
                        main();
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))
    
    def test79(self):
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
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
        
    def test80(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
        
    def test81(self):
        input = """
                    main : function void () {
                        a = 2;
                        b = 3;
                        c: array [3] of integer = {1,2,3};
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
        
    def test82(self):
        input = """
                    main : function void () {
                        a = 2;
                        b = 3;
                        c: array [3] of integer = {1,2,3};
                        d: array [3] of integer = {1,2,3};
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
    
    def test83(self):
        input = """
        main : function void () {
            a: string = "abc";
            b: string = "abc";
            c: string;
            c = a::b;
            
            return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))
        
    def test84(self):
        input = """
        main : function void () {
            printBoolean(true);
            
            return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
        
    def test85(self):
        input = """
        main : function void () {
            printFloat(1.2);
            
            return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
        
    def test86(self):
        input = """
                    main : function integer () {
                        a: boolean = True;
                        b: boolean = False;
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
        
    def test87(self):
        input = """main : function void () {
                        a: array[2, 2] of integer = {{1, 2}, {3, 4}};
                        printInteger(a[1, 1]);
                        b: integer = 3;
                        c: integer = b + a[1, 1];
                        printInteger(c);
                        
                        return;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))
        
    def test88(self):
        input = """
                    main : function void () {
                        a: integer = readInteger();
                        printInteger(a + 10 - 5 * 2 / 2);
                        return;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))
        
    def test89(self):
        input = """
                    bubbleSort : function array [3] of integer (arr: integer) {
                        for (i = 0, i < n, i + 1) {
                            for (j = 0, j < n - i - 1, j + 1) {
                                if (arr[j] > arr[j + 1]) {
                                    swap(arr[j], arr[j + 1]);
                                }
                            }
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))
