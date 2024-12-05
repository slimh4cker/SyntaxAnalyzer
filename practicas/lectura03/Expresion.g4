grammar Expresion;

start:
'Slim^' '{' body '}'
;

body:
    expr* | assignment
    ;

assignment: ID '=' expr;

expr:
    expr (POR | DIV) expr  #mulDiv
    |
    expr (SUM | RES) expr  #sumRes
    |
    '(' expr ')'           #parenthesis
    |
    NUMBER                 #number
    ;

POR: '*';
DIV: '/';
SUM: '+';
RES: '-';
NUMBER: [0-9]+;
ID: [a-zA-Z_][a-zA-Z]*;
WS: [ \t\r\n]+ -> skip;
