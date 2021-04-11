all: ../bin/servotest

../bin/servotest: servotest.o 
	gcc -o ../bin/servotest servotest.o -lpigpio -lrt -lpthread

servotest.o: servotest.c servotest.h
	gcc -c -Wall -Wextra servotest.c

clean:
	rm -f ../bin/servotest servotest.o
