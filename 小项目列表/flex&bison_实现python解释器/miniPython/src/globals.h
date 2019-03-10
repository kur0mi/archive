#ifndef _GLOBALS_H
#define _GLOBALS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern int lineno;     // 记录源程序的行号
extern FILE* source;
extern FILE* listing;

typedef enum { forK, ifK, printK } treeType;

#define MAXCHILDREN 3
// 语法树节点的定义（未完成）
typedef struct treeNode
{	
    struct treeNode * child[MAXCHILDREN];
	struct treeNode * sibling;
	int line_no;
	treeType type;
} TreeNode;

/* copyString 分配一块内存以放置新的字符串，并返回其首地址 */
char * copyString(char * s);

/* 创建一个新的树节点 */
//TreeNode* createTreeNode(treeType type);

#endif
