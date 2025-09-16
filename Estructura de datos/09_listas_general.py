lista_vacia = []
print(f"{lista_vacia}")

lista_con_data = ["Angel Morales", "Kira Morales", 10, True]
numeros = [80, 20, 34, 100, 44, 59, 78]

# acceder al ultimo una lista
print(f"El ultimo de la lista: {lista_con_data[-1]}")
# acceder al primero de la lista
print(f"El primero de la lista: {lista_con_data[0]}")
# recorrer una lista
for item in lista_con_data:
    print(f"Objeto de la lista: {item}")

# Recorrer una lista, mostrar el index y el valor
for index, item in enumerate(lista_con_data):
    print(f"Indice: {index} con el valor de: {item}")
# modificar el valor en una posición
lista_con_data[1] = "Kira Morales Maldonado"
print(lista_con_data)
# agregar elementos en la ultima posición
lista_con_data.append(False)
# Agregar un elemento en una posición
lista_con_data.insert(2, "Posición 2")
print(lista_con_data)

# Eliminar un valor de la lista, se solicita eliminar el 10
lista_con_data.remove(10)
print(lista_con_data)
# eliminar por el indice o index
del lista_con_data[0]
print(lista_con_data)
# mostrar la longitud de la lista
print(len(lista_con_data))
# mostrar lista de números
print(numeros)
# mostrar la lista ordenada
numeros.sort()
print(numeros)
# Crear una lista de cuadrados con la lista de números
cuadrados = [x**2 for x in numeros]
print(cuadrados)
