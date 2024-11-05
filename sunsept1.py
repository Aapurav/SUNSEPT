import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

# Initialize the speech engine
mac = pyttsx3.init()

# Get voices and set the voice to female (index 1)
voices = mac.getProperty('voices')
mac.setProperty('voice', voices[1].id)

# Function to speak text
def speak(voice):
    mac.say(voice)
    mac.runAndWait()

speak("Hello Master! This is SUNSEPT")

def prt(txt):
    speak(txt)
    print(txt)

# Greet based on the time of the day
def wishme():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning sir.")
    elif 12 <= hour < 18:
        speak("Good afternoon sir.")
    elif 18 <= hour < 24:
        speak("Good evening sir.")
    else:
        speak("Time to sleep sir.")
    speak("Welcome back sir. How may I help you?")

# Function to tell the current time
def time():
    current_time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(f"Current time is {current_time}.")

# Function to tell the current date
def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    speak(f"Today is {day} {month} {year}.")

# Function to take commands from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        prt('Listning...')
        r.pause_threshold = 1
        voice = r.listen(source)
    try:
        prt('Recognizing...')
        query = r.recognize_google(voice, language="en-in")
        print(f"User said: {query.lower()}")
        return query.lower()
    except Exception as e:
        print(e)
        
        return "none"

# Main program
if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'chrome' in query:
            speak("What should I search for in Chrome?")
            print("What should I search for in Chrome?")
            search_query = takeCommand()
            search_url = f"https://www.google.com/search?q={search_query}"
            
            # Use the default web browser to search (works if Chrome is the default browser)
            # wb.open(search_url)
            # If you want to explicitly use Chrome, use the correct path in raw string format
            chrome_path = r' C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s'
            webbrowser.get(chrome_path).open(search_url)
        elif 'stop' in query:
            speak("Goodbye!")
            break
