import tkinter
from tkinter import ttk, colorchooser

window = tkinter.Tk()
window.title("Open Bootcamp")

title = ttk.Label(window, text="Colores Preferidos:")
title.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)


def CurSelect(event):
    values = [listbox.get(idx) for idx in listbox.curselection()]
    elegida = ttk.Label(window, text=f"Has elegido: {', '.join(values)}")
    elegida.grid(row=5, column=0, sticky=tkinter.W, padx=5, pady=5)


lista = ['rojo', 'azul', 'amarillo', 'celeste', 'verde', 'negro', 'blanco']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, listvariable=lista_items, height=6, selectmode=tkinter.MULTIPLE)
listbox.bind("<Button-1>", CurSelect)
listbox.grid(row=2, column=0, sticky=tkinter.E+tkinter.W, padx=5, pady=5)


window.mainloop()
