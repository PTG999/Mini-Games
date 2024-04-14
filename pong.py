import pygame
from pygame.locals import*
import time
pygame.init()
screen=pygame.display.set_mode((600,300))
pygame.display.set_caption("Pong Game")
def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("freesans", size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
def pong_game():
    pygame.init()
    screen=pygame.display.set_mode((600,300))
    pygame.display.set_caption("Pong Game")
    white=(255,255,255)
    black=(0,0,0)
    red=(255,0,0)
    green=(0,255,0)
    blue=(0,0,255)
    yellow2=(255, 203, 59)
    purple=(236, 112, 255)
    x=25
    y=90
    x2=550
    y2=90
    x3=300
    y3=150
    flag="stay"
    flag2="stay"
    flag3="stay"
    xchange=0.5
    ychange=0.5
    left=0
    right=0
    while True:
        screen.fill(purple)
        pygame.draw.line(screen,white,(300,0),(300,300),10)
        c=pygame.draw.circle(screen,yellow2,(x3,y3),20)
        r1=pygame.draw.rect(screen,red,(x,y,25,110))
        r2=pygame.draw.rect(screen,blue,(x2,y2,25,110))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==KEYDOWN:
                if event.key==K_w:
                    flag="up"
                if event.key==K_s:
                    flag="down"
                if event.key==K_UP:
                    flag2="up"
                if event.key==K_DOWN:
                    flag2="down"
            if event.type==KEYUP:
                flag="stay"
                flag2="stay"
        if flag=="up":
            y=y-.5
        if flag=="down":
            y=y+.5
        if flag2=="up":
            y2=y2-.5
        if flag2=="down":
            y2=y2+.5
        if y<0:
            y=0
        if y>190:
            y=190
        if y2<0:
            y2=0
        if y2>190:
            y2=190
        x3=x3+xchange
        y3=y3+ychange
        if c.colliderect(r2)==True:
            xchange=-0.5
        if c.colliderect(r1)==True:
            xchange=0.5
        if x3>=620:
            x3=300
            left+=1
        if x3<=-20:
            x3=300
            right+=1
        if y3<=20:
            ychange=.5
        if y3>=280:
            ychange=-.5
        if right>=3:
            pygame.display.update()
            show_text("PLAYER BLUE WINS!!!", 100,150,blue,50)
            pygame.display.update()
            time.sleep(1)
            import main_menu
            main_menu.menu()
        if left >=3:
            pygame.display.update()
            show_text("PLAYER RED WINS!!!",100,150,red,50)
            pygame.display.update()
            time.sleep(1)
            import main_menu
            main_menu.menu()
        show_text(str(left),25,25,black,30)
        show_text(str(right),575,25,black,30)
        pygame.display.update()
    exit()