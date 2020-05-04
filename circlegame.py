import pygame as pg
from random import randint as rand
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
    
    if ixko + 32 == kcx and iyko + 32 == kcy:
        print('Radi')
        kcx = rand(100,700)
        kcy = rand(100,400)

    krug(kcx,kcy)
    igrac(logo,ixko,iyko)
    pg.display.update()