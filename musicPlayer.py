from pygame import mixer
import os
import threading
import random
import time
# from pynput import keyboard

print("\n---------------------------------------------------")
vol = float(input("what volume (from 0 to 1): "))
print("input 'p' to pause, 'r' to resume, 'l' to loop and unloop and 'e' to skip !\n")
print("---------------------------------")
print("---playlist is starting! enjoy---")
print("---------------------------------\n")
    
def Play():
    while True:
        songs = os.listdir('music/')
        for x in range (len(songs)):
            rng = random.randint(0, len(songs) - 1)
            newName = songs[rng][:-4]  # get rid of file extension
            print("-playing \"" + newName + "\"-")
            mixer.init()
            mixer.music.load('music//' + songs[rng])
            mixer.music.set_volume(vol)
            
            mixer.music.play()
            x = threading.Thread(target=InputDetect)
            x.start()

            while True:
                if mixer.music.get_busy() == False and query != "p" and query != "r" and loop == True:
                    mixer.music.play()
                elif mixer.music.get_busy() == False and query != "p" and query != "r" and loop == False:
                    break

            while True:
                if mixer.music.get_busy() == False and query != "p" and query != "r":
                    songs.pop(rng)
                    break

        print("\n-you have finished your whole playlist! (good job)-")
        print("-playlist will restart now-")

def InputDetect():
    global query
    query = ""
    global loop 
    loop = False
    while True:
        query = input("")

        if query == 'p':
            # Pausing the music
            mixer.music.pause()
            print("no way u paused the song")

        elif query == 'r':
            
            # Resuming the music
            mixer.music.unpause()
            time.sleep(0.00001)
            query = ''
            print("song resumed :0")
            
        elif query == 'e':
            # Stop the mixer
            mixer.music.stop()
            print("song skipped (what power)\n")
            break
        elif query == 'l' and loop == True:
            loop = False
            print("loop ended :)")

        elif query == 'l':
            loop = True
            print("loop started :)")
Play()