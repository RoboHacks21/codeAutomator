import tkinter as tk
from tkinter import *
import time
from datetime import datetime

# declare variables
import playByFreq

currentTime = time.time()
previousTime = time.time()
timeDiff = 0

notesArray = []
timingArray = []

app = tk.Tk()
app.title("Piano input")
app.geometry("700x500")
app.configure(background="light green")

# to add the icon
# app.iconbitmap('FireAnts_logo.ico')

# white keys
pianoKey1 = tk.Button(app,
                       text="C5\n\n\n\n\n\n\nA",
                       width=6,
                       height=10)
pianoKey2 = tk.Button(app,
                       text="D5\n\n\n\n\n\n\nS",
                       width=6,
                       height=10)
pianoKey3 = tk.Button(app,
                       text="E5\n\n\n\n\n\n\nD",
                       width=6,
                       height=10)
pianoKey4 = tk.Button(app,
                       text="F5\n\n\n\n\n\n\nF",
                       width=6,
                       height=10)
pianoKey5 = tk.Button(app,
                       text="G5\n\n\n\n\n\n\nG",
                       width=6,
                       height=10)
pianoKey6 = tk.Button(app,
                       text="A5\n\n\n\n\n\n\nH",
                       width=6,
                       height=10)
pianoKey7 = tk.Button(app,
                       text="B5\n\n\n\n\n\n\nJ",
                       width=6,
                       height=10)
pianoKey8 = tk.Button(app,
                       text="C6\n\n\n\n\n\n\nK",
                       width=6,
                       height=10)
pianoKey9 = tk.Button(app,
                       text="D6\n\n\n\n\n\n\nL",
                       width=6,
                       height=10)
pianoKey10 = tk.Button(app,
                       text="E6\n\n\n\n\n\n\n;",
                       width=6,
                       height=10)

# black keys
pianoKeyB1 = tk.Button(app,
                       text="CS5\n\n\n\n\n\n\nW",
                       width=6,
                       height=10)
pianoKeyB2 = tk.Button(app,
                       text="DS5\n\n\n\n\n\n\nE",
                       width=6,
                       height=10)
pianoKeyB3 = tk.Button(app,
                       text="FS5\n\n\n\n\n\n\nR",
                       width=6,
                       height=10)
pianoKeyB4 = tk.Button(app,
                       text="GS5\n\n\n\n\n\n\nT",
                       width=6,
                       height=10)
pianoKeyB5 = tk.Button(app,
                       text="AS5\n\n\n\n\n\n\nY",
                       width=6,
                       height=10)
pianoKeyB6 = tk.Button(app,
                       text="CS6\n\n\n\n\n\n\nU",
                       width=6,
                       height=10)
pianoKeyB7 = tk.Button(app,
                       text="DS6\n\n\n\n\n\n\nI",
                       width=6,
                       height=10)

# place white keys
pianoKey1.place(x=50, y=325)
pianoKey2.place(x=110, y=325)
pianoKey3.place(x=170, y=325)
pianoKey4.place(x=230, y=325)
pianoKey5.place(x=290, y=325)
pianoKey6.place(x=350, y=325)
pianoKey7.place(x=410,y=325)
pianoKey8.place(x=470, y=325)
pianoKey9.place(x=530, y=325)
pianoKey10.place(x=590, y=325)

# place black keys
pianoKeyB1.place(x=80, y=175)
pianoKeyB2.place(x=140, y=175)
pianoKeyB3.place(x=260, y=175)
pianoKeyB4.place(x=320, y=175)
pianoKeyB5.place(x=380, y=175)
pianoKeyB6.place(x=500, y=175)
pianoKeyB7.place(x=560, y=175)

# set the color for the black keys
pianoKeyB1.configure(bg="#222222", fg="white", activebackground='gray')
pianoKeyB2.configure(bg="#222222", fg="white", activebackground='gray')
pianoKeyB3.configure(bg="#222222", fg="white", activebackground='gray')
pianoKeyB4.configure(bg="#222222", fg="white", activebackground='gray')
pianoKeyB5.configure(bg="#222222", fg="white", activebackground='gray')
pianoKeyB6.configure(bg="#222222", fg="white", activebackground='gray')
pianoKeyB7.configure(bg="#222222", fg="white", activebackground='gray')

# link functions to white keys
pianoKey1.configure(command=lambda: getNotePart(pianoKey1['text']))
pianoKey2.configure(command=lambda: getNotePart(pianoKey2['text']))
pianoKey3.configure(command=lambda: getNotePart(pianoKey3['text']))
pianoKey4.configure(command=lambda: getNotePart(pianoKey4['text']))
pianoKey5.configure(command=lambda: getNotePart(pianoKey5['text']))
pianoKey6.configure(command=lambda: getNotePart(pianoKey6['text']))
pianoKey7.configure(command=lambda: getNotePart(pianoKey7['text']))
pianoKey8.configure(command=lambda: getNotePart(pianoKey8['text']))
pianoKey9.configure(command=lambda: getNotePart(pianoKey9['text']))
pianoKey10.configure(command=lambda: getNotePart(pianoKey10['text']))

# link functions to black keys
pianoKeyB1.configure(command=lambda: getNotePart(pianoKeyB1['text']))
pianoKeyB2.configure(command=lambda: getNotePart(pianoKeyB2['text']))
pianoKeyB3.configure(command=lambda: getNotePart(pianoKeyB3['text']))
pianoKeyB4.configure(command=lambda: getNotePart(pianoKeyB4['text']))
pianoKeyB5.configure(command=lambda: getNotePart(pianoKeyB5['text']))
pianoKeyB6.configure(command=lambda: getNotePart(pianoKeyB6['text']))
pianoKeyB7.configure(command=lambda: getNotePart(pianoKeyB7['text']))

titleLabel = Label(app,
    text="Song Title",
    foreground='black',
    background='light green',
    font=('Comic Sans MS', 12),
    width=10,
    height=2)

noteText = Label(app,
    text="",
    background='green',
    foreground='white',
    font=('Comic Sans MS', 12),
    width=10,
    height=2)

titleEntry = Entry(app,
                   width=30,
                   )

recordBtn = Button(app,
               text="Start Recording [,]",
                   width=15,
                   height=2)

playBtn = Button(app,
               text="Play",
                 width=10,
                 height=2)

nextBtn = Button(app,
               text="Save",
                 width=10,
                 height=2)

titleEntry.place(x=185, y=35)
titleLabel.place(x=80, y=20)
nextBtn.place(x=550, y=40)
noteText.place(x=300, y=100)
recordBtn.place(x=80, y=100)
playBtn.place(x=550, y=100)


recordBtn.configure(command=lambda: toggle_recording())
nextBtn.configure(command=lambda: nextScreen())
playBtn.configure(command=lambda: playBack())

def playBack():
    playByFreq.playFromArray(notesArray, timingArray)


def nextScreen():
    generateOutPut()

    # check if the array is empty
    if len(notesArray) == 0:
        # show tkinter message box
        print("cannot proceed, array empty")
    else:
        print("Save")
        # go to next screen

    noteText["text"] = "Saved!"



def toggle_recording():
    if recordBtn['text'] == "Stop Recording [,]":
        currentTime  = time.time()
        global previousTime
        timeDiff = round((currentTime - previousTime) * 4)
        timingArray.append(timeDiff)

        # append time diff
        noteText["text"] = "stop!"

        recordBtn['text'] = "Start Recording [,]"

        for i in range(len(timingArray)):
            if timingArray[i] == 0:
                timingArray[i] = 1

        print(notesArray)
        print(timingArray)
        print(len(notesArray))
        print(len(timingArray))

    else:
        # append blank note to
        noteText["text"] = "start!"
        recordBtn['text'] = "Stop Recording"
        time.sleep(1)
        recordBtn['text'] = "Stop Recording [,]"
        notesArray.clear()
        timingArray.clear()
        previousTime = time.time()

def getNotePart(noteStr):
    noteParts = noteStr.split()
    note = noteParts[0]
    addNote(note)

def addNote(note):
    global previousTime

    # add the time difference estimate to the list of timings
    if len(notesArray) != 0:
        currentTime = time.time()
        timeDiff = round((currentTime - previousTime) * 4)
        timingArray.append(timeDiff)
        previousTime = currentTime
    else:
        previousTime = time.time()

    # add the new note to the notes array
    notesArray.append(note)

    # play the note
    playByFreq.playNote(note)
    # playThread = threading.Thread(target=playByFreq.playNote(note))
    # playThread.start()
    # playThread.join()
    noteText["text"] = note

def keydown(event):
    note, charInList = getNoteRepresentation(event.char)
    if charInList:
        addNote(note)
    else:
        if event.char == ",":
            toggle_recording()


def getNoteRepresentation(character):
    if character.lower() == "a":
        return "C5", True
    elif character.lower() == "s":
        return "D5", True
    elif character.lower() == "d":
        return "E5", True
    elif character.lower() == "f":
        return "F5", True
    elif character.lower() == "g":
        return "G5", True
    elif character.lower() == "h":
        return "A5", True
    elif character.lower() == "j":
        return "B5", True
    elif character.lower() == "k":
        return "C6", True
    elif character.lower() == "l":
        return "D6", True
    elif character == ";" or character == ":":
        return "E6", True
    elif character.lower() == "w":
        return "CS5", True
    elif character.lower() == "e":
        return "DS5", True
    elif character.lower() == "r":
        return "FS5", True
    elif character.lower() == "t":
        return "GS5", True
    elif character.lower() == "y":
        return "AS5", True
    elif character.lower() == "u":
        return "CS6", True
    elif character.lower() == "i":
        return "DS6", True
    else:
        return character, False

def generateOutPut():
    # get the file name
    title = titleEntry.get()
    if not title.strip():
        now = datetime.now()
        title = now.strftime("%m%d%Y") + "_CCode"
    convert_to_C(notesArray, title, False)


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
    }\n"""

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

app.bind('<KeyPress>', keydown)


app.mainloop()