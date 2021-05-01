/*********************************
 * Team 7
 *
 * levelDetection.h
 *
 * Description:
 * This header file contains the
 * functions used within 
 * levelDetection.c. Each function
 * is given a description of its 
 * inputs, outputs, and what it 
 * does
 *
*********************************/

/*********************************
 * int initHardware()
 * 
 * INPUTS:
 *  void
 * 
 * OUTPUTS:
 *  int initHardware: 1 if no issues 
 *  initilizing sensors, 0 if any 
 *  issues occured
 * 
 * DESCRIPTION:
 *  This function initilizes the GPIO
 *  on the pi and sets up the trigger
 *  and echo pins for the 3 ultrasonic
 *  sensors and the LED pins. It sets
 *  the LED values to initially off.
 * 
*********************************/
int initHardware(void);

/*********************************
 * calculateDistance()
 * 
 * INPUTS:
 *  int trigPin: pin number which the
 *  trigger pin is connected to 
 *  int echoPin : pin number which the
 *  echo pin is connected to
 * OUTPUTS:
 *  int distance: distance in cm from
 *  the ultrasonic sensor
 * 
 * DESCRIPTION:
 *  This function calculates the distance
 *  the closests object is from the 
 *  ultrasonic sensor and returns it 
 *  as an integer in cm.
 * 
*********************************/
int calculateDistance(int trigPin, int echoPin);

/*********************************
 * ledLogic()
 * 
 * INPUTS:
 *  int sensor1Dist: measurement of sensor
 *  1
 *  int sensor2Dist: measurement of sensor
 *  2
 *  int sensor3Dist: measurement of sensor 
 *  3
 * OUTPUTS:
 *  void
 * 
 * DESCRIPTION:
 *  This function turns on the LEDs if the
 *  corresponding measurement is less than 15cm
 * 
*********************************/
void ledLogic(int sensor1Dist, int sensor2Dist, int sensor3Dist);

