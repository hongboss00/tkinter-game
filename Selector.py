from tkinter import *
class Selector:
   
    #객체 초기화 main.py에 구현할 cansvas를 인수로 받아옴
    def __init__(self, canvas, tk):
        self.root = tk
        self.mcanvas = canvas
        self.level = 0                  #초기 이지 하드 값 0 = easy, 1 = hard
        self.unit_index = 0             #초기 캐릭터 index list로 표현할 것이므로 index값 0,1,2 3개 존재
        
        self.selected = False
        self.level_selected = False     #Level이 선택되었는지 확인 False:선택 안됨 
                                        #enter키를 누를때 True로 바꿔준다              
                                        #leve_selected가 True고 Enter가 눌렸을때 True로 바꿔준다.
        self.select_index = 0

        self.x = 200
        self.y = 150
        
        self.root.bind("<space>", self.keySpace)

        self.img1 = PhotoImage(file = "unit1.png").subsample(2)
        self.img2 = PhotoImage(file = "unit2.png").subsample(2)
        self.img3 = PhotoImage(file = "unit3.png").subsample(2)

    #Level 선택 창 easy / hard
    def LevelSprite(self, selected):

        if not selected:
            self.mcanvas.delete('all')

            if not self.level_selected:
                self.mcanvas.create_rectangle(self.x + 400*(self.select_index%3),self.y,
                                            self.x + 400*(self.select_index%3)+400,self.y+400,
                                            outline = 'white', fill = 'white')

            self.mcanvas.create_text(400, 200, fill = '#222222', font = ('Arial', 40), anchor = CENTER,
                                        text = 'EASY')
            self.mcanvas.create_text(800, 200, fill = '#222222', font = ('Arial', 40), anchor = CENTER,
                                        text = 'NORMAL')
            self.mcanvas.create_text(1200, 200, fill = '#222222', font = ('Arial', 40), anchor = CENTER,
                                        text = 'HARD')

            self.mcanvas.create_image(400, 400, anchor = CENTER, image = self.img1)
            self.mcanvas.create_text(400, 500, fill = '#222222', font = 'Arial', anchor = CENTER,
                                        text = 'DONG EUI')

            self.mcanvas.create_image(800, 400, anchor = CENTER, image = self.img2)
            self.mcanvas.create_text(800, 500, fill = '#222222', font = 'Arial', anchor = CENTER,
                                        text = 'SEONG GI')

            self.mcanvas.create_image(1200, 400, anchor = CENTER, image = self.img3)
            self.mcanvas.create_text(1200, 500, fill = '#222222', font = 'Arial', anchor = CENTER,
                                        text = 'HYUN RO')
            self.mcanvas.create_text(800, 700, fill = 'white', font = 'Arial', anchor = CENTER,
                                        text = 'PRESS <SPACE> TO SELECT AND PRESS <INSERT> TO START')
        else:
            self.mcanvas
            pass
        
            
    ''' 키보드 왼쪽 오른쪽으로 난이도 / 캐릭터 고르고 확정되면 Enter로 확정
        즉 난이도 고르고 엔터 누르고 캐릭터 고르고 엔터 누르면 게임시작'''


    #키보드 space 버튼을 눌렀을때
    def keySpace(self, event):
        self.select_index += 1
        return

    #키보드 insert 버튼을 눌렀을때 게임시작
    def keyInsert(self, event):
        self.selected = True
        return

    #selected가 True가 되면 다음 화면 즉 게임이 시작됨 main.py에서 이 함수를 부른다
    def Selected(self):
        #return self.level_selected and self.unit_selected
        return self.selected

    def getUnitindex(self):
        return (self.select_index % 3)