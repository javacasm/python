# Programa que pide el nombre al usurario y lo saluda

nombre = input("Dime tu nombre: ")

print('Hola', nombre)

edad = int(input('¿Cual es tu edad? '))  # convierte de cadena a entero

print('Hola, ' + nombre + '. Tienes ' + str(edad) + ' años')

año_actual = 2022
año_nacimiento = año_actual    -   edad

print(nombre + " naciste en " + str(año_nacimiento)+'.')


