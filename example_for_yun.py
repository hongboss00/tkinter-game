from tkinter import *
from guide_unitselector import *

root = Tk()
mcanvas = Canvas(root, bg = "#222222", bd = 3, width = 1600, height = 800)

mselector = Selector(mcanvas, root)

def Loop():
    mselector.LevelSprite()
    root.after(10, Loop)


Loop()
mcanvas.pack()
root.mainloop()
