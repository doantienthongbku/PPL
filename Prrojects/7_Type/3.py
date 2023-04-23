class Type(ABC): pass
class IntType(Type): pass
class FloatType(Type): pass
class BoolType(Type): pass
class NoType(Type): pass

class Symbol:   # save type 
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ
        
class Utils:
    def infer(symbol_list, name, typ):
        for symbol in symbol_list:
            if symbol.name == name:
                symbol.typ = typ
                return typ
        
class StaticCheck(Visitor):
    # program: decl: List[VarDecl], stmts: List[Assign]
    def visitProgram(self,ctx:Program,o):
        o = []
        for decl in ctx.decl:
            o = self.visit(decl, o)
        for stmt in ctx.stmts:
            self.visit(stmt, o)

    def visitVarDecl(self,ctx:VarDecl,o):
        return o + [Symbol(ctx.name, NoType())]

    def visitAssign(self,ctx:Assign,o):
        rtype = self.visit(ctx.rhs, o)
        ltype = self.visit(ctx.lhs, o)
        
        if type(ltype) is NoType and type(rtype) is NoType:
            raise TypeCannotBeInferred(ctx)
        
        if type(ltype) is NoType:
            ltype = Utils.infer(o, ctx.lhs.name, rtype)
            return
        if type(rtype) is NoType:
            rtype = Utils.infer(o, ctx.rhs.name, ltype)
            return 
        
        if type(ltype) is type(rtype): return
        raise TypeMismatchInStatement(ctx)
    
    # x + 1, x: int
    def visitBinOp(self,ctx:BinOp,o):
        e1t = self.visit(ctx.e1, o)     # NoType()
        e2t = self.visit(ctx.e2, o)     # IntType()
        
        if ctx.op in ['+', '-', '*', '/']:
            if type(e1t) is NoType:
                e1t = Utils.infer(o, ctx.e1.name, IntType())
            if type(e2t) is NoType:
                e2t = Utils.infer(o, ctx.e2.name, IntType())
            if type(e1t) is IntType and type(e2t) is IntType:
                return IntType()
            raise TypeMismatchInExpression(ctx)
            
        if ctx.op in ['+.', '-.', '*.', '/.']:
            if type(e1t) is NoType:
                e1t = Utils.infer(o, ctx.e1.name, FloatType())
            if type(e2t) is NoType:
                e2t = Utils.infer(o, ctx.e2.name, FloatType())
            if type(e1t) is FloatType and type(e2t) is FloatType:
                return FloatType()
            raise TypeMismatchInExpression(ctx)
        
        if ctx.op in ['>', '=']:
            if type(e1t) is NoType:
                e1t = Utils.infer(o, ctx.e1.name, IntType())
            if type(e2t) is NoType:
                e2t = Utils.infer(o, ctx.e2.name, IntType())
            if type(e1t) is IntType and type(e2t) is IntType:
                return BoolType()
            raise TypeMismatchInExpression(ctx)

        if ctx.op in ['>.', '=.']:
            if type(e1t) is NoType:
                e1t = Utils.infer(o, ctx.e1.name, FloatType())
            if type(e2t) is NoType:
                e2t = Utils.infer(o, ctx.e2.name, FloatType())
            if type(e1t) is FloatType and type(e2t) is FloatType:
                return BoolType()
            raise TypeMismatchInExpression(ctx)
            
        if ctx.op in ['&&', '||', '>b', '=b']:
            if type(e1t) is NoType:
                e1t = Utils.infer(o, ctx.e1.name, BoolType())
            if type(e2t) is NoType:
                e2t = Utils.infer(o, ctx.e2.name, BoolType())
            if type(e1t) is BoolType and type(e2t) is BoolType:
                return BoolType()
            raise TypeMismatchInExpression(ctx)

    def visitUnOp(self,ctx:UnOp,o):
        et = self.visit(ctx.e, o)
        
        if ctx.op == '!':
            if type(et) is NoType:
                et = Utils.infer(o, ctx.e.name, BoolType())
            if type(et) is not BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        
        if ctx.op == 'i2f':
            if type(et) is NoType:
                et = Utils.infer(o, ctx.e.name, IntType())
            if type(et) is not IntType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
            
        if ctx.op == 'floor':
            if type(et) is NoType:
                et = Utils.infer(o, ctx.e.name, FloatType())
            if type(et) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return IntType()
            
        if ctx.op == '-':
            if type(et) is NoType:
                et = Utils.infer(o, ctx.e.name, IntType())
            if type(et) is not IntType:
                raise TypeMismatchInExpression(ctx)
            return IntType()
            
        if ctx.op == '-.':
            if type(et) is NoType:
                et = Utils.infer(o, ctx.e.name, FloatType())
            if type(et) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()

    def visitIntLit(self,ctx:IntLit,o): return IntType()

    def visitFloatLit(self,ctx,o): return FloatType()

    def visitBoolLit(self,ctx,o): return BoolType()

    def visitId(self,ctx,o):
        for symbol in o:
            if ctx.name == symbol.name:
                return symbol.typ
        
        raise UndeclaredIdentifier(ctx.name)