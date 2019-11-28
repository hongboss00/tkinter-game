class Character:
    def __init__(self, x, y, dx, dy, tk, canvas, width=50, height=50):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.width = width
        self.height = height

        self.xwidth = self.x + self.width
        self.yheight = self.y + self.height

        self.root = tk
        self.mcanvas = canvas

    def draw(self):
        self.mcanvas.create_rectangle(self.x, self.y, self.xwidth, self.yheight, outline = "red", fill = 'yellow')

    #주인공 x, y 좌표 설정
    def move(self):
        self.x += self.dy
        self.y += self.dy

    #주인공 속도 조절
    def setDx(self, dx):
        self.dx = dx
    def setDy(self, dy):
        self.dy = dy
    

    

    