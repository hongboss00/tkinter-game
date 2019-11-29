#현로 나랑 짐승쎅쓰 하자
class Selector:
    #객체 초기화 main.py에 구현할 cansvas를 인수로 받아옴
    def __init__(self, canvas):
        self.mcanvas = canvas
        self.level = 0                  #초기 이지 하드 값 0 = easy, 1 = hard
        self.unit_index = 0             #초기 캐릭터 index list로 표현할 것이므로 index값 0,1,2 3개 존재
        self.level_selected = False     #Level이 선택되었는지 확인 False:선택 안됨 
                                        #enter키를 누를때 True로 바꿔준다              
        self.unit_selected = False      #unitdl 선택되었는지 확인 False:선택안됨
                                        #leve_selected가 True고 Enter가 눌렸을때 True로 바꿔준다.


    #Level 선택 창 easy / hard
    def LevelSprite(self):


    #character 선택 창 캐릭터는 총 3개
    def UnitSprite(self):

    
    ''' 키보드 왼쪽 오른쪽으로 난이도 / 캐릭터 고르고 확정되면 Enter로 확정
        즉 난이도 고르고 엔터 누르고 캐릭터 고르고 엔터 누르면 게임시작'''
    #키보드 왼쪽 버튼 눌렀을때 
    def keyLeft(self, event):

    #키보드 오른쪽 버튼 눌렀을때 
    def keyRight(self, event):

    #키보드 엔터 버튼 눌렀을때 
    def keyEnter(self, event):

    #selected가 True가 되면 다음 화면 즉 게임이 시작됨 main.py에서 이 함수를 부른다
    def Selected(self):
        return self.level_selected and self.unit_selected