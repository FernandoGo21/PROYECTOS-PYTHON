# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:19:16 2020

@author: Fernando Gomez
"""
import queue
from tkinter import *
from serial import *
import serial, time
import os
from os import system
ser = serial.Serial('COM6', 9600)
ventana = Tk()
ventana.title("DATOS")
ventana.geometry('400x300')
cola = queue.Queue()
cola2 = queue.Queue()
vect = []
distancias1 = []
distancias = []
angulos = []
def codigoBoton4():
    for i in range(10):
        try:
            datos = ser.readline()
            vect=str(datos).split(',')
            x= int(vect[-3])
            distancias.append(int(x))
            print(distancias)
        except KeyboardInterrupt:
                    break
    distancia = []
def codigoBoton():
 for i in range(10):
        try:
            datos = ser.readline()
            vect=str(datos).split(',')
            y= int(vect[-2])
            angulos.append(int(y))
            print(angulos)
        except KeyboardInterrupt:
                    break
angulos = []
 
def codigoBoton2():
       ventana.destroy()
def codigoBoton3():
    for i in range(10):
        try:
            datos = ser.readline()
            vect=str(datos).split(',')
            x= int(vect[-3])
            y= int(vect[-2])
            distancias.append(int(x))
            print(distancias)
            angulos.append(int(y))
            print(angulos)
        except KeyboardInterrupt:
                    break
angulos = []
distancia = []
boton=Button(ventana, text="Distancias", command=codigoBoton).place(x=30,y=10)
boton3=Button(ventana, text="Angulos y Distancias", command=codigoBoton3).place(x=90,y=50)
boton2=Button(ventana, text="Salir", command=codigoBoton2).place(x=200,y=200)
boton4=Button(ventana, text="Angulos", command=codigoBoton4).place(x=125,y=100)
ventana.mainloop()