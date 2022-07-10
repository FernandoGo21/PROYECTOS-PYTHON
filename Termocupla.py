# -*- coding: utf-8 -*-
"""
Created on Wed Oct  29 15:44:18 2020

@author: Fernando Gomez
"""
from array import array
from tkinter import *
from tkinter.font import Font
from matplotlib.pyplot import text
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
import serial, time
ser = serial.Serial('COM6', 9600)
temp=[]
vect=[]
time.sleep(0.5)   #Espera 2 segundos para conectarse al puerto serial
#while 1:
for i in range(1):
    ser.write('m'.encode())
    time.sleep(0.5) 
for i in range(20):
    ser.write('t'.encode())
    time.sleep(1)
    try:
        datos = ser.readline()
        datosf = datos[1:6] 
        vect.append(float(datosf))
        print(datosf)
    except KeyboardInterrupt:
        break
        data = vect
for i in range(1,21,2):
        data = (vect[i])
        temp.append(data)
print(temp)
plt.plot(temp)
plt.title('Grafica termocupla')
plt.show
ser.close()