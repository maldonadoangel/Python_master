class Mascota:

    # Constructor
    def __init__(self, tipoAnimal, nombre):
        self.tipoAnimal = tipoAnimal
        self.nombre = nombre

    def habla(self):
        print("Sonido de Animal....")

    @classmethod
    def factory(cls):
        return cls("Gato", "Slash")


mascota3 = Mascota("Loro", "Botas")
print(mascota3.habla())

mascota = Mascota("Gato", "Kira")

mascota2 = Mascota.factory()
print(mascota2.tipoAnimal, mascota2.nombre)
