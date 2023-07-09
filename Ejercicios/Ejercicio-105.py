from tkinter import *

objVentana = Tk()
objVentana.title("APP Python")
objVentana.geometry("250x250")

lblNombre = Label(objVentana, text="...")
lblNombre.grid(column=0, row=0)

txtNombre = Entry(objVentana, width=12)
txtNombre.grid(column=1, row=0)


def accionSaludar():
    datoEntrada = txtNombre.get()
    lblNombre.config(text="Hola " + datoEntrada)


btnNombre = Button(objVentana, text="Presiona para Saludar", command=accionSaludar)
btnNombre.grid(column=2, row=0)

objVentana.mainloop()
