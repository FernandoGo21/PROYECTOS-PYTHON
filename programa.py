import pygame, sys

from pygame.locals import *
import time
pygame.init()
a,x = 400,400
screen=pygame.display.set_mode((a,x))
pygame.display.set_caption("Balanza")

AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
GRIS = (128, 128, 128)
BLANCO = (255, 255, 255)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BLANCO)
    ball=pygame.draw.circle(screen,NEGRO,(75, 145), 25, 0)
    pygame.draw.rect(screen, AZUL, (50, 170, 300, 20))
    pygame.draw.rect(screen, ROJO, (188, 170, 25, 150))
    fuente=pygame.font.SysFont("Arial",30)
    pygame.display.flip()
    time.sleep(0.1)
pygame.quit()
ser.close()
