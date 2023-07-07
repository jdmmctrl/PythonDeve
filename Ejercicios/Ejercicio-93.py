class calcularIMC:
    # Constructor
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def imprimirIMC(self):
        imc = self.peso / (self.altura * self.altura)
        print("Tu IMC es: ", imc)


objCalcularIMC = calcularIMC(70, 1.70)
objCalcularIMC.imprimirIMC()
