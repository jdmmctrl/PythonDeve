from tkinter import *
from tkinter import messagebox

objVentana = Tk()
objVentana.title("Aplicacion para calcular IMC")
objVentana.geometry("150x150")

lblPeso = Label(objVentana, text="Peso: ")
lblPeso.pack()

txtPeso = Entry(objVentana, width=12)
txtPeso.pack()


lblAltura = Label(objVentana, text="Altura: ")
lblAltura.pack()

txtAltura = Entry(objVentana, width=12)
txtAltura.pack()


def eventoParaCalcularIMC():
    peso = float(txtPeso.get())
    altura = float(txtAltura.get())
    imc = peso / (altura * altura)

    messagebox.showinfo("Resultado", "Su IMC es: " + str(imc))

    if imc < 18.5:
        messagebox.showwarning("Peso...", "Peso muy bajo")
    else:
        if imc > 18.5 and imc < 29.9:
            messagebox.showinfo("Peso...", "Peso normal, ¡Felicitaciones!")
        else:
            if imc > 29.9:
                messagebox.showerror(
                    "Peso...", "Con sobre peso, Peso muy alto, ¡Realiza Ejercicio!"
                )


btnIMC = Button(objVentana, text="Calcular IMC", command=eventoParaCalcularIMC)
btnIMC.pack()

objVentana.mainloop()
