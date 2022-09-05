import tkinter
from tkinter import ttk, colorchooser
import random

window = tkinter.Tk()
window.title("Manu")

# GEOMETRIA 'PACK'

#label_saludo = tkinter.Label(window, text="Hola Mundo", bg="red", fg="white")
## bg=background, fg=foreground (color de fuente)
#label_saludo.pack(ipadx=50, ipady=15, fill='both', expand=True, side='left')
## ipadx= eje x (ancho), ipady= eje y (alto), expand= expandir al agrandar o achicar, fill= rellenar, side = alineacion


#label_adios = tkinter.Label(window, text="Adios Mundo", bg="green", fg="white")
#label_adios.pack(ipadx=30, ipady=100, fill='both', expand=True, side='right')

# GEOMETRIA 'GRID'

window.columnconfigure(0, weight=1)     # weight= N° cosas que puedo insertar en la columna
window.columnconfigure(1, weight=3)

## Usuario
# Etiqueta Usuario
username_label = ttk.Label(window, text="Username:")
username_label.grid(row=0, column=0, sticky=tkinter.W, padx=5, pady=5)
# sticky en funcion de los puntos cardinales (N,S,E,W)

# Campo Usuario
username_entry = ttk.Entry(window)      # Entry es un campo de texto
username_entry.grid(row=0, column=1, sticky=tkinter.E, padx=5, pady=5)

## Password
# Etiqueta Password
password_label = ttk.Label(window, text="Password:")
password_label.grid(row=1, column=0, sticky=tkinter.W, padx=5, pady=5)

# Campo Password
password_entry = ttk.Entry(window, show="*")
password_entry.grid(row=1, column=1, sticky=tkinter.E, padx=5, pady=5)

## Boton
login_button = ttk.Button(window, text="Login")
login_button.grid(row=3, column=1, sticky=tkinter.E, padx=5, pady=5)

## Frames
frame = ttk.Frame(window, relief=tkinter.SUNKEN)
label5 = ttk.Label(frame, text="Frame")
label5.grid(row=0, column=0, sticky=tkinter.W, padx=2, pady=10)

frame.grid(row=10, column=1, sticky=tkinter.E+tkinter.W, padx=5, pady=5)

## Listbox

lista = ['Windows', 'MacOS', 'Linux', 'Android', 'iOS', 'Ubuntu', 'Debian']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, listvariable=lista_items, height=6, selectmode=tkinter.BROWSE)
listbox.grid(row=2, column=0, columnspan=2, sticky=tkinter.E+tkinter.W, padx=5, pady=5)

## RadioButton

selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="Si", value=1, variable=selected)
r2 = ttk.Radiobutton(window, text="No", value=1, variable=selected)
r3 = ttk.Radiobutton(window, text="Quiza", value=1, variable=selected)
r1.grid(row=10, column=0, sticky=tkinter.W, padx=5, pady=5)
r2.grid(row=10, column=1, sticky=tkinter.W, padx=5, pady=5)
r3.grid(row=10, column=2, sticky=tkinter.W, padx=5, pady=5)


## CheckButton


def mifuncion():
    print("Clickado")


checkbox = ttk.Checkbutton(window, text="Acepto las condiciones", variable=selected, command=mifuncion)
checkbox.grid(row=11, column=0, sticky=tkinter.W, padx=5, pady=5)

## EOP

window3 = tkinter.Tk()
window3.title("EOP")


def saludar(event):
    print("Hola Mundo")


def saludarDoble(event):
    print("Hola Mundo Doble")


def salir(event):
    print("Adios Mundo")
    window3.quit()


boton = ttk.Button(window3, text="Haz clic")
boton.pack()

boton.bind("<Button-1>", saludar)   # <Button-1> es el boton principal (usualmente el izquierdo) del mouse
boton.bind("<Double-1>", saludarDoble)   # <Double-1> es el doble clic del mouse

boton_salir = ttk.Button(window3, text="Salir")
boton_salir.pack()
boton_salir.bind("<Button-1>", salir)


## Colorchooser

colorchooser.askcolor(initialcolor="blue")


#GEOMETRIA 'PLACE'

#window2 = tkinter.Tk()
#window2.title("Manu")

#label1 = tkinter.Label(window2, text="Hola Mundo", bg="red", fg="white")
#label1.place(x=15, y=50)

#label2 = tkinter.Label(window2, text="Hola yo", bg="blue", fg="yellow")
#label2.place(x=0.1, y=0.15)

colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "black", "white", "gray"]

#for i in range(0, 10):
 #   color = random.randint(0, len(colors))
 #   color2 = random.randint(0, len(colors))
 #   label = tkinter.Label(window2, text='Etiqueta', bg=colors[color], fg=colors[color2])
 #   label.place(x=random.randint(0, 100), y=random.randint(0, 100))


window3.mainloop()
