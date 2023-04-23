"""
    @author dtthong
    @id 1915352
"""
from Visitor import Visitor
from Utils import Utils
from StaticError import *
from AST import *
from abc import ABC

from functools import reduce


class Variable_Decl:
    def __init__(self, name, typ, value=None):
        self.name = name
        self.typ = typ
        self.value = value


class Function_Decl:
    def __init__(self, name, param, ret, inherit=None, is_inherit=False):
        self.name = name
        self.param = param
        self.ret = ret
        self.inherit = inherit
        self.is_inherit = is_inherit


class Param_Decl:
    def __init__(self, name, typ, is_inherit=False, is_out=False):
        self.name = name
        self.typ = typ
        self.is_inherit = is_inherit
        self.is_out = is_out

class StaticChecker(Visitor, Utils):
    def __init__(self, ast):
        self.ast = ast
        self.prototypes = []    # list of FuncDecl (prototype)
        self.in_loop = False    # check if in loop
        self.current_function = None    # current function
    
    def check(self):
        global_env = [[
            Function_Decl(name="readInteger", param=[], ret=IntegerType()),
            Function_Decl(name="readFloat", param=[], ret=FloatType()),
            Function_Decl(name="readBoolean", param=[], ret=BooleanType()),
            Function_Decl(name="readString", param=[], ret=StringType()),
            Function_Decl(name="printInteger", param=[], ret=VoidType()),
            Function_Decl(name="printFloat", param=[], ret=VoidType()),
            Function_Decl(name="printBoolean", param=[], ret=VoidType()),
            Function_Decl(name="printString", param=[], ret=VoidType()),
            Function_Decl(name="super", param=[], ret=None),
            Function_Decl(name="preventDefault", param=[], ret=None),
        ]]
        return self.visitProgram(self.ast, global_env)
        
    def infer(self, name, typ, env):
        for symbol_list in env:
            for symbol in symbol_list:
                if symbol.name == name:
                    symbol.typ = typ
                    return typ
        
    def visitProgram(self, ast:Program, env):
        has_main = False
        for decl in ast.decls:
            if isinstance(decl, FuncDecl) and decl.name == "main":
                if not (len(decl.params) > 0 or type(self.visit(decl.return_type, env)) is not VoidType):
                    has_main = True
                    break

        for decl in ast.decls:
            self.visit(decl, env)

        # print(global_env)
        if not has_main:
            raise NoEntryPoint()
        
    def visitVarDecl(self, ast: VarDecl, env):
        is_redeclared = self.lookup(ast.name, env[0], lambda x: x.name)

        if is_redeclared is not None:
            raise Redeclared(Variable(), ast.name)

        name = ast.name
        typ = self.visit(ast.typ, env)

        if ast.init is not None:
            init_typ = self.visit(ast.init, env)
            if isinstance(typ, AutoType):
                typ = init_typ
            elif isinstance(typ, ArrayType):
                if isinstance(init_typ, ArrayType):
                    if isinstance(typ.typ, AutoType):
                        typ.typ = init_typ.typ
                    elif not isinstance(typ.typ, type(init_typ.typ)):
                        raise TypeMismatchInVarDecl(ast)
                else:
                    raise TypeMismatchInVarDecl(ast)
            elif isinstance(init_typ, IntegerType) and isinstance(typ, FloatType):
                pass
            else:
                if not isinstance(typ, type(init_typ)):
                    raise TypeMismatchInVarDecl(ast)
        else:
            if isinstance(typ, AutoType):
                raise Invalid(Variable(), name)
        
        env[0] += [Variable_Decl(name=name, typ=typ, value=ast.init)]

    def visitParamDecl(self, ast: ParamDecl, env):
        is_redeclared = self.lookup(ast.name, env[0], lambda x: x.name)
        if is_redeclared is not None:
            raise Redeclared(Parameter(), ast.name)
        
        name = ast.name
        typ = self.visit(ast.typ, env)
        is_inherit = ast.inherit
        is_out = ast.out
        
        env[0] += [Param_Decl(name, typ, is_inherit=is_inherit, is_out=is_out)]
        return Param_Decl(name, typ, is_inherit=is_inherit, is_out=is_out)

    def visitFuncDecl(self, ast: FuncDecl, env):
        is_redeclared_func = self.lookup(ast.name, env[0], lambda x: x.name)
        if is_redeclared_func is not None:
            raise Redeclared(Function(), ast.name)
        
        param_list = []
        local_env = [[]] + env
        for param in ast.params:
            param_list.append(self.visit(param, local_env))
        
        is_redeclared_param = self.lookup(ast.name, param_list, lambda x: x.name)
        if is_redeclared_param is not None:
            raise Redeclared(Parameter(), ast.name)
        
        local_env[0] += [Function_Decl(name=ast.name, param=param_list, ret=ast.return_type)]
        self.current_function = ast.name
        self.visit(ast.body, local_env)     # check body
        self.current_function = None

        env[0] += [Function_Decl(name=ast.name, param=param_list, ret=ast.return_type)]
        
    def visitId(self, ast, env):
        for symbol_list in env:
            for symbol in symbol_list:
                if ast.name == symbol.name:
                    if isinstance(symbol, Function_Decl):
                        return symbol.ret
                    return symbol.typ
        
        raise Undeclared(Identifier(), ast.name)
    
    def visitBlockStmt(self, ast:BlockStmt, env):
        for x in ast.body:
            self.visit(x, env)

    def visitBinExpr(self, ast: BinExpr, env):
        left = self.visit(ast.left, env)
        right = self.visit(ast.right, env)

        if ast.op in ['+', '-', '*', '/']:
            if isinstance(left, IntegerType) and isinstance(right, IntegerType):
                return IntegerType()
            elif isinstance(left, FloatType) and isinstance(right, FloatType):
                return FloatType()
            elif isinstance(left, IntegerType) and isinstance(right, FloatType) \
                    or isinstance(left, FloatType) and isinstance(right, IntegerType):
                return FloatType()
            elif isinstance(left, AutoType):
                if isinstance(right, IntegerType) or isinstance(right, FloatType):
                    self.infer(ast.left.name, right, env)
                    return right
                else:
                    raise TypeMismatchInExpression(ast)
            elif isinstance(right, AutoType):
                if isinstance(left, IntegerType) or isinstance(left, FloatType):
                    self.infer(ast.right.name, left, env)
                    return left
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['%']:
            if isinstance(left, IntegerType) and isinstance(right, IntegerType):
                return IntegerType()
            elif isinstance(left, AutoType):
                if isinstance(right, IntegerType):
                    self.infer(ast.left.name, IntegerType(), env)
                    return IntegerType()
                else:
                    raise TypeMismatchInExpression(ast)
            elif isinstance(right, AutoType):
                if isinstance(left, IntegerType):
                    self.infer(ast.right.name, IntegerType(), env)
                    return IntegerType()
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
            
        elif ast.op in ['&&', '||']:
            if isinstance(left, BooleanType) and isinstance(right, BooleanType):
                return BooleanType()
            elif isinstance(left, AutoType):
                if isinstance(right, BooleanType):
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
            if isinstance(left, StringType) and isinstance(right, StringType):
                return StringType()
            elif isinstance(left, AutoType):
                if isinstance(right, StringType):
                    self.infer(ast.left.name, StringType(), env)
                    return StringType()
                else:
                    raise TypeMismatchInExpression(ast)
            elif isinstance(right, AutoType):
                if isinstance(left, StringType):
                    self.infer(ast.right.name, StringType(), env)
                    return StringType()
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['<', '>', '<=', '>=']:    # int, float -> bool
            if isinstance(left, (IntegerType, FloatType)) and isinstance(right, (IntegerType, FloatType)):
                return BooleanType()
            elif isinstance(left, AutoType):
                if isinstance(right, IntegerType) or isinstance(right, FloatType):
                    self.infer(ast.left.name, right, env)
                    return BooleanType()
                else:
                    raise TypeMismatchInExpression(ast)
            elif isinstance(right, AutoType):
                if isinstance(left, IntegerType) or isinstance(left, FloatType):
                    self.infer(ast.right.name, left, env)
                    return BooleanType()
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
            
        elif ast.op in ['==', '!=']:    # int, bool -> bool
            if isinstance(left, (IntegerType, BooleanType)) and isinstance(right, (IntegerType, BooleanType)):
                return BooleanType()
            elif isinstance(left, AutoType):
                if isinstance(right, IntegerType) or isinstance(right, BooleanType):
                    self.infer(ast.left.name, right, env)
                    return BooleanType()
                else:
                    raise TypeMismatchInExpression(ast)
            elif isinstance(right, AutoType):
                if isinstance(left, IntegerType) or isinstance(left, BooleanType):
                    self.infer(ast.right.name, left, env)
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
            if isinstance(val, BooleanType):
                return BooleanType()
            elif isinstance(val, AutoType):
                self.infer(ast.val.name, BooleanType(), env)
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == '-':     # int, float -> int, float
            if isinstance(val, (IntegerType, FloatType)):
                return val
            elif isinstance(val, AutoType):
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
        item = None
        
        # check if name is declared
        for sub_env in env:
            item = self.lookup(name, sub_env, lambda x: x.name)
            if item is not None: break
        if item is None:
            raise Undeclared(Identifier(), name)
        
        # check if name is array
        for i in range(len(cell)):
            typ_cell_item = self.visit(cell[i], env)
            if not isinstance(typ_cell_item, IntegerType):
                raise TypeMismatchInExpression(ast)
        
        return item.typ.typ
        
    def visitArrayLit(self, ast:ArrayLit, env):
        exp_list = ast.explist
        if len(exp_list) != 0:
            typ = self.visit(exp_list[0], env)
            for i in range(1, len(exp_list)):
                item_typ = self.visit(exp_list[i], env)
                if not isinstance(typ, type(item_typ)):
                    raise IllegalArrayLiteral(ast)
        else:
            typ = AutoType()
        return ArrayType(exp_list, typ)

    def visitIntegerLit(self, ast, env): return IntegerType()
    def visitFloatLit(self, ast, env): return FloatType()
    def visitStringLit(self, ast, env): return StringType()
    def visitBooleanLit(self, ast, env): return BooleanType()
    
    def visitFuncCall(self, ast, env):
        func = None
        for sub_env in env:
            func = self.lookup(ast.name, sub_env, lambda x: x.name)
            if func is not None: break
        if func is None:
            raise Undeclared(Function(), ast.name)
        
        if len(ast.args) != len(func.param):
            raise TypeMismatchInExpression(ast)
        
        return func.ret
    
    def visitAssignStmt(self, ast:AssignStmt, env): 
        lhs = self.visit(ast.lhs, env)
        rhs = self.visit(ast.rhs, env)
        
        if isinstance(lhs, VoidType) or isinstance(lhs, ArrayType):
            raise TypeMismatchInStatement(ast)
        elif not isinstance(lhs, type(rhs)):
            raise TypeMismatchInStatement(ast)
        elif isinstance(lhs, AutoType) and not isinstance(rhs, AutoType):
            self.infer(ast.lhs.name, rhs, env)
            return
        elif not isinstance(lhs, AutoType) and isinstance(rhs, AutoType):
            self.infer(ast.rhs.name, lhs, env)
            return
        
    def visitIfStmt(self, ast:IfStmt, env):
        local_env = [[]] + env
        cond = self.visit(ast.cond, local_env)
        if not isinstance(cond, BooleanType):
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.tstmt, local_env)
        self.visit(ast.fstmt, local_env)
        
    def visitForStmt(self, ast:ForStmt, env):
        local_env = [[]] + env
        
        self.visit(ast.init, local_env)  # AssignStmt
        init_lhs_typ = self.visit(ast.init.lhs, local_env)
        if isinstance(init_lhs_typ, IntegerType):
            raise TypeMismatchInStatement(ast.init)

        cond = self.visit(ast.cond, local_env)
        if not isinstance(cond, BooleanType):
            raise TypeMismatchInStatement(ast)
        
        upd_typ = self.visit(ast.upd, local_env)
        if not isinstance(upd_typ, IntegerType):
            raise TypeMismatchInStatement(ast)
        
        self.in_loop = True
        self.visit(ast.stmt, local_env)
        self.in_loop = False
        
    def visitWhileStmt(self, ast:WhileStmt, env):
        local_env = [[]] + env
        cond = self.visit(ast.cond, local_env)
        if not isinstance(cond, BooleanType):
            raise TypeMismatchInStatement(ast)
        
        self.in_loop = True
        self.visit(ast.stmt, local_env)
        self.in_loop = False
    
    def visitDoWhileStmt(self, ast:DoWhileStmt, env):
        local_env = [[]] + env
        self.visit(ast.stmt, local_env)
        cond = self.visit(ast.cond, local_env)
        
        if not isinstance(cond, BooleanType):
            raise TypeMismatchInStatement(ast)
        
    def visitBreakStmt(self, ast:BreakStmt, env):
        if not self.in_loop:
            raise MustInLoop(ast)
    
    def visitContinueStmt(self, ast:ContinueStmt, env):
        if not self.in_loop:
            raise MustInLoop(ast)
        
    def visitReturnStmt(self, ast:ReturnStmt, env):
        if self.current_function is None:
            raise TypeMismatchInStatement(ast)
        
        func = self.lookup(self.current_function, env[0], lambda x: x.name)
        
        if ast.expr is None:
            if not isinstance(func.return_type, VoidType):
                raise TypeMismatchInStatement(ast)
        else:
            expr_typ = self.visit(ast.expr, env)
            if not isinstance(expr_typ, type(func.return_type)):
                raise TypeMismatchInStatement(ast)
            elif isinstance(expr_typ, AutoType) and not isinstance(func.return_type, AutoType):
                return
            elif not isinstance(expr_typ, AutoType) and isinstance(func.return_type, AutoType):
                self.infer(func.name, expr_typ, env)
                return
        
    def visitCallStmt(self, ast, env):
        func = None
        for sub_env in env:
            func = self.lookup(ast.name, sub_env, lambda x: x.name)
            if func is not None: break
        if func is None:
            raise Undeclared(Function(), ast.name)
        
        if len(ast.args) != len(func.params):
            raise TypeMismatchInStatement(ast)
