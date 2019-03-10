bison -d parser.y
flex -o parser.lex.c parser.l

gcc -c main.c
gcc -c globals.c
gcc -c parser.tab.c
gcc -c parser.lex.c
gcc -o parser main.o globals.o parser.tab.o parser.lex.o

