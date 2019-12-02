from tkinter import *
from Pattern1 import *

t = 0

root = Tk()
mCanvas = Canvas(root, bg = "#222222", bd = 3, width = 1600, height = 800)
mCanvas.pack()

Pattern1 = Pattern1(root, mCanvas)

def Loop():
    global t

    t += 10
    mCanvas.delete('all')
    Pattern1.show1()
    Pattern1.show2(t)
    root.after(10, Loop)

Loop()
root.mainloop()