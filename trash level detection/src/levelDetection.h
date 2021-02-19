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
 * int initSensors()
 * 
 * INPUTS:
 *  void
 * 
 * OUTPUTS:
 *  int initSensors: 1 if no issues 
 *  initilizing sensors, 0 if any 
 *  issues occured
 * 
 * DESCRIPTION:
 *  This function initilizes the GPIO
 *  on the pi and sets up the trigger
 *  and echo pins for the 3 ultrasonic
 *  sensors
 * 
*********************************/
int initSensors(void);

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