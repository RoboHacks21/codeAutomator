
# to write to a file
f = open("testingText/demoWrite.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("testingText/demoWrite.txt", "r")
print(f.read())