import collections


pila = []
pila.append(1)
pila.append(2)
pila.append(3)
pila.append(4)
print(pila)
ultimoElemento = pila.pop()
print(ultimoElemento)
print(pila)
print(pila[-1])

pila.pop()
pila.pop()
pila.pop()
if not pila:
    print("Pila vacia")
