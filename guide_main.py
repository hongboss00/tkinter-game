from tkinter import *
from Map import *
from Character import *
from random import *
from math import *
from Selector import *

class pattern:
    def __init__(self, canvas):
        self.x = 700
        self.y = 650
        self.mcanvas = canvas
        self.dx = 0.8
        self.dy = 0
        self.t = 0

        self.obj = object()
        self.obj2 = object()

    def create(self):
        self.obj = self.mcanvas.create_rectangle(-50, 650, 50,50, outline = 'green', fill = 'green')
        

    def start(self):
        self.t += 0.3
        self.mcanvas.delete(self.obj)
        self.x = 500*sin(0.02*self.t) + 5
        self.y += self.dy
        self.obj = self.mcanvas.create_rectangle(self.x, self.y, self.x + 50, self.y +50, outline = 'green', fill = 'green')    

        '''self.mcanvas.delete(self.obj)
        self.x -= self.dx
        self.y += self.dy
        self.obj = self.mcanvas.create_rectangle(self.x, self.y, self.x + 50, self.y +50, outline = 'green', fill = 'green')'''

        


#전역객체 초기화
root = Tk()
mCanvas = Canvas(root, bg = "#222222", bd = 3, width = 1600, height = 800)
mCanvas.pack()

user = Character(775, 400, root, mCanvas)

#맵구현부
flat1 = Map(0,750, 1600, mCanvas)
flat2 = Map(80,600, 360, mCanvas)
flat3 = Map(490,450, 620, mCanvas)
flat4 = Map(1160,600, 360, mCanvas)
map1 = [flat1,flat2,flat3,flat4]

#전역변수 초기화
unit_speed = 0.5
game_speed = 5          #1ms 단위로 canvas 업데이트 gameLoop()참고

page = 1
selected = False

#Test
testP = pattern(mCanvas)
page1 = Selector(mCanvas, root)

def keyInsert(event):
    global selected
    selected = True

#초기화 할 것들 정리
def init():
    pass

def createMap():
    #map1 생성
    for flat in map1:

        flat.create()

def selectorLoop(selected):
        page1.LevelSprite(selected)

#실제 gameLoop game_speed로 설정한 초만큼 화면을 표현 즉, 1ms마다 화면 갱신
def gameLoop():
    global game_speed
    global page
    global mCanvas
    global selected

    #user.clearCanvas()
    if user.checkCollison(map1):
        user.setDy(0)
        user.setJumpStatus(False)
    else:
        user.Gravity()
        user.setJumpStatus(True)
    user.move()
    user.draw()

    if not(0 < user.x or user.x < 1600):
        user.setDx(0)
        
    #testP.start()

def mainLoop():
    global selected
    global game_speed

    if not selected:
        selectorLoop(selected)
    elif selected:
        mCanvas.delete('all')
        #print(page1.getUnitindex())
        createMap()
        gameLoop()
    
    root.after(5, mainLoop)


#구현부
init()
root.bind("<Insert>", keyInsert)

#test
#testP.create()
mainLoop()
root.mainloop()