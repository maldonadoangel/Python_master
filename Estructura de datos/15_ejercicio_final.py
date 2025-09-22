# 1. Eliminar los especios en blanco de un string y devolver una lista con los
# caracteres restantes

palabra = "Bienvenido a la programació n"
palabra_sin_espacios = ""

for letra in palabra:
    if letra != " ":
        palabra_sin_espacios = palabra_sin_espacios + letra

print(palabra_sin_espacios)

# 2. contar con un diccionario cuanto se repiten los caracteres de un string

conteo = {letra: palabra.count(letra) for letra in palabra}
print(conteo)

# 3 ordenar las llaves de un diccionario por el valor que tienen y devolver una lista

ordenar = {"a": 3, "b": 2, "c": 4, "d": 5}
