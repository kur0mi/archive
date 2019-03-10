%expect 1
%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "globals.h"
static TreeNode* savedTree;

void yyerror(char * message);   // yacc解析失败时自动调用
%}

%union {
    struct treeNode* node;
    int num;
    char * idName;
    char * indentStr;
}
%token <num> NUM
%token <idName> ID
%token <indentStr> INDENT

%nonassoc NOTEQ

%token FOR RANGE IN IF AND PRINT
%token LPAREN RPAREN COMMA COLON
%token ERROR

%type <node> stmt_list stmt
%type <node> for_stmt if_stmt print_stmt body exp

%start program

%% /* 文法 */

program     : stmt_list
            {   //savedTree = $1;
                printf("规约完毕，语法分析树已建立\n");
            }
            ;
stmt_list   :
            { $$ = NULL;}
            | stmt_list stmt
            {/*
                TreeNode* t = $1;
                if (t != NULL) {
                    while (t->sibling != NULL)  
                        t = t->sibling;
                    t->sibling = $2;
                    $$ = $1;
                }
                else {
                    $$ = $2;
                }*/
            }
            ;
stmt        : for_stmt      { $$ = $1;}
            | if_stmt       { $$ = $1;}
            | print_stmt    { $$ = $1;}
            ;
for_stmt    : FOR ID IN RANGE LPAREN NUM COMMA NUM RPAREN COLON body
            {
                //$$->type = forK;
                printf("for %s : %d-%d\n", $2, $6, $8);   
                $$ = NULL;
            }
            ;
if_stmt     : IF exp COLON      { printf("if stmt\n");}
            body
            ;
print_stmt  : PRINT LPAREN ID COMMA ID COMMA ID RPAREN { printf("print stmt\n");}
            ;
body        : stmt   {}
            ;
exp         : ID NOTEQ ID   {}
            | exp AND exp   {}
            | LPAREN exp RPAREN         {}
            ;

%%

void yyerror(char * message)
{	
    printf("Syntax error : %s\n", message);
}

TreeNode* parse() {
    printf("开始解析...\n");
    iniLexer();         // 词法分析器初始化
    yyparse();          // 语法分析开始 yacc解析入口函数
    printf("结束\n");
    printf("\n源文件 总行数: %d\n", lineno);
    return savedTree;
}
