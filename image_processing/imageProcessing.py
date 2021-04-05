#!/usr/bin/env python3
###############################################################################
#
#  Project:  Embedded Learning Library (ELL)
#  File:     tutorial.py
#  Authors:  Byron Changuion
#
#  Requires: Python 3.x
#
###############################################################################

import time
import cv2

# Import helper functions
import tutorial_helpers as helpers

# Import the Python wrapper for the ELL model
import model


def get_image_from_camera(camera):
    """Read an image from the camera"""
    if camera:
        ret, frame = camera.read()
        if not ret:
            raise Exception("your capture device is not returning images")
        return frame
    return None


def main():
    # Open the video camera. To use a different camera, change the camera
    # index.
    camera = cv2.VideoCapture(0)

    
    while (cv2.waitKey(1) & 0xFF) == 0xFF:
        # Get an image from the camera.
        image = get_image_from_camera(camera)

        

        # Display the image
        cv2.imshow("SimpleSort", image)

   

if __name__ == "__main__":
    main()
