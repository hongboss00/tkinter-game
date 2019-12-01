class Enemy:
    def __init__(self, canvas):
        self.x = 0
        self.y = 0
    
    def draw(self):
        self. obj = self.mcanvas.create_rectangle(self.x, self.y, 
                                                  self.x + self.width,
                                                  self.y + self.height,
                                                  outline = "red", fill = 'yellow')

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
        self.dy += 9.8 * 0.0006
        
    #점프는 한번만 허용
    def setJumpStatus(self, whether):
        self.jumpstatus = whether


    def clearCanvas(self):
        self.mcanvas.delete(self.obj)

    

    def checkCollison(self, map):