
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

    image = get_image_from_camera(camera)


    #show camera and prompt to take picture
    while (cv2.waitKey(1) & 0xFF) == 0xFF:

        image = get_image_from_camera(camera)
        cv2.imshow("SimpleSort: press any key to take picture", image)



    
   

if __name__ == "__main__":
    main()
