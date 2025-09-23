class Perro():
    # Atributo o propiedad
    cantidad_patas = 4

    # constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Creamos un metodo para llamar al perro
    def llamar_perro(self):
        print(
            f"El perro que vino se llama: {self.nombre} y tiene la edad de: {self.edad} años")


perro = Perro("Dante", 4)
perro.llamar_perro()
print(f"El perro {perro.nombre} tiene: {perro.cantidad_patas} patas")
perro2 = Perro("Scooby", 12)
perro2.cantidad_patas = 3
print(f"El perro {perro2.nombre} tiene: {perro2.cantidad_patas} patas")
