punto = {"x": 20, "y": 10}
print(punto)
# imprimimr el valor de la llave x
print(punto["x"])
print(punto["y"])

# Agregar data
punto["z"] = 30
print(punto)

# Agregamos lala
punto["lala"] = "Me encontraste soy lala"

# buscar algo en el diccionario
if "lala" in punto:
    print(punto["lala"])
else:
    print("No existe ese elemento en el diccionario")


usuarios = [
    {"id": 1, "nombre": "Angel Morales"},
    {"id": 2, "nombre": "Hernán Morales"},
    {"id": 3, "nombre": "Felipe Guzman"}
]

# Mostrar los nombres de los usuarios del diccionario
for usuario in usuarios:
    print(usuario["nombre"])

# pasar las palabras de una lista a un diccioinario y mostrar las veces que se cuentan
palabras = ["Python", "JAVA", "JS", "C#", "c++", "c++", "Python"]
conteo = {palabra: palabras.count(palabra) for palabra in set(palabras)}
print(conteo)

# Agarrar una lista de números y multiplicarlo al cuadrado, luego guardar todo eso en un diccionario
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_al_cuadrado = {numero: numero**2 for numero in numeros}
print(numeros_al_cuadrado)
