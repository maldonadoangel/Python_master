from abc import ABC, abstractmethod


class Model(ABC):

    # def __init__(self):
    #     if not self.tabla:
    #         print("Error tienes que definir una tabla")

    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("Guardando usuario")


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)
