import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pickle
import time

data_dir = 'flowers'
CATEGORIES = [catname for catname in os.listdir(data_dir)]
data = []

# def transform_data():
#     for category in CATEGORIES:
#         path = os.path.join(data_dir, category)
#         label = CATEGORIES.index(category)

#         for img_name in os.listdir(path):
#             image_path = os.path.join(path, img_name)
#             image = cv2.imread(image_path)
    
#             try:
#                 image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#                 image = cv2.resize(image, (224, 224))
#                 image = np.array(image, dtype = np.float32)
#                 data.append([image, label])
#             except Exception as e:
#                 pass
#     pik = open('transformed_data.pickle', 'wb')
#     pickle.dump(data, pik)
#     pik.close()

# transform_data()

def load_data():
    pik = open('transformed_data.pickle', 'rb')
    data = pickle.load(pik)
    pik.close()

    np.random.shuffle(data)
    features = []
    labels = []
    
    for img, label in data:
        features.append(img)
        labels.append(label)
    
    features = np.array(features, dtype = np.float32)
    labels = np.array(labels)

    features = features/255.0

    return [features, labels]