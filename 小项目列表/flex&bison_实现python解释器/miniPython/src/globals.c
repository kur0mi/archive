#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "globals.h"

char * copyString(char * s)
{	
    int n;
	char* t;
	if (s==NULL) 
        return NULL;
	n = strlen(s) + 1;
	t = (char *)malloc(n);
	if (t==NULL)
		printf("Out of memory error.\n");
	else 
        strcpy(t,s);
	return t;
}
