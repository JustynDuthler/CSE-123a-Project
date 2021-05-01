
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
    pin4.off()
    pin5.off()

    # Open the video camera. To use a different camera, change the camera
    # index.
    camera = cv2.VideoCapture(0)

    img_height = 224
    img_width = 224


    #show camera and prompt to take picture
    while (cv2.waitKey(1) & 0xFF) == 0xFF:

        image = get_image_from_camera(camera)
        cv2.imshow("SimpleSort: press any key to take picture", image)

    # Get an image from the camera.
    image = get_image_from_camera(camera)

    resized_img = cv2.resize(image, (img_height, img_width))

    # Display the image
    cv2.imshow("SimpleSort", image)

    X = np.array(resized_img)
    X = X / 255

    # increases dimension by 1
    X = tf.expand_dims(X, 0) # Create a batch
    #print(X.shape)

    model = tf.keras.models.load_model('saved-model/model')

    prediction = model.predict(X)
    score = tf.nn.softmax(prediction[0])

    class_names = ["cardboard", "compost", "glass", "metal", "paper", "plastic", "trash"]

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )
   
    cat = np.argmax(score)

    if cat == 0 or cat == 2 or cat == 3 or cat == 4 or cat == 5:
        print("recycle, gpio 4")
        pin4.on()
        pin5.off()

    elif cat == 1:
        print("compost, gpio 5")
        pin4.off()
        pin5.on()

    elif cat == 6:
        print("trash, gpio 4 & gpio 5")
        pin4.on()
        pin5.on()
        

if __name__ == "__main__":
    main()
