import pygame

import AudioPlayer

# get the name of the file
def get_file_name():
    fileTitle = get_file_name_input()
    fileTitleInvalid = True

    while(fileTitleInvalid):
        # check if the title has spaces
        if (" " in fileTitle):
            print("File name cannot have spaces!")
            fileTitle = get_file_name_input()
            continue
        elif (not fileTitle.strip()):
            print("File name cannot be empty!")
            fileTitle = get_file_name_input()

            continue
        elif not (fileTitle.isalpha() or fileTitle.isalnum() or fileTitle.isnumeric()):
            print("File name should be contain alphabets or numbers")
            fileTitle = get_file_name_input()
            continue

        fileTitleInvalid = False

    return fileTitle

def get_file_name_input():
    return input("What should the file be called? ")

# get the string of text representing the music
def get_Notes():
    notesList = ["c", "d", "e", "f", "g", "a", "b", "c1"]

    songNotes = []

    print("Enter notes")
    print("example:" + str(notesList))
    print('Enter "done" to end')
    note = ""

    while(note != "done"):
        note = input()
        if note in notesList:
            songNotes.append(note)
            print(note)
        elif note == "done":
            continue
        else:
            print("Invalid input!")

    print("notes recorded!")
    print(songNotes)

    return songNotes

# test play the notes
def test_play_notes(songNotes):
    for note in songNotes:
        notePath = "audioFiles/piano/" + note.upper() + ".wav"
        AudioPlayer.start_music(notePath, 0.5)


def get_note_for_C(note):
    notesList = ["c", "d", "e", "f", "g", "a", "b", "c1"]
    notesC = ["NOTE_C4",
              "NOTE_D4",
              "NOTE_E4",
              "NOTE_F4",
              "NOTE_G4",
              "NOTE_A4",
              "NOTE_B4",
              "NOTE_C5"]
    return notesC[notesList.index(note)]



def convert_to_C(songNotes, filename, loopSound):
    # create the new text file in the output folder
    filePath = "codeOutputs/" + filename + ".txt"
    f = open(filePath, "a")

    # add imports
    f.write('#include "pitches.h"')

    f.write('#define noteDurations 4')

    # add notes array
    f.write("int melody[] = {")
    notesString = ""

    for noteIndex in (len(songNotes) - 1):
        notesString += get_note_for_C(songNotes[noteIndex]) + ","

    notesString += get_note_for_C(songNotes[-1])

    f.write(notesString)

    f.write("};")

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

    f.write("void setup() {")

    if not loopSound:
        f.writelines(musicLoop)

    f.write("}")

    f.write("void loop() {")

    if loopSound:
        f.writelines(musicLoop)

    f.write("}")

    # add timing variable

    f.close()


if __name__ == '__main__':
    print("Create new file")
    filename = get_file_name()

    notesNotEntered = True
    while (notesNotEntered):
        print("Enter the notes")
        songNotes = get_Notes()

        print("Playing song")
        test_play_notes(songNotes)

        inputInvalid = True
        confirmation = ""
        while(inputInvalid):
            confirmation = input("Is the song correct? [y/n]: ")
            if confirmation == "y":
                break
            elif confirmation == "n":
                break
            else:
                print("Input invalid!")

        if confirmation == "y":
            break

    loopSound = False
    inputInvalid = True
    while (inputInvalid):
        confirmation = input("Loop song? [y/n]: ")
        if confirmation == "y":
            break
            loopSound = True
            print("Input invalid!")
        elif confirmation == "n":
            break
            print("Input invalid!")

    print("Converting to Arduino Code")

    convert_to_C(songNotes, filename, loopSound)

    print("Song converted! Bye!")
    input()



