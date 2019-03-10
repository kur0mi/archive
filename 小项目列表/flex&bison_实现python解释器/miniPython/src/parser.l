%option noyywrap
%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "globals.h"
#include "parser.tab.h"

%}

digit       [0-9]
num         {digit}+
letter      [a-zA-Z]
id          ({letter}|_)({letter}|{digit}|_)*
/* indent      ^[ \t]* */
whitespace  [ \t]*

%%

"for"       { return FOR; }
"range"     { return RANGE; }
"in"        { return IN; }
"if"        { return IF; }
"and"       { return AND; }
"print"     { return PRINT; }

{num}           { yylval.num = atoi(yytext); return NUM; }
{id}            { yylval.idName = copyString(yytext); return ID; }
{whitespace}    { /* ignore */ }

"("         { return LPAREN; }
")"         { return RPAREN; }
","         { return COMMA; }
":"         { return COLON; }
"!="        { return NOTEQ; }

\n          { lineno++; }
.           { printf("unknown text at line %d: %s\n", lineno, yytext); return ERROR; }

%%

void iniLexer() {
    lineno = 1;
    yyin = source;
    yyout = listing;
}

// {indent}        { yylval.indentStr = copyString(yytext); return INDENT; }