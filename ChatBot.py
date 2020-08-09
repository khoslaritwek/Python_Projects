################## chatbot ##########
################### RNN support to be added ####################
import speech_recognition as sr
import time
import re

def timeAndDate():
    return time.asctime( time.localtime(time.time()) )

def IsTimeQuestion(text):
    if re.search(".*time.*|.*date.*|.*year.*",text):
        print ( "Bot :" + timeAndDate())

def IsAboutMe(text):
    if re.search(".*who.*you|.*you.*|.*created.*|.*creatd.*|.*yourself.*", text):
        print ("Bot : I am just a naive text bot preprogrammed to answer you stupid queries this is that way these things work dont they ? some  one with lots of time created me lol")

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
