// Student ID: 1915352
grammar MT22;

@lexer::header {
from lexererr import *
}

// @parser::members {
// id_count = 0
// expr_count = 0
// }

options{
	language=Python3;
}

// program
program: decllist EOF;
decllist: decl decllist | decl;
decl: vardecl | funcdecl ;

// function declaration
funcdecl: ID COLON FUNCTION func_typ LB paramlist RB (INHERIT ID)? block_stmt;
// parameter declaration
paramlist: paramprime | ;
paramprime: param COMMA paramprime | param;
param: INHERIT? OUT? ID COLON typ;

// block_stmt
block_stmt: LP stmtlist RP;
stmtlist: stmt stmtlist | ;
stmt: vardecl | assignstmt | returnstmt | callstmt | ifstmt
	| forstmt | whilestmt | dowhilestmt | breakstmt | spec_func
	| continuestmt | block_stmt;

// Statements
assignstmt: scalar_var ASSIGN expr SEMI;
ifstmt: IF LB expr RB stmt (ELSE stmt)?;
forstmt: FOR LB scalar_var ASSIGN expr COMMA expr COMMA expr RB stmt;
whilestmt: WHILE LB expr RB stmt;
dowhilestmt: DO block_stmt WHILE LB expr RB SEMI;
breakstmt: BREAK SEMI;
continuestmt: CONTINUE SEMI;
returnstmt: RETURN expr? SEMI;
callstmt: ID LB arglist RB SEMI;

// Special functions
spec_func: readInt | printInt | readFloat | printFloat| readBool 
		 | printBool | readString | printString | superr | preventDefault;
readInt: 'readInteger' LB RB SEMI;
printInt: 'printInteger' LB intVal RB SEMI;
readFloat: 'readFloat' LB RB SEMI;
printFloat: 'printFloat' LB floatVal RB SEMI;
readBool: 'readBoolean' LB RB SEMI;
printBool: 'printBoolean' LB boolVal RB SEMI;
readString: 'readString' LB RB SEMI;
printString: 'printString' LB stringVal RB SEMI;
superr: 'super' LB exprlist RB SEMI;
preventDefault: 'preventDefault' LB RB SEMI;

intVal: ID | INTLIT | expr;
floatVal: ID | FLOATLIT | expr;
stringVal: ID | STRINGLIT | expr;
boolVal: ID | boollit | expr;

// vardecl: idlist COLON var_typ (ASSIGN exprlist)? SEMI {
// if self.id_count != self.expr_count and self.expr_count != 0:
// 	raise SyntaxError("Error on line " + str(self._input.LT(-1).line) + 
// 					  " col " + str(self._input.LT(-1).column) + ": " + self._input.LT(-1).text)
// self.id_count = 0
// self.expr_count = 0
// };

// Variable declarations
vardecl: helper SEMI;
basecase: ID COLON typ ASSIGN expr;
helper: ID COMMA helper COMMA expr | basecase; 

// scalar variable
scalar_var: ID | ID idx_op;

// exprlist: expr COMMA {
// self.expr_count += 1
// if self.id_count == self.expr_count and self._input.LT(-1).text != ';':
// 	raise SyntaxError("Error on line " + str(self._input.LT(-1).line) + 
// 					  " col " + str(self._input.LT(-1).column) + ": " + self._input.LT(-1).text)
// 	self.id_count = 0
// 	self.expr_count = 0
// } exprlist | expr {self.expr_count += 1};

// expressions
exprlist: expr COMMA exprlist | expr;

expr: expr1 CONCAT expr1 | expr1;
expr1: expr2 op_relational expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 op_mul expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUB expr6 | expr7;
expr7: expr8 idx_op | expr8;
expr8: subexpr | ID | INTLIT | FLOATLIT | boollit | STRINGLIT | callexpr | arraylit;

subexpr: LB expr RB;
idx_op: LS exprlist RS;
callexpr: ID LB arglist RB;

arglist: arglistprime | ;
arglistprime: expr COMMA arglistprime | expr;

// idlist
// idlist: ID COMMA {self.id_count += 1} idlist 
// 	  | ID {self.id_count += 1};
idlist: ID COMMA idlist 
	  | ID;

// array type
arraylit: LP subarrayitem RP;
subarrayitem: arritems | ;
arritems: expr COMMA arritems | expr;

// Literals
func_typ: typ | VOID | arraydecl;
var_typ: typ | arraydecl;
arraydecl: ARRAY LS intlist RS OF typ;
intlist: INTLIT COMMA intlist | INTLIT;

typ: FLOAT | INTEGER | BOOLEAN | STRING | AUTO;	// one of 4 atomic types
// type operators
op_relational: SMALLER | SMALLER_OR_EQUAL | GREATER | GREATER_OR_EQUAL
			 | EQUAL | DIFF;
op_mul: MUL | DIV | MOD;

boollit: TRUE | FALSE;

// comment
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' .*? ~[\r\n]* -> skip;

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
COMMA: ','; SEMI: ';'; ASSIGN: '='; COLON: ':'; DOT: '.';
LB: '('; RB: ')'; LP: '{'; RP: '}'; LS: '['; RS: ']';

// atomic types
INTLIT: '0'
	  | [1-9] [0-9]* ('_' [0-9]+)* {self.text = self.text.replace('_', '')};

FLOATLIT: (DIGIT_UNDERSCORE DECIMAL? SCIENTIFIC 
		| DIGIT_UNDERSCORE DECIMAL SCIENTIFIC?
		| DIGIT_UNDERSCORE? DECIMAL SCIENTIFIC) {self.text = self.text.replace('_', '')};
fragment DIGIT_UNDERSCORE: [0-9]+ ('_' [0-9]+)*;
fragment SCIENTIFIC: [eE] [+-]? [0-9]+;
fragment DECIMAL: '.' [0-9]*;

STRINGLIT: DoubleQuote ( StringChar*) DoubleQuote 
{ 
	result = str(self.text)
	self.text = result[1:-1]
};
fragment StringChar: ~[\f\r\n"\\] | EscapeSequence;
fragment EscapeSequence: '\\' [bfrnt"'\\];
fragment IllegalString: '\\' ~[bfrnt"'\\] | '\\';
fragment DoubleQuote: '"';

// identifier
ID: [a-zA-Z_]  [a-zA-Z_0-9]*;


WS : [ \t\r\n\b\f]+ -> skip ; // skip spaces, tabs, newlines

// Error handling
ERROR_CHAR: . { raise ErrorToken(self.text) };
UNCLOSE_STRING: DoubleQuote StringChar* ([\f\n\r"\\] | EOF)
{
	unclose_str = str(self.text)
	possible = ['\f', '\n', '\r', '"', '\\']
	if unclose_str[-1] in possible:
		raise UncloseString(unclose_str[1:-1])
	else:
		raise UncloseString(unclose_str[1:])
};
ILLEGAL_ESCAPE: DoubleQuote StringChar* IllegalString 
{
	illegal_str = str(self.text)
	raise IllegalEscape(illegal_str[1:]) 
} ;