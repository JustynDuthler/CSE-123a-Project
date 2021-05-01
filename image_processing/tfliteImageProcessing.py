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
            raise Exception("your capture device ius not returning images")
        return frame
    return None

def main():
    pi1 = pigpio.pi()
    pi1.write(4, 0)
    pi1.write(5, 0)

    camera = cv2.VideoCapture(0)

    img_height = 224
    img_width = 224

    while (cv2.waitKey(1) & 0xFF) == 0xFF:
        image = get_image_from_camera(camera)
        cv2.imshow("SimpleSort: Press any key to take a picture", image)

    image = get_image_from_camera(camera)

    # taken from tfliteTest
    interpreter = tf.lite.Interpreter(model_path="model.tflite")

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.allocate_tensors()

    resized_img = cv2.resize(image, (img_height, img_width))

    # display the image
    cv2.imshow("SimpleSort", image)

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
        pi1.write(4, 1)
    elif num == 1:
        print("compost, gpio5")
        pi1.write(5, 1)
    elif num == 6:
        print("trash, gpio 4 & gpio 5")
        pi1.write(4, 1)
        pi1.write(5, 1)

if __name__ == "__main__":
    main()


