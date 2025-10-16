
try:
    numero1 = int(input("Ingresa primer número: "))
except ValueError as e:
    print("Ingrese un valor del tipo correcto")
except NameError as e:
    print("Ocurrio un error, !")
