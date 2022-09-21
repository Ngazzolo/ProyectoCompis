grammar Mistery;

prog:	(Aa)* ;

// Describe con palabras lo que acepta la regla Aa

Aa:	ID ('[' (ID | INTEGER) ']') +
    ;

//SOLUCION
//A[S][13] Aa es una produccion de letra seguido de corchetes que pueden ser letras o numeros o un
// corchete que inicia con letra y luego digito




ID: Letter LetterOrDigit*;
INTEGER : [0-9]+ ;

// fragment es para crear segmentos de token que solamente serán usados en este archivo, pero que no
// generan un token. Son como definiciones "locales" a este archivo.

fragment LetterOrDigit
    : Letter
    | [0-9]
    ;

fragment Letter : [a-zA-Z$_] ;