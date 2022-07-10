import pygame, sys
from pygame.locals import *
import time
pygame.init()

                    
ancho,largo = 400,400
screen=pygame.display.set_mode((ancho,largo))
pygame.display.set_caption("Balanza")
blanco=(255,255,255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
positionx =100

# configuracion serial  
#serialport='/dev/tty.wchusbserial1410'
#serialspeed=(115200)
#ser=serial.Serial(serialport,serialspeed)


while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
            
    screen.fill(blanco)
    ball=pygame.draw.circle(screen,NEGRO,(75, 145), 25, 0)
    pygame.draw.rect(screen, AZUL, (50, 170, 300, 20))
    pygame.draw.rect(screen, ROJO, (188, 170, 25, 150))
    fuente=pygame.font.SysFont("Arial",30)
    pygame.display.flip()
    time.sleep(0.1)
    
    
pygame.quit()