class calcularIMC:
    # Constructor
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def imprimirIMC(self):
        imc = self.peso / (self.altura * self.altura)
        print("Tu IMC es: ", imc)


# Herencia
class mostrarPesoIdeal(calcularIMC):
    def imprimirPeso(self):
        if self.imc < 18.5:
            print("Tu peso es ideal")
        elif self.imc >= 18.5 and self.imc <= 29.9:
            print("Tu peso es normal")
        else:
            if self.imc >= 30 and self.imc <= 34.9:
                print("Obesidad")


# instancias
objCalcularIMC = calcularIMC(70, 1.70)
objCalcularIMC.imprimirIMC()

obj2CalcularIMC = calcularIMC(80, 1.80)
obj2CalcularIMC.imprimirIMC()


obj3CalcularIMC = mostrarPesoIdeal(70, 1.70)
obj3CalcularIMC.imprimirIMC()
obj3CalcularIMC.imprimirPeso()
