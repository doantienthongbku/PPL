class Exp:
    def eval(self):
        pass

class IntLit(Exp):
    def __init__(self, value: int) -> None:
        self.value = value
    def eval(self):
        return self.value
    def printPrefix(self):
        return str(self.value)
    
class FloatLit(Exp):
    def __init__(self, value: float) -> None:
        self.value = value
    def eval(self):
        return self.value
    def printPrefix(self):
        return str(self.value)

class BinExp(Exp):
    def __init__(self, num1: Exp, oper: str, num2: Exp) -> None:
        self.num1 = num1
        self.oper = oper
        self.num2 = num2
        assert self.oper in ['+', '-', '*', '/']
    def eval(self):
        if self.oper == '+': return self.num1.eval() + self.num2.eval()
        elif self.oper == '-': return self.num1.eval() - self.num2.eval()
        elif self.oper == '*': return self.num1.eval() * self.num2.eval()
        elif self.oper == '/': return self.num1.eval() / self.num2.eval()
    def printPrefix(self):
        return self.oper + " " + self.num1.printPrefix() + " " + self.num2.printPrefix()
        
class UnExp(Exp):
    def __init__(self, oper: str, num: Exp) -> None:
        self.oper = oper
        self.num = num
        assert self.oper in ['+', '-']
    def eval(self):
        if self.oper == '+': return + self.num.eval()
        elif self.oper == '-': return - self.num.eval()
    def printPrefix(self):
        return self.oper + "." + " " + self.num.printPrefix()


if __name__ == '__main__':
    x1 = IntLit(1)
    x2 = FloatLit(2.0)
    x3 = BinExp(x1,"+",x1)
    x4 = UnExp("-",x1)
    x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))
    for x in [x1, x2, x3, x4, x5]:
        print(x.eval())
