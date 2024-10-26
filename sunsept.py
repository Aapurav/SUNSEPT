import pyttsx3
import datetime
import speech_recognition as sr

mac = pyttsx3.init()
mac.say("hello master")
mac.runAndWait()

def speak(voice):
    mac.say(voice)
    mac.runAndWait()

speak("this is SUNSEPT")

def wishme():
    hour =(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("good afternoon sir")
    elif hour>=18 and hour<24:
        speak("good evening sir")
    else:
        speak("time to sleep sir")

# wishme()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

# time()

def date():
    year= str(datetime.datetime.now().year)
    month= str(datetime.datetime.now().month)
    date= str(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

# date()

def wishme():
    speak("welcome back sir. How may i help you")
    
# wishme()

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        speak("listening")
        r.pause_threshold=1
        voice =r.listen(source)
    try:
        print("recongnizning...")
        speak("recongnizning...")
        query = r.recognize_google(voice, language="en-in")

        if query == ('stop','exit','sleep'):
            exit(0)

    except Exception as e:
        print(e)
        speak("Master! please repeat again....")

        return "none"
    return query

while True:
    print(takeCommand())   
