import pygame
import random

pygame.init()
screen=pygame.display.set_mode((600,400))

bee=pygame.image.load('images/bee.png')
bg=pygame.image.load('images/backgroundgrass.png')
f=pygame.image.load('images/flower.png')

playing=True

x=300
y=300

score=0

f_x=100
f_y=200

font=pygame.font.SysFont('Times New Roman',50)

while playing:
    screen.blit(bg,(0,0))
    screen.blit(bee,(x,y))
    screen.blit(f,(f_x,f_y))
    text=font.render('score: '+str(score),True,(0,0,0))
    screen.blit(text,(50,50))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x=x-7
            if event.key==pygame.K_RIGHT:
                x=x+7
            if event.key==pygame.K_UP:
                y=y-7
            if event.key==pygame.K_DOWN:
                y=y+7
    if ((f_x-10)<x<(f_x+10)) and ((f_y-10)<y<(f_y+10)):
        f_x=random.randint(5,550)
        f_y=random.randint(5,350)
        score=score+1
    print(x,y)

    pygame.display.update()
