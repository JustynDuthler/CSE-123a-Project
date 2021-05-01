
###############################################################################

import time
import cv2


import PIL
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
import cv2

import gpiozero
from gpiozero import LED
from gpiozero import Button


def get_image_from_camera(camera):
    """Read an image from the camera"""
    if camera:
        ret, frame = camera.read()
        if not ret:
            raise Exception("your capture device is not returning images")
        return frame
    return None

trigger = LED(18)
echo = BUTTON(23)


def distance():
    # set trigger
    trigger.on()
 
    # set trigger for 10 us
    time.sleep(0.00001)
    trigger.off()
 
    start = time.time()
    stop = time.time()
 
    # start timer
    while not echo.is_pressed:
        start = time.time()
 
    # stop timer
    while echo.is_pressed:
        stop = time.time()
 
    # elapsed time
    time = stop - start
    # distance in cm
    distance = time / 58
 
    return distance

def main():

    pin4 = LED(4)
    pin5 = LED(5)

    # Open the video camera. To use a different camera, change the camera
    # index.
    camera = cv2.VideoCapture(0)

    while True: 
        
        pin4.off()
        pin5.off()

        img_height = 224
        img_width = 224

        #detect object within 13 cm
        distance = distance()

        print("waiting for trash")

        while distance > 13:

            distance = distance();

            time.sleep(0.06)

        print("trash detected")    


        # Get an image from the camera.
        image = get_image_from_camera(camera)

        # taken from tfliteTest
        interpreter = tf.lite.Interpreter(model_path="model.tflite")

        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        interpreter.allocate_tensors()

        resized_img = cv2.resize(image, (img_height, img_width))

        

        resized_img = np.asarray(resized_img, dtype='float32')
        resized_img /= 255.0
        tf.shape(tf.squeeze(resized_img))

        interpreter.set_tensor(input_details[0]['index'], [resized_img])

        interpreter.invoke()

        output_data = interpreter.get_tensor(output_details[0]['index'])

        print("The output is {}".format(output_data))

        max = np.max(output_data)
        print(max)

        num = np.argmax(output_data)
    
        if num == 0 or num == 2 or num == 3 or num == 4 or num == 5 or num == 5:
            print("recycle, gpio 4")
            pin4.on()
            pin5.off()
            time.sleep(2)

        elif num == 1:
            print("compost, gpio5")
            pin4.off()
            pin5.on()
            time.sleep(2)
        elif num == 6:
            print("trash, gpio 4 & gpio 5")
            pin4.on()
            pin5.on()
            time.sleep(2)
    
        #wait for sorting to finish
        print("waiting for sorting to finish")    
        time.sleep(2)
   

if __name__ == "__main__":
    main()
