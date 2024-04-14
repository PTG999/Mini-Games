import pygame
from pygame.locals import*
import time
pygame.init()
screen=pygame.display.set_mode((300,300))
pygame.display.set_caption("Tic Toe")
def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("freesans", size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
def tic_game():
    pygame.init()
    screen=pygame.display.set_mode((300,300))
    pygame.display.set_caption("Tic Toe")
    white=(255,255,255)
    black=(0,0,0)
    red=(255,0,0)
    green=(0,255,0)
    dark_blue=(12,38,79)
    light_blue=(136, 168, 219)
    flag="x"
    x=0
    y=0
    def grid():
        pygame.draw.line(screen,light_blue,(0,100),(300,100),5)
        pygame.draw.line(screen,light_blue,(0,200),(300,200),5)
        pygame.draw.line(screen,light_blue,(100,0),(100,300),5)
        pygame.draw.line(screen,light_blue,(200,0),(200,300),5)
    def draw_x(x,y):
        pygame.draw.line(screen,red,(x-30,y-30),(x+30,y+30),5)
        pygame.draw.line(screen,red,(x-30,y+30),(x+30,y-30),5)
    def draw_o(x,y):
        pygame.draw.circle(screen,green,(x,y),30,5)
    tic={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
    screen.fill(dark_blue)
    while True:
        grid()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==MOUSEBUTTONDOWN:
                a,b=event.pos
                if a in range(0,100) and b in range(0,100):
                    if tic[1]=="":
                        if flag=="x":
                            draw_x(50,50)
                            flag="o"
                            tic[1]="x"
                        elif flag=="o":
                            draw_o(50,50)
                            flag="x"
                            tic[1]="o"
                elif a in range(100,200) and b in range(0,100):
                    if tic[2]=="":
                        if flag=="x":
                            draw_x(150,50)
                            flag="o"
                            tic[2]="x"
                        elif flag=="o":
                            draw_o(150,50)
                            flag="x"
                            tic[2]="o"
                elif a in range(200,300) and b in range(0,100):
                    if tic[3]=="":
                        if flag=="x":
                            draw_x(250,50)
                            flag="o"
                            tic[3]="x"
                        elif flag=="o":
                            draw_o(250,50)
                            flag="x"
                            tic[3]="o"
                elif a in range(0,100) and b in range(100,200):
                    if tic[4]=="":
                        if flag=="x":
                            draw_x(50,150)
                            flag="o"
                            tic[4]="x"
                        elif flag=="o":
                            draw_o(50,150)
                            flag="x"
                            tic[4]="o"
                elif a in range(100,200) and b in range(100,200):
                    if tic[5]=="":
                        if flag=="x":
                            draw_x(150,150)
                            flag="o"
                            tic[5]="x"
                        elif flag=="o":
                            draw_o(150,150)
                            flag="x"
                            tic[5]="o"
                elif a in range(200,300) and b in range(100,200):
                    if tic[6]=="":
                        if flag=="x":
                            draw_x(250,150)
                            flag="o"
                            tic[6]="x"
                        elif flag=="o":
                            draw_o(250,150)
                            flag="x"
                            tic[6]="o"
                elif a in range(0,100) and b in range(200,300):
                    if tic[7]=="":
                        if flag=="x":
                            draw_x(50,250)
                            flag="o"
                            tic[7]="x"
                        elif flag=="o":
                            draw_o(50,250)
                            flag="x"
                            tic[7]="o"
                elif a in range(100,200) and b in range(200,300):
                    if tic[8]=="":
                        if flag=="x":
                            draw_x(150,250)
                            flag="o"
                            tic[8]="x"
                        elif flag=="o":
                            draw_o(150,250)
                            flag="x"
                            tic[8]="o"
                elif a in range(200,300) and b in range(200,300):
                    if tic[9]=="":
                        if flag=="x":
                            draw_x(250,250)
                            flag="o"
                            tic[9]="x"
                        elif flag=="o":
                            draw_o(250,250)
                            flag="x"
                            tic[9]="o"
        if tic[1]=="x" and tic[2]=="x" and tic[3]=="x" or \
            tic[4]=="x" and tic[5]=="x" and tic[6]=="x" or \
            tic[7]=="x" and tic[8]=="x" and tic[9]=="x" or \
            tic[1]=="x" and tic[4]=="x" and tic[7]=="x" or \
            tic[2]=="x" and tic[5]=="x" and tic[8]=="x" or \
            tic[3]=="x" and tic[6]=="x" and tic[9]=="x" or \
            tic[1]=="x" and tic[5]=="x" and tic[9]=="x" or \
            tic[3]=="x" and tic[5]=="x" and tic[7]=="x" :
            pygame.display.update()
            time.sleep(0.5)
            screen.fill(light_blue)
            show_text("player x has won the game",5,100,white,25)
            pygame.display.update()
            time.sleep(1)
            import main_menu
            main_menu.menu()
        if tic[1]=="o" and tic[2]=="o" and tic[3]=="o" or \
            tic[4]=="o" and tic[5]=="o" and tic[6]=="o" or \
            tic[7]=="o" and tic[8]=="o" and tic[9]=="o" or \
            tic[1]=="o" and tic[4]=="o" and tic[7]=="o" or \
            tic[2]=="o" and tic[5]=="o" and tic[8]=="o" or \
            tic[3]=="o" and tic[6]=="o" and tic[9]=="o" or \
            tic[1]=="o" and tic[5]=="o" and tic[9]=="o" or \
            tic[3]=="o" and tic[5]=="o" and tic[7]=="o" :
            pygame.display.update()
            time.sleep(0.5)
            screen.fill(light_blue)
            show_text("player o has won the game",5,100,white,25)
            pygame.display.update()
            time.sleep(1)
            import main_menu
            main_menu.menu()
        a = list(tic.values())
        if "" not in a:
            pygame.display.update()
            time.sleep(0.5)
            screen.fill(light_blue)
            show_text("it's a draw",5,100,white,25)
            pygame.display.update()      
            time.sleep(1)
            import main_menu
            main_menu.menu()
        pygame.display.update()