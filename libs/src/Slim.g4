grammar Slim;

start:
    'Slim^' '{' body '}'
    ;

body:
    (print | assignment | expr ';')*
    ;

print:
    (ID | expr) ';'
    ;


assignment:
    ID '=' expr ';'
    ;

expr:
    expr (POR | DIV) expr   #mulDiv
    |
    expr (SUM | RES) expr   #sumRes
    |
    expr EXP expr           #exponential
    |
    '(' expr ')'            #parenthesis
    |
    NUMBER                  #number
    |
    ID                      #variableId
    ;

POR: '*';
DIV: '/';
SUM: '+';
RES: '-';
EXP: '^';
NUMBER: [-]?[0-9]+;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
WS: [ \t\r\n]+ -> skip;
