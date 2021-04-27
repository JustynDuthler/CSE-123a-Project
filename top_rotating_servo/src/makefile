all: ../bin/topservo ../bin/ipc

../bin/topservo: topservo.o 
	gcc -o ../bin/topservo topservo.o -lpigpio -lrt -lpthread
	
../bin/ipc: ipc.o 
	gcc -o ../bin/ipc ipc.o -lpigpio -lrt -lpthread	

topservo.o:topservo.c topservo.h
	gcc -c -Wall -Wextra topservo.c

ipc.o:ipc.c topservo.h
	gcc -c -Wall -Wextra ipc.c

clean:
	rm -f ../bin/topservo topservo.o ../bin/ipc ipc.o
