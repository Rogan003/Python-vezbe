import pygame
from random import randint as rand

pygame.init()

ekran = pygame.display.set_mode((800,600))

pygame.display.set_caption('Football game')
logo = pygame.image.load('Static files/lopta.png')
pygame.display.set_icon(logo)

slikaIgraca = pygame.image.load('Static files/igrac.png')

xko = 370
yko = 480
xpromena = 0
ypromena = 0

def igrac(img,x,y):
    ekran.blit(img, (x,y))

lxko = rand(0,768)
lyko = rand(300,568)
slikaLopte = pygame.image.load('Static files/ball.png')

def lopta(img,x,y):
    ekran.blit(img,(x,y))

gxko = 272
gyko = -64
slikaGola = pygame.image.load('Static files/goal.png')

def gol(img,x,y):
    ekran.blit(img,(x,y))

tok = True

while tok:
    ekran.fill((0,150,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tok = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xpromena-=0.2
            if event.key == pygame.K_RIGHT:
                xpromena+=0.2
            if event.key == pygame.K_UP:
                ypromena-=0.2
            if event.key == pygame.K_DOWN:
                ypromena+=0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xpromena=0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ypromena=0

    xko+=xpromena
    yko+=ypromena

    if xko>=732:
        xko = 732
    elif xko<=0:
        xko = 0
    if yko<=0:
        yko = 0
    elif yko>=532:
        yko = 532
   
    igrac(slikaIgraca,xko,yko)
    lopta(slikaLopte,lxko,lyko)
    gol(slikaGola,gxko,gyko)
    pygame.display.update()