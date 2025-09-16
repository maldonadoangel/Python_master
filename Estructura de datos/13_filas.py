from collections import deque


fila = deque([1, 2])
# agregar valores a la fila
# fila.append(3)
# fila.append(4)
# fila.append(5)
print(fila)
# eliminar elemento a la izquierda
fila.popleft()
fila.popleft()
print(fila)
# validar si la fila esta vacia
if not fila:
    print("La fila esta vacia")
