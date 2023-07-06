# Crear una aplicacion que solicite al usuario que ingrese una lista de numeros

print("Cuantos numeros desea ingresar")
numero = int(input())

contadornumeros = 1
listaNumeros = []

# leer la cantidad de numeros que se van a ingresar

while contadornumeros <= numero:
    print("Ingrese un numero de la posicion" + str(contadornumeros) + ":")
    numeros = int(input())
    listaNumeros.append(numeros)
    contadornumeros += 1
print(listaNumeros)
