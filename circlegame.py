import pygame as pg
from random import randint as rand
from math import sqrt as koren

pg.init()

ekran = pg.display.set_mode((800,600))

pg.display.set_caption('Circle game')
logo = pg.image.load('Static files/krug.png')
pg.display.set_icon(logo)

ixko = 368
iyko = 534
ixpr = 0
iypr = 0
def igrac(slika,x,y):
    ekran.blit(slika,(x,y))

kcx = rand(100,700)
kcy = rand(100,400)
def krug(x,y):
    pg.draw.circle(ekran,pg.Color('red'),(x,y),32,1)

def pogodak(x,y,a,b):
    razmak = koren((x+32-a)**2+(y+32-b)**2)
    if razmak<27:
        return True
    else:
        return False

font = pg.font.SysFont('Ariel',60)
score = 0
def poruka(poeni):
    return font.render("Score: " + str(score),True,pg.Color('black'))

igrica = True

while igrica:
    ekran.fill((120,0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            igrica = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                ixpr -= 0.3
            if event.key == pg.K_RIGHT:
                ixpr += 0.3
            if event.key == pg.K_UP:
                iypr -= 0.3
            if event.key == pg.K_DOWN:
                iypr += 0.3
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                ixpr = 0
            if event.key == pg.K_UP or event.key == pg.K_DOWN:
                iypr = 0
    
    ekran.blit(poruka(score),(0,0))

    ixko += ixpr
    iyko += iypr

    if ixko>=732:
        ixko = 732
    elif ixko<=0:
        ixko = 0
    if iyko<=0:
        iyko = 0
    elif iyko>=532:
        iyko = 532
    
    if pogodak(ixko,iyko,kcx,kcy):
        kcx = rand(100,700)
        kcy = rand(100,400)
        score+=1

    krug(kcx,kcy)
    igrac(logo,ixko,iyko)
    pg.display.update()