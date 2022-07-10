# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 15:44:18 2020

@author: Fernando Gomez
"""
from tkinter import *
from array import array
from time import sleep
from matplotlib import*
import matplotlib.pyplot as plt
import numpy as np
import serial, time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
ser = serial.Serial('COM6', 9600)
temp=[]
vect=[]
ventana = Tk()
ventana.title("Proyecto digitales")
ventana.geometry('500x300')
temperatura=StringVar()
max7219=StringVar()
Label(ventana, text="Termocupla y max7219", fg="black", font=("Comic Sans Ms",16)).place(x=150, y=10)
caja1=Entry(ventana, textvariable=temperatura).place(x=100,y=100)
caja2=Entry(ventana, textvariable=max7219).place(x=100,y=175)
def codigoBoton():
    ser.write('t'.encode())
    datos = ser.readline()
    datosf = datos[1:6]
    print(datosf)
    temperatura.set(datosf)
    max7219.set("")
def codigoBoton2():
    ser.write('m'.encode()) 
    max7219.set("Funcionando")
    temperatura.set("")
def codigoBoton3():
 for i in range(20):
        ser.write('t'.encode())
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


boton=Button(ventana, text="Sensar temperatura", command=codigoBoton).place(x=100,y=120)
boton2=Button(ventana, text="Max7219",command=codigoBoton2).place(x=100,y=200)
boton3=Button(ventana, text="Crear array y plottear",command=codigoBoton3).place(x=325, y=125)
ventana.mainloop()
ser.close()
