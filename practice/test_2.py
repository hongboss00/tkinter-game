from Sprite import *
from tkinter import *
from math import *
from random import *

speed = 3

root = Tk()
mcanvas = Canvas(root, bg = "#222222", bd = 3, width = 1000, height = 800)
mcanvas.pack()

user = Sprite(root, 800, 400, mcanvas, 20, 20)

def keypressed(event):
    global speed

    pressedkey = event.keysym
    if(pressedkey == 'Left'):
        user.setDx(-speed)
    if(pressedkey == 'Right'):
        user.setDx(speed)
    if(pressedkey == 'Up'):
        user.jump()
        
def keyreleased(event):
    global speed
    user.setDx(0)
    #user.dy = 0

def gameLoop():
    mcanvas.delete('all')
    user.move()
    user.draw()
    root.after(10, gameLoop)


mcanvas.focus_set()
mcanvas.bind("<KeyPress>", keypressed)
mcanvas.bind("<KeyRelease>", keyreleased)

gameLoop()
root.mainloop()