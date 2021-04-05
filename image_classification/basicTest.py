import PIL
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
import cv2

img_height = 224
img_width = 224

data_dir = Path('/home/justynduthler/Desktop/CSE-123a-Project/image_classification/test-images/lem.jpg')
img = cv2.imread(str(data_dir))
resized_img = cv2.resize(img, (img_height, img_width))
print(resized_img.shape)

X = np.array(resized_img)
X = X / 255

# increases dimension by 1
X = tf.expand_dims(X, 0) # Create a batch
print(X.shape)

model = tf.keras.models.load_model('saved-model/model')

prediction = model.predict(X)
score = tf.nn.softmax(prediction[0])

class_names = ["cardboard", "compost", "glass", "metal", "paper", "plastic", "trash"]

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)

""" 
# basic banana peel test
ban_path = Path('/home/justynduthler/Desktop/CSE-123a-Project/image_classification/ban.jpg')
img = tf.keras.preprocessing.image.load_img(ban_path, target_size=(160, 160))
img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "This banana image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
) 

# basic can test
can_path = Path('/home/justynduthler/Desktop/CSE-123a-Project/image_classification/can.jpg')
img = tf.keras.preprocessing.image.load_img(can_path, target_size=(160, 160))
img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "This can image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)  
# basic bag test
bag_path = Path('/home/justynduthler/Desktop/CSE-123a-Project/image_classification/bag.jpg')
img = tf.keras.preprocessing.image.load_img(bag_path, target_size=(160, 160))
img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "This bag image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
) """

