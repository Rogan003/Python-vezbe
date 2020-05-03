import pygame

pygame.init()

ekran = pygame.display.set_mode((800,600))

pygame.display.set_caption('Football game')
logo = pygame.image.load('Static files/lopta.png')
pygame.display.set_icon(logo)

slikaIgraca = pygame.image.load('Static files/igrac.png')

xko=370
yko=480

def igrac(img,x,y):
    ekran.blit(img, (x,y))

tok = True

while tok:
    ekran.fill((0,150,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tok = False

    igrac(slikaIgraca,xko,yko)

    pygame.display.update()