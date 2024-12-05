grammar Expresion;

expresion: expresion '*' expresion | ID | NUM
    | expresion '/' expresion
    | expresion '+' expresion
    | expresion '-' expresion;

///// LEXER

ID: [a-z_0-9]+;
NUM: [0-9]+;
ESPACIOS: [ \t\r\n] -> skip;
