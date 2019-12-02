import tkinter
from tkinter import *
from tkinter import messagebox

class Levelselector:
   def __init__(self, tk, canvas):
      self.root = tk

      self.game_speed = 3 #easy게임속도
      self.game_photo = tkinter.PhotoImage(file="src/hi.png")
      self.text1 = ""
      self.text2 = ""

      self.level = IntVar()
      self.champ = IntVar()

   def show(self):
      self.text1 = '난이도 선택되지 않음. ' #아무것도 선택안한 경우 출력값
      if self.level.get() == 1:
         self.text1 = "난이도 쉬움 선택, " #각 경우에 맞는 문구 할당
         self.game_speed = 3
      elif self.level.get() == 2:
         self.text1 = "난이도 보통 선택, "
         self.game_speed = 2
      elif self.level.get() == 3:
         self.text1 = "난이도 어려움 선택, "
         self.game_speed = 1

         self.text2 = '캐릭터 선택되지 않음.'
      if self.champ.get() == 4:
         self.text2 = "차영완 선택"
         self.game_photo = tkinter.PhotoImage(file="src/hi.png")
      elif self.champ.get() == 5:
         self.text2 = "홍선기 선택"
         self.game_photo = tkinter.PhotoImage(file="src/hi.png")
      elif self.champ.get() == 6:
         self.text2 = "김동의 선택"
         self.game_photo = tkinter.PhotoImage(file="src/hi.png")
         messagebox.showinfo("선택한 난이도와 캐릭터", text1+text2) #메세지 띄우기

                                                                  

#라벨 설정
i1=Label(root, text="\n\n\n\n\n\n\n\n난이도를 선택하세요.")
i1.pack()

#라디오 버튼 총 6개 선언
#각 테스트, 상황값, 인덱스
#설정된 후 변수 선
bt1 = Radiobutton(root,text="easy",value=1,variable=level) 
bt2 = Radiobutton(root,text="normal",value=2,variable=level)
bt3 = Radiobutton(root,text="hard",value=3,variable=level)
bt4 = Radiobutton(root,text="차영완",value=4,variable=champ)
bt5 = Radiobutton(root,text="홍선기",value=5,variable=champ)
bt6 = Radiobutton(root,text="김동의",value=6,variable=champ)

bt1.pack()
bt2.pack()
bt3.pack()

i2=Label(root, text="\n캐릭터를 선택하세요.")
i2.pack()

bt4.pack()
bt5.pack()
bt6.pack()

i3=Label(root, text="\n")
i3.pack()


button = Button(root,width=10, text="선택하기",overrelief="solid",command=show)
button.pack()

#다음 장면으로 넘어가기...

root.mainloop()   