import numpy as np
from scipy.io import wavfile
import AudioPlayer

notesArray = [659.8025, 784.645, 880.735, 880.735, 988.5925, 784.645, 659.8025, 784.645,
              880.735, 880.735, 880.735, 1175.64, 988.5925, 988.5925, 1319.61, 1319.61, 13,
              19.61, 1569.29, 1481.2125, 1319.61, 1175.64, 1047.375, 988.5925, 880.735, 65,
              9.8025, 988.5925]

def get_piano_notes():
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
    base_freq = 440  # Frequency of Note A4
    keys = np.array([x + str(y) for y in range(0, 9) for x in octave])
    # Trim to standard 88 keys
    start = np.where(keys == 'A0')[0][0]
    end = np.where(keys == 'C8')[0][0]
    keys = keys[start:end + 1]

    note_freqs = dict(zip(keys, [2 ** ((n + 1 - 49) / 12) * base_freq for n in range(len(keys))]))
    note_freqs[''] = 0.0  # stop
    return note_freqs

def get_sine_wave(frequency, duration, sample_rate=44100, amplitude=4096):
    t = np.linspace(0, duration, int(sample_rate*duration)) # Time axis
    wave = amplitude*np.sin(2*np.pi*frequency*t)
    return wave

# Get middle C frequency
note_freqs = get_piano_notes()
frequency = note_freqs['C4']

# Pure sine wave
for noteFreq in notesArray:
    sine_wave = get_sine_wave(noteFreq, duration=2, amplitude=2048)
    wavfile.write('pure_c.wav', rate=44100, data=sine_wave.astype(np.int16))

    AudioPlayer.start_music("pure_c.wav", 0.5)