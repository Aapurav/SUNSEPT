import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pygame

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
        speak("Good morning Master.")
    elif 12 <= hour < 18:
        speak("Good afternoon Master.")
    elif 18 <= hour < 24:
        speak("Good evening Master.")
    else:
        speak("Time to sleep Master.")

# Function to tell the current time
def currenttime():
    current_time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(f"Current time is {current_time}.")

# Function to tell the current date
def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    speak(f"Today is {day} {month} {year}.") 
speak("Welcome back sir. How may I help you?")

# Function to play all songs in the directory
# Function to play all songs in the directory
def play_full_playlist():
    songs_dir = 'C:\\Users\\SONU AGARWAL\\Desktop\\armaan malik'
    
    if os.path.exists(songs_dir) and os.listdir(songs_dir):
        songs = os.listdir(songs_dir)
        speak("Playing your playlist, Master.")
        
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Loop through each song in the directory and play it
        for song in songs:
            song_path = os.path.join(songs_dir, song)
            pygame.mixer.music.load(song_path)  # Load the song
            pygame.mixer.music.play()  # Play the song
            is_paused = False  # Flag to track whether the song is paused or not

            # Listen for commands while the song is playing
            while pygame.mixer.music.get_busy():  # Check if song is still playing
                query = takeCommand()  # Continuously take command while song is playing

                # Pause command
                if 'pause' in query and not is_paused:
                    pygame.mixer.music.pause()   # Pauses the music
                    is_paused = True  # Set the paused flag to True
                    speak("Music paused. Say resume to continue.")
                    
                # Resume command
                elif 'resume' in query and is_paused:
                    pygame.mixer.music.unpause()   # Resume the music
                    is_paused = False  # Set the paused flag to False
                    speak("Music resumed.")
                    
                # Stop or close playlist command
                elif 'close the playlist' in query or 'stop' in query:
                    pygame.mixer.music.stop()  # Stops the playback completely
                    speak("Playlist stopped.")
                    return  # Exit the function and stop the playlist entirely

    else:
        speak("Sorry, I couldn't find any songs to play.")
        
    # Quit the mixer after playing all songs
    pygame.mixer.quit()
# Function to take commands from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        prt('Listening...')
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
            currenttime()

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
            chrome_path = r' C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s'
            webbrowser.get(chrome_path).open(search_url)

        elif 'logout my laptop' in query:
            os.system("shutdown /l")

        elif 'restart my laptop' in query:
            os.system("shutdown /r /t 1")
        
        elif 'shutdown my laptop' in query:
            os.system("shutdown /s /t 1")
        
        elif 'play songs for me' in query:
            speak("Yes, Master")
            play_full_playlist()
            
        elif 'stop' in query:
            speak("Bye MASTER")
            break
