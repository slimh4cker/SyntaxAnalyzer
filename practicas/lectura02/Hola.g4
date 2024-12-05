grammar Hola;

// MAIN RULE:
saludar: 'Hola' NAME;

NAME: [A-Z][a-z]+;
WS: [ \t\r\n] -> skip;