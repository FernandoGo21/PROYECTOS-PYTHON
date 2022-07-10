# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:42:41 2020

@author: FernandoGo
"""
from matplotlib.backends.backend_tkagg import FigureCanvasAgg, NavigationToolbar2Tk
from time import sleep
from tkinter import *
from serial import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import serial, time
ser = serial.Serial('COM6', 9600)
distancias = []
angulos = []
vect2 = []
avance = 10
angulo = avance
a = avance
b = 180-avance
alcance = 70
scale = 100
tiempo = 83.33
xi = [avance]
yi = [0]
retraso = tiempo
figura = plt.figure()
grafica = figura.add_subplot(111, projection='polar')
grafica.set_xlim(0,np.pi)
grafica.set_ylim(0,scale)
grafica.set_title('Radar de Ultradonido')

tamano = (180//avance)//2
ri = np.array(xi[-tamano:])/180*np.pi
di = yi[-tamano:]
barrido, = grafica.plot(ri, di, 'c')
pulsox = [0,ri[-1]]
pulsoy = [0,di[-1]]
PulsoLinea, = grafica.plot(pulsox,pulsoy, 'b')
PulsoPunto, = grafica.plot(ri[-1],yi[-1],'ro')

ventana = Tk()
ventana.title("Guardado de datos")
ventana.geometry('165x165')
def codigoBoton():
    plt.close('all')
    for i in range(10):
        try:
            data = ser.readline()
            vect2=str(data).split(',')
            x= int(vect2[-3]) 
            distancias.append(int(x))
            print(distancias)
        except KeyboardInterrupt:
                    break
def codigoBoton4():
    plt.close('all')
    for i in range(10):
        try:
            data = ser.readline()
            vect2=str(data).split(',')
            y= int(vect2[-2])
            angulos.append(int(y))
            print(angulos)
        except KeyboardInterrupt:
                    break
def codigoBoton3():
    plt.close('all')
    for i in range(10):
        try:
            data = ser.readline()
            vect2=str(data).split(',')
            x= int(vect2[-3])
            y= int(vect2[-2])
            distancias.append(int(x))
            print(distancias)
            angulos.append(int(y))
            print(angulos)
        except KeyboardInterrupt:
                    break
def codigoBoton2():
    plt.close('all')
    ventana.destroy()

def unatrama(i, xi, yi,angulo,avance):
    if len(xi)>0:
        angulo = xi[-1]
    else:
        angulo = 0
    direccion = 1
    if (len(xi)>=2):
        sentido = xi[-1]-xi[-2]
        direccion = np.sign(sentido)
        if angulo>=(180-avance) and sentido>0:
            direccion = -1
        if angulo<=avance and sentido<0:
            direccion = 1

    angulo = angulo + direccion*avance
    alcance = 40
    vect = []
    datos = ser.readline()
    vect=str(datos).split(',')
    x= int(vect[-3])
    y= int(vect[-2])
    print(x)
    print(y)

    xi.append(y)
    yi.append(x)
    
    tamano = (180//avance)//2
    ri=np.array(xi[-tamano:])/180*np.pi
    di = yi[-tamano:]
    barrido.set_xdata(ri)
    barrido.set_ydata(di)
    
    pulsox = [0,ri[-1]]
    pulsoy = [0,yi[-1]]
    
    PulsoLinea.set_xdata(pulsox)
    PulsoLinea.set_ydata(pulsoy)
    
    PulsoPunto.set_xdata(pulsox[1])
    PulsoPunto.set_ydata(pulsoy[1])
    if len(xi)>1000:
        xi.pop(0)
        yi.pop(0)
    
    return()
ani = animation.FuncAnimation(figura,
                              unatrama,
                              fargs=(xi, yi,angulo,avance),
                              interval=retraso,
                              blit=True)
plt.show()
boton=Button(ventana, text="Distancias", command=codigoBoton).place(x=55,y=50)
boton3=Button(ventana, text="Angulos y Distancias", command=codigoBoton3).place(x=30,y=10)
boton2=Button(ventana, text="Salir", command=codigoBoton2).place(x=63,y=130)
boton4=Button(ventana, text="Angulos", command=codigoBoton4).place(x=55,y=90)
ventana.mainloop()