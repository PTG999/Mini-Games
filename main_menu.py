import pygame
from pygame.locals import * 
import time
pygame.init()  
screen=pygame.display.set_mode((300,500)) 
pygame.display.set_caption("Base Code")
def show_text(msg, x, y, color, size):
    fontobj= pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))
def menu():
    pygame.init()  
    screen=pygame.display.set_mode((300,500))  
    pygame.display.set_caption("Base Code")
    white=(255,255,255)
    black=(0,0,0)
    red=(255,0,0)
    dred=(130, 22, 22)
    green=(107, 194, 76)
    dgreen=(36, 74, 21)
    blue=(0,0,255)
    yellow=(255, 196, 33)
    dyellow=(166, 127, 18)
    light_yellow=(255, 201, 115)
    redorange=(255, 89, 64)
    purple=(236, 112, 255)
    dpurple=(143, 46, 158)
    yellow2=(255, 203, 59)
    dark_blue=(12,38,79)
    dblue=(3, 14, 31)
    light_blue=(136, 168, 219)
    fcolor=yellow
    pcolor=purple
    tcolor=dark_blue
    scolor=green
    qcolor=red
    while True: 
        f=pygame.draw.rect(screen,fcolor,(50,50,200,50))
        pygame.draw.circle(screen,light_yellow,(50,75),20)
        pygame.draw.line(screen,redorange,(240,75),(265,70),5)
        pygame.draw.line(screen,redorange,(240,75),(265,80),5)
        pygame.draw.circle(screen,white,(220,70),12)
        pygame.draw.circle(screen,black,(227,70),5)
        show_text("Flappy Bird",90,60,black,22)

        p=pygame.draw.rect(screen,pcolor,(50,150,200,50))
        pygame.draw.line(screen,red,(60,150),(60,180),7)
        pygame.draw.line(screen,blue,(240,160),(240,190),7)
        pygame.draw.line(screen,white,(150,150),(150,199),5)
        pygame.draw.circle(screen,yellow2,(75,170),10)
        show_text("Pong",120,160,black,27)

        t=pygame.draw.rect(screen,tcolor,(50,250,200,50))
        pygame.draw.line(screen,light_blue,(115,250),(115,299),3)
        pygame.draw.line(screen,light_blue,(175,250),(175,299),3)
        pygame.draw.line(screen,light_blue,(50,265),(250,264),3)
        pygame.draw.line(screen,light_blue,(50,285),(250,284),3)
        show_text("Tic-Tac-Toe",90,260,white,30)

        s=pygame.draw.rect(screen,scolor,(50,350,200,50))
        pygame.draw.rect(screen,dark_blue,(60,360,10,10))
        pygame.draw.rect(screen,dark_blue,(60,371,10,10))
        pygame.draw.rect(screen,dark_blue,(71,371,10,10))
        pygame.draw.rect(screen,dark_blue,(82,371,10,10))
        pygame.draw.rect(screen,dark_blue,(93,371,10,10))
        pygame.draw.circle(screen,red,(114,375),7)
        show_text("Snake",130,360,black,30)

        q=pygame.draw.rect(screen,qcolor,(100,430,100,40))
        show_text("QUIT",120,430,black,30)

        for event in pygame.event.get(): 
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==MOUSEMOTION:
                if f.collidepoint(event.pos):
                    fcolor=dyellow
                else:
                    fcolor=yellow
                if p.collidepoint(event.pos):
                    pcolor=dpurple
                else:
                    pcolor=purple
                if t.collidepoint(event.pos):
                    tcolor=dblue
                else:
                    tcolor=dark_blue
                if s.collidepoint(event.pos):
                    scolor=dgreen
                else:
                    scolor=green
                if q.collidepoint(event.pos):
                    qcolor=dred
                else:
                    qcolor=red
            if event.type==MOUSEBUTTONDOWN:
                if f.collidepoint(event.pos):
                    import flappy_bird
                    flappy_bird.flappy_bird_game()
                if p.collidepoint(event.pos):
                    import pong
                    pong.pong_game()
                if t.collidepoint(event.pos):
                    import tic_tac_toe
                    tic_tac_toe.tic_game()
                if s.collidepoint(event.pos):
                    import snake_game   
                    snake_game.snake_play()
                if q.collidepoint(event.pos):
                    time.sleep(.5)
                    exit()
        pygame.display.update() 
menu()