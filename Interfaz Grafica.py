import tkinter as tk 
import tkMessageBox
root = tk.Tk()
#funcio de message box  mediciones
def mc02 ():
 tkMessageBox.showinfo("Variable sensada ",message = " este sera el  valor de la medicion")
def mt ():
 tkMessageBox.showinfo("Variable sensada ",message = " este sera el  valor de la medicion")
def mh ():
 tkMessageBox.showinfo("Variable sensada ",message = " este sera el  valor de la medicion")
# componentes de la ventana
root.title("PROYECTO TRANSVERSAL")# ventana 
root.geometry('728x400') # dimensiones
root.configure(background='black') #color fondo
img2 = tk.PhotoImage(file = "fa.png")
img  = tk.PhotoImage(file = "m.gif")
log=tk.Label(root,image=img).place(x=0,y=0)
etiqueta=tk.Label(root,text = " Bienvenido a la interfaz grafica de   ",bg ="black",
fg = "white").place(x=300,y=5) #etiqueta
b_ex= tk.Button(root, text="Exit",activeforeground = "white",background='black',
fg= "white",command=root.destroy).place(x=660,y=5)
b_ad=tk.Button(root, text="adelanate",activeforeground = "white",background='black',
fg= "white",height = 2).place(x=120,y=160)
b_at=tk.Button(root, text="..atras..",activeforeground = "white",background='black',
fg= "white",height= 2).place(x=120,y=290)
b_iz=tk.Button(root, text="izquirda.",activeforeground = "white",background='black',
fg= "white",height= 2).place(x=40,y=225)
b_de=tk.Button(root, text=".derecha.",activeforeground = "white",background='black',
fg= "white",height= 2).place(x=200,y=225)
co2=tk.Button(root, text=" CO2  ",activeforeground = "white",command = mc02,
background='black',fg= "white",height=2,width=30).place(x=450,y=180)
temp=tk.Button(root, text="temperatura",activeforeground = "white",command = mt,
background='black',fg= "white",height=2,width=30).place(x=450,y=255)
hum=tk.Button(root, text="humedad",activeforeground = "white",command= mh,
background='black',fg= "white",height=2,width=30).place(x=450,y=325)
et2=tk.Label(root,text =" Elija opcion a sensar ",bg = "black", fg="red").place(x=540,y=150)
et3=tk.Label(root,text ="  Botones de movimiento    ",bg = "black", fg="red").place(x=90,y=120)
#caja= tk.Entry(root, textvariable = ob).place(x=19,y= 130)
#b2= tk.Button(root,text = "publicar ",command =  cj).place(x= 19,y= 150)


root.mainloop()