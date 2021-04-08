
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

    #image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    time.sleep(1)

    threshold=25

    #show camera and prompt to take picture
    while (cv2.waitKey(1) & 0xFF) == 0xFF:

        image1 = get_image_from_camera(camera)

        #image1 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        
        difference = cv2.subtract(image1, image2)
        b, g, r = cv2.split(difference)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("motion not detected")
        else :
            print("motion detected")
        
        	
        time.sleep(1)

        image2 = get_image_from_camera(camera)

        #image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    
   

if __name__ == "__main__":
    main()
