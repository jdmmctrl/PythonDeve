from tkinter import *

objVentana = Tk()
objVentana.title("Mi primer programa")
objVentana.geometry("400x400")
btnSaludar = Button(objVentana, text="Saludar")
btnSaludar.grid(column=0, row=0)
btnSaludar.pack()


objVentana.mainloop()
