grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}
// Use ANTLR to write regular expressions describing 
// Pascal strings are made up of a sequence of characters between single quotes: 'string'. 
// The single quote itself can appear as two single quotes back to back in a string: 'isn''t'.

// '*' zero or many
// '+' one or many
// '?' zero or one
// '|' or
// '~' not
// '*' greedy (tham lam)
// '*?' non-greedy (khong tham lam)


program: decllist EOF;
decllist: decl decllist | decl;
decl: vardecl | funcdecl;

vardecl:  typ idlist SEMI;
funcdecl: typ ID paramdecl body;

COMMA: ',';
SEMI: ';';
LB: '(';
RB: ')';
LP: '{';
RP: '}';
ASSIGN: '=';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
RETURN_TEXT: 'return';
FLOAT: 'float';
INT: 'int';
typ: FLOAT | INT;
INTLIT: '0'
      | [1-9][0-9]*;
FLOATLIT: INTEGER ('.' INTEGER)? SCIENTIFIC
		| INTEGER '.' INTEGER;
fragment DIGIT: [0-9];
fragment INTEGER: DIGIT+;
fragment SCIENTIFIC: [eE] [+-]? INTEGER;

ID: [a-zA-Z] [a-zA-Z0-9]*; // includes a sequence of alphabetic characters.
idlist: ID COMMA idlist | ID;

paramdecl: LB paramlist RB;
paramlist: paramprime | ;
paramprime: param SEMI paramprime | param;
param: typ idlist;

// body: 'body';
body: LP stmtlist RP;
stmtlist: stmt stmtlist | ;
stmt: vardecl | assignstmt | callstmt | returnstmt;

assignstmt: ID ASSIGN expr SEMI;
returnstmt: RETURN_TEXT expr SEMI;
callstmt: ID LB arglist RB SEMI;
arglist: arglistprime | ;
arglistprime: expr COMMA arglistprime | expr;

// expression
expr: expr1 ADD expr | expr1;
expr1: expr2 SUB expr1 | expr2;
expr2: expr3 (MUL | DIV) expr2 | expr3;
expr3: subexpr | ID | INTLIT | FLOATLIT | callexpr;
subexpr: LB expr RB;
callexpr: ID LB arglist RB;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;