import pandas as pd

# Using readlines()
file1 = open('frequencies.txt', 'r')
Lines = file1.readlines()


for line in Lines:
    # split the string
    words = line.split()

    # get the second argument
    note = words[1]

    # get the characters from 5 onwards using split

    notation = note.split("NOTE_")

    print(notation[1])

