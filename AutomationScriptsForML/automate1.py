
###############################################################################################################################
#    Automate1 wrapper class for loading and visuzlizing csv data sets                                                        #
###############################################################################################################################

## loading Dependencies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import sklearn
import sys
import os
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


## defining dataloader Class
class DataLoader():

  ##class members
  mDataFrame = ''
  mEnteries  = 0
  mFeaturesRequired = []
  mFeaturesNeedMapping = []
  mIsTrainFrame = False
  mIsMappingDoneYet = False
  mTarget = []
  mCopyofOriginalDataFrame = ''

  ## Constructor
  ## the constructor load dataFrame
  ## As well as Creates a Copy for future
  ## use
  def __init__(self, path = '', isTrainFrame = False):
    self.mDataFrame = pd.read_csv(path)
    self.mEnteries = len (self.mDataFrame)
    self.mCopyofOriginalDataFrame = self.mDataFrame
    self.mIsTrainFrame = isTrainFrame
  
  ## display Function for DataFrame
  def DisplayData(self, start = 0, end = -1):
    return (self.mDataFrame[start : end ])
  
  ## Describing the dataFrame
  def DescribeTheFrame (self):
    return (self.mDataFrame.describe())

  ## Function for getting info on dataTypes
  def FrameInfo(self):
    return (self.mDataFrame.info())
  
  ## function For retruning columns of dataFrame
  def Columns(self):
    return  list (self.mDataFrame.columns)

  ## FirstInsight Function returns the histogram for the given frame
  def FirstInsight(self, width = 10 , height = 10):
    fig = plt.figure(figsize = (width, height))
    ax = fig.gca()
    self.mDataFrame.hist(ax = ax)
    plt.show()

  ## function for interpolating nan values
  ## using forward fill functionality of pandas
  def InterPolateNanValues(self):
    self.mDataFrame = self.mDataFrame.fillna(method='ffill')
    print('And with that Nan Values went away ...........')

  ## Function for setting required features for training
  def SetTrainingAndMappingFeatures(self, trainingFeatures, MappingFeatures, target):
    if len(trainingFeatures) == 0:
      print ('Select atleast one Feature.......')
      return

    self.mFeaturesRequired = trainingFeatures
    self.mFeaturesNeedMapping = MappingFeatures
    
    if self.mIsTrainFrame == True:
      self.mTarget = np.array(self.mDataFrame[target], dtype = 'float32')
    
  
  ## Now the following function has working modes
  ## a.) maps only the object data to numeric values
  ## b.) map both object data along with a given dataFrame
  def MultiModeMapper (self, mode = 'single', otherFrame = []):
    
    ## choosing the selected features from the dataFrame
    self.mDataFrame = self.mDataFrame[self.mFeaturesRequired]
    if mode != 'single':
      otherFrame = otherFrame[self.mFeaturesRequired]
    
    for member in self.mFeaturesNeedMapping:
      uset = set (self.mDataFrame[member])
      umap = {}
      i = 0

      for mem in uset:
        umap[mem] = i
        i += 1
      
      self.mDataFrame[member] = self.mDataFrame[member].map(umap)
      if mode != 'single':
        otherFrame[member] = otherFrame[member].map(umap)
      
    
    if mode != 'single':
      return otherFrame
    else:
      print ('Done..... but do A sanity Check')
    
  ## Function 2D visualization of dataSet
  ## afterPCAClustering and returns data along
  ## axes that has most varience
  def VisualizeData2D (self):
    pca = PCA(n_components = 2 )
    data = np.array(self.mDataFrame, dtype = 'float32')
    stdsc = StandardScaler()
    data = stdsc.fit_transform(data) 
    pca.fit(data)
    transformedFeatures = pca.transform(data)

    ## lets make this a dataFrame
    dimReducedDataFrame = pd.DataFrame(transformedFeatures)
    dimReducedDataFrame = dimReducedDataFrame.rename(columns = { 0: 'V1', 1 : 'V2'})
    dimReducedDataFrame['Target'] = self.mTarget

    ## Plotting this
    plt.figure(figsize = (10, 5))
    sb.scatterplot(data = dimReducedDataFrame, x = 'V1', y = 'V2',hue = 'Target')
    plt.grid(True)
    plt.show()

    return data

