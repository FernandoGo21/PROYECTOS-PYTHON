import ssl	
import sys
import paho.mqtt.client as mqtt
import smbus2
import time
import RPi.GPIO as GPIO
import pygame, sys
import serial
from pygame.locals import *
import board
import busio


I2C_BUS = 1
I2C_SLAVE_MBED = 0x10
i2c = smbus.SMBus(I2C_BUS)
s = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(s)
chan = AnalogIn(ads, ADS.P0)

broker_address = "192.168.0.21"
broker_port = 1883

bus = smbus.SMBus(1)
def lm75a():
  lec=bus.read_word_data(0x4c,0) & 0xFFFF
  lec= ((lec<<8) & 0xFF00) +(lec>>8)
  temp=((lec/32.0))/8
 # print ('temperatura: {0:0.2f} *C'.format(temp))
  client.publish("mqtt/primer/",temp)
  return temp
  
######## conectar a  mqtt #################  
def on_connect(client, userdata, flags, rc):    
        
#	print("Connected with result code "+str(rc))
	client.subscribe("mqtt/primer/")


def on_message(client, userdata, message):
    (message.payload.decode("utf-8"))
    client.subscribe("mqtt/primer/")
    

broker_address="192.168.0.21"
def on_message(client, userdata, message):
  print("Mensaje recibido=", str(message.payload.decode("utf-8")))
  print("Topic=", message.topic)
  a=int(str(message.payload.decode("utf-8")))
  if a==1:
      print("hola")
      led.on()
      
  elif a==0:
      print("porfin")
      led.off()

  
client = mqtt.Client() 
client.on_message = on_message 
client.connect(broker_address, broker_port, 60) 
client.subscribe("mqtt/primer/") 

while True :
    lm75a()
    
    client.loop()

client.loop_forever()