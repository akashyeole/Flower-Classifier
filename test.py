from utils import load_data, CATEGORIES
import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import os

# (feature, labels) = load_data()

x_train, x_test, y_train, y_test = train_test_split(feature, labels, test_size = 0.1)


img_path = 'test.jpg'
image = cv2.imread(img_path)
image = cv2.resize(image, (224, 224))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
# image = image.reshape(224, 224, 3)
# image = np.array(image, dtype = np.float32)
# image = np.array(image, dtype = np.float32)
image = image / 255.0
img_batch = np.expand_dims(image, axis=0)
model = tf.keras.models.load_model('model.h5')
# model.evaluate(x_test, y_test, verbose = 1)

prediction = model.predict(img_batch)
print(max(prediction[0]) * 100)
plt.figure(figsize=(9,9))

plt.subplot(3, 3, 1)
plt.imshow(image)
plt.xlabel(CATEGORIES[np.argmax(prediction[0])])
plt.xticks([])

plt.show()