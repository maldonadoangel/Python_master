# crear una clase padre la cual va a heredar metodos a sus clases hijas
class Caminador:
    def caminar(self):
        print("caminando")


class Nadador:
    def nadar(self):
        print("Nadando")


class Volador():
    def volar(self):
        print("Volando")


class Pato(Caminador, Nadador, Volador):
    def sonido(self):
        print("Cuack")


pato = Pato()
pato.sonido()
pato.caminar()
pato.volar()
pato.nadar()
