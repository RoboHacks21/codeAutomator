from __future__ import division
import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn
from scipy.signal import argrelextrema
from scipy.interpolate import interp1d
import abjad
import re

import playByFreq
from pythonCLIinput import get_file_name

# get wave input from the files selection
# WAV = 'testSong.wav'
WAV = input("Which file to get notes from: ")

rate, data = wavfile.read(WAV)
time = np.arange(len(data[:,0]))*1.0/rate


nfft = 1024*6
pxx, freq, bins, plot = plt.specgram(data[:,0],NFFT=nfft)

plt.show()

a = np.mean(pxx,axis=0)
aa = np.arange(len(a))
a = a/np.max(a)*np.max(data[:,0])
aa = aa/np.max(aa) * time[-1]

f = interp1d(aa,a)
newSmooth = f(time)

indMax = argrelextrema(newSmooth, np.greater)[0]
indMin = argrelextrema(newSmooth, np.less)[0]

lastValue = np.where(newSmooth==newSmooth[-1])[0]
indMin = np.hstack((indMin,lastValue))

# plt.plot(time,data[:,0])
# plt.plot(aa,a)
# plt.plot(time[indMax],newSmooth[indMax])
# plt.plot(time[indMin],newSmooth[indMin])
# plt.show()


NoteFile = pd.read_excel('NoteFreq.xlsx',0)
notes = np.array([indMax,indMin]).T


def getHarmonics(p,f,maxPower,maxFrequency,harmonics,harm):

    x = maxFrequency/harm
    #problem is that its not exactly in f
    ind1 = np.where(f<=x+1)
    ind2 = np.where(f>=x-1)
    mask = np.in1d(ind1,ind2)
    index = np.where(mask == True)[0]

    # print('frequency')
    # print (f[index])
    condition = p[index]/maxPower
    try:
        condition = condition[0]
    except IndexError:
        pass

    #if p[index]/maxPower>=0.90:
    if condition>=0.90:
        harmonics.append(f[index][0])

    return harmonics


def getFreq(notes):
    individualNotes = []
    freqs = []
    letterNotes = []

    for i,v in enumerate(notes):

        individualNotes.append(data[v[0]:v[1],0])

        p = 20*np.log10(np.abs(np.fft.rfft(data[v[0]:v[1], 0])))
        f = np.linspace(0, rate/2.0, len(p))
        #plt.plot(f,p)
        #plt.show()

        harmonics = []
        maxPower = np.max(p)
        maxFrequency = f[np.where(p==max(p))][0]

        # print ('HERE')
        # print (i)

        for j in range(2,8):
            harmonics = getHarmonics(p,f,maxPower,maxFrequency,harmonics,j)

        if harmonics==[]:
            harmonics = [maxFrequency]
        #
        # print ('HARMONICS')
        # print (harmonics)

        maxFreq = harmonics

        a = NoteFile[NoteFile['Lower']<maxFreq[0]]
        b = NoteFile[NoteFile['Upper']>maxFreq[0]]
        note = a.join(b,how='inner',lsuffix='Lower').index[0]

        letterNotes.append(note)

    return letterNotes, freqs, individualNotes


letterNotes, freqs, individualNotes = getFreq(notes)

staff = abjad.Staff()

def fixNotes(letters):

    m = letters

    if m[-1]=='0':
        #note = m[0].upper()+ m[0].upper()+ m[0].upper()
        note = m[0]+3*','

    if m[-1]=='1':
        #note = m[0].upper()+ m[0].upper()
        note = m[0]+2*','

    if m[-1]=='2':
        note = m[0]+','

    if m[-1]=='3':
        note = m[0]

    if m[-1]=='4':
        note = m[0]+"'"

    if m[-1]=='5':
        note = m[0]+2*"'"

    if m[-1]=='6':
        note = m[0]+3*"'"

    if m[-1]=='7':
        note = m[0]+4*"'"

    if m[-1]=='8':
        note = m[0]+5*"'"

    if m[-1]=='9':
        note = m[0]+6*"'"

    if m[-1]=='10':
        note = m[0]+7*"'"

    if m[1]=='s':
        fixed = note
        fixed = fixed[:1]+'s'+fixed[1:]
    else:
        fixed = note

    return fixed

notesSheet = pd.read_csv("constFiles/freqMatch.csv")
print(notesSheet)

frequenciesArray = []
notesArray = []
for i,v in enumerate(letterNotes):
    # print (v)
    # print(i)
    notesArray.append(notesSheet["LetterRep"][v + 14])
    frequenciesArray.append(notesSheet["AvgFreq"][v + 14])
    letters = letterNotes[i]
    try:
        fixed = fixNotes(letters)
        staff.append(fixed)
        # print("YAY")
    except UnboundLocalError:
        m = re.search('\w.\d',letters)
        shortenedNote = m.group(0)
        newNote = shortenedNote[0]+'s'+shortenedNote[-1]
        fixed = fixNotes(newNote)
        # print (fixed)
        staff.append(fixed)

        pass
    except:
        pass
        # print("Some error")


try:
    abjad.show(staff)
except:
    pass
    # print("lmao rip")

print("frequenciesArray")
print(frequenciesArray)
print("notesArray")
print(notesArray)


print("Playing song ...")
playByFreq.playNotesFromFreqArr(frequenciesArray)

print("Song ended")




def getNotesForC(note):
    return "NOTE_" + note

def convert_to_C(songNotes, filename, loopSound):
    # create the new text file in the output folder
    filePath = "codeOutputs/" + filename + ".txt"
    f = open(filePath, "a")

    # add imports
    f.write('#include "pitches.h"\n')

    f.write('#define noteDurations 4\n\n')

    # add notes array
    f.write("int melody[] = {\n")
    notesString = ""

    for noteIndex in range(len(songNotes)):
        notesString += getNotesForC(songNotes[noteIndex]) + ", "
        if noteIndex % 6 == 5:
            notesString += "\n"

    notesString += getNotesForC(songNotes[-1])

    f.writelines(notesString + "\n")

    f.write("};\n\n")

    musicLoop = """   // iterate over the notes of the melody:
    for (int thisNote = 0; thisNote < 8; thisNote++) {
        // to calculate the note duration, take one second
        // divided by the note type.
        //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
        int noteDuration = 1000/noteDurations;
        tone(8, melody,noteDuration);
        //pause for the note's duration plus 30 ms:
        delay(noteDuration +30);
    }"""

    f.write("void setup() {\n")

    if not loopSound:
        f.writelines(musicLoop)

    f.write("}\n\n")

    f.write("void loop() {\n")

    if loopSound:
        f.writelines(musicLoop)

    f.write("}\n\n")

    # add timing variable

    f.close()


# Ask to generate C code
confirmation = ""
while(True):
    confirmation = input("Generate C code [y/n]: ")
    if confirmation == "y":
        break
    elif confirmation == "n":
        break
    else:
        print("Input invalid!")

if confirmation == "y":
    # get c code file name and param
    cCodeTitle = get_file_name()

    loopSound = False
    inputInvalid = True
    while (inputInvalid):
        confirmation = input("Loop song? [y/n]: ")
        if confirmation == "y":
            loopSound = True
            break
        elif confirmation == "n":
            break

    print("Converting to Arduino Code")

    convert_to_C(notesArray, cCodeTitle, loopSound)

    print("Song converted! Bye!")

input("(Press any key to exit)")