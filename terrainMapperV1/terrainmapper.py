
#################################################################
# Implementing a terrain mapper using segmentation model        #
# input size 128 * 128 * 3 ouput Size 128*128*1                 #
#################################################################


from google.colab import files
files.upload()
!ls

! unzip inputDir.zip
! ls

## making some essential imports
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter

# laoding model
model = tf.keras.models.load_model('./inputDir/RouteGenerator.h5')

# image Preprocessing function
def ImageProcessorAndPredictor(img, model):
  img = cv2.resize(img, (128, 128))
  predictions = model.predict(np.array([img]))

  r = predictions[0,:,:,0]
  g = predictions[0,:,:,0]
  b = predictions[0,:,:,0]

  return np.array(500 *cv2.merge((r, g, b)), dtype = 'uint8')

# defining main function
def Main(model, path):
  cap = cv2.VideoCapture(path)

  # writer object
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter('output.avi',fourcc, 20.0, (128, 128))

  startTime = perf_counter()

  while (cap.isOpened()):

    ret, frame = cap.read()
    if (ret == True):
      out.write(ImageProcessorAndPredictor(frame, model))
    else:
      endTime = perf_counter()
      print ('Time to render {}'.format(endTime - startTime))
      break

  cap.release()
  out.release()
  return

Main(model, './inputDir/vid.mp4')

