import pygame
from pygame.rect import *

class player:
    def __init__(self,screen,screen_width,screen_height):
        self.screen=screen
        self.screen_width=screen_width
        self.screen_height=screen_height
        self.move=Rect(0,0,0,0)
        self.score=0
        self.isGameOver=False
        self.player=pygame.image.load('airplane.png')
        self.player=pygame.transform.scale(self.player,(30,30))
        self.recPlayer =self.player.get_rect()
        self.recPlayer.centerx=(1)
        self.recPlayer.centery=(self.screen_height/2)
    
    def eventProcess(self):
        for event in pygame.event.get(): #유저가 입력한 것 리스트를 사용하여 가져옴
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                if event.key==pygame.K_LEFT:
                    self.move.x=-1
                if event.key==pygame.K_RIGHT:
                    self.move.x=1
                if event.key==pygame.K_UP:
                    self.move.y=-1
                if event.key==pygame.K_DOWN:
                    self.move.y=1

    def movePlayer(self):
        self.recPlayer.x +=self.move.x
        self.recPlayer.y +=self.move.y
        if self.recPlayer.x <0:
            self.recPlayer.x=0
        if self.recPlayer.x >self.screen_width-self.recPlayer.width:
            self.recPlayer.x=self.screen_width-self.recPlayer.width
        if self.recPlayer.y <0:
            self.recPlayer.y=0
        if self.recPlayer.y >self.screen_height-self.recPlayer.height:
            self.recPlayer.y=self.screen_height-self.recPlayer.height
        self.screen.blit(self.player,self.recPlayer)

    def checkCollision(self,birds):
        if self.isGameOver:
            return
        for bird in birds:
            if bird.recBird.x==-1:
                continue
            if bird.recBird.top<self.player.get_rect().bottom \
                and self.player.get_rect().top<bird.recBird.bottom\
                and bird.recBird.left<self.player.get_rect().right\
                and self.player.get_rect().left<bird.recBird.right:
                print("충돌")
                self.isGameOver=True
                break
        self.score+=1