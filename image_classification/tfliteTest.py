import numpy as np
import tensorflow as tf
import cv2
import pathlib

# # Load TFLite model and allocate tensors.
# interpreter = tf.lite.Interpreter(model_path="model.tflite")
# interpreter.allocate_tensors()

# # Get input and output tensors.
# input_details = interpreter.get_input_details()
# output_details = interpreter.get_output_details()

# # input details
# print(input_details)
# # output details
# print(output_details)

# # Test model on random input data.
# input_shape = input_details[0]['shape']
# input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
# interpreter.set_tensor(input_details[0]['index'], input_data)

# interpreter.invoke()

# # The function `get_tensor()` returns a copy of the tensor data.
# # Use `tensor()` in order to get a pointer to the tensor.
# output_data = interpreter.get_tensor(output_details[0]['index'])
# print(output_data)

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

folder_path = 'c:/Users/shirl/OneDrive/Desktop/compostnet-dataset-Extra-Food/testphotos'

for file in pathlib.Path(folder_path).iterdir():
    
    # read and resize the image
    img = cv2.imread(r"{}".format(file.resolve()))
    new_img = cv2.resize(img, (224, 224))
    
    # input_details[0]['index'] = the index which accepts the input
    interpreter.set_tensor(input_details[0]['index'], [new_img])
    
    # run the inference
    interpreter.invoke()
    
    # output_details[0]['index'] = the index which provides the input
    output_data = interpreter.get_tensor(output_details[0]['index'])
    
    print("For file {}, the output is {}".format(file.stem, output_data))