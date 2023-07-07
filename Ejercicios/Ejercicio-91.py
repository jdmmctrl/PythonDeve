# Calcular el IMC e indicar si esta con sobrepeso o no
# IMC = peso / altura^2
# IMC > 18.5 (Peso Bajo)
# IMC >= 18.5 y < 29.9 (normal)
# IMC >= 30 y < 39.9 (sobrepeso)


def calcularIMC(peso, estatura):
    IMC = peso / (estatura * estatura)

    if IMC < 18.5:
        print("Peso Bajo")
    elif IMC >= 18.5 and IMC < 29.9:
        print("Normal")
    elif IMC >= 30 and IMC < 39.9:
        print("Sobrepeso")
    else:
        print("Obesidad")


print("Cual es tu estatura en metros: ")
estatura = float(input())

print("Cual es tu peso en kilogramos: ")
peso = float(input())

calcularIMC(peso, estatura)
