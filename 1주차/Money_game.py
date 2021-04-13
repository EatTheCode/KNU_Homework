import pygame
import time
import random
from pygame.locals import *

pygame.init()


size = [1280, 720]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Money Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



done = False
flag_1 = True
clock = pygame.time.Clock()
key_status = ""
key = None

font = pygame.font.SysFont('malgungothic', 30)
font_1 = pygame.font.SysFont('malgungothic', 25)


def text_render(a, b, c):
    text = font_1.render(a, True, GREEN)
    screen.blit(text, (b, c))


def IMG_Draw(path, a, b):
    image = pygame.image.load(path)
    x = a
    y = b
    screen.blit(image, (x, y))


bitcoin_price = 100
money = 500
bitcoin = 0
elapsed_time = 0
counter = 0



while not done:

    clock.tick(10)

    screen.fill(WHITE)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:
            done = True

    counter = counter + 1
#    print(counter)

    if counter > 40:
        counter = counter - 40
        elapsed_time = elapsed_time+1
        print(elapsed_time)










    if elapsed_time - 1 == 0:
        random_number = random.randrange(-80, 80)
        change = random_number
        elapsed_time = elapsed_time - 1
        bitcoin_price = bitcoin_price + change
        print(elapsed_time)

    if bitcoin_price < 9:
        bitcoin_price = bitcoin_price + 10


    keys = pygame.key.get_pressed()

    title = font.render("B를 누르면 구입됩니다, S를 누르면 판매됩니다", True, RED)
    screen.blit(title, (360,50))
    discribe = font_1.render("게임설명", True, BLUE)
    screen.blit(discribe, (570, 90))
    discribe2 = font_1.render("코인의 가격이 수시로 변합니다. 저렴할때 구입하고 비쌀때 팔아서 현금 5000만원을 넘어보세요", True, BLACK)
    screen.blit(discribe2, (180, 130))
#    running_time = font_1.render("시간" + str(elapsed_10sec), True, BLACK)
#    screen.blit(running_time, (180, 150))

    IMG_Draw('bitcoin_250.png', 800, 225)
    IMG_Draw('cash_200.png', 100, 250)

    my_money = font_1.render("보유 현금 : " + str(money), True, BLACK)
    screen.blit(my_money, (200, 500))

    my_bit = font_1.render("보유 비트 : " + str(bitcoin), True, BLACK)
    screen.blit(my_bit, (860, 550))

    bit_price = font_1.render("코인 가격 : " + str(bitcoin_price), True, BLACK)
    screen.blit(bit_price, (860, 500))


    if keys[pygame.K_b]:
        time.sleep(0.3)
        if money < bitcoin_price:
            text_render("돈이 부족합니다", 400, 500)
        else:
            text_render("코인을 구입했습니다", 400, 500)
            money = money - bitcoin_price
            bitcoin = bitcoin + 1

    elif keys[pygame.K_s]:
        time.sleep(0.3)
        if bitcoin == 0:
            text_render("코인이 없습니다", 400, 500)
        else:
            text_render("코인을 판매했습니다", 400, 500)
            money = money + bitcoin_price
            bitcoin = bitcoin - 1

    if money > 5000:
        text_render("승리하였습니다", 400, 500)
        break


    pygame.display.flip()

pygame.quit()
