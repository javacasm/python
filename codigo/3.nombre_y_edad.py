# saludo con edad

nombre = input("¿como te llamas? ")

cadena_edad = input("¿cual es tu edad? ")

entero_edad = int(cadena_edad)

año_nacimiento = 2022 - entero_edad

print("Hola",nombre,'tienes', entero_edad,'años')
print("Naciste en ",año_nacimiento)
