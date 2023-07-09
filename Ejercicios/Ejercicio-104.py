from tkinter import *

objVentana = Tk()
objVentana.title("Mi primer ventana")
objVentana.geometry("250x250")

lblNombre = Label(objVentana, text="Hola")
lblNombre.grid(column=0, row=0)


def saludar():
    lblNombre.configure(text="Hola Juan")


btnSaludar = Button(objVentana, text="Saludar ahora", command=saludar)
btnSaludar.grid(column=1, row=0)


objVentana.mainloop()
