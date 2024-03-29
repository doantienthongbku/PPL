class Exp(ABC):pass
class BinExp(Exp):
    def __init__(self,o1,op,o2):
        self.left = o1
        self.op = op
        self.right = o2
class UnExp(Exp): 
    def __init__(self,op,o1):
        self.op = op
        self.operand = o1
class IntLit(Exp):
    def __init__(self,v):
        self.value = v
class FloatLit(Exp):
    def __init__(self,v):
        self.value = v
        
class Eval:
    def visit(self, ctx: Exp):
        if type(ctx) is IntLit or type(ctx) is FloatLit:
            return ctx.value
        elif type(ctx) is BinExp:
            left = self.visit(ctx.left)
            right = self.visit(ctx.right)
            op = ctx.op
            return eval("{} {} {}".format(left, op, right))
        elif type(ctx) is UnExp:
            value = self.visit(ctx.operand)
            return - value if ctx.op == '-' else value
    
class PrintPrefix:
    def visit(self, ctx: Exp):
        if type(ctx) is IntLit or type(ctx) is FloatLit:
            return str(ctx.value)
        elif type(ctx) is BinExp:
            return ctx.op + " " + self.visit(ctx.left) + " " + self.visit(ctx.right)
        elif type(ctx) is UnExp:
            return ctx.op + "." + " " + self.visit(ctx.operand)
        
class PrintPostfix:
    def visit(self, ctx: Exp):
        if type(ctx) is IntLit or type(ctx) is FloatLit:
            return str(ctx.value)
        elif type(ctx) is BinExp:
            return self.visit(ctx.left) + " " + self.visit(ctx.right) + " " + ctx.op
        elif type(ctx) is UnExp:
            return self.visit(ctx.operand) + " " + ctx.op + "." + " "
        

if __name__ == "__main__":
    x1 = IntLit(1)
    x2 = FloatLit(2.0)
    x3 = BinExp(x1,"+",x1)
    x4 = UnExp("-",x1)
    x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))