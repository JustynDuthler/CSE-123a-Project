
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


def get_image_from_camera(camera):
    """Read an image from the camera"""
    if camera:
        ret, frame = camera.read()
        if not ret:
            raise Exception("your capture device is not returning images")
        return frame
    return None


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

        image2 = get_image_from_camera(camera)

    

        image2 = cv2.resize(image2, (10, 10))

        time.sleep(1)

        motion = 0

    
        while (cv2.waitKey(1) & 0xFF) == 0xFF and motion < 3:

            image1 = get_image_from_camera(camera)
            image1 = cv2.resize(image1, (10, 10))
        
        
            difference = cv2.subtract(image1, image2)
            b, g, r = cv2.split(difference)

            if cv2.countNonZero(b) < 60 and cv2.countNonZero(g) < 60 and cv2.countNonZero(r) < 60:
                print("motion not detected")
                motion = 0
            else :
                print("motion detected")
                motion = motion + 1

        
        	
            time.sleep(1)

            image2 = get_image_from_camera(camera)
            image2 = cv2.resize(image2, (10, 10))


        # Get an image from the camera.
        image = get_image_from_camera(camera)

        resized_img = cv2.resize(image, (img_height, img_width))

        # Display the image
        #cv2.imshow("SimpleSort", image)

        X = np.array(resized_img)
        X = X / 255

        # increases dimension by 1
        X = tf.expand_dims(X, 0) # Create a batch
    

        model = tf.keras.models.load_model('saved-model/model')

        prediction = model.predict(X)
        score = tf.nn.softmax(prediction[0])

        #class_names = ["cardboard", "compost", "glass", "metal", "paper", "plastic", "trash"]

        #print(
        #    "This image most likely belongs to {} with a {:.2f} percent confidence."
        #    .format(class_names[np.argmax(score)], 100 * np.max(score))
        #)
   
        cat = np.argmax(score)

        if cat == 0 or cat == 2 or cat == 3 or cat == 4 or cat == 5:
            print("recycle, gpio 4")
            pin4.on()
            pin5.off()
            time.sleep(2)

        elif cat == 1:
            print("compost, gpio 5")
            pin4.off()
            pin5.on()
            time.sleep(2)

        elif cat == 6:
            print("trash, gpio 4 & gpio 5")
            pin4.on()
            pin5.on()
            time.sleep(2)
        
    
   

if __name__ == "__main__":
    main()
