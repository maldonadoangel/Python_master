class Perro:

    # Atributo
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @property  # esto sirve para convertir el get_nombre en una propiedad
    # property sirve para las funciones que nos devuelve el valor (getters)
    def nombre(self):
        print("Pasando por getter")
        return self.__nombre

    # La manera de validar si atributo cumple ciertos criterios
    # es utilizando un metodo set
    @nombre.setter
    def nombre(self, nombre):
        print("Pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
            return


perro = Perro("Kira", 3)
print(perro.nombre)
print(perro.edad)
