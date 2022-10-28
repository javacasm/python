# Programa que pide el nombre al usurario y lo saluda

nombre = input("Dime tu nombre: ")

print('Hola', nombre)

edad_cadena = input('¿Cual es tu edad? ') # ¡¡ES UNA CADENA!!
edad = int(edad_cadena)  # convierte de cadena a entero

print('Hola,', nombre,'. Tienes',edad,'años')

año_actual = 2022
año_nacimiento = año_actual - edad

print(nombre,"naciste en",año_nacimiento)

