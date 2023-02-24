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
RETURN: 'return';
FLOAT: 'float';
INT: 'int';
typ: FLOAT | INT;

ID: [a-zA-Z]+; // includes a sequence of alphabetic characters.
idlist: ID COMMA idlist | ID;

paramdecl: LB paramlist RB;
paramlist: paramprime | ;
paramprime: param SEMI paramprime | param;
param: typ idlist;

body: LP stmtlist RP;
stmtlist: stmt stmtlist | stmt;
stmt: vardecl | assignstmt | call | return;

assignstmt: ID ASSIGN expr SEMI;
return: RETURN expr SEMI;
call: ID LB arglist RB SEMI;
arglist: arglistprime | ;
arglistprime: expr COMMA arglistprime | expr;

expr: 'expr';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;