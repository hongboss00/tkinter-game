from tkinter import *

class Character:
    def __init__(self, x, y, tk, canvas, width=40, height=40):
        self.speed = 3
        self.jump = 8
        self.jump_option = 7

        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.width = width
        self.height = height

        self.xwidth = self.x + self.width
        self.yheight = self.y + self.height
        
        self.jumpstatus = False
        self.overlapped = False

        self.root = tk
        self.mcanvas = canvas
        self.obj = object()

        self.unit_index = 0
        self.unit_photo = [PhotoImage(file = 'unit1.png').subsample(4), 
                            PhotoImage(file = 'unit2.png').subsample(4), 
                            PhotoImage(file = 'unit3.png').subsample(4)]

        self.root.bind('<Left>', self.keyLeft)
        self.root.bind('<Right>', self.keyRight)
        self.root.bind('<Up>', self.keyUp)
        self.root.bind('<KeyRelease>', self.keyRelease)


    def draw(self):
        '''self. obj = self.mcanvas.create_rectangle(self.x, self.y, 
                                                  self.x + self.width,
                                                  self.y + self.height,
                                                  outline = "red", fill = 'yellow')'''
        self.obj = self.mcanvas.create_image(self.x, self.y, image = self.unit_photo[self.unit_index])

    #주인공 x, y 좌표 설정
    def move(self):
        self.x += self.dx
        self.y += self.dy

    #주인공 속도 조절
    def setDx(self, dx):
        self.dx = dx
    def setDy(self, dy):
        self.dy = dy

    #중력 적용
    def Gravity(self):
        self.dy += 9.8 * 0.02
        
    #점프는 한번만 허용
    def setJumpStatus(self, whether):
        self.jumpstatus = whether


    def clearCanvas(self):
        self.mcanvas.delete(self.obj)

    

    def checkCollison(self, map):
        for obj in map:
            p1x = self.x
            p1y = self.y
            p2x = self.x + self.width
            p2y = self.y + self.height
            p3x = obj.x
            p3y = obj.y
            p4x = obj.xwidth
            p4y = obj.yheight

            self.overlapped = ((p3x < p1x and p2x < p4x) \
                                or (p1x < p3x < p2x) or \
                                    (p1x <p4x<p2x ))and (abs(p2y - p3y) < 4)
            if self.overlapped:
                break
        return self.overlapped


    def keyLeft(self, event):
        self.dx = -self.speed    
    def keyRight(self, event):
        self.dx = self.speed
    def keyUp(self, event):
        if not self.jumpstatus:
            self.dy -= self.jump
            self.y -= self.jump_option
        else:
            return
    def keyRelease(self, event):
        if event.keysym == 'Up':
            return
        else:
            self.dx = 0

    def setUnit(self, unit_index):
        self.unit_index = unit_index