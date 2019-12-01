from tkinter import *

class Map:
    def __init__(self, x,y, width, canvas):
        self.x = x
        self.y = y
        self.width = width
        self.xwidth = self.x + self.width
        self.height = 10
        self.yheight = self.y + self.height
        self.mcanvas = canvas

    def create(self):
        self.mcanvas.create_rectangle(self.x, self.y, self.xwidth, self.yheight,
                                      outline = 'red', fill = 'red')