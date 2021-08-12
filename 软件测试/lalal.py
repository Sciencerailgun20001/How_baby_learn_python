# import calendar
# calendar.setfirstweekday(firstweekday=6)
# print(calendar.calendar(2019, w=1, l=1, c=5))

#
# import datetime
# today = datetime.date.today()
# print (today)
# tomorrow = today + datetime.timedelta(days=1)
# print(tomorrow)
#

import datetime
import pygame,sys,random,os
from pygame.locals import*

state = 'START'
que = ''
isRight = 'none'
def fillText(text, position):
    TextFont = pygame.font.Font('images/font1.ttf', 50)
    newText = TextFont.render(text, True, (234,255,128))
    canvas.blit(newText, position) 

def handleEvent():
    global state,que
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_n:
            state = 'RUNNING'
            que = 1
        if state == 'WIN':
            if event.type == MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if 1200>x>1000 and 660>y>600:
                    exit()
        
def button():
    global isRight,que,wt
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                return 'UP'
            elif event.key == K_DOWN:
                return 'DOWN'
            elif event.key == K_LEFT:
                return 'LEFT'
            elif event.key == K_RIGHT:
                return 'RIGHT'
        if isRight==True:
            if event.type == MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if 1200>x>1000 and 660>y>600:
                    que += 1
                    if que <=5:
                        wt = pygame.image.load("images/"+str(que)+".png")
                    isRight = 'none'
        
            

def question():
    global state,que,isRight
    if que == 1:
        k = button()
        if k == 'DOWN':
            isRight = True
            comPaint()
        if k=='UP' or k=='LEFT' or k=='RIGHT':
            isRight = False
            comPaint()
    if que == 2:
        k = button()
        if k == 'DOWN':
            isRight = True
            comPaint()
        if k=='UP' or k=='RIGHT' or k=='LEFT':
            isRight = False
            comPaint()
    if que == 3:
        k = button()
        if k == 'DOWN':
            isRight = True
            comPaint()
        if k=='UP' or k=='LEFT' or k=='RIGHT':
            isRight = False
            comPaint()
    if que == 4:
        k = button()
        if k == 'UP':
            isRight = True
            comPaint()
        if k=='RIGHT' or k=='DOWN' or k=='LEFT':
            isRight = False
            comPaint()
    if que == 5:
        k = button()
        if k == 'UP':
            state = 'WIN'
        if k=='LEFT' or k=='DOWN' or k=='RIGHT':
            isRight = False
            
            
def comPaint():
    global isRight
    if isRight==True:
            canvas.blit(wt,(0,0))
            canvas.blit(bingo,(1000,620))
    elif isRight=='none':
        canvas.blit(wt,(0,0))
        canvas.blit(error,(1000,620))
    elif isRight==False:
        canvas.blit(wt,(0,0))
        canvas.blit(error,(1000,620))
        
        
canvas.blit(s,(0,0))
fillText('',(500,650))

            

while True:
    if state == 'RUNNING':
        comPaint()
        question()
    if state == 'WIN':
        canvas.blit(wt,(0,0))
        canvas.blit(goahead,(1000,620))
        
    handleEvent()
    pygame.display.update()



flag = True
while flag:
    a = int(input("请输入年"))
    if 1900 <= a <= 2050:
        flag = False
    else:
        flag = True
        print("输入越界请重新输入一个大于1900且小于2050的数")

flag = True
while flag:
    b = int(input("请输入月"))
    if 1 <= b <= 12:
        flag = False
    else:
        flag = True
        print("输入越界请重新输入一个大于1且小于12的数")
        # b = input()

flag = True
while flag:
    c = int(input("请输入日"))
    if b == 1 or b==3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
        if 1 <= c <= 31:
            flag = False
        else:
            flag = True
            print("输入越界请重新输入一个大于0且小于31的数")
        # c = input()
    elif b == 3 or b == 4 or b == 6 or b == 9 or b == 11:
        if 1 <= c <= 30:
            flag = False
        else:
            flag = True
            print("输入越界请重新输入一个大于0且小于30的数")
            # c = input()
    elif b == 2:
        if a % 4 == 0 or a % 100 != 0:
            if 1 <= c <= 29:
                flag = False
            else:
                flag = True
                print("输入越界请重新输入一个大于0且小于29的数")
                # c = input()
        else:
            if 1 <= c <= 28:
                flag = False
            else:
                flag = True
                print("输入越界请重新输入一个大于0且小于28的数")
                # c = input()

d1 = datetime.date(a, b, c)
print(d1)
print(d1 + datetime.timedelta(+1))  # timedelta(day=0,seconds=0,microseconds=0)
