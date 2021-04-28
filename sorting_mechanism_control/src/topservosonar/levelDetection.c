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
 * level. Red = >90%.
 *
**********************************/
#include <stdlib.h>
#include <stdio.h>
#include <pigpio.h>
#include <unistd.h>
#include <sys/time.h>
#include "levelDetection.h"

int initHardware(void)
{
    if (gpioInitialise() < 0) {
        return 0;
    }
    // init Sensor pins
    gpioSetMode(trigger, PI_OUTPUT);
    gpioSetMode(sensorEcho, PI_INPUT); 
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

void ledLogic(int sensorDist, char compartment) {
    if (sensorDist < 20) { // turn on led
        if (compartment == 't') {
	    gpioWrite(led1Pin, 0);
	} else if (compartment == 'r') {
	    gpioWrite(led2Pin, 0);
	} else {
            gpioWrite(led3Pin, 1); // not common anode, if using command anode change to 1
	}
    } else { // turn off led 
        if (compartment == 't') {
	    gpioWrite(led1Pin, 1);
	} else if (compartment == 'r') {
	    gpioWrite(led2Pin, 1);
	} else {
            gpioWrite(led3Pin, 0); // not common anode, if using command anode change to 1
	}
    }
}

