import pygame
from pygame.locals import*
import time
import random
pygame.init()
screen=pygame.display.set_mode((400,500))
pygame.display.set_caption("Flappy Bird")
def show_text(msg, x, y, color, size):
    fontobj= pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
dark_blue=(12,38,79)
light_blue=(136, 168, 219)
yellow=(255, 196, 33)
light_yellow=(255, 201, 115)
redorange=(255, 89, 64)
x=200
y=250
x1=450
x2=700
flag="down"
score=0
l=random.randint(50,300)
l1=random.randint(50,300)
bird=top=bottom=None
def bird_draw(x,y):
    global bird
    bird=pygame.draw.circle(screen,yellow,(x,y),20)
    pygame.draw.circle(screen,light_yellow,(x-15,y),10)
    pygame.draw.circle(screen,white,(x+10,y-10),7)
    pygame.draw.circle(screen,black,(x+14,y-10),4)
    pygame.draw.line(screen,redorange,(x+15,y),(x+25,y-5),5)
    pygame.draw.line(screen,redorange,(x+15,y),(x+25,y+5),5)
def obstacle(x1):
    global top,bottom
    top=pygame.draw.rect(screen,green,(x1,0,50,l))
    bottom=pygame.draw.rect(screen,green,(x1,l+150,50,400))
def obstacle2(x2):
    global top1,bottom1
    top1=pygame.draw.rect(screen,green,(x2,0,50,l1))
    bottom1=pygame.draw.rect(screen,green,(x2,l1+150,50,400))
def game_over():
    screen.fill(dark_blue)
    show_text("GAME OVER",50,250,white,50)
    pygame.display.update()
    time.sleep(1)
def flappy_bird_game():
    pygame.init()
    screen=pygame.display.set_mode((400,500))
    pygame.display.set_caption("Flappy Bird")
    x=200
    y=250
    x1=450
    x2=700
    flag="down"
    score=0
    l=random.randint(50,300)
    l1=random.randint(50,300)
    while True:
        screen.fill(light_blue)
        bird_draw(x,y)
        obstacle(x1)
        obstacle2(x2)
        show_text(str(score),10,10,black,20)
        x1=x1-.1
        x2=x2-.1
        if x1<=-50:
            x1=450
            l=random.randint(50,300)
        if x2<=-50:
            x2=450
            l1=random.randint(50,300)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==K_SPACE:
                    flag="up"
            if event.type==KEYUP:
                v=0.5
                for i in range(1,10):
                    y=y-v
                    v=v-0.05
                    pygame.display.update()
                flag="down"
        if bird.colliderect(top) or bird.colliderect(bottom):
            game_over()
            import main_menu
            main_menu.menu()
        if bird.colliderect(top1) or bird.colliderect(bottom1):
            game_over()
            import main_menu
            main_menu.menu()
        if 179.9<=x1<=180 or 179.9<=x2<=180:
            score=score+1
            pygame.display.update()
        if flag=="up":
            y=y-0.5
        if flag=="down":
            y=y+.1
        if y>=480:
            game_over()
            import main_menu
            main_menu.menu()
        if y<=20:
            game_over()
            import main_menu
            main_menu.menu()
        pygame.display.update()