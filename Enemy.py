from tkinter import *
class Enemy:
    def __init__(self, x, y, tk, canvas, index):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

        self.width = 100
        self.height = 100
        

        self.root = tk
        self.mcanvas = canvas

        self.index = index
        if index == 0:
            self.width = 100
            self.height = 100
        elif index == 1:
            self.width = 100
            self.height = 100
        elif index == 2:
            self.width = 100
            self.height = 100
        else:
            self.width = 100
            self.height = 100

        self.sprites = [PhotoImage(file = 'enemy1.png').subsample(3),
                        PhotoImage(file = 'enemy2.png').subsample(5),
                        PhotoImage(file = 'enemy3.png').subsample(2),
                        PhotoImage(file = 'enemy4.png').subsample(4),
                        PhotoImage(file = 'enemy2.png').subsample(2)]
    
    def draw(self):
        '''self. obj = self.mcanvas.create_rectangle(self.x, self.y, 
                                                  self.x + self.width,
                                                  self.y + self.height,
                                                  outline = "red", fill = 'yellow')'''
        self.obj = self.mcanvas.create_image(self.x, self.y,
                                            anchor = CENTER,
                                            image = self.sprites[self.index])

    #주인공 x, y 좌표 설정
    def move(self):
        self.x += self.dx
        self.y += self.dy

    #주인공 속도 조절
    def setDx(self, dx):
        self.dx = dx
    def setDy(self, dy):
        self.dy = dy

    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y

    #중력 적용
    def Gravity(self):
        self.dy += 9.8 * 0.0006
        

    def clearCanvas(self):
        self.mcanvas.delete(self.obj)

    

    def checkCollision(self, unit) :
        p1x = self.x
        p1y = self.y
        p2x = self.x + self.height
        p2y = self.y + self.width
        p3x = unit.x
        p3y = unit.y
        p4x = unit.x + unit.width
        p4y = unit.y + unit.height
        
        overlapped = not( p4x < p1x \
                         or p3x > p2x \
                         or p2y < p3y \
                         or p1y > p4y)
        return overlapped