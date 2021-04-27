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
#define sensor3Echo 25
#define led1Pin	    13
#define led2Pin     19
#define led3Pin     26

int initHardware(void)
{
    if (gpioInitialise() < 0) {
        return 0;
    }
    // init Sensor pins
    gpioSetMode(trigger, PI_OUTPUT); // Trigger
    gpioSetMode(sensor1Echo, PI_INPUT); 
    gpioSetMode(sensor2Echo, PI_INPUT); 
    gpioSetMode(sensor3Echo, PI_INPUT);
    // init LED pin
    gpioSetMode(led1Pin, PI_OUTPUT);
    gpioSetMode(led2Pin, PI_OUTPUT);    
    gpioSetMode(led3Pin, PI_OUTPUT);
    // turn LEDs off (2 of the LEDs are common anode (2,3) 1 is not)
    gpioWrite(led1Pin, 1);
    gpioWrite(led2Pin, 1);
    gpioWrite(led3Pin, 0);    
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
    printf("Waiting on Pin: %d\n", echoPin);
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

void ledLogic(int sensor1Dist, int sensor2Dist, int sensor3Dist) {
    if (sensor1Dist < 15) {
	gpioWrite(led1Pin, 0);	
    } else { gpioWrite(led1Pin, 1); } 
    if (sensor2Dist < 15) {
        gpioWrite(led2Pin, 0);   
    } else { gpioWrite(led2Pin, 1); }
    if (sensor3Dist < 15) {
        gpioWrite(led3Pin, 1); // not common anode, if using common anode change to 0
    } else { gpioWrite(led3Pin, 0); }
}
