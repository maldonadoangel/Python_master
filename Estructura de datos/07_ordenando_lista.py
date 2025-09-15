numeros = [1, 4, 9, 18, 20, 44, 31, 22]

# ordenar una lista modificando la lista original
# numeros.sort()
print(numeros)


# ordenar una lista al reves o descendente siempre de la
# lista original
# numeros.sort(reverse=True)

# ordenar una lista sin afectar a la lista original
numeros_ordenados_alreves = sorted(numeros, reverse=True)
print(numeros_ordenados_alreves)


usuarios = [
    [4, "Chanchito"],
    [1, "Felipe"],
    [5, "pulga"]
]
usuarios.sort()
print(usuarios)
