import RPi.GPIO as GPIO
import pygame, sys
import serial
from pygame.locals import *
import time
import smbus
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from tkinter import *
from tkinter.font import Font
from time import sleep 
pygame.init()

I2C_BUS = 1
I2C_SLAVE_MBED = 0x10
i2c = smbus.SMBus(I2C_BUS)
s = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(s)
chan = AnalogIn(ads, ADS.P0)

w,h = 600,500
pantalla=pygame.display.set_mode((w,h))
pygame.display.set_caption("Balanza")

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
    
while True:
    print("{:>3.1f}".format(chan.voltage))
    distancia= i2c.read_byte(I2C_SLAVE_MBED)
    sys.stdout.write("distancia: %d\n\r" % distancia)
    #i2c.write_byte(I2C_SLAVE_MBED,setpoint)
    positionx=distancia*12
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
     
            
            
    pantalla.fill(NEGRO)
    ball=pygame.draw.circle(pantalla,AZUL,(positionx, 200), 50, 0)
    pygame.draw.rect(pantalla,ROJO, (50, 250, 450, 10))
    #linea vertical
    pygame.draw.rect(pantalla, AZUL, (250, 250, 10, 200))
    fuente=pygame.font.SysFont("Arial",30)
    pygame.display.flip()
    time.sleep(0.1)
    l1=Button(vent,text='ADS115',command=button1,cursor='circle')
l1.place(x=58,y=40)
vent.mainloop()
pygame.quit()
sys.exit(0)