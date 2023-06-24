
# Crear una aplicacion con el IMC

# IMC = Peso / Altura^2

print("Proporciona tu peso en kg: ")

peso = float(input())

print("Proporciona tu altura en metros: ")

altura = float(input())


imc = peso / altura ** 2

print(f"Tu indice de masa corporal es: {imc}")