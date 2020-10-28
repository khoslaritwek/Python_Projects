# -*- coding: utf-8 -*-
"""SolutionTo3rdProblem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hRGAUIvLnJgtcrsEsU42K_LBQdib-gD0
"""

from google.colab import files
files.upload()

!unzip dataBase-20201028T153957Z-001.zip

!ls

import numpy as np
import pandas as pd 
import os

###########################################################################
#   Notes:  I recently tackled such problem in a hackerearth deep learning #
# competition and am i sending you a modified version of that notebook     #
# The approach that i am using is Transerfer learning.                     #
# I am using Resnet50 without its head hence it can give me the features i #
# want upon this i can apply  kmeans / algomerative clusttering   with     #
# centres equals to the images present in the directory                    #
# after that its just a prediction to make                                 #
############################################################################

##################### Making Essential Imports ############################
import sklearn
import os
import sys
import matplotlib.pyplot as plt
import cv2
import numpy as np
import pandas as pd
import tensorflow as tf

#####################################
# Defining a skeleton for our       #
# DataFrame                         #
#####################################

DataFrame = {
    'photo_name' : [],
    'flattenPhoto' : [],
    }

#######################################################################################
#      The Approach is to apply transfer learning hence using Resnet50 as my          #
#      pretrained model                                                               #
#######################################################################################

MyModel = tf.keras.models.Sequential()
MyModel.add(tf.keras.applications.ResNet50(
    include_top = False, weights='imagenet',    pooling='avg',
))

# freezing weights for 1st layer
MyModel.layers[0].trainable = False

### Now defining dataloading Function
def LoadDataAndDoEssentials(path, h, w, returnVector):
    img = cv2.imread(path)
    img = cv2.resize(img, (h, w))
    ## Expanding image dims so this represents 1 sample
    img = img = np.expand_dims(img, 0)
    
    img = tf.keras.applications.resnet50.preprocess_input(img)
    extractedFeatures = MyModel.predict(img)
    extractedFeatures = np.array(extractedFeatures)

    if returnVector == False:
      DataFrame['flattenPhoto'].append(extractedFeatures.flatten())
    else:
      return extractedFeatures.flatten()

### with this all done lets write the iterrrative loop
def ReadAndStoreMyImages(path):
    list_ = os.listdir(path)

    for mem in list_:
        DataFrame['photo_name'].append(mem)
        imagePath = path + '/' + mem
        LoadDataAndDoEssentials(imagePath, 224, 224, False)

### lets give the address of our Parent directory and start
path = './dataBase'
ReadAndStoreMyImages(path)

######################################################
#        lets now do clustering                      #
######################################################

Training_Feature_vector = np.array(DataFrame['flattenPhoto'], dtype = 'float64')
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = len(os.listdir(path)) )
kmeans.fit(Training_Feature_vector)

predictions = kmeans.labels_

i = 0 
for mem in DataFrame['photo_name']:
  print ("Image Name: " + str(mem) + " Cluster centre: " + str(predictions[i]))
  i += 1

## let us now see which image is most familiar to query image
queryVector = LoadDataAndDoEssentials('querry.jpg', 224, 224, True)
kmeans.predict([queryVector])

## hence the from above cluster given querry is most similar to image-14
myAnswerImage = cv2.imread('dataBase/14.jpg')
querryImage = cv2.imread('querry.jpg')

import matplotlib.pyplot as plt
plt.figure(figsize =  (10, 10))

plt.subplot(1, 2, 1)
plt.imshow(querryImage)

plt.subplot(1,2, 2)
plt.imshow(myAnswerImage)