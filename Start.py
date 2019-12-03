from tkinter import *
class Start:
    def __init__(self, tk, canvas):
        self.root = tk
        self.mcanvas = canvas
        self.mainphoto = PhotoImage(file = 'titlepage.png')
        self.b1 = Button(self.mcanvas, text="시작하기",width=20, height=3,
            relief="solid",bg="black",fg="red")
    
    def show(self):
        self.mcanvas.create_image(800,400,image = self.mainphoto)
        self.mcanvas.create_window(1300, 700, window = self.b1)

root = Tk()
mCanvas = Canvas(root, bg = "#222222", bd = 3, width = 1600, height = 800)
mCanvas.pack()

page0 = Start(root, mCanvas)
page0.show()
root.mainloop()