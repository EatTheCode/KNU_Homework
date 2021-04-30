import pygame
from pygame.rect import *
import random
class goodItem:
    def __init__(self):
        self.item=pygame.image.load('medicine.png')
        self.item=pygame.transform.scale(self.item,(50,50))
        self.recItem =self.item.get_rect()

    def setSpeed(self):
        return 1

    def moveItem(self,SCREEN,SCREEN_WIDTH,SCREEN_HEIGHT):
        self.recItem.x-=2
        if  self.recItem.x<0:
             self.recItem.x=SCREEN_WIDTH
             self.recItem.y=random.randint(0,SCREEN_HEIGHT)
        SCREEN.blit(self.item, self.recItem)


    def checkCollision(self,recPlayer):
        if self.recItem.top<recPlayer.bottom \
            and recPlayer.top<self.recItem.bottom\
            and self.recItem.left<recPlayer.right\
            and recPlayer.left<self.recItem.right:
            return True