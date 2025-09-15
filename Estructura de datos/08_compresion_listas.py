usuarios = [
    ["Kira", 4],
    ["Pepe", 13],
    ["Scooby", 1]
]

# mascotas = []

# for mascota in usuarios:
#     mascotas.append(mascota[0])

# print(mascotas)

# transformar
nombres = [usuario[0] for usuario in usuarios]

print(nombres)

# filtrar
nombres = [usuario for usuario in usuarios if usuario[1] > 10]
print(nombres)
