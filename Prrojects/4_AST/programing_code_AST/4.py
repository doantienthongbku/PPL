"""
program: vardecl+ EOF;
vardecl: mptype ids ';' ;
mptype: INTTYPE | FLOATTYPE;
ids: ID (',' ID)*; 
INTTYPE: 'int';
FLOATTYPE: 'float';
ID: [a-z]+ ;
"""

class Program:#decl:list(VarDecl)
    pass

class Type(ABC): pass

class IntType(Type): pass

class FloatType(Type): pass

class VarDecl: #variable:Id; varType: Type
    pass

class Id: #name:str
    pass

class ASTGeneration(MPVisitor):
    # program: vardecl+ EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return reduce(lambda prev, curr: prev + self.visit(curr), ctx.vardecl(), [])

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        mptype = self.visit(ctx.mptype())   # IntType()
        ids = self.visit(ctx.ids())         # [Id(x), Id(y)]
        return list(map(lambda x: VarDecl(x, mptype), ids))

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    # ids: ID (',' ID)*
    def visitIds(self,ctx:MPParser.IdsContext):
        return list(map(lambda x: Id(x.getText()), ctx.ID()))