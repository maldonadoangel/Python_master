"""funciones"""


def saludo(nombre, apellido="Sin apellido"):
    """Funcion de saludo"""
    print(f"Saludos {nombre} {apellido}")


nombre = "Kira"

saludo(nombre)

nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingresa tu apellido: ")
saludo(nombre, apellido)


# Argumentos nombrados
saludo(apellido="Maldonado", nombre="Genesis")
