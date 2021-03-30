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

# path to dataset and printing out number of images
data_dir = Path('/home/justynduthler/Desktop/CSE-123a-Project/image_classification/compostnet-dataset-resized')
PATH = os.path.join(os.path.dirname(data_dir), 'compostnet-dataset-resized')
image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

# define batch size and image dimensions for training
batch_size = 32
img_size = (160, 160)

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

prediction_layer = tf.keras.layers.Dense(num_classes)
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
