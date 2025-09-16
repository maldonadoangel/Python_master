# desempaquetar
listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(*listaNumeros)

lista2 = [11, 12]

# combinamos dos listas
combinada = ["Hola", *listaNumeros, "Mundo", *lista2]
print(*combinada)
