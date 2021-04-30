import pygame
from pygame.rect import *
import random
class bird:
    def __init__(self,screen):
        self.bird_width=30
        self.bird_height=30
        self.time_delay=0
        self.birdSpeed=2
        self.screen =screen
        self.bird=pygame.image.load('bird.jpg')
        self.bird=pygame.transform.scale(self.bird,(self.bird_width,self.bird_height))
        self.recBird=self.bird.get_rect()
        self.recBird.x=-1

    def makeBird(self,screen_width,screen_height):#랜덤한 위치에 새 출력
        self.recBird.y=random.randint(0,screen_height)
        self.recBird.x=screen_width

    def moveBird(self,screen_width,screen_height):
        if self.recBird.x==-1:
            return
        self.recBird.x-=self.birdSpeed
        if self.recBird.x<=0:
            self.recBird.x=screen_width
            self.recBird.y=random.randint(0,screen_height)
        self.screen.blit(self.bird,self.recBird)

    def setSpeed(self,speed):
        self.birdSpeed=speed
