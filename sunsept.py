import pyttsx3
import datetime
import speech_recognition as sr

# Initializing  the speech engine
mac = pyttsx3.init()

# VOICE #
voices = mac.getProperty('voices')       #getting details of current voice
mac.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# mac.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


mac.say("hello master")
mac.runAndWait()

# speak function
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

wishme()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year= str(datetime.datetime.now().year)
    month= str(datetime.datetime.now().month)
    date= str(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("welcome back sir. How may i help you")
    
# Speech Recognition
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

        if 'stop' in query:
            exit(0)

    except Exception as e:
        print(e)
        speak("Master! please repeat again....")

        return "none"
    return query


# run for main file only
if __name__ == '__main__':
    time()
    date()
    wishme()
    while True:
        print(takeCommand())   

