from tkinter import *
from Map import *
from Character import *
from math import *
from Selector import *
from Pattern import *
from Score import *

'''class Start:
    def __init__(self, tk, canvas):
        self.root = tk
        self.mcanvas = canvas
        self.mainphoto = PhotoImage(file = 'titlepage.png')
        self.b1 = Button(self.mcanvas, text="시작하기",width=20, height=3,
            relief="solid",bg="black",fg="red")
    
    def show(self):
        self.mcanvas.create_image(800,400,image = self.mainphoto)
        self.mcanvas.create_window(1300, 700, window = self.b1)'''

#전역객체 초기화
root = Tk()
mCanvas = Canvas(root, bg = "#222222", bd = 3, width = 1600, height = 800)
mCanvas.pack()
user = Character(775, 600, root, mCanvas)
pattern1 = Pattern1(root, mCanvas, user)
mainphoto = PhotoImage(file = 'titlepage.png')


#맵 구현
flat1 = Map(0,750, 1600, mCanvas)
flat2 = Map(80,600, 360, mCanvas)
flat3 = Map(490,450, 620, mCanvas)
flat4 = Map(1160,600, 360, mCanvas)
map1 = [flat1,flat2,flat3,flat4]        #check Collison 함수 사용에 용이하기 위해 리스트로 묶음

#전역변수 초기화
unit_speed = 0.5
game_speed = 10                         #1ms 단위로 canvas 업데이트 gameLoop()참고
t = 0                                   #pattern timer 겸사 겸사 score
selected = False                        #page2에서 Level 골랐는지 확인
death = False

#page
#page0 = Start(root, mCanvas)
page1 = Selector(mCanvas, root)
page3 = Score(root, mCanvas)

#Selector select버튼 대신 Insert 사용
def keyInsert(event):
    global selected
    selected = True

#초기화 할 것들 정리
def init():
    global mainphoto
    #global b1

    b1 = Button(mCanvas, text="시작하기",width=20, height=3,
            relief="solid",bg="black",fg="red", command = mainLoop)
    mCanvas.create_image(800,400,image = mainphoto)
    mCanvas.create_window(1300, 700, window = b1)

#map 생성
def createMap():
    for flat in map1:

        flat.create()

#page 2
def selectorLoop(selected):
        page1.LevelSprite(selected)

#실제 gameLoop game_speed로 설정한 초만큼 화면을 표현 즉, 1ms마다 화면 갱신
def gameLoop():
    global game_speed
    global mCanvas
    global selected
    global pattern1
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
    pattern1.show1(t)
    pattern1.show2(t)
    pattern1.show3(t)
    #Pattern1.show4(t)
    if pattern1.whetherTouched():
        #mCanvas.create_rectangle(0,0,100,100, fill = 'white')
        death = True

    mCanvas.create_text(50,50, text = str(t), fill = 'white', font = ('Arial', 20),
                        anchor = NW)

def score():
    global page3
    global t
    global selected
    
    page3.recieveScore(t)
    page3.show()
    if page3.getrestart():
        selected = False
        death = False
        page3.setrestart(False)
        

def mainLoop():
    global selected
    global game_speed
    global death
    
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
    
    root.after(game_speed, mainLoop)


#구현부
init()
root.bind("<Insert>", keyInsert)
#mainLoop()
#page0.show()
root.mainloop()