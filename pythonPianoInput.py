import tkinter as tk
import time
import datetime

# declare variables
# timeNow
# previousTime
# calculate time difference timeDiff



# declare function to append


def onKeyPress(event):
    text.insert('end', 'You pressed %s\n' % (event.char, ))

root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()