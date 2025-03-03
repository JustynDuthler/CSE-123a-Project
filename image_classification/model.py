# Simple Sort
#
# Reference: https://www.tensorflow.org/tutorials/images/classification

import PIL
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory
import tensorflow_hub as hub
import cv2
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

# path to dataset and printing out number of images
data_dir = Path('/home/justynduthler/Desktop/CSE-123a-Project/image_classification/compostnet-dataset-resized')
image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

dataset_dict = {
  'cardboard': list(data_dir.glob('cardboard/*')),
  'compost': list(data_dir.glob('compost/*')),
  'glass' : list(data_dir.glob('glass/*')),
  'metal' : list(data_dir.glob('metal/*')),
  'paper' : list(data_dir.glob('paper/*')),
  'plastic': list(data_dir.glob('plastic/*')),
  'trash': list(data_dir.glob('trash/*')),
}

dataset_labels_dict = {
  'cardboard': 0,
  'compost': 1,
  'glass' : 2,
  'metal' : 3,
  'paper' : 4,
  'plastic': 5,
  'trash': 6,
}

print(dataset_dict['cardboard'][:5])
# define batch size and image dimensions for training
batch_size = 32
img_size = (224, 224)

X, y = [], []

for trash_name, images in dataset_dict.items():
    for image in images:
        img = cv2.imread(str(image))
        resized_img = cv2.resize(img,(224,224))
        X.append(resized_img)
        y.append(dataset_labels_dict[trash_name])

X = np.array(X)
y = np.array(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


X_train_scaled = X_train / 255
X_test_scaled = X_test / 255

feature_extractor_model = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"

pretrained_model_without_top_layer = hub.KerasLayer(
    feature_extractor_model, input_shape=(224, 224, 3), trainable=False)

num_of_classes = 7

model = tf.keras.Sequential([
  pretrained_model_without_top_layer,
  tf.keras.layers.Dense(num_of_classes)
])

model.summary()

model.compile(
  optimizer="adam",
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['acc'])

model.fit(X_train_scaled, y_train, epochs=8)

model.evaluate(X_test_scaled,y_test)

model.save('saved-model/model')

'''
# create training and validation sets from complete dataset
# create training and validation sets from complete dataset
train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  validation_split = 0.2,
  subset = "training",
  seed = 123,
  image_size = img_size,
  batch_size = batch_size)

train_dataset = image_dataset_from_directory(data_dir,
                                             shuffle=True,
                                             validation_split = 0.2,
                                             subset="training",
                                             seed = 123,
                                             batch_size=batch_size,
                                             image_size=img_size)

validation_dataset = image_dataset_from_directory(data_dir,
                                                  shuffle=True,
                                                  validation_split = 0.2,
                                                  subset="validation",
                                                  seed = 123,
                                                  batch_size=batch_size,
                                                  image_size=img_size)
# define the 3 class names: compost, recycling, trash
class_names = train_dataset.class_names
print(class_names)
# buffer image loading for faster training
AUTOTUNE = tf.data.AUTOTUNE
train_dataset = train_dataset.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
validation_dataset = validation_dataset.cache().prefetch(buffer_size=AUTOTUNE)

# process pixel values to fall within -1, 1 range
preprocess_input = tf.keras.applications.resnet_v2.preprocess_input

# define number of classes
num_classes = 3

# augment images to yeild more images for training
data_augmentation = tf.keras.Sequential([
  tf.keras.layers.experimental.preprocessing.RandomFlip('horizontal'),
  tf.keras.layers.experimental.preprocessing.RandomRotation(0.2),
  tf.keras.layers.experimental.preprocessing.RandomZoom(0.1),
])

IMG_SHAPE = img_size + (3,)
base_model = tf.keras.applications.ResNet50V2(input_shape=IMG_SHAPE,
                                               include_top=False,
                                               weights='imagenet')

image_batch, label_batch = next(iter(train_dataset))
feature_batch = base_model(image_batch)

# fine tune layers past 100
base_model.trainable = False

base_model.summary()

global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
feature_batch_average = global_average_layer(feature_batch)

prediction_layer = tf.keras.layers.Dense(num_classes, activation = "softmax")
prediction_batch = prediction_layer(feature_batch_average)

inputs = tf.keras.Input(shape=(160, 160, 3))
x = data_augmentation(inputs)
x = preprocess_input(x)
x = base_model(x, training=False)
x = global_average_layer(x)
x = tf.keras.layers.Dropout(0.2)(x)
outputs = prediction_layer(x)
model = tf.keras.Model(inputs, outputs)

base_learning_rate = 0.0001
model.compile(optimizer=tf.keras.optimizers.Adam(lr=base_learning_rate),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.summary()

# evaluate model without training
loss0, accuracy0 = model.evaluate(validation_dataset)
print("initial loss: {:.2f}".format(loss0))
print("initial accuracy: {:.2f}".format(accuracy0))

# train model for 10 epochs
epochs = 15
history = model.fit(train_dataset,
                    epochs=epochs,
                    validation_data=validation_dataset)


# print out model results
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

model.save('saved-model/model')
'''