#---------------------------------
# Team 7 
#
# Makefile for trash level detection
#
# --------------------------------

all: ../bin/levelDetection 

../bin/levelDetection: levelDetection.o 
	gcc -o ../bin/levelDetection levelDetection.o 

levelDetection.o: levelDetection.c levelDetection.h
	gcc -c -Wall -Wextra levelDetection.c

clean:
	rm -f ../bin/levelDetection levelDetection.o

