
from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print("Guardando en BBDD")


class Sesion(Model):
    def guardar(self):
        print("Guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()
# implementamos polimorfismo para llamar los multiples guardar
# esto porque no es necesario tener una accion igual
# cuando se trata de polimorfismo solo son parecidas las acciones
guardar([sesion, usuario])
