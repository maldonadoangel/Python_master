class Perro:
    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre

    def presenta(self):
        print(f"El perro se llama {self.nombre}!")


mi_perro = Perro("Scooby")
mi_perro2 = Perro("Felipe")


mi_perro.presenta()
mi_perro2.presenta()
