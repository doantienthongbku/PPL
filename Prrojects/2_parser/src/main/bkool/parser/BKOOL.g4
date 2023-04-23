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

vardecl: typ idlist SEMI;
funcdecl: typ idlist LP paramdecl RP body;

typ: INT | FLOAT;

idlist: ID (COMMA idlist) | ID;
paramdecl: paramprime | ;
paramprime: param (SEMI paramprime) | param;
param: typ idlist;


body: 'body';

FLOAT: 'float';
INT: 'int';
ID: [a-zA-Z0-9_]+; 

COMMA: ',';
SEMI: '.';
LP: '(';
RP: ')';


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;