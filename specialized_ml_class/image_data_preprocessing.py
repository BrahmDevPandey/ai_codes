# -*- coding: utf-8 -*-
"""image_data_preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ja5T7TwzN4sfJBX0CIzsG6peix3pOe5b
"""

d = { 1: 2, 2: 3, 3: 4, 4: 5}
print(d)

# l = [y for x in d.keys() and (d[x] > 3)]
# print(l)

"""#**Focus on cleaning data: Data preprocessing**"""

!cd "/content"

ls

!wget "https://archive.ics.uci.edu/ml/machine-learning-databases/00389/DevanagariHandwrittenCharacterDataset.zip"



!unzip

!unzip ./Dev*

# finding the number of folders in train folder
import os
diff_folders = os.listdir("/content/DevanagariHandwrittenCharacterDataset/Train")
print(len(diff_folders))

path = "/content/DevanagariHandwrittenCharacterDataset/Train/"
for folder in diff_folders:
  print((os.listdir(path + folder)))

image_path = "/content/DevanagariHandwrittenCharacterDataset/Train/digit_9/86640.png"
print(image_path)

single_folder_path = path + diff_folders[0]
single_image_path = single_folder_path + "/" + os.listdir(single_folder_path)[0]
print(single_image_path)

# to show the iamge to the user
import matplotlib.pyplot as plt
img_np_array = plt.imread(single_image_path)  # convert the image into an np array

print(img_np_array)   # show the obtained np array

plt.imshow(img_np_array, cmap="gray")  # show the image using imshow()

!apt update

!apt upgrade

# my_path = "/content/modified pic.png"
# my_arr = plt.imread(my_path)
# plt.imshow(my_arr)

import numpy as np

# convert all the images into a dataset
base_path = "/content/DevanagariHandwrittenCharacterDataset/Train"
images_table = list()

for i in range(len(diff_folders)):
  single_folder_path = base_path + "/" + diff_folders[i]
  single_folder_images = os.listdir(single_folder_path)
  for image_name in single_folder_images:
    single_image_path = single_folder_path + "/" + image_name
    img_np_array = plt.imread(single_image_path)
    reshaped_img_np_array = np.reshape(img_np_array, newshape=(1024,))
    images_table.append(reshaped_img_np_array)

print(len(images_table))

input_features = np.array(images_table)  # this will work as input features
print(input_features.shape)
plt.imshow(input_features)

answers = list()   # to create the answers
for folder_name in diff_folders:
  answers.extend([folder_name]*1700)

len(answers)

answers = np.array(answers)   # convert it into an np array

import pandas as pd

# creating column names
columns_name = list()

for pixel_number in range(1, 1025):
  columns_name.append("Pixel#"+str(pixel_number))   # append each name to the list

training_data_df = pd.DataFrame(data=input_features, columns=columns_name)
training_data_df["image_label"] = answers
training_data_df

training_data_df.to_csv("./Devnagari_Handwritten_Characters_Train.csv")   # save data to a csv file

training_data_df.to_csv("/content/drive/MyDrive/Devnagari_Handwritten_Characters_Train.csv")   # save a copy in my drive

# training on the dataset
from sklearn.linear_model import LogisticRegression
logistic_regression_algo = LogisticRegression(max_iter=2000)
logistic_regression_algo.fit(X=input_features, y=answers)

# now perform the testing by preparing a dataset of the testing features
test_base_path = "/content/DevanagariHandwrittenCharacterDataset/Test"
test_folders = os.listdir(test_base_path)
# an array to store all the images data
test_images_table = list()

for folder_name in test_folders:
  test_subfolders_path = test_base_path + "/" + folder_name
  print(len(os.listdir(test_subfolders_path)))
  for image_name in os.listdir(test_subfolders_path):
    image_path = test_subfolders_path + "/" + image_name
    test_img_np_array = plt.imread(image_path)
    reshaped_test_img_np_array = np.reshape(test_img_np_array, newshape=(1024,))
    test_images_table.append(reshaped_test_img_np_array)  # append the final reshaped array to the table

# creating the test input features using an np array
test_input_features = np.array(test_images_table)
print(test_input_features.shape)

# the real answers of test data
test_answers = list()
for folder_name in test_folders:
  test_answers.extend([folder_name]*300)
# convert test answers list to an np array
test_answers = np.array(test_answers)

exam_answers = logistic_regression_algo.predict(test_input_features)

from sklearn.metrics import classification_report
report = classification_report(y_true=test_answers, y_pred=exam_answers)
print(report)