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

int main() {


    printf("Flickering LED\n");
    if (gpioInitialise() < 0) {
        exit(EXIT_FAILURE);
    }
    gpioSetMode(26, PI_OUTPUT);
    for(;;) {
	time_sleep(1);
        gpioWrite(26,0);
	time_sleep(1);
	gpioWrite(26,1);
    }




    return EXIT_SUCCESS;
}
