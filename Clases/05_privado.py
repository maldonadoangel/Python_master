class Mascota:

    # Constructor
    def __init__(self, tipoAnimal, nombre):
        self.tipoAnimal = tipoAnimal
        self.__nombre = nombre

    def habla(self):
        print(f"Sonido de {self.__nombre}")

    def get_nombre(self):
        return self.__nombre
    # Si queremos modificar el valor de un atributo privado se utiliza un metodo con el nombre de set

    def set_nombre(self, nombre):
        self.__nombre = nombre

    @classmethod
    def factory(cls):
        return cls("Gato", "Slash")


mascota = Mascota.factory()

mascota.habla()

# Con esto podemos ver que no podemos acceder al atributo de nuestro constructor
# unicamente podemos acceder desde los metodos de la clase
# print(mascota.__nombre)


# La unica manera de poder acceder es atraves de un metodo que creemos para obtener el nombre como utilizar get_nombre
# Con esto nos aseguramos que se puedan leer el nombre pero no puedan modificar su valor
print(mascota.get_nombre())
