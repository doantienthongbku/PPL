grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: EOF;

// '*' zero or many
// '+' one or many
// '?' zero or one
// '|' or
// '~' not
// '*' greedy (tham lam)
// '*?' non-greedy (khong tham lam)


SHEXA: DIGIT+ LETTER* {int(self.text, 16) % 2 == 0}?;

fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;