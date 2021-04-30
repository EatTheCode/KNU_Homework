import pygame
from pygame.rect import *
import random
from item.bad import badItem
from item.good import goodItem

#전역변수
isActive =True
SCREEN_WIDTH=800
SCREEN_HEIGHT=800
BIRD_WIDTH=30
BIRD_HEIGHT=30
move=Rect(0,0,0,0)
time_delay=0
score=0
isGameOver=False
birdNumber=30
birdSpeed=1

def eventProcess():
    for event in pygame.event.get(): #유저가 입력한 것 리스트를 사용하여 가져옴
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
            if event.key==pygame.K_LEFT:
                move.x=-1
            if event.key==pygame.K_RIGHT:
                move.x=1
            if event.key==pygame.K_UP:
                move.y=-1
            if event.key==pygame.K_DOWN:
                move.y=1


def movePlayer():
    recPlayer.x +=move.x
    recPlayer.y +=move.y
    if recPlayer.x <0:
        recPlayer.x=0
    if recPlayer.x >SCREEN_WIDTH-recPlayer.width:
        recPlayer.x=SCREEN_WIDTH-recPlayer.width
    if recPlayer.y <0:
        recPlayer.y=0
    if recPlayer.y >SCREEN_HEIGHT-recPlayer.height:
        recPlayer.y=SCREEN_HEIGHT-recPlayer.height
    SCREEN.blit(player,recPlayer)

def timeDelay():
    global time_delay
    if time_delay>6:
        time_delay=0
        return True
    time_delay+=1
    return False

def makeBird():#랜덤한 위치에 새 출력
    if timeDelay():
        index=random.randint(0,len(bird)-1)
        if recBird[index].x==-1:
            recBird[index].y=random.randint(0,SCREEN_HEIGHT)
            recBird[index].x=SCREEN_WIDTH


def moveBird():
    makeBird()
    for i in range(len(bird)):
        if recBird [i].x==-1:
            continue
        recBird[i].x-=birdSpeed
        if recBird[i].x<=0:
            recBird[i].x=SCREEN_WIDTH
            recBird[i].y=random.randint(0,SCREEN_HEIGHT)
        SCREEN.blit(bird[i],recBird[i])

def checkCollision():
    global score,isGameOver
    if isGameOver:
        return
    for rec in recBird:
        if rec.x==-1:
            continue
        if rec.top<recPlayer.bottom \
            and recPlayer.top<rec.bottom\
            and rec.left<recPlayer.right\
            and recPlayer.left<rec.right:
            print("충돌")
            isGameOver=True
            break
    score+=1

def setText():
    global score
    font=pygame.font.SysFont("arial",20,True,False)
    SCREEN.blit(font.render(f"score : {score}",True,'red'),(10,10,10,10))

def makeItem():
    #pass
    #if timeDelay():
        if random.randint(1,1800)==1:
            items.append(badItem())
        elif random.randint(1,1800)==2:
            items.append(goodItem())

def moveItem():
    #pass
    global birdSpeed
    for i in range(len(items)):
        items[i].moveItem(SCREEN,SCREEN_WIDTH,SCREEN_HEIGHT)
        if items[i].checkCollision(recPlayer):
                birdSpeed=items[i].setSpeed()


pygame.init()
SCREEN =pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('test')

#item
items=[]

#player
player=pygame.image.load('airplane.png')
player=pygame.transform.scale(player,(30,30))
recPlayer =player.get_rect()
recPlayer.centerx=(1)
recPlayer.centery=(SCREEN_HEIGHT/2)

#bird
bird=[pygame.image.load('bird.jpg') for i in range(birdNumber)]
recBird=[None for i in range(len(bird))]
for i in range(len(bird)):
    bird[i]=pygame.transform.scale(bird[i],(BIRD_WIDTH,BIRD_HEIGHT))
    recBird[i]=bird[i].get_rect()
    recBird[i].x=-1

#item

clock=pygame.time.Clock()

while isActive:
    SCREEN.fill((255,255,255))
    eventProcess()
    movePlayer()#유저 이동
    moveBird()# 새 이동
    checkCollision()#충돌
    makeItem()#아이템 생성
    moveItem()#아이템 이동 및 속도 변화
    setText()
    pygame.display.flip()#화면 갱신
    clock.tick(100)