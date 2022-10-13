
nombre = input("introduce tu nombre: ")
nombre_capitalizado = nombre.capitalize()
try:
    edad = int(input("introduzca tu edad: "))
    año_nacimiento = 2022-edad
    print(f'Hola {nombre_capitalizado}, naciste en {año_nacimiento} y tienes {edad} años')
except Exception as e:
    print("Se ha producido un error: ",e)