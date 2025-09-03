

# kwargs sirve para nombrar n cantidad de parametros
# y poderlos pasar sin problema dentro de la función
def get_product(**datos):
    print(datos["id"], datos["name"])


get_product(id="01",
            name="Billetera",
            descrip="Esto es un iphone")
