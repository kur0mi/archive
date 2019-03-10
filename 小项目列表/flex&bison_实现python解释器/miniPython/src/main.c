#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "globals.h"

int lineno = 0;
FILE* source;
FILE* listing;

int main() {
    source = fopen("test.py", "r");
    listing = stdout;

    parse();
    return 0;
}
