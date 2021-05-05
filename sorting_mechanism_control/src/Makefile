all: ../bin/topservo ../bin/ipc ../bin/topservosonar 

../bin/topservo: topservo/topservo.o 
	gcc -o ../bin/topservo topservo/topservo.o -lpigpio -lrt -lpthread
	
../bin/ipc: ipc/ipc.o 
	gcc -o ../bin/ipc ipc/ipc.o -lpigpio -lrt -lpthread

../bin/topservosonar: topservosonar/topservosonar.o topservosonar/levelDetection.o
	gcc -o ../bin/topservosonar topservosonar/topservosonar.o topservosonar/levelDetection.o -lpigpio -lrt -lpthread

/topservo/topservo.o: topservo/topservo.c 
	gcc -c -Wall -Wextra topservo/topservo.c

/ipc/ipc.o: ipc/ipc.c 
	gcc -c -Wall -Wextra ipc/ipc.c

/topservosonar/topservosonar.o: topservosonar/topservosonar.c topservosonar/levelDetection.h
	gcc -c -Wall -Wextra topservosonar/topservosonar.c 

/topservosonar/levelDetection.o: topservosonar/levelDetection.c topservosonar/levelDetection.h
	gcc -c -Wall -Wextra topservosonar/levelDection.c

clean:
	rm -f ../bin/topservo topservo/topservo.o ../bin/ipc ipc/ipc.o ../bin/topservosonar topservosonar/topservosonar.o topservosonar/levelDection.o

