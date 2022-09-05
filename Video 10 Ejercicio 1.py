import tkinter
from tkinter import ttk, colorchooser
import random

window = tkinter.Tk()
window.title("Open Bootcamp")

elegida = ttk.Label(window, text="")
elegida.grid(row=5, column=0, sticky=tkinter.W, padx=5, pady=5)


def selection():
    selected = f"La opcion seleccionada es: {radio.get()}"
    elegida.config(text=selected)


radio = tkinter.StringVar()
radio.set("")
title = ttk.Label(window, text="Comida Favorita:")
title.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)
r1 = ttk.Radiobutton(window, text="Hamburguesa", value='Hamburguesa', variable=radio, command=selection)
r2 = ttk.Radiobutton(window, text="Pizza", value='Pizza', variable=radio, command=selection)
r3 = ttk.Radiobutton(window, text="Pollo", value='Pollo', variable=radio, command=selection)
r1.grid(row=3, column=1, sticky=tkinter.W, padx=5, pady=5)
r2.grid(row=3, column=2, sticky=tkinter.W, padx=5, pady=5)
r3.grid(row=3, column=3, sticky=tkinter.W, padx=5, pady=5)


def reset():
    radio.set("")
    elegida.config(text="")


reset_button = ttk.Button(window, text="Reset", command=reset)
reset_button.grid(row=7, column=0, sticky=tkinter.W, padx=5, pady=5)


window.mainloop()
