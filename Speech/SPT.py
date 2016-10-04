import speech_recognition as sr
import os
import time
import Config
import Web
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
    while userIn.lower() != "shutdown":
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
                break;
        except sr.RequestError as e:
            counter = counter+1;
            userIn = "noR"
            if (counter == 2):
                counter = 0
                say("Good Bye")
                userIn = "shutdown"
                break;
        print(userIn)
        userIn = userIn.lower()
        if ("hello" in userIn):
        	say("Hi "+name+", how can I help you, I am Jacbis")
        elif ("remind" in userIn):
            say("I will remind you to do that")
        elif (userIn == "shutdown"):
            say("Good Bye")
        elif ("info on" in userIn or "information on" in userIn or "information about" in userIn or "search" in userIn or "look up" in userIn):
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
            s = Web.getSubject(userIn)
            say ("Playing "+s)
            Web.music(s)
        elif (len(userIn) == 0):
            counter = counter+1;
            if (counter == 2):
                counter = 0
                say("Good Bye")
                userIn = "shutdown"
                break;
        elif ("nor" == userIn):
            pass
        else:
            say("I did not understand that, If you can add that to my database, that would be great.")























