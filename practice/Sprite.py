from tkinter import *

############################## 범용 부모 클래스 생성부 ###################################
# 게임의 스프라이트를 나타내는 클래스로 공통적으로 사용되는 변수와 메소드를 가지고 있다.
class Sprite:
    # 생성자
    def __init__(self, tk, x, y, canvas, width = 0,height =0):
        self.root = tk
        #self.img = image # 스프라이트가 가지고 있는 이미지
        self.x = x # 현재 위치의 x좌표
        self.y = y # 현재 위치의 y좌표
        self.dx = 0 # 단위 시간에 움직이는 x방향 거리
        self.dy = 0 # 단위 시간에 움직이는 y방향 거리
        self.width = width
        self.height = height

        self.mcanvas = canvas
        self.obj = object()
    
    # 스프라이트의 가로 길이 반환
    def getWidth(self) :
        #return self.img.width()
        return self.width
    
    # 스프라이트의 세로 길이 반환
    def getHeight(self) :
        #return self.img.height()
        return self.height
    
    # 스프라이트를 화면에 그리기
    def draw(self) :
        #g.create_image(self.x, self.y, anchor=NW, image=self.img)
        self.obj = self.mcanvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                         outline = 'yellow', fill = 'red')
    
    # 스프라이트를 움직이는 메소드
    def move(self) :
        self.x += self.dx
        self.y += self.dy
    
    # dx를 설정하는 설정자 메소드
    def setDx(self, dx) :
        self.dx = dx
        
    # dy를 설정하는 설정자 메소드
    def setDy(self, dy) :
        self.dy = dy
        
    # dx를 반환하는 접근자 메소드
    def getDx(self) :
        return self.dx
    
    # dy를 반환하는 접근자 메소드
    def getDy(self) :
        return self.dy
    
    # x를 반환하는 접근자 메소드
    def getX(self) :
        return self.x
    
    # y를 반환하는 접근자 메소드
    def getY(self) :
        return self.y
    
    # 다른 스프라이트와의 충돌 여부를 계산한다. 충돌이면 true를 반환한다.
    def checkCollision(self, other) :
        p1x = self.x
        p1y = self.y
        p2x = self.x + self.getWidth()
        p2y = self.y + self.getHeight()
        p3x = other.x
        p3y = other.y
        p4x = other.x + other.getWidth()
        p4y = other.y + other.getHeight()
        
        overlapped = not( p4x < p1x \
                         or p3x > p2x \
                         or p2y < p3y \
                         or p1y > p4y)
        return overlapped
    
    # 충돌을 처리한다. 현재는 아무 일도 하지 않는다. 자식 클래스에서 오버라이드 한다.
    def handleCollision(self, other) :
        pass
