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
    char c;
 
	for(;;){
		printf("Enter t r or c:");
		c = getchar();
		getchar();
		
		if (c=='t'){
			printf("trash pwm speed \n");
			gpioPWM(25, 255);		
		}if (c=='r'){
			printf("recycle pwm speed \n");
			gpioPWM(25, 128);
		}if (c=='c'){
			printf("compost pwm speed \n");
			gpioPWM(25, 0);
		}
	}
    
    
return EXIT_SUCCESS;
}    
