from tkinter import *

class Score():
    #버튼 클릭시
    def clicked(self):
        self.users[self.e1.get()] = self.score
        self.sortedArr = sorted(self.users.items(), reverse = True)
        print(self.e1.get())
        self.btn_clicked = True

    def __init__(self, tk, canvas):
        self.root = tk
        self.mcanvas = canvas

        self.btn_clicked = False
        self.score = 0

        self.text = StringVar()
        self.users = {'UNKNOWN1' : 0, 'UNKNOWN2' : 0, 'UNKNOWN3' : 0, 'UNKNOWN4' : 0, 'UNKNOWN5' : 0,
        'UNKNOWN6' : 0, 'UNKNOWN7' : 0, 'UNKNOWN8' : 0, 'UNKNOWN9' : 0, 'UNKNOWN10' : 0}

        self.sortedArr = sorted(self.users.items(), reverse = True)

        self.e1 = Entry(self.root, textvariable = self.text, font = ('Arial',30 ), width = 20)
        self.b1 = Button(self.root, text = 'Enter!', command = self.clicked, 
            width = 10, height = 3, bg = 'white')

    def show(self):
        if not self.btn_clicked:
            self.mcanvas.create_text(800, 100, fill = 'white', font = ('Arial', 20), 
                            text = 'Enter Your NAME', anchor = CENTER)
            self.mcanvas.create_window(1050, 200, window = self.b1)
            self.mcanvas.create_window(780,200, window = self.e1)
        else:
            for i in range(1, 10):
                self.mcanvas.create_text(800, 250 + 40*i, text =  str(i) +': '+ self.sortedArr[i-1][0] +'    '+ str(self.sortedArr[i-1][1]), fill = 'white',
                                        anchor = N, font = ('Arial', 25))   
            
    def recieveScore(self, score):
        self.score = score
