
class Perro:
    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre

    def habla(self):
        print("Guau!")


mi_perro = Perro("Scooby")
mi_perro2 = Perro("Felipe")
print(mi_perro.nombre)
print(mi_perro2.nombre)
print(type(mi_perro))

mi_perro.habla()
print(isinstance(mi_perro, Perro))
