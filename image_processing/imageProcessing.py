
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

    img_height = 224
    img_width = 224

    #while (cv2.waitKey(1) & 0xFF) == 0xFF:
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
   

if __name__ == "__main__":
    main()
