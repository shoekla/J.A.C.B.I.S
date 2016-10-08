import speech_recognition as sr
import os
import time
import Config
import sys
import Web
import CAL
import urllib2
import re
import nltk
import csv
import time
import requests
import string
from bs4 import BeautifulSoup
from urllib2 import urlopen
import os
import fire
import webbrowser
voice = Config.voice
name = Config.name
def say(s):
    os.system("say -v "+voice+" "+str(s))
def convo():
    os.system("say -v "+voice+" How can I be of service?")
    # obtain audio from the microphone
    counter = 0
    r = sr.Recognizer()
    userIn = ""
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)


    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        userIn = str(r.recognize_google(audio))
    except sr.UnknownValueError:
        counter = counter+1;
        userIn = "noR"
        if (counter == 2):
            counter = 0
            say("Good Bye")
            userIn = "shutdown"
    except sr.RequestError as e:
        counter = counter+1;
        userIn = "noR"
        if (counter == 2):
            counter = 0
            say("Good Bye")
            userIn = "shutdown"
    print(userIn)
    userIn = userIn.lower()
    if ("hello" in userIn):
    	say("Hi "+name+", I am Jacbism how can I help you")
    elif (userIn == "shutdown"):
        say("Good Bye")
    elif ("info on" in userIn or "information on" in userIn or "information about" in userIn or "look up" in userIn):
        begin = userIn.find("info")
        index = userIn.find(" ",userIn.find(" ",begin+1)+1)
        say("Pulling up information on "+userIn[index:])
        Web.infoOn(userIn[index:])
    elif ("video" in userIn):
        begin = userIn.find("video")
        index = userIn.find(" ",userIn.find(" ",begin+1)+1)
        say("Pulling up videos on "+userIn[index:])
        Web.openInWeb(Web.getYoutubeLink(userIn[index:]))
    elif ("play" in userIn):
        if "on youtube" in userIn:
            s = userIn[userIn.find(" ",userIn.find("play")):]
            s = s.replace("on youtube","")
            say ("Playing "+s)
            Web.music(s)
            return
        s = Web.getSubject(userIn)
        print s
        say ("Playing "+s)
        Web.music(s)
    elif (len(userIn) == 0):
        counter = counter+1;
        if (counter == 2):
            counter = 0
            say("Good Bye")
            userIn = "shutdown"
    elif ("definition" in userIn or "mean" in userIn):
        s = Web.definition(userIn)
        say(s)
    elif ("nor" == userIn):
        pass
    elif ("remind me to" in userIn):
        index = userIn.find("remind me to")
        begin = userIn.find(" ",index+len("remind me to"))
        re = userIn[begin:]
        if "comes out" in userIn:
            re = re.replace("watch","")
            re = re.replace("go to","")
            re = re.replace("when it comes out","") + "film "
            re = "Watch " +re + Web.getMovieDate(re)
            
            re = re.replace("film","")

        CAL.createEvent(re)
        print re
        say("ok i will remind you to "+re)
    elif ("give me searches" in userIn):
        userIn.strip()
        userIn = userIn[len("give me searches for"):]
        if ("youtube" in userIn):
            userIn = userIn.replace("on youtube","")
            userIn = userIn.replace("youtube","")
            say("Getting searches for "+userIn+"on youtube")
            Web.youtubeSearchs(userIn)
            return
        say("Getting searches for "+userIn+"on google")
        Web.openInWeb(Web.googLink(userIn))
    elif ("open" in userIn and "chrome" in userIn):
        say("Opening new Window in chrome")
        Web.openWindow()

    else:
        s = Web.getAnswer(userIn)
        if Config.firebaseR:
            if len(s) > 0:
                say(s)
                return
            s = fire.getMyRespPyth(userIn)
            if len(s) > 0:
                say(s)
                return
            s = fire.getMyResp(userIn)
            if len(s) > 0:
                say(s)
                return
            if Config.randomR:
                say(fire.getRandomResponse())
                return
        say("I did not understand that, If you can add that to my database, that would be great.")

convo()
print "Reached"
sys.exit(0)



















