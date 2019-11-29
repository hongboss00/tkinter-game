from tkinter import *

#전역객체 초기화
root = Tk()
mCanvas = Canvas(root, bg = "#222222", bd = 3, width = 1600, height = 800)

#전역변수 초기화
unit_speed = 0.5
game_speed = 1          #1ms 단위로 canvas 업데이트 gameLoop()참고


#초기화 할 것들 정리
def init():
    pass

#실제 gameLoop game_speed로 설정한 초만큼 화면을 표현 즉, 1ms마다 화면 갱신
def gameLoop():
    global game_speed
    root.after(game_speed, gameLoop)

#구현부
init()
gameLoop()
root.mainloop()

