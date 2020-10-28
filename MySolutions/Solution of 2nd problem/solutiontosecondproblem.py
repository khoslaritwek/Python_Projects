#####################################################################
#                            coding convetions                      #
#####################################################################
# variable name starts with small letters                           #
# Function name starts with capital letters                         #
# REFRENCES/FILEHANDLES are represtented in all caps                #
#####################################################################

#####################################################################
# Notes: since in python it's not possible to restart a process that#
# gets stop therefore using sleep functionality  To stop a process  #
# I would have raised an exception but in that case the proccess    #
# restarted would not be the same hence this approach               #
# This is a recurrsice codes with 1 minute duration and performs the#
# given task beautifully                                            #
# Thanks                                                            #
#####################################################################

# making imports only need these 2 libs
from threading import *
import time

# Time Variables
# also since seconds have values between 0 - 59 a correction of 60 is
# added to make a correction turning negative values of timeElapsed to positive values
startTime = time.localtime().tm_sec
currentTime = int (time.localtime().tm_sec)
timeElapsed = currentTime - int (startTime)


# A function for thread Handling
def ThreadNameAndTime ():
  while 1:
    currentTime = int (time.localtime().tm_sec) 
    timeElapsed = currentTime - int (startTime)

    if timeElapsed < 0:
      timeElapsed += 60
    
    if timeElapsed % 5 == 0:
      print("\n" + current_thread().getName() +' is running at ' + str (timeElapsed))
      time.sleep(1)

    if timeElapsed == 20 and current_thread().getName() == 'Thread-1':
      print("Thread-1 goes to sleep and Thread-2 awakes")
      if flag == False:
        flagForT2 = True
        t2.start()

      time.sleep(18)

    if timeElapsed == 38 and current_thread().getName() == 'Thread-3':
      print("Thread-3 goes to sleep Thread-1 wakes")
      time.sleep(22)

    if timeElapsed == 59 and current_thread().getName() == 'Thread-2':
      print ("restoring original state ie Thread -1 and  Thread-3 active Thread -2 goes to sleep")
      time.sleep(21)

      


  
# Just a main functon nothing much here
def main():
  global t1, t2, t3, flag
  flag = False
  t1 = Thread(target = ThreadNameAndTime)
  t2 = Thread(target = ThreadNameAndTime)
  t3 = Thread(target = ThreadNameAndTime)
 

  t1.start()
  t3.start()
  



main()
