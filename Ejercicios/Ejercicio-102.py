from tkinter import *

objVentana = Tk()
objVentana.title("Mi primer APP")

lblNombre = Label(objVentana, text="Nombre")

lblNombre.grid(row=0, column=0)

objVentana.mainloop()
