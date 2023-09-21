import cv2
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
import numpy as np
import os

person_name = input("Enter the name of the person: ")
folder_name = os.path.join('captured_images', person_name)

images = []
labels = []

img_height = 128
img_width = 128
num_classes = 1  #this is no. of people you want to identify

for filename in os.listdir(folder_name):
    if filename.endswith('.jpg'):
        img_path = os.path.join(folder_name, filename)
        img = cv2.imread(img_path)  
        img = cv2.resize(img, (img_width, img_height)) 
        img = img / 255.0  # Normalize pixel values to [0, 1]
        images.append(img)
        labels.append(person_name)  

images = np.array(images)
labels = np.array(labels)

X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)




