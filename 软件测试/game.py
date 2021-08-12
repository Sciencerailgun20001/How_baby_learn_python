import pygame,sys,random,os
from pygame.locals import*
pygame.init()
canvas=pygame.display.set_mode((1200,720))
pygame.display.set_caption('题目')
a = pygame.image.load("图片路径.jpg")
s = pygame.transform.smoothscale(a, (1200,720))#平滑缩放图片
wt = pygame.image.load("图片路径。png")
bingo = pygame.image.load("图片路径.png")
error  = pygame.image.load("图片路径.png")
goahead = pygame.image.load("图片路径.png")
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
                    pygame.quit()
                    os.system('python 跳转.py')
                    sys.exit()
        
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
            fillText('想写的文字',(50,520))
    elif isRight=='none':
        canvas.blit(wt,(0,0))
        canvas.blit(error,(1000,620))
        fillText('选择答题的方法',(400,620))#要改的话记得把上面也改了，比如上下左右对应K_UP啥的
    elif isRight==False:
        canvas.blit(wt,(0,0))
        canvas.blit(error,(1000,620))
        fillText('错误提示',(400,620))
        
        
canvas.blit(s,(0,0))
fillText('',(500,650))

            

while True:
    if state == 'RUNNING':
        comPaint()
        question()
    if state == 'WIN':
        canvas.blit(wt,(0,0))
        canvas.blit(goahead,(1000,620))
        fillText('成果提示',(200,520))
        
    handleEvent()
    pygame.display.update()
