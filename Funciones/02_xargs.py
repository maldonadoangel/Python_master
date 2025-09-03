
# el * ayuda a iterar los argumenos permitiendo agregar n
# cantidad de argumentos y convertirlos en iterables
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)
suma(2, 6)
suma(1, 8, 5, 32, 1, 3)
