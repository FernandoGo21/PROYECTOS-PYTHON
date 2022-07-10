from tkinter import *
from tkinter.font import Font
from time import sleep 
import serial
import time
import sys

#Crear un objeto Tk() 
vent=Tk()
#TITULO DE LA INTERFAZ
vent.title("     COMUNICACION SERIAL PYTHON   -  MBED")
#DIMENSIONES DE LA INTERFAZ
vent.geometry('320x300')
temp=[]
vect=[]
tex= Text(vent,width=20,height=2)
#CREACION DE TEXTO

#ESTABLECER POSICIONES DE LO
tex.place(x=125,y=140)

#----------------------------------------
#CREACION DE FUNCIONES ASOCIADOS A CADA BOTON DE LA INTERFAZ GRAFICA
def button1(): #CUANDO SE PRESIONA EL BOTON DE "LED ON"
    global vent
    mystring=str(2)
    l1=Button(vent,text='ADS115',command=button1,cursor='circle')
    l1.place(x=130,y=200)
    i2c.write('m'.encode())
    time.sleep(20)
    print("Matriz 7219")
    #ESCRIBIR 
    tex.delete(1.0,END) 
    #INSERTAR UN MENSJAE EN LA INTERFAZ GRAFICA
    tex.insert(1.0,"La matriz esta funcionando") 
def button2():#CUANDO SE PRESIONA EL BOTON DE "LED OFF"
    global vent
    mystring=str(1)
    l2=Button(vent,text='MAX7219',command=button2,cursor='circle') 
    lb2.place(x=48,y=40)
    vent.mainloop()  

l1=Button(vent,text='TERMO',command=button1,cursor='circle')
l2=Button(vent,text='MAX7219',command=button2,cursor='circle') 
lab1=Label(vent,text='ESTADO DE MBED',width=15,height=3)
lb2=Label(vent,text='PROYECTO DIGITALES',width=38,height=4)
l1.place(x=130,y=200)
l2.place(x=220,y=200)
lab1.place(x=150,y=100)
lb2.place(x=48,y=40)
vent.mainloop()
sys.exit(0)
 