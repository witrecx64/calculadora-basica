import tkinter as tk
from tkinter import StringVar, ttk
from math import * 
import webbrowser as web

crash_pc =input("Quiere probar el modo experimental/crash_mode (si) o (no): ")



def virus_error ():
   if crash_pc == "si":
       
        for troll in range(10):
            troll = web.open("https://www.youtube.com/watch?v=mCdA4bJAGGk&ab_channel=sweetblue.")
     
        


def botonclick(num):
    global operador 
    operador = operador+str(num)
    input_text.set (operador)
    
def resultado ():
    global operador
    try : 
        opera = str(eval(operador))
        input_text.set(opera)
    except: 
        input_text.set("ERROR")
        virus_error()
    operador =""    

def borrar(): 
    global operador
    operador =("")
    input_text.set(0)
   
ventana = tk.Tk()

ventana.title("Calculadora basica")
ventana.config(height=600, width=400)

input_text = StringVar ()
operador = ""     

etiqueta_resultado = ttk.Entry(text="Resultado: ", textvariable=input_text)
etiqueta_resultado.place(x=20, y= 120)
etiqueta_resultado.config(width=20)


boton_1 = ttk.Button(text="1", command=lambda:botonclick(1))
boton_1.place(x=20, y=20 )
boton_2 = ttk.Button(text="2", command=lambda:botonclick(2))
boton_2.place(x=80, y=20 )
boton_3 = ttk.Button(text="3", command=lambda:botonclick(3))
boton_3.place(x=140, y=20 )
boton_4 = ttk.Button(text="4", command=lambda:botonclick(4))
boton_4.place(x=20, y=40 )
boton_5 = ttk.Button(text="5", command=lambda:botonclick(5))
boton_5.place(x=80, y=40 )
boton_6 = ttk.Button(text="6", command=lambda:botonclick(6))
boton_6.place(x=140, y=40 )
boton_7 = ttk.Button(text="7", command=lambda:botonclick(7))
boton_7.place(x=20, y=60 )
boton_8 = ttk.Button(text="8", command=lambda:botonclick(8))
boton_8.place(x=80, y=60 )
boton_9 = ttk.Button(text="9", command=lambda:botonclick(9))
boton_9.place(x=140, y=60 )
boton_0 = ttk.Button(text="0", command=lambda:botonclick(0))
boton_0.place(x=20, y=80 )
boton_suma = ttk.Button(text="+", command=lambda:botonclick("+"))
boton_suma.place(x=80, y=80 )
boton_resta = ttk.Button(text="-", command=lambda:botonclick("-"))
boton_resta.place(x=140, y=80 )
boton_multi = ttk.Button(text="x", command=lambda:botonclick("*"))
boton_multi.place(x=220, y=20 )
boton_divi = ttk.Button(text="/", command=lambda:botonclick("/"))
boton_divi.place(x=220, y=40 )
boton_borrar = ttk.Button(text="AC", command=borrar)
boton_borrar.place(x=220, y=60 )
boton_igual = ttk.Button(text="=", command=resultado)
boton_igual.place(x=220, y=80 )


ventana.mainloop()




#librerias utilizadas:
# https://docs.python.org/es/3/library/webbrowser.html (Webbroser)
#https://docs.python.org/es/3/library/tkinter.html (Tkinter)
#https://docs.python.org/3/library/math.html (Math)



#Hecho por witrecx64

#Explicación basica: Creamos una interfaz de tkinter con solo botones y un "Entry" que ayuda poner la respuesta, curioso podriamos cambiar el "Entry" por una label
#Despues hacemos 4 funciones 3 de ellas sirven para ejecutar la operacion +, *, -,/ , = y borrar o AC.
#La cuarta funcion combinada con una de las 3 previene que el usario use el comando 0/0 ya que es imposible
#Cuando usted use ese comando (0/0 o parecidos) va salir error acompañado de un RickRoll o varios, para deshabilitar esto en el principio diga no.
#Y eso sería todo cualquier duda escriba en Github.