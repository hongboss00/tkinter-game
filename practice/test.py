from tkinter import *
from math import *
#from Pil import *

class obstacle:
    def __init__(self, x,y, canvas, width = 50,height = 50):
        self.x = x
        self.y = y
        self.width = width
        self.xwidth = x + width
        self.height = height
        self.yheight = y + height
        self.mcanvas = canvas

    def create(self):
        self.mcanvas.create_rectangle(self.x, self.y, self.xwidth, self.yheight, outline = "red", fill = 'yellow')


#전역변수
gamespeed = 1
speed = 0.6
velx = 0
vely = 0
x = 800
y = 0
jumpstatus = True
obstacles = []


#Test
lastkey = ''

#Gui
root = Tk()
mCanvas = Canvas(root, bg = "#222222", bd = 3, width = 1600, height = 800)

#objects
img = PhotoImage(file = "src/hi_2.png")
user = mCanvas.create_rectangle(x, y, x+50, y+50, outline = 'white', fill = 'white')
obstacle1 = obstacle(800, 480 ,mCanvas,100,10)
obstacle2 = obstacle(600, 700, mCanvas,1000, 10)
obstacle3 = obstacle(1400, 480, mCanvas,100, 10)

#init
mCanvas.pack()
obstacles.append(obstacle1)
obstacles.append(obstacle2)
obstacles.append(obstacle3)

def init():
    global obstacles

    for obj in obstacles:
        obj.create()
        

def gravity():
    global vely
    vely += 9.8 * 0.0006
    

def move():
    global x
    global y
    global user
    global vely
    global obstacles
    global jumpstatus

    mCanvas.delete(user)

    if checkCollison():
        vely = 0
        jumpstatus = False
    else: 
        gravity()
        jumpstatus = True

    x += velx
    y += vely
    user = mCanvas.create_rectangle(x, y, x+50, y+50, outline = 'white', fill = 'white')

def clearboard():
    mCanvas.delete("all")


def key_press(event):
    global velx
    global vely
    global y
    global lastkey 
    global speed

    lastkey = event.keysym

    if(lastkey == "Left"):
        velx = -speed
    if(lastkey == "Right"):
        velx = speed
    if(lastkey == 'Up'):
        vely -=1.7
        y -= 4

def keyLeft(event):
    global velx
    velx = -speed

def keyRight(event):
    global velx
    velx = speed

def keyUp(event):
    global vely
    global y
    global jumpstatus

    if jumpstatus == False:
        vely -=1.7
        y -= 4
    else:
        return


def key_release(event):
    global velx
    global lastkey
    if lastkey == 'Up':
        return
    else:
        velx = 0

def checkCollison():
    global obstacles

    for obj in obstacles:
        p1x = x
        p1y = y
        p2x = x + 50
        p2y = y + 50
        p3x = obj.x
        p3y = obj.y
        p4x = obj.xwidth
        p4y = obj.yheight
        
        '''overlapped = not( p4x < p1x \
                        or p3x > p2x \
                        or p2y < p3y \
                        or p1y > p4y)'''
        overlapped = not( p4x < p1x \
                        or p3x > p2x \
                        or p2y != p3y )
        overlapped = (p3x < p1x and p2x < p4x) and ( abs(p2y-p3y) < 5)

        if overlapped:
            break
    return overlapped

def gameLoop():
    global x
    global y

    move()

    if x+50 > 1600 :
        x = 1500
        y = 0
    if y+50 > 800 :
        x = 500
        y = 0

    root.after(gamespeed, gameLoop)

mCanvas.focus_set()
mCanvas.bind("<Left>", keyLeft)
mCanvas.bind("<Right>", keyRight)
mCanvas.bind("<Up>", keyUp)
mCanvas.bind("<KeyRelease>", key_release)

init()
gameLoop()
root.mainloop()