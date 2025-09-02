"""Strings o cadenas de texto"""
nombre_curso = "Ultimate python"
descripcion_curso = """
Este curso contempla todos los temas
que necesitas para aprender y conseguir
un empleo como programador.
"""
print(nombre_curso, descripcion_curso)


print("La longitud del nombre del curso es: ", len(nombre_curso))


"""Traer texto"""

print("Primer letra: ", nombre_curso[0])

"""Traer texto en un rango"""
print("traer 4 letra: ", nombre_curso[0:4])
"""traer despues de una posición especifico"""
print("traer despues de una posición especifico: ", nombre_curso[8:])
print("traer despues de una posición especifico: ", nombre_curso[:6])
