mascotas = ["Pelusa", "Pulga", "Felipe",
            "Kira", "Wolfgang", "PEPE", "Scooby", "Pulga"]

# Formas de agregar valores a nuestra lista
mascotas.insert(1, "Melvin")
mascotas.append("Chanchito triste")
print(mascotas)

# eliminar la primera coincidencia de un elemento de la lista
mascotas.remove("Pulga")
print(mascotas)

# eliminar el ultimo elemento de nuestro arreglo
mascotas.pop()
print(mascotas)

# eliminar un elemento en especifico

mascotas.pop(1)
print(mascotas)

# otra forma de eliminar elementos por medio del index
del mascotas[0]
print(mascotas)
