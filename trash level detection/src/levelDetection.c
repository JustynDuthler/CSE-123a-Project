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
#include "levelDetection.h"

#define trigger     21
#define sensor1Echo 20
#define sensor2Echo 16
#define sensor3Echo 26

int main() 
{
    if (initSensors() == 0) {
        printf("pigpio cannot initialise gpio\nRestart Program\n");
        exit(EXIT_FAILURE);
    }
    int sensor1Dist, sensor2Dist, sensor3Dist;
    for (;;) {
        sensor1Dist = calculateDistance(trigger, sensor1Echo);
	sensor2Dist = calculateDistance(trigger, sensor2Echo);
	sensor3Dist = calculateDistance(trigger, sensor3Echo);

	
        printf("Sensor 1 Distance = %d\nSensor 2 Distance: %d\nSensor 3 Distance: %d\n", sensor1Dist, sensor2Dist, sensor3Dist);
        time_sleep(1);
    }
    
    return EXIT_SUCCESS;
}

int initSensors(void)
{
    if (gpioInitialise() < 0) {
        return 0;
    }
    gpioSetMode(trigger, PI_OUTPUT); // Trigger
    gpioSetMode(sensor1Echo, PI_INPUT); 
    gpioSetMode(sensor2Echo, PI_INPUT); 
    gpioSetMode(sensor3Echo, PI_INPUT);

    // settle trigger pin
    gpioWrite(21, 0);
    return 1;
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
    long startTimeM = (startTime.tv_sec * 1000000)  + startTime.tv_usec;
    long stopTimeM = (stopTime.tv_sec * 1000000) + stopTime.tv_usec;
    long timeDiff = stopTimeM - startTimeM;
    int distance = timeDiff / 58;
    return distance;
}
