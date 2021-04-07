
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

import pigpio


def get_image_from_camera(camera):
    """Read an image from the camera"""
    if camera:
        ret, frame = camera.read()
        if not ret:
            raise Exception("your capture device is not returning images")
        return frame
    return None


def main():

    pi1 = pigpio.pi() #create instance of pigpio.pi class

    # Open the video camera. To use a different camera, change the camera
    # index.
    camera = cv2.VideoCapture(0)

    image2 = get_image_from_camera(camera)

    cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    time.sleep(1)

    threshold=25

    #show camera and prompt to take picture
    while (cv2.waitKey(1) & 0xFF) == 0xFF:

        image1 = get_image_from_camera(camera)

        cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        
        #find absolute difference
        diff = cv2.absdiff(image1, image2);

        #get threshold to get foreground
        thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]

        #get contours
        (_, cnts, _) = cv2.findContours(thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # return None, if no contours detected
        if len(cnts) == 0:
            print("no motion")
        else:
            #
            print("motion detected")
        	
        time.sleep(1)

        image2 = get_image_from_camera(camera)

        cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    
   

if __name__ == "__main__":
    main()
