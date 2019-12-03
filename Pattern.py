from Enemy import *
class Pattern(object):
    def __init__(self, tk, canvas, character):
        self.root =tk
        self.mcanvas = canvas
        self.unit = character
        self.enemies = []

    def whetherTouched(self):
        overlapped = False
        for i in self.enemies:
            if i.checkCollision(self.unit):
                overlapped = True
        return overlapped

class Pattern1(Pattern):
    def __init__(self, tk, canvas, character):
        super().__init__(tk, canvas, character)

        self.t = 0

        self.enemy1 = Enemy(0 ,0 ,self.root, self.mcanvas, 0)

        self.enemy2_1 = Enemy(-150 , -100 ,self.root, self.mcanvas, 1)
        self.enemy2_2 = Enemy(-150 ,900 ,self.root, self.mcanvas, 1)
        self.enemy2_3 = Enemy(1750 ,-100 ,self.root, self.mcanvas, 1)
        self.enemy2_4 = Enemy(1750 ,900 ,self.root, self.mcanvas, 1)

        self.enemy3_1 = Enemy(400, 1000,self.root, self.mcanvas, 2)
        self.enemy3_2 = Enemy(800, 1200, self.root, self.mcanvas, 2)
        self.enemy3_3 = Enemy(1200,  1400, self.root, self.mcanvas, 2)

        self.enemy4_1 = Enemy(-100, 100, self.root, self.mcanvas, 3)
        self.enemy4_2 = Enemy(-100, 400, self.root, self.mcanvas, 3)
        self.enemy4_3 = Enemy(-100, 700, self.root, self.mcanvas, 3)

        self.enemy5_1 = Enemy(-40, -20, self.root, self.mcanvas, 4)

        self.many = []
        for i in range(5):
            self.many.append(Enemy(0, 0, self.root, self.mcanvas, 0))

        self.enemies = [self.enemy1, self.enemy2_1, self.enemy2_2, self.enemy2_3,self.enemy2_4,
                        self.enemy3_1, self.enemy3_2, self.enemy3_3,
                         self.enemy4_1,  self.enemy4_2,  self.enemy4_3,
                         self.enemy5_1]
    
    def show1(self, t):
        if 9000> t > 1000:
            self.enemy3_1.setDy(-5)
            self.enemy3_2.setDy(-5)
            self.enemy3_3.setDy(-5)

            self.enemy3_1.move()
            self.enemy3_2.move()
            self.enemy3_3.move()

            self.enemy3_1.draw()
            self.enemy3_2.draw()
            self.enemy3_3.draw()

    def show2(self, t):
        if 9000 > t > 3000:
            self.enemy4_1.setDx(5)
            self.enemy4_2.setDx(5)
            self.enemy4_3.setDx(5)

            self.enemy4_1.move()
            self.enemy4_2.move()
            self.enemy4_3.move()

            self.enemy4_1.draw()
            self.enemy4_2.draw()
            self.enemy4_3.draw()
    
    def show3(self, t):
        if 9000 > t > 5000:
            self.enemy2_1.setDx(4)
            self.enemy2_2.setDx(4)
            self.enemy2_3.setDx(-4)
            self.enemy2_4.setDx(-4)

            self.enemy2_1.setDy(3)
            self.enemy2_2.setDy(-3)
            self.enemy2_3.setDy(3)
            self.enemy2_4.setDy(-3)

            self.enemy2_1.move()
            self.enemy2_2.move()
            self.enemy2_3.move()
            self.enemy2_4.move()

            self.enemy2_1.draw()
            self.enemy2_2.draw()
            self.enemy2_3.draw()
            self.enemy2_4.draw()
    def show4(self, t):
        if t > 7000:

            self.enemy5_1.setDx(2)
            self.enemy5_1.move()
            self.enemy5_1.draw()
            '''if t > 7500:
                self.many[0].set'''

