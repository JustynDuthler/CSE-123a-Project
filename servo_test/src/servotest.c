/*********************************
 * Team 7
 * 
 * servotest.c
 *
 * Description:
 * This source file contains the code
 * that tests servos one at a time

**********************************/
#include <stdlib.h>
#include <stdio.h>
#include <pigpio.h>
#include <unistd.h>

int main() {

   
    if (gpioInitialise() < 0) {
        exit(EXIT_FAILURE);
    }
    gpioSetMode(25, PI_OUTPUT);
   
    gpioSetPWMfrequency(25,50);
	gpioSetPWMrange(25,20000);
		
	
	
	gpioPWM(25, 1500);
	
	for(;;){
		
		
		
			gpioPWM(25, 2500);
			gpioDelay(3000000);
			gpioPWM(25, 500);
			gpioDelay(3000000);
		
	}
    
    
    
return EXIT_SUCCESS;
}   
