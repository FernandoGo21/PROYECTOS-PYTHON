import serial
import time
import sys
import pygame, sys
from tkinter import *
from tkinter.font import Font
from time import sleep 
import serial
import time
import sys
import pygame, sys
from pygame.locals import *
import time

pygame.init()
    #I2C_BUS = 1
    #I2C_SLAVE_MBED = 0x10
    #i2c = smbus.SMBus(I2C_BUS)
   # s = busio.I2C(board.SCL, board.SDA)
    #ads = ADS.ADS1115(s)
   # chan = AnalogIn(ads, ADS.P0)
    
ancho,largo = 400,400
screen=pygame.display.set_mode((ancho,largo))
pygame.display.set_caption("Balanza")
blanco=(255,255,255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
positionx =100

vent=Tk()
vent.title("I2C ADS115")
vent.geometry('150x150')
tex= Text(vent,width=15,height=2)
tex.place(x=10,y=70)
    
def button1(): 
        global vent
        tex.insert(1.0,"{:>3.1f}".format(chan.voltage))
        vent.mainloop()
l1=Button(vent,text='ADS115',command=button1,cursor='circle')
l1.place(x=58,y=40)
  
screen.fill(blanco)
ball=pygame.draw.circle(screen,NEGRO,(75, 145), 25, 0)
pygame.draw.rect(screen, AZUL, (50, 170, 300, 20))
pygame.draw.rect(screen, ROJO, (188, 170, 25, 150))
fuente=pygame.font.SysFont("Arial",30)
pygame.display.flip()
    
vent.mainloop()
while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            