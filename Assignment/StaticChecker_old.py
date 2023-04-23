"""
    @author dtthong
    @id 1915352
"""
from Visitor import Visitor
from StaticError import *
from Utils import Utils
from AST import *
from functools import reduce


class Symbol:
    def __init__(self, name, mtype, value=None, inherit=False, out=False):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.inherit = inherit
        self.out = out


class StaticChecker(Visitor, Utils):
    def __init__(self, ast):
        self.ast = ast
        self.prototypes = []    # list of FuncDecl (prototype)
        self.in_loop = False    # check if in loop
        
    def infer(self, name, typ, env):
        for symbol_list in env:
            for symbol in symbol_list:
                if symbol.name == name:
                    symbol.typ = typ
                    return typ
        
    def visit(self, ast, env):
        if isinstance(ast, IntegerType):
            return self.visitIntegerType(ast, env)
        elif isinstance(ast, FloatType):
            return self.visitFloatType(ast, env)
        elif isinstance(ast, BooleanType):
            return self.visitBooleanType(ast, env)
        elif isinstance(ast, StringType):
            return self.visitStringType(ast, env)
        elif isinstance(ast, ArrayType):
            return self.visitArrayType(ast, env)
        elif isinstance(ast, AutoType):
            return self.visitAutoType(ast, env)
        elif isinstance(ast, VoidType):
            return self.visitVoidType(ast, env)
        elif isinstance(ast, BinExpr):
            return self.visitBinExpr(ast, env)
        elif isinstance(ast, UnExpr):
            return self.visitUnExpr(ast, env)
        elif isinstance(ast, Id):
            return self.visitId(ast, env)
        elif isinstance(ast, ArrayCell):
            return self.visitArrayCell(ast, env)
        elif isinstance(ast, IntegerLit):
            return self.visitIntegerLit(ast, env)
        elif isinstance(ast, FloatLit):
            return self.visitFloatLit(ast, env)
        elif isinstance(ast, StringLit):
            return self.visitStringLit(ast, env)
        elif isinstance(ast, BooleanLit):
            return self.visitBooleanLit(ast, env)
        elif isinstance(ast, ArrayLit):
            return self.visitArrayLit(ast, env)
        elif isinstance(ast, FuncCall):
            return self.visitFuncCall(ast, env)
        elif isinstance(ast, AssignStmt):
            return self.visitAssignStmt(ast, env)
        elif isinstance(ast, BlockStmt):
            return self.visitBlockStmt(ast, env)
        elif isinstance(ast, IfStmt):
            return self.visitIfStmt(ast, env)
        elif isinstance(ast, ForStmt):
            return self.visitForStmt(ast, env)
        elif isinstance(ast, WhileStmt):
            return self.visitWhileStmt(ast, env)
        elif isinstance(ast, DoWhileStmt):
            return self.visitDoWhileStmt(ast, env)
        elif isinstance(ast, BreakStmt):
            return self.visitBreakStmt(ast, env)
        elif isinstance(ast, ContinueStmt):
            return self.visitContinueStmt(ast, env)
        elif isinstance(ast, ReturnStmt):
            return self.visitReturnStmt(ast, env)
        elif isinstance(ast, CallStmt):
            return self.visitCallStmt(ast, env)
        elif isinstance(ast, VarDecl):
            return self.visitVarDecl(ast, env)
        elif isinstance(ast, ParamDecl):
            return self.visitParamDecl(ast, env)
        elif isinstance(ast, FuncDecl):
            return self.visitFuncDecl(ast, env)
        elif isinstance(ast, Program):
            return self.visitProgram(ast, env)
        
    def visitProgram(self, ast:Program, env):
        env = [[]]
        is_main_func_defined = False
        
        # check 'main' function
        for x in ast.decls:
            if isinstance(x, FuncDecl) and x.name.name == 'main':
                if not (len(ast.params) > 0 or type(self.visit(ast.returnType, env)) is not VoidType):
                    is_main_func_defined = True
                    break
        
        # visit all declarations
        env = [self.visit(decl, env) for decl in ast.decls]
        if not is_main_func_defined:
            raise NoEntryPoint()
        
    def visitVarDecl(self, ast:VarDecl, env):
        # check redeclared variable
        for symbol in env[0]:
            if symbol.name == ast.name:
                raise Redeclared(Variable(), ast.name)

        name = ast.name    
        typ = self.visit(ast.typ, env)

        # check relative initialization
        if ast.init is not None:
            init_typ = self.visit(ast.init, env)
            if typ is AutoType:
                typ = init_typ
                env[0] += Symbol(name, typ, ast.init)
            elif init_typ is not typ:
                raise TypeMismatchInVarDecl(ast)
        else:
            if typ is AutoType:
                raise Invalid(Variable(), name)
            env[0] += [Symbol(name, typ)]

    def visitParamDecl(self, ast:ParamDecl, env):
        symbol = Symbol(name=ast.name, mtype=self.visit(ast.typ, env),
                        value=None, inherit=ast.inherit, out=ast.out)
        env[0] += [symbol]
        
    def visitFuncDecl(self, ast:FuncDecl, env):
        local_env = [[]] + env
        param_list = []
        
        # check redeclared param
        for param in ast.params:
            if param.name in param_list:
                raise Redeclared(Parameter(), param.name)
            param_list.append(param.name)
            self.visit(param, local_env)
                
        # check redeclared function
        for item in env[0]:
            if isinstance(item, FuncDecl) and item.name == ast.name:
                raise Redeclared(Function(), ast.name)
        
        self.visit(ast.body, local_env)
        # TODO
        
    def visitId(self, ast, env):
        for symbol_list in env:
            for symbol in symbol_list:
                if ast.name == symbol.name:
                    return symbol.typ
        
        raise Undeclared(Identifier(), ast.name)

    def visitBinExpr(self, ast: BinExpr, env):
        left = self.visit(ast.left, env)
        right = self.visit(ast.right, env)

        if ast.op in ['+', '-', '*', '/']:
            if type(left) is IntegerType and type(right) is IntegerType:
                return IntegerType()
            elif type(left) is FloatType and type(right) is FloatType:
                return FloatType()
            elif type(left) is IntegerType and type(right) is FloatType or type(left) is FloatType and type(right) is IntegerType:
                return FloatType()
            elif type(left) is AutoType:
                if type(right) is IntegerType or type(right) is FloatType:
                    self.infer(ast.left.name, type(right), env)
                    return type(right)
                else:
                    raise TypeMismatchInExpression(ast)
            elif type(right) is AutoType:
                if type(left) is IntegerType or type(left) is FloatType:
                    self.infer(ast.right.name, type(left), env)
                    return type(left)
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['%']:
            if type(left) is IntegerType and type(right) is IntegerType:
                return IntegerType()
            elif type(left) is AutoType:
                if type(right) is IntegerType:
                    self.infer(ast.left.name, IntegerType(), env)
                    return IntegerType()
                else:
                    raise TypeMismatchInExpression(ast)
            elif type(right) is AutoType:
                if type(left) is IntegerType:
                    self.infer(ast.right.name, IntegerType(), env)
                    return IntegerType()
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
            
        elif ast.op in ['&&', '||']:
            if type(left) is BooleanType and type(right) is BooleanType:
                return BooleanType()
            elif type(left) is AutoType:
                if type(right) is BooleanType:
                    self.infer(ast.left.name, BooleanType(), env)
                    return BooleanType()
                else:
                    raise TypeMismatchInExpression(ast)
            elif type(right) is AutoType:
                if type(left) is BooleanType:
                    self.infer(ast.right.name, BooleanType(), env)
                    return BooleanType()
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['::']:
            if type(left) is StringType and type(right) is StringType:
                return StringType()
            elif type(left) is AutoType:
                if type(right) is StringType:
                    self.infer(ast.left.name, StringType(), env)
                    return StringType()
                else:
                    raise TypeMismatchInExpression(ast)
            elif type(right) is AutoType:
                if type(left) is StringType:
                    self.infer(ast.right.name, StringType(), env)
                    return StringType()
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['<', '>', '<=', '>=']:    # int, float -> bool
            if type(left) in [IntegerType, FloatType] and type(right) in [IntegerType, FloatType]:
                return BooleanType()
            elif type(left) is AutoType:
                if type(right) is IntegerType or type(right) is FloatType:
                    self.infer(ast.left.name, type(right), env)
                    return BooleanType()
                else:
                    raise TypeMismatchInExpression(ast)
            elif type(right) is AutoType:
                if type(left) is IntegerType or type(left) is FloatType:
                    self.infer(ast.right.name, type(left), env)
                    return BooleanType()
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
            
        elif ast.op in ['==', '!=']:    # int, bool -> bool
            if type(left) in [IntegerType, BooleanType] and type(right) in [IntegerType, BooleanType]:
                return BooleanType()
            elif type(left) is AutoType:
                if type(right) is IntegerType or type(right) is BooleanType:
                    self.infer(ast.left.name, type(right), env)
                    return BooleanType()
                else:
                    raise TypeMismatchInExpression(ast)
            elif type(right) is AutoType:
                if type(left) is IntegerType or type(left) is BooleanType:
                    self.infer(ast.right.name, type(left), env)
                    return BooleanType()
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            raise TypeMismatchInExpression(ast)
        
            
    def visitUnExpr(self, ast, env):
        val = self.visit(ast.val, env)
        
        if ast.op == '!':
            if type(val) is BooleanType:
                return BooleanType()
            elif type(val) is AutoType:
                self.infer(ast.val.name, BooleanType(), env)
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == '-':     # int, float -> int, float
            if type(val) in [IntegerType, FloatType]:
                return type(val)
            elif type(val) is AutoType:
                self.infer(ast.val.name, IntegerType(), env)    # TODO: check this
                return IntegerType()
            else:
                raise TypeMismatchInExpression(ast)
        else:                                                   # TODO: check index operator
            raise TypeMismatchInExpression(ast)
    
        
    def visitIntegerType(self, ast, env): return IntegerType()
    def visitFloatType(self, ast, env): return FloatType()
    def visitBooleanType(self, ast, env): return BooleanType()
    def visitStringType(self, ast, env): return StringType()
    
    def visitAutoType(self, ast, env): return AutoType()
    def visitVoidType(self, ast, env): return VoidType()
    
    def visitArrayType(self, ast:ArrayType, env):
        ele_typ = self.visit(ast.typ, env)
        return ArrayType(ast.dimensions, ele_typ)

    def visitArrayCell(self, ast:ArrayCell, env):
        name = ast.name
        cell = ast.cell
        
        # check if name is declared
        if self.lookup(name, env, lambda x: x.name) is None:
            raise Undeclared(Identifier(), name)
        
        # check if name is array
        for i in range(len(cell)):
            if type(cell[i]) is not IntegerType:
                raise TypeMismatchInExpression(ast)
            
        return self.lookup(name, env, lambda x: x.typ)
        
    def visitArrayLit(self, ast:ArrayLit, env):
        exp_list = ast.explist
        if len(exp_list) != 0:
            typ = self.visit(exp_list[0], env)
            for i in range(1, len(exp_list)):
                if type(typ) is not type(self.visit(exp_list[i], env)):
                    raise IllegalArrayLiteral(ast)
        else:
            typ = AutoType()
        return ArrayType(len(exp_list), typ)
        #TODO: fix this

    def visitIntegerLit(self, ast, env): return IntegerType()
    def visitFloatLit(self, ast, env): return FloatType()
    def visitStringLit(self, ast, env): return StringType()
    def visitBooleanLit(self, ast, env): return BooleanType()
    
    def visitFuncCall(self, ast, env): pass        
    def visitAssignStmt(self, ast:AssignStmt, env): 
        lhs = self.visit(ast.lhs, env)
        rhs = self.visit(ast.rhs, env)
        
        if type(lhs) is not type(rhs):
            raise TypeMismatchInStatement(ast)
        elif type(lhs) is AutoType and type(rhs) is not AutoType:
            self.infer(ast.lhs.name, type(rhs), env)
            return
        elif type(lhs) is not AutoType and type(rhs) is AutoType:
            self.infer(ast.rhs.name, type(lhs), env)
            return 
        # TODO: check this
        
    def visitBlockStmt(self, ast, env): pass
    def visitIfStmt(self, ast:IfStmt, env):
        local_env = [[]] + env
        cond = self.visit(ast.cond, local_env)
        if not isinstance(cond, BooleanType):
            raise TypeMismatchInStatement(ast)
        
        tstmt = self.visit(ast.tstmt, local_env)
        fstmt = self.visit(ast.fstmt, local_env)
        
        if type(tstmt) is not type(fstmt):
            raise TypeMismatchInStatement(ast)  
        
    def visitForStmt(self, ast:ForStmt, env):
        local_env = [[]] + env
        init = self.visit(ast.init, local_env)  # AssignStmt
        if not type(ast.init.lhs) is IntegerType:
            raise TypeMismatchInStatement(ast)
        
        cond = self.visit(ast.cond, local_env)
        if not isinstance(cond, BooleanType):
            raise TypeMismatchInStatement(ast)
        
        upd = self.visit(ast.upd, local_env)
        self.in_loop = True
        stmt = self.visit(ast.stmt, local_env)
        self.in_loop = False
        
        # TODO: check this
        
    def visitWhileStmt(self, ast:WhileStmt, env):
        local_env = [[]] + env
        cond = self.visit(ast.exp, local_env)
        if not isinstance(cond, BooleanType):
            raise TypeMismatchInStatement(ast)
        
        self.in_loop = True
        stmt = self.visit(ast.stmt, local_env)
        self.in_loop = False
        
        # TODO: check this
    
    def visitDoWhileStmt(self, ast:DoWhileStmt, env):
        local_env = [[]] + env
        stmt = self.visit(ast.stmt, local_env)
        cond = self.visit(ast.exp, local_env)
        
        if not isinstance(cond, BooleanType):
            raise TypeMismatchInStatement(ast)
        
        # TODO: check this
        
    def visitBreakStmt(self, ast:BreakStmt, env):
        if not self.in_loop:
            raise MustInLoop(ast)
    
    def visitContinueStmt(self, ast:ContinueStmt, env):
        if not self.in_loop:
            raise MustInLoop(ast)
        
    def visitReturnStmt(self, ast, env):
        pass
        
        
    def visitCallStmt(self, ast, env):
        pass
