# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:38:35 2020

@author: Fernando
"""

from matplotlib.backends.backend_tkagg import FigureCanvasAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.widgets import Button
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import serial, time
from serial import*
#from matplotlib.figure import figure
ser = serial.Serial('COM6', 9600)
print ("connected to: " + ser.portstr)
# PARAMETROS DE LA GRAFICA
# angulo
avance = 15
angulo = avance
a = avance
b = 180-avance
# alcance del radar
alcance = 50
scale = 100
tiempo = 83.33
# Datos a graficar
xi = [avance]
yi = [0]

# GRAFICA figura
# tiempo entre tramas
retraso = tiempo
figura = plt.figure()
grafica = figura.add_subplot(111, projection='polar')
grafica.set_xlim(0,np.pi)
grafica.set_ylim(0,scale)
grafica.set_title('Radar de Ultradonido')

# Linea de barrido y ventana de datos a graficar
tamano = (180//avance)//2
# El gráfico usa radianes
ri = np.array(xi[-tamano:])/180*np.pi
di = yi[-tamano:]
barrido, = grafica.plot(ri, di, 'b')

# linea del pulso y puntoreferencia:
pulsox = [0,ri[-1]]
pulsoy = [0,di[-1]]
PulsoLinea, = grafica.plot(pulsox,pulsoy,'r')
PulsoPunto, = grafica.plot(ri[-1],yi[-1],'ro')

# Nueva Trama
def unatrama(i, xi, yi,angulo,avance):

    # ---DATOS EJEMPLO|INICIO

    # Posición en ángulo
    if len(xi)>0:
        angulo = xi[-1]
    else:
        angulo = 0
    # Dirección de barrido
    direccion = 1
    if (len(xi)>=2):
        sentido = xi[-1]-xi[-2]
        direccion = np.sign(sentido)
        if angulo>=(180-avance) and sentido>0:
            direccion = -1
        if angulo<=avance and sentido<0:
            direccion = 1

    angulo = angulo + direccion*avance
   
    # alcance del radar
    alcance = 30
    
    
    ys = []
    cadena= ser.readline()
    ys=str(cadena).split(',')
    print(ys)
    x=int(ys[-3])
    y= int(ys[-2])
    print(x)
    print(y)

    xi.append(x)
    yi.append(y)
    
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
    # Si los datos son más de 1000
    # Elimina el más antiguo del historial
    if len(xi)>1000:
        xi.pop(0)
        yi.pop(0)
    
    return()
class Index(object):
    ind=0
    
    def next(self, event):
       ser.close()
       plt.draw()
       plt.close('all')
       
callback = Index()
axnext = plt.axes([0.81, 0.05,0.1,0.075])
bnext = Button(axnext, 'cerrar')
bnext.on_clicked(callback.next)
       

# Animación
ani = animation.FuncAnimation(figura,
                              unatrama,
                              fargs=(xi, yi,angulo,avance),
                              interval=retraso,
                              blit=True)

plt.show()