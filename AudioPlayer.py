import time
from threading import Thread
from pygame import mixer


def play_music(wav_file):
    # Starting the mixer
    mixer.init()

    # Loading the morse code
    mixer.music.load(wav_file)

    # Setting the volume
    mixer.music.set_volume(1)

    # Start playing the morse code
    mixer.music.play(loops=1)


def stop_music(music_thread, duration):
    time.sleep(duration)
    mixer.music.stop()
    mixer.quit()
    music_thread.join()

def start_music(wav_file, duration):
    # Play Music on Separate Thread (in background)
    music_thread = Thread(target=play_music, args=(wav_file,))

    stop_music_thread = Thread(target=stop_music, args=(music_thread, duration,))

    music_thread.start()

    stop_music_thread.start()
    stop_music_thread.join()
