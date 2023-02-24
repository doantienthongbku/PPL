// Student ID: 1915352
grammar MT22;

@lexer::header {
from lexererr import *
}

@parser::members {
id_count = 0
expr_count = 0
}

options{
	language=Python3;
}

// Literals
typ: FLOAT | INTEGER | BOOLEAN | STRING | AUTO;	// one of 4 atomic types
func_typ: typ | VOID | ARRAY;
var_typ: typ | arraydecl;

// array type
arraylit: LP subarrayitem RP;
subarrayitem: arritems | ;
arritems: (INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | arraylit) COMMA arritems 
		| (INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | arraylit);

arraydecl: ARRAY LS intlist RS OF typ;
intlist: INTLIT COMMA intlist | INTLIT;

// Variable declarations
vardecl: idlist COLON var_typ (ASSIGN (exprlist | arraylit))? SEMI {
if self.id_count != self.expr_count and self.expr_count != 0:
	raise SyntaxError("Error on line " + str(self._input.LT(-1).line) + 
					  " col " + str(self._input.LT(-1).column) + ": " + self._input.LT(-1).text)
};
// idlist
idlist: ID COMMA {self.id_count += 1} idlist 
	  | ID {self.id_count += 1};
// function declaration
funcdecl: ID COLON FUNCTION func_typ LB paramlist RB body;
// parameter declaration
paramdecl: paramlist;
paramlist: paramprime | ;
paramprime: param COMMA paramprime | param;
param: INHERIT? OUT? ID COLON typ;

// program
program: decllist EOF;
decllist: decl decllist | decl;
decl: vardecl | funcdecl;

// expression
exprlist: expr COMMA exprlist {self.expr_count += 1}
		| expr {self.expr_count += 1};

expr: expr1 CONCAT expr1 | expr1;
expr1: expr2 OP_RELATIONAL expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 OP_MUL expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUB expr6 | expr7;
expr7: expr7 idx_op | expr8;
expr8: subexpr | ID | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | callexpr;

subexpr: LB expr RB;
idx_op: ID LS exprlist RS;
callexpr: ID LB arglist RB;

// type operators
OP_RELATIONAL: SMALLER | SMALLER_OR_EQUAL | GREATER | GREATER_OR_EQUAL
			 | EQUAL | DIFF;
OP_MUL: MUL | DIV | MOD;

// body: 'body';
body: LP stmtlist RP;
stmtlist: stmt stmtlist | ;
stmt: vardecl | assignstmt | returnstmt | callstmt | ifstmt
	| forstmt | whilestmt | dowhilestmt | breakstmt | spec_func
	| continuestmt;

block_stmt: body | stmt;
// Statements
assignstmt: (ID | idx_op) ASSIGN expr SEMI;
ifstmt: IF LB expr RB block_stmt (ELSE block_stmt)?;
forstmt: FOR LB ID EQUAL expr COMMA expr COMMA expr RB;
whilestmt: WHILE LB expr RB block_stmt;
dowhilestmt: DO block_stmt WHILE LB expr RB SEMI;
breakstmt: BREAK SEMI;
continuestmt: CONTINUE SEMI;
returnstmt: RETURN expr SEMI;
callstmt: ID LB arglist RB SEMI;
arglist: arglistprime | ;
arglistprime: expr COMMA arglistprime | expr;

// Special functions
spec_func: readInt | printInt | readFloat | printFloat| readBool 
		 | printBool | readString | printString | superr | preventDefault;
readInt: 'readInteger()' SEMI;
printInt: 'printInteger' LB intVal RB SEMI;
readFloat: 'readFloat()' SEMI;
printFloat: 'printFloat' LB floatVal RB SEMI;
readBool: 'readBoolean()' SEMI;
printBool: 'printBoolean' LB boolVal RB SEMI;
readString: 'readString()' SEMI;
printString: 'printString' LB stringVal RB SEMI;
superr: 'super' LB exprlist RB SEMI;
preventDefault: 'preventDefault()' SEMI;

intVal: ID | INTLIT;
floatVal: ID | FLOATLIT;
stringVal: ID | STRINGLIT;
boolVal: ID | BOOLLIT | expr;

// comment
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' .*? [\r\n] -> skip;

// Keywords
AUTO: 'auto'; BREAK: 'break'; BOOLEAN: 'boolean';
DO: 'do'; ELSE: 'else'; FALSE: 'false';
FLOAT: 'float'; FOR: 'for'; FUNCTION: 'function';
IF: 'if'; INTEGER: 'integer'; RETURN: 'return';
STRING: 'string'; TRUE: 'true'; WHILE: 'while';
VOID: 'void'; OUT: 'out'; CONTINUE: 'continue';
OF: 'of'; INHERIT: 'inherit'; ARRAY: 'array';

// Operators
ADD: '+'; SUB: '-'; MUL: '*'; DIV: '/'; 
MOD: '%'; NOT: '!'; AND: '&&'; OR: '||'; EQUAL: '==';
DIFF: '!='; SMALLER: '<'; SMALLER_OR_EQUAL: '<='; 
GREATER: '>'; GREATER_OR_EQUAL: '>='; CONCAT: '::';

// type operators
OP_BOOL: NOT | AND | OR | EQUAL | DIFF;
OP_INT: ADD | SUB | MUL | DIV | MOD | EQUAL | DIFF
	  | SMALLER | SMALLER_OR_EQUAL | GREATER | GREATER_OR_EQUAL;
OP_FLOAT:ADD | SUB | MUL | DIV | EQUAL | DIFF
	    | SMALLER | SMALLER_OR_EQUAL | GREATER | GREATER_OR_EQUAL;
OP_STRING: CONCAT;

// Seperators
COMMA: ','; DOT: '.'; SEMI: ';'; ASSIGN: '='; COLON: ':';
LB: '('; RB: ')'; LP: '{'; RP: '}'; LS: '['; RS: ']';

// atomic types
INTLIT: '0'
	  | [1-9] [0-9]* ('_' [0-9]+)* {self.text = self.text.replace('_', '')};
FLOATLIT: DIGIT_UNDERSCORE (DOT DIGIT_UNDERSCORE?)? SCIENTIFIC {self.text = self.text.replace('_', '')}
		| DIGIT_UNDERSCORE DOT DIGIT_UNDERSCORE? {self.text = self.text.replace('_', '')};
fragment DIGIT_UNDERSCORE: [0-9_]+;
fragment SCIENTIFIC: [eE] [+-]? DIGIT_UNDERSCORE;
// STRINGLIT: '"' ('\\' ["\\] | ~[" \\])* '"';
STRINGLIT : '"' ( EscapeSequence | ~["\\] )* '"' {self.text = self.text[1:-1]};
fragment EscapeSequence: '\\' ( 'b' | 'f' | 'r' | 'n' | 't' | '\'' | '\\' | '"' );
BOOLLIT: TRUE | FALSE;

KEYWORD: AUTO | BREAK | BOOLEAN | DO | ELSE | FALSE | FLOAT | FOR | FUNCTION
		| IF | INTEGER | RETURN | STRING | TRUE | WHILE | VOID | OUT
		| CONTINUE | OF | INHERIT | ARRAY;
// identifier
ID: [a-zA-Z_]  [a-zA-Z_0-9]*;// {if self.text in KEYWORD: raise IllegalIdentifier(self.text)};


WS : [ \t\r\n\b\f]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' {raise UncloseString(self.text)};
ILLEGAL_ESCAPE: ESC_ILLEGAL {raise IllegalEscape(self.text)};
fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;