from tkinter import *
from Map import *
from Character import *
from random import *
from math import *
from Selector import *
from Pattern import *
from Score import *


#전역객체 초기화
root = Tk()
mCanvas = Canvas(root, bg = "#222222", bd = 3, width = 1600, height = 800)
mCanvas.pack()

user = Character(775, 600, root, mCanvas)
Pattern1 = Pattern1(root, mCanvas, user)

Looper = object()

#맵구현부
flat1 = Map(0,750, 1600, mCanvas)
flat2 = Map(80,600, 360, mCanvas)
flat3 = Map(490,450, 620, mCanvas)
flat4 = Map(1160,600, 360, mCanvas)
map1 = [flat1,flat2,flat3,flat4]

#전역변수 초기화
unit_speed = 0.5
game_speed = 10                         #1ms 단위로 canvas 업데이트 gameLoop()참고
t = 0                                   #pattern timer 겸사 겸사 score
selected = False                        #page2에서 Level 골랐는지 확인
death = False

#page
page1 = Selector(mCanvas, root)
page3 = Score(root, mCanvas)

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
    global mCanvas
    global selected
    global Pattern1
    global t
    global death


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
    t += 10
    Pattern1.show1(t)
    Pattern1.show2(t)
    Pattern1.show3(t)
    #Pattern1.show4(t)
    if Pattern1.whetherTouched():
        #mCanvas.create_rectangle(0,0,100,100, fill = 'white')
        death = True

    mCanvas.create_text(50,50, text = str(t), fill = 'white', font = ('Arial', 20),
                        anchor = NW)

def score():
    global page3
    global t
    
    page3.recieveScore(t)
    page3.show()
        

def mainLoop():
    global selected
    global game_speed
    global death
    global Looper

    if not selected:
        selectorLoop(selected)
    elif selected and (not death):
        mCanvas.delete('all')
        user.setUnit(page1.getUnitindex())
        createMap()
        gameLoop()
    elif death:
        mCanvas.delete('all')
        score()
        #root.after_cancel(Looper)
    
    Looper = root.after(game_speed, mainLoop)


#구현부
init()
root.bind("<Insert>", keyInsert)
mainLoop()
root.mainloop()