import os
import time

def play_full_playlist():
    # Path to the directory containing music
    songs_dir = 'C:\\Users\\SONU AGARWAL\\Desktop\\armaan malik'
    
    # Check if the directory exists and contains songs
    if os.path.exists(songs_dir) and os.listdir(songs_dir):
        songs = os.listdir(songs_dir)  # List all files in the directory
        speak("Playing your playlist, Master.")
        
        # Loop through each song in the directory and play it
        for song in songs:
            song_path = os.path.join(songs_dir, song)
            os.startfile(song_path)  # Play each song
            
            # Wait for the song duration or a specific time before playing the next song
            time.sleep(5)  # Adjust or remove this if you want it to wait until the song ends
    else:
        speak("Sorry, I couldn't find any songs to play.")
