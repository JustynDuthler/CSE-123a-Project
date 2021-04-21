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

#define topServo 17
#define leftServo 27
#define rightServo 22

int main() {

   
    if (gpioInitialise() < 0) {
        exit(EXIT_FAILURE);
    }
    gpioSetMode(topServo, PI_OUTPUT); 
    gpioSetMode(leftServo, PI_OUTPUT); 
    gpioSetMode(rightServo, PI_OUTPUT); 
    char c;
    gpioSetPWMfrequency(topServo,50);
	gpioSetPWMrange(topServo,20000);
		
	gpioSetPWMfrequency(leftServo,50);
	gpioSetPWMrange(leftServo,20000);
	
	gpioSetPWMfrequency(rightServo,50);
	gpioSetPWMrange(rightServo,20000);
	
	gpioPWM(topServo, 1500);
	gpioPWM(leftServo, 1900);
	gpioPWM(rightServo, 500);
	
	for(;;){
		printf("Enter:\n't' for trash\n'r' for recycling\n'c' for compost\n'd' to lower the tray\n'u' to raise the tray\n");
		c = getchar();
		getchar();
		
		
		if (c=='t'){
			printf("trash pwm speed \n");
			gpioDelay(1000000);
			gpioPWM(leftServo,1100);  // was 500
			gpioPWM(rightServo,1300); // was 1900
			gpioDelay(2000000);
			gpioPWM(leftServo,1900);
			gpioPWM(rightServo,500);
			gpioDelay(1000000);	
		}if (c=='r'){
			printf("recycle pwm speed \n");
			gpioPWM(topServo, 2388);
			gpioDelay(1000000);
			gpioPWM(leftServo,1100);
			gpioPWM(rightServo,1300);
			gpioDelay(2000000);
			gpioPWM(leftServo,1900);
			gpioPWM(rightServo,500);
			gpioDelay(1000000);
			gpioPWM(topServo, 1500);
		}if (c=='c'){
			printf("compost pwm speed \n");
			gpioPWM(topServo, 612);
			gpioDelay(1000000);
			gpioPWM(leftServo,1100);
			gpioPWM(rightServo,1300);
			gpioDelay(2000000);
			gpioPWM(leftServo,1900);
			gpioPWM(rightServo,500);
			gpioDelay(1000000);
			gpioPWM(topServo, 1500);	
		}if (c=='d'){
			printf("lower tray mode\n");
			gpioPWM(leftServo,1100);
			gpioPWM(rightServo,1300);
			gpioDelay(2000000);
		}if (c=='u'){
			printf("raise tray mode\n");
			gpioPWM(leftServo,1900);
			gpioPWM(rightServo,500);
		}
		
		c='n';
	}
    
    
    
return EXIT_SUCCESS;
}    
