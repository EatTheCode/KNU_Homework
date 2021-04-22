import pygame
from pygame.rect import *
import random
from item.bad import badItem
from item.good import goodItem
from obstacle.bird import bird
from player.player import player

#전역변수
isActive =True
SCREEN_WIDTH=800
SCREEN_HEIGHT=800
time_delay=0
birdNumber=30

def timeDelay():
    global time_delay
    if time_delay>50:
        time_delay=0
        return True
    time_delay+=1
    return False

def setText():
    global score
    font=pygame.font.SysFont("arial",20,True,False)
    SCREEN.blit(font.render(f"score : {player.score}",True,'red'),(10,10,10,10))

def makeItem():
    if random.randint(1,1600)==1:
        items.append(badItem())
    elif random.randint(1,1600)==2:
        items.append(goodItem())

def moveItem():
    for i in range(len(items)):
        items[i].moveItem(SCREEN,SCREEN_WIDTH,SCREEN_HEIGHT)
        if items[i].checkCollision(player.recPlayer):
            for bird in birds:
                bird.setSpeed(items[i].setSpeed())


pygame.init()
SCREEN =pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('test')

#item
items=[]

#player
player=player(SCREEN,SCREEN_WIDTH,SCREEN_HEIGHT)

#bird
birds=[]
for i in range(birdNumber):
    birds.append(bird(SCREEN))


clock=pygame.time.Clock()

def makeBird():
    if timeDelay():
        index=random.randint(0,len(birds)-1)
        if birds[index].recBird.x==-1:
            birds[index].makeBird(SCREEN_WIDTH,SCREEN_HEIGHT)


while isActive:
    SCREEN.fill((255,255,255))
    player.eventProcess()
    player.movePlayer()#유저 이동
    for i in range(birdNumber):
        makeBird()
        birds[i].moveBird(SCREEN_WIDTH,SCREEN_HEIGHT)
        
    player.checkCollision(birds)#충돌
    makeItem()#아이템 생성
    moveItem()#아이템 이동 및 속도 변화
    setText()
    pygame.display.flip()#화면 갱신
    clock.tick(100)