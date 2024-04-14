import pygame
from pygame.locals import*
import time
import random
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake Game")
def show_text(msg, x, y, color, size):
    fontobj= pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))
def snake_play():
    pygame.init()
    screen=pygame.display.set_mode((500,500))
    pygame.display.set_caption("Snake Game")
    white=(255,255,255)
    black=(0,0,0)
    red=(255,0,0)
    green=(107, 194, 76)
    dark_blue=(12,38,79)
    light_blue=(136, 168, 219)
    yellow=(255, 196, 33)
    light_yellow=(255, 201, 115)
    redorange=(255, 89, 64)
    flag="stay"
    x=220
    y=220
    x1=(random.randint(1,500))
    y1=(random.randint(1,500))
    score=0
    def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("freesans", size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
    body=[[x,y]]
    snake_list=[]
    clock=pygame.time.Clock()
    while True:
        clock.tick(7)
        screen.fill(green)
        show_text(str(score),5,5,black,30)
        snake_list=[]
        for i in body:
            snake=pygame.draw.rect(screen,dark_blue,(i[0],i[1],30,30))
            pygame.draw.rect(screen,light_blue,(i[0],i[1],29,29),2)
            snake_list.append(snake)
        a=pygame.draw.circle(screen,red,(x1,y1),15)
        pygame.draw.circle(screen,yellow,(x1,y1),14,2)
        collide1=snake_list[0].collidelist(snake_list[2:])
        if 0<collide1<len(snake_list):
            screen.fill(light_blue)
            show_text("GAME OVER!!",100,200,black,40)
            pygame.display.update()
            time.sleep(1)
            import main_menu
            main_menu.menu()
        if a.colliderect(snake_list[0]):
            x1=(random.randint(1,500))
            y1=(random.randint(1,500))
            score=score+1
            show_text(str(score),5,5,black,30)
            pygame.display.update()
            body.insert(0,[x,y])
        for event in pygame.event.get(): 
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==KEYDOWN:
                if event.key==K_UP and flag!="down":
                    flag="up"
                if event.key==K_DOWN and flag!="up":
                    flag="down"
                if event.key==K_RIGHT and flag!="left":
                    flag="right"
                if event.key==K_LEFT and flag!="right":
                    flag="left"
                if event.key==K_w and flag!="down":
                    flag="up"
                if event.key==K_s and flag!="up":
                    flag="down"
                if event.key==K_d and flag!="left":
                    flag="right"
                if event.key==K_a and flag!="right":
                    flag="left"
        if flag=="up":
            y=y-30
        if flag=="down":
            y=y+30
        if flag=="right":
            x=x+30
        if flag=="left":
            x=x-30
        body.insert(0,[x,y])
        body.pop()
        if x>=470 or x<=0:
            screen.fill(light_blue)
            show_text("GAME OVER!!",100,200,black,40)
            pygame.display.update()
            time.sleep(1)
            import main_menu
            main_menu.menu()
        if y>=470 or y<=0:
            screen.fill(light_blue)
            show_text("GAME OVER!!",100,200,black,40)
            pygame.display.update()
            time.sleep(1)
            import main_menu
            main_menu.menu()
        pygame.display.update()