/*********************************
 * Team 7
 * 
 * topservo.c
 *
 * Description:
 * This source file contains the code
 * that controls the top servo that
 * rotates the intial compartment  
 * of the trashcan.

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
    gpioSetMode(23, PI_OUTPUT);
    gpioSetMode(24, PI_OUTPUT);
    char c;
    gpioSetPWMfrequency(25,50);
	gpioSetPWMrange(25,20000);
		
	gpioSetPWMfrequency(23,50);
	gpioSetPWMrange(23,20000);
	
	gpioSetPWMfrequency(24,50);
	gpioSetPWMrange(24,20000);
	
	gpioPWM(25, 1500);
	gpioPWM(23, 1900);
	gpioPWM(24, 500);
	
	for(;;){
		printf("Enter t r or c:");
		c = getchar();
		getchar();
		
		
		if (c=='t'){
			printf("trash pwm speed \n");
			gpioDelay(1000000);
			gpioPWM(23,500);
			gpioPWM(24,1900);
			gpioDelay(2000000);
			gpioPWM(23,1900);
			gpioPWM(24,500);
			gpioDelay(1000000);	
		}if (c=='r'){
			printf("recycle pwm speed \n");
			gpioPWM(25, 2388);
			gpioDelay(1000000);
			gpioPWM(23,500);
			gpioPWM(24,1900);
			gpioDelay(2000000);
			gpioPWM(23,1900);
			gpioPWM(24,500);
			gpioDelay(1000000);
			gpioPWM(25, 1500);
		}if (c=='c'){
			printf("compost pwm speed \n");
			gpioPWM(25, 612);
			gpioDelay(1000000);
			gpioPWM(23,500);
			gpioPWM(24,1900);
			gpioDelay(2000000);
			gpioPWM(23,1900);
			gpioPWM(24,500);
			gpioDelay(1000000);
			gpioPWM(25, 1500);
			
		}
		c='n';
	}
    
    
    
return EXIT_SUCCESS;
}    
