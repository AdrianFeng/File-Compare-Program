mainexec	:	foo.o main.o
	g++ foo.o main.o -o mainexec
foo.o	:	foo.h fo.cpp
	g++ -c foo.cpp -o foo.o
main.o	:	foo.h main.cpp
	g++ -c main.cpp -o main.o	
