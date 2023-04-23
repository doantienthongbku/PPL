class Exp(ABC):pass
class BinExp(Exp):
    def __init__(self,o1,op,o2):
        self.left = o1
        self.op = op
        self.right = o2
    def accept(self,v): return v.visitBinExp(self)
class UnExp(Exp): 
    def __init__(self,op,o1):
        self.op = op
        self.operand = o1
    def accept(self,v): return v.visitUnExp(self)
class IntLit(Exp):
    def __init__(self,v):
        self.value = v
    def accept(self,v): return v.visitIntLit(self)
class FloatLit(Exp):
    def __init__(self,v):
        self.value = v
    def accept(self,v): return v.visitFloatLit(self)

class Visitor:
    def visit(self, ctx: Exp):
        return ctx.accept(self)

class Eval(Visitor):
    def visitIntLit(self, ctx: IntLit):
        return ctx.value
    
    def visitFloatLit(self, ctx: FloatLit):
        return ctx.value
    
    def visitBinExp(self, ctx: BinExp):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op
        return eval("{} {} {}".format(left, op, right))

    def visitUnExp(self, ctx: UnExp):
        value = self.visit(ctx.operand)
        return - value if ctx.op == '-' else value
    
class PrintPrefix(Visitor):
    def visitIntLit(self, ctx: IntLit):
        return str(ctx.value)
    
    def visitFloatLit(self, ctx: FloatLit):
        return str(ctx.value)
    
    def visitBinExp(self, ctx: BinExp):
        return ctx.op + " " + self.visit(ctx.left) + " " + self.visit(ctx.right)

    def visitUnExp(self, ctx: UnExp):
        return ctx.op + ". " + self.visit(ctx.operand)
        
class PrintPostfix(Visitor):
    def visitIntLit(self, ctx: IntLit):
        return str(ctx.value)
    
    def visitFloatLit(self, ctx: FloatLit):
        return str(ctx.value)
    
    def visitBinExp(self, ctx: BinExp):
        return self.visit(ctx.left) + " " + self.visit(ctx.right) + " " + ctx.op

    def visitUnExp(self, ctx: UnExp):
        return self.visit(ctx.operand) + ctx.op + ". "

if __name__ == "__main__":
    x1 = IntLit(1)
    x2 = FloatLit(2.0)
    x3 = BinExp(x1,"+",x1)
    x4 = UnExp("-",x1)
    x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))