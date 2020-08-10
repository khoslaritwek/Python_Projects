################## chatbot ##########
################### RNN support to be added ####################
import speech_recognition as sr
import time
import re
import numpy as np
import pandas as pd

def timeAndDate():
    return time.asctime( time.localtime(time.time()) )


def IsTimeQuestion(text):
    if re.search(".*time.*|.*date.*|.*year.*",text):
        print ( "Bot :" + timeAndDate())
        

def IsAboutMe(text):
    if re.search(".*who.*you|.*you.*|.*yourself.*", text):
        print ("Bot : Just another chat bot answering your questions Duh!!")
    if re.search(".*creator.*|.*created.*", text):
        print ("Bot : Someone with alots of time created me ")
    if re.search(".*sing.*|.*song.*", text):
        print ("Bot: I am a baaad  guuuy Duh!!")
        

def Speech2Text():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
            print('listening....')
            audio = rec.listen(source, timeout = 5, phrase_time_limit = 5)
            text = ''
            try :
                    text = rec.recognize_google(audio)
            except:
                    print(' Bot : Sorry i was not able to catch that,Speak again herhaps')

    return text




def main():
    text = ''
    while text not in ['exit', 'close', 'bye', 'close application', 'exit now', 'turn off']:
        text = Speech2Text()
        print (" Bot : You asked me => {}".format(text))
        IsTimeQuestion(text)
        IsAboutMe(text)



main()
