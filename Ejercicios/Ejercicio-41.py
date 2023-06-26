# Realiza una aplicacion que le pida al usuario determinada cantidad de numeros.
# Muestre al usuario todos los numeros impares que existen en la longitud de los numeros ingresados.
cantidad = int(input("Ingrese la cantidad de numeros que desea ingresar: "))
numero = 1

print("Los numeros impares son: ")

while numero < cantidad:
    if numero % 2 != 0:
        print(numero)
    numero += 1
