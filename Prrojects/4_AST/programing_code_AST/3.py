class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

class Type(AST):
    __metaclass__ = ABCMeta
    pass

class IntType(Type):
    def __str__(self):
        return "IntType"

    def accept(self, v, param):
        return v.visitIntType(self, param)

class FloatType(Type):
    def __str__(self):
        return "FloatType"

    def accept(self, v, param):
        return v.visitFloatType(self, param)


class Program(AST):
    #decl:list(Decl)
    def __init__(self, decl):
        self.decl = decl
    
    def __str__(self):
        return "Program([" + ','.join(str(i) for i in self.decl) + "])"
    
    def accept(self, v: Visitor, param):
        return v.visitProgram(self, param)

class Decl(AST):
    __metaclass__ = ABCMeta
    pass

class VarDecl(Decl):
    #variable:Id
    #varType: Type
    def __init__(self, variable, varType):
        self.variable = variable
        self.varType = varType

    def __str__(self):
        return "VarDecl(" + str(self.variable) + "," + str(self.varType) + ")"

    def accept(self, v, param):
        return v.visitVarDecl(self, param)


class Id(AST):
    #name:string
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Id(" + self.name + ")"

    def accept(self, v, param):
        return v.visitId(self, param)
    
    
class ASTGeneration(MPVisitor):
    # program: vardecls EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(self.visit(ctx.vardecls()))

    # vardecls: vardecl vardecltail;
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    # vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if ctx.vardecl():
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
        return []

    # vardecl: mptype ids ';' 
    # int x, y;
    def visitVardecl(self,ctx:MPParser.VardeclContext):
        mptype = self.visit(ctx.mptype())   # IntType()
        ids = self.visit(ctx.ids())         # [Id(x), Id(y)]
        return list(map(lambda x: VarDecl(x, mptype), ids))

    # MPtype: INTTYPE | FLOATTYPE
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    # ids: ID ',' ids | ID;
    # x, y, z
    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())] + self.visit(ctx.ids())  # [Id(y), Id(z)]