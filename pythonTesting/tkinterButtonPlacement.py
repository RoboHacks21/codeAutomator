import tkinter as tk
from tkinter import *
import time
from threading import Thread

# declare variables
timeNow = time.time()
previousTime = time.time()
timeDiff = 0

app = tk.Tk()
app.title("Piano input")
app.geometry("700x500")
app.configure(background="light green")

# to add the icon
# app.iconbitmap('FireAnts_logo.ico')

# white keys
pianoKey1 = tk.Button(app,
                       text="C1\n\n\n\n\n\n\nA",
                       width=6,
                       height=10)
pianoKey2 = tk.Button(app,
                       text="D1\n\n\n\n\n\n\nS",
                       width=6,
                       height=10)
pianoKey3 = tk.Button(app,
                       text="E1\n\n\n\n\n\n\nD",
                       width=6,
                       height=10)
pianoKey4 = tk.Button(app,
                       text="F1\n\n\n\n\n\n\nF",
                       width=6,
                       height=10)
pianoKey5 = tk.Button(app,
                       text="G1\n\n\n\n\n\n\nG",
                       width=6,
                       height=10)
pianoKey6 = tk.Button(app,
                       text="A1\n\n\n\n\n\n\nH",
                       width=6,
                       height=10)
pianoKey7 = tk.Button(app,
                       text="B2\n\n\n\n\n\n\nJ",
                       width=6,
                       height=10)
pianoKey8 = tk.Button(app,
                       text="C2\n\n\n\n\n\n\nK",
                       width=6,
                       height=10)
pianoKey9 = tk.Button(app,
                       text="D2\n\n\n\n\n\n\nL",
                       width=6,
                       height=10)
pianoKey10 = tk.Button(app,
                       text="E2\n\n\n\n\n\n\n;",
                       width=6,
                       height=10)

# black keys
pianoKeyB1 = tk.Button(app,
                       text="CS1\n\n\n\n\n\n\nW",
                       width=6,
                       height=10)
pianoKeyB2 = tk.Button(app,
                       text="DS1\n\n\n\n\n\n\nE",
                       width=6,
                       height=10)
pianoKeyB3 = tk.Button(app,
                       text="FS1\n\n\n\n\n\n\nR",
                       width=6,
                       height=10)
pianoKeyB4 = tk.Button(app,
                       text="GS1\n\n\n\n\n\n\nT",
                       width=6,
                       height=10)
pianoKeyB5 = tk.Button(app,
                       text="AS1\n\n\n\n\n\n\nY",
                       width=6,
                       height=10)
pianoKeyB6 = tk.Button(app,
                       text="CS2\n\n\n\n\n\n\nU",
                       width=6,
                       height=10)
pianoKeyB7 = tk.Button(app,
                       text="DS2\n\n\n\n\n\n\nI",
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
               text="Record",
                   width=10,
                   height=2)

playBtn = Button(app,
               text="Play",
                 width=10,
                 height=2)

saveBtn = Button(app,
               text="Save",
                 width=10,
                 height=2)

titleEntry.place(x=185, y=35)
titleLabel.place(x=80, y=20)
saveBtn.place(x=550, y=40)
noteText.place(x=300, y=100)
recordBtn.place(x=80, y=100)
playBtn.place(x=550, y=100)


recordBtn.configure(command=lambda: start_recording())
saveBtn.configure(command=lambda: print("save"))
playBtn.configure(command=lambda: print("play"))

def updateLabelText(label, text):
    label["text"] = text

def start_recording():
    # 3 sec countdown
    updateThread = Thread(target=updateLabelText(noteText, 3))
    updateThread.start()
    updateThread.join()
    time.sleep(1)
    updateThread = Thread(target=updateLabelText(noteText, 2))
    updateThread.start()
    updateThread.join()
    time.sleep(1)
    updateThread = Thread(target=updateLabelText(noteText, 1))
    updateThread.start()
    updateThread.join()
    time.sleep(1)

    global previousTime
    previousTime = time.time()
    print("records")

def getNotePart(noteStr):
    noteParts = noteStr.split()
    note = noteParts[0]
    addNote(note)

def addNote(note):
    # play the note
    noteText["text"] = note

    # add the new note to the notes array

    # add the time difference estimate to the list of timings

    print(note)

def onKeyPress(event):
    note, charInList = getNoteRepresentation(event.char)
    addNote(note)

def getNoteRepresentation(character):
    if character.lower() == "a":
        return "C1", True
    elif character.lower() == "s":
        return "D1", True
    elif character.lower() == "d":
        return "E1", True
    elif character.lower() == "f":
        return "F1", True
    elif character.lower() == "g":
        return "G1", True
    elif character.lower() == "h":
        return "A2", True
    elif character.lower() == "j":
        return "B2", True
    elif character.lower() == "k":
        return "C2", True
    elif character.lower() == "l":
        return "D2", True
    elif character == ";" or character == ":":
        return "E2", True
    elif character.lower() == "w":
        return "CS1", True
    elif character.lower() == "e":
        return "DS1", True
    elif character.lower() == "r":
        return "FS1", True
    elif character.lower() == "t":
        return "GS1", True
    elif character.lower() == "y":
        return "AS1", True
    elif character.lower() == "u":
        return "CS2", True
    elif character.lower() == "i":
        return "DS2", True
    else:
        return "", False



app.bind('<KeyPress>', onKeyPress)


app.mainloop()