numeros = [1, 2, 3]

# feo
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

primero, segundo, tercero = numeros
print(primero, segundo, tercero)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# como obtener el primero y el ultimo unicamente con esta sintaxis
primer, segundo, *otros, ultimo = numeros
print(primer, segundo, otros, ultimo)
