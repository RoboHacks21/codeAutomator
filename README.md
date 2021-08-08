# codeAutomator
A simple python project to automatically generate codes for a few repetitive tasks

## Functionality

### 1) The CLI interface

#### pythonCLIinput.py
For users that already know how to read musical notations or have a simple song sheet consisting of alphabetical music notes of a song that they can refer to, the CLI interface helps them easily convert their song into Arduino

### 2) The Virtual Piano Interface

#### pythonPianoInput.py

For the more musically inclined users they can simply play the song on our virtual piano.
The piano has two inputs, clicking the piano key buttons on the screen, or playing the piano using the keys on their keyboard. Users can save their songs and play them back to see how they sound. They can then click the Save button to convert their song into Arduino code. 

In addition to allowing users to easily transcribe their music, the virtual piano allows users to easily create and save their own songs without the need for external software.

### 3) Converting a Wav file to C code

#### pythonWavtoNotes.py
For the users who have no concept of music notation and just want a fast way to convert their music files directly into working Arduino codes, the Wav file converter is the go to interface for them. All they need to do is to run the python

This wav file can either be from a song they like, or it can be generated from an external software such as bandlab lab and exported. For instance, in my video example the testNotes.wav song was created by me in bandlab, which offers more advanced features for song creation.

With these 3 interfaces, users are sure to be able convert their songs to Arduino codes easily

## Credits

* The code for the extraction of musical notes from a .wav file was adapted from [here](https://github.com/wesleybowman/misc/blob/master/Stephanie/specgram.py), which was shared on this [stackoverflow thread](https://stackoverflow.com/questions/22226059/finding-notes-in-a-wav-file). 

* The sample code for the Arduino tone generation was taken from the Arduino built in sample codes and adapted to be used as a template for the different melodies. The original code can be found [here](https://www.arduino.cc/en/Tutorial/BuiltInExamples/toneMelody).


