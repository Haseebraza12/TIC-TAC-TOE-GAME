import pygame
from pygame.locals import *
pygame.init()
#global variable
screen_width=300
screen_height=300
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Tic Tac Toe')
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

line_width=6
line_clr=(255,0,0)

markers=[]
clicked=False
pos=[]

player=1

green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)
winner=0
game_over=False

font=pygame.font.SysFont(None,40)
win_Text=None
again_rect=Rect(screen_width//2-80,screen_height//2,160,50)
#functions
def draw_grid():
    bg=(255,222,255)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen,line_clr,(0,x*100),(screen_width,x*100),line_width)
        pygame.draw.line(screen,line_clr,(x*100,0),(x*100,screen_height),line_width)

for x in range(3):
    row=[0]*3
    markers.append(row)



def draw_markers():
    x_pos=0
    for x in markers:
        y_pos=0
        for y in x:
            if y==1:
                pygame.draw.line(screen,red,(x_pos*100+15,y_pos*100+15),(x_pos*100+85,y_pos*100+85),line_width)
                pygame.draw.line(screen,red,(x_pos*100+15,y_pos*100+85),(x_pos*100+85,y_pos*100+15),line_width)
            if y==-1:
                    pygame.draw.circle(screen,green,(x_pos*100+50,y_pos*100+50),38,line_width)
            y_pos+=1
        x_pos+=1
        

def win_condition():
    global winner,game_over,win_Text
    y_pos=0
    for x in markers: # chek columns
        if sum(x)==3:
         winner=1
         game_over=True
        if sum(x)==-3:
          winner=2
          game_over=True
        if markers[0][y_pos]+markers[1][y_pos]+markers[2][y_pos]==3:#rows
            winner=1
            game_over=True
        if markers[0][y_pos]+markers[1][y_pos]+markers[2][y_pos]==-3:
            winner=2
            game_over=True
        y_pos+=1
        #check cross
        if markers[0][0]+markers[1][1]+markers[2][2]==3 or markers[2][0]+markers[1][1]+markers[0][2]==3:
            winner=1
            game_over=True
        
        if markers[0][0]+markers[1][1]+markers[2][2]==-3 or markers[2][0]+markers[1][1]+markers[0][2]==-3:
            winner=1
            game_over=True
    if game_over==False:
        tie=True
        for now in markers:
            for i in now:
                if i==0:
                    tie=False
        if tie==True:
            game_over=True
            winner=0



    
def draw_winner(winner):
    if winner!=0:
          win_Text='Player '+ str(winner)+"wins!!!"
    elif winner==0:
        win_Text='DRAW HOGAYA!!'
    win_img=font.render(win_Text,True,blue)
    pygame.draw.rect(screen,green,(screen_width//2-100,screen_height//2-60,230,50))
    screen.blit(win_img,(screen_width//2-100,screen_height//2-50))

    again_Text='Play Again?'
    again_img=font.render(again_Text,True,red)
    pygame.draw.rect(screen,green,again_rect)
    screen.blit(again_img,(screen_width//2-80,screen_height//2+10))





run=True
while run:
    draw_grid()
    draw_markers()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if game_over==0:
            if event.type==pygame.MOUSEBUTTONDOWN and clicked==False:
                clicked=True
            if event.type==pygame.MOUSEBUTTONUP and clicked==True:
                    clicked=False
                    pos=pygame.mouse.get_pos()
                    box_x=pos[0]
                    box_y=pos[1]
                    if markers[box_x//100][box_y//100]==0:
                        markers[box_x//100][box_y//100]=player
                        player*=-1
                        win_condition()
    if game_over==True:
      draw_winner(winner)
      if event.type==pygame.MOUSEBUTTONDOWN and clicked==False:
          clicked=True
      if event.type==pygame.MOUSEBUTTONDOWN and clicked== True:
          clicked=False
          pos=pygame.mouse.get_pos()
          if again_rect.collidepoint(pos):
              markers=[]
              pos=[]
              player=1
              winn1=0
              game_over=False
              for x in range(3):
                row=[0]*3
                markers.append(row)
    pygame.display.update()

pygame.quit()
