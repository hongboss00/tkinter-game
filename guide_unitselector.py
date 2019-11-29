#현로 나랑 짐승쎅쓰 하자
class Selector:
        #키보드 오른쪽 버튼 눌렀을때 
    def keyRight(self, event):
        self.select_index += 1
        print('right')
        print(self.select_index % 3)
        return

    #객체 초기화 main.py에 구현할 cansvas를 인수로 받아옴
    def __init__(self, canvas, tk):
        self.root = tk
        self.mcanvas = canvas
        self.level = 0                  #초기 이지 하드 값 0 = easy, 1 = hard
        self.unit_index = 0             #초기 캐릭터 index list로 표현할 것이므로 index값 0,1,2 3개 존재
        self.level_selected = False     #Level이 선택되었는지 확인 False:선택 안됨 
                                        #enter키를 누를때 True로 바꿔준다              
        self.unit_selected = False      #unitdl 선택되었는지 확인 False:선택안됨
                                        #leve_selected가 True고 Enter가 눌렸을때 True로 바꿔준다.
        self.select_index = 1

        self.x = 340
        self.y = 600
        
        self.root.bind("<Right>", self.keyRight)

    #Level 선택 창 easy / hard
    def LevelSprite(self):
        self.mcanvas.delete('all')
        self.mcanvas.create_rectangle(340, 400, 340+50, 400+50, outline = 'white', fill = 'white')
        self.mcanvas.create_rectangle(680, 400, 680+50, 400+50, outline = 'white', fill = 'white')
        self.mcanvas.create_rectangle(1020, 400, 1020+50, 400+50, outline = 'white', fill = 'white')
        if not self.level_selected:
            self.mcanvas.create_rectangle(self.x + self.x*(self.select_index%3),self.y,
                                        self.x + self.x*(self.select_index%3)+30,self.y+30,
                                        outline = 'white', fill = 'white')
        

    #character 선택 창 캐릭터는 총 3개
    def UnitSprite(self):
        pass
        

    
    ''' 키보드 왼쪽 오른쪽으로 난이도 / 캐릭터 고르고 확정되면 Enter로 확정
        즉 난이도 고르고 엔터 누르고 캐릭터 고르고 엔터 누르면 게임시작'''
    #키보드 왼쪽 버튼 눌렀을때 
    def keyLeft(self, event):
        self.select_index -=1
        return


    #키보드 엔터 버튼 눌렀을때 
    def keyEnter(self, event):
        if self.level_selected:
            self.level_selected = True
        else:
            self.unit_selected = True
        return

    #selected가 True가 되면 다음 화면 즉 게임이 시작됨 main.py에서 이 함수를 부른다
    def Selected(self):
        return self.level_selected and self.unit_selected