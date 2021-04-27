import numpy as np
import tensorflow as tf
import cv2
import pathlib

# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="model.tflite")

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

interpreter.allocate_tensors()

# input details
print(input_details)
# output details
print(output_details)

print(interpreter.get_input_details())

# this is the folder for all of the test images
folder_path = 'c:/Users/shirl/OneDrive/Desktop/compostnet-dataset-Extra-Food/testphotos'

for file in pathlib.Path(folder_path).iterdir():
    
    # read and resize the image
    img = cv2.imread(r"{}".format(file.resolve()))
    new_img = cv2.resize(img, (224, 224))

    # change dtype to float32 and decrease dimension
    new_img = np.asarray(new_img, dtype='float32')
    new_img /= 255.0
    tf.shape(tf.squeeze(new_img))

    print(new_img.shape)

    # input_details[0]['index'] = the index which accepts the input
    interpreter.set_tensor(input_details[0]['index'], [new_img])
    
    # run the inference
    interpreter.invoke()
    
    # output_details[0]['index'] = the index which provides the input
    output_data = interpreter.get_tensor(output_details[0]['index'])
    
    # this prints 7 numbers and the highest one is the classification result
    # order of numbers: cardboard, compost, glass, metal, paper, plastic, trash
    print("For file {}, the output is {}".format(file.stem, output_data))