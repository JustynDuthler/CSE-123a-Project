all: ../bin/topservo 

../bin/topservo: topservo.o 
	gcc -o ../bin/topservo topservo.o -lpigpio -lrt -lpthread

topservo.o: topservo.c topservo.h
	gcc -c -Wall -Wextra topservo.c

clean:
	rm -f ../bin/topservo topservo.o
