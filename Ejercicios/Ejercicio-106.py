from tkinter import *
from tkinter import messagebox

objVentana = Tk()
objTitulo = objVentana.title("Crear Messagebox")
objVentana.geometry("300x300")


def mostratMensajes():
    messagebox.showinfo("Titulo", "Mensaje de informacion")
    messagebox.showwarning("Titulo", "Mensaje de advertencia")
    messagebox.showerror("Titulo", "Mensaje de error")
    messagebox.askquestion("Titulo", "Mensaje de pregunta")
    messagebox.askokcancel("Titulo", "Mensaje de Cancel")
    messagebox.askyesno("Titulo", "Mensaje de Si o No")
    messagebox.askretrycancel("Titulo", "Mensaje de Cancelar y volver a intentar")


btnMostrar = Button(objVentana, text="Mostrar Mensajes", command=mostratMensajes)
btnMostrar.grid(row=0, column=0)

objVentana.mainloop()
