/*********************************
 * Team 7
 * 
 * levelDetection.c
 *
 * Description:
 * This source file contains the code
 * that implements the level detection
 * for how much trash is in each bin
 * and sets the corresponding LEDS
 * to a color that matches the trash
 * level. Green = <25% Yellow = <75%
 * Red = >90%.
 *
**********************************/
#include <stdlib.h>
#include <stdio.h>
#include <pigpio.h>
#include <unistd.h>
#include <sys/time.h>
int main() 
{
    if (initSensors() == 0) {
        printf("pigpio cannot initialise gpio\nRestart Program\n");
        exit(EXIT_FAILURE);
    }
    int recycleDist;
    for (;;) {
        recycleDist = calculateDistance(21, 20);
        printf("Recycle Distance = %d\n", recycleDist);
        time_sleep(1);
    }
    
    return EXIT_SUCCESS;
}

int initSensors(void)
{
    if (gpioInitialise() < 0) {
        return 0;
    }
    gpioSetMode(21, PI_OUTPUT); // Trigger
    gpioSetMode(20, PI_INPUT);  // Echo
    // settle trigger pin
    gpioWrite(21, 0);
}

int calculateDistance(int trigPin, int echoPin)
{
    // generate trigger pulse 
    gpioWrite(trigPin, 1);
    gpioDelay(10);
    gpioWrite(trigPin, 0);
    // wait for echo pin to turn high
    struct timeval startTime, stopTime;
    while (gpioRead(echoPin) != 1) {
        gettimeofday(&startTime, NULL); // update start time
    };
    // wait for echo pin to turn low
    while(gpioRead(echoPin) != 0) {
        gettimeofday(&stopTime, NULL);
    }
    // convert time to microseconds;
    long startTimeM = (startTime.tv_sec + startTime.tv_usec) * 1000000;
    long stopTimeM = (stopTime.tv_sec + stopTime.tv_usec) * 1000000;
    long timeDiff = stopTimeM - startTimeM;
    int distance = timeDiff / 58;
    return distance;
}