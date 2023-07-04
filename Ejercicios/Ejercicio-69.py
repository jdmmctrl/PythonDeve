marcasCarrosTupla = ("Ford", "Chevrolet", "Volkswagen",
                     "Honda", "Toyota", "Fiat")

print(marcasCarrosTupla)
listaMarcasCarros = list(marcasCarrosTupla)

print(listaMarcasCarros)

listaMarcasCarros.append("Renault")
marcasCarrosTupla = tuple(listaMarcasCarros)
print(marcasCarrosTupla)
