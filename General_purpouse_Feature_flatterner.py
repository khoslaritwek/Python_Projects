import os
import sys
import numpy as np
import sklearn
import matplotlib.pyplot as pl
import cv2
import pandas as pd

def WriteToCsv(object_):
    object_.to_csv('./proccessedData.csv')
    print('i was called')

    
def ConvertMapToDataFrame(map_):
    return pd.DataFrame(map_)

def GiveMeFlattenImage(path, h, w):
    img = cv2.imread(path, 0)
    img = cv2.resize(img,(h,w))
    img1 = img.flatten()
    img1 = img1 / 255
    return img1

DataFrame = {
    'photo_name' : [],
    'flattenPhoto' : []

    }

def ReadAndStoreMyImages(path):
    list_ = os.listdir(path)

    for mem in list_:
        DataFrame['photo_name'].append(mem)
        imagePath = path + '//' + mem
        DataFrame['flattenPhoto'].append(GiveMeFlattenImage(imagePath,100,100))
    

def main():
    path = 'C:\\Users\\Dell\\Desktop\\data_to_analyze\\Dataset'
    source = path + '\\Test Data'
    ReadAndStoreMyImages(source)
    newDataFrame = ConvertMapToDataFrame(DataFrame)
    print(os.getcwd())
    newDataFrame.to_csv('./dataSetPrime.csv')
    return newDataFrame









main()

Training_Feature_vector = np.array(DataFrame['flattenPhoto'], dtype = 'float64')
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3)
kmeans.fit(Training_Feature_vector)
