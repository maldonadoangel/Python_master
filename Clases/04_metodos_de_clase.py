class Mascota:

    # Constructor
    def __init__(self, tipoAnimal, nombre):
        self.tipoAnimal = tipoAnimal
        self.nombre = nombre

    @classmethod
    def habla(cls):
        print("Sonido de Animal....")

    @classmethod
    def factory(cls):
        return cls("Gato", "Slash")


Mascota.habla()
mascota = Mascota("Gato", "Kira")

mascota2 = Mascota.factory()
print(mascota2.tipoAnimal, mascota2.nombre)
