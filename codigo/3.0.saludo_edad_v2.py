# Programa que pide el nombre al usurario y lo saluda

# import datetime
from datetime import date

nombre = input("Dime tu nombre: ")

print('Hola', nombre)

edad_cadena = input('¿Cual es tu edad? ') # ¡¡ES UNA CADENA!!
edad = int(edad_cadena)  # convierte de cadena a entero

# print('Hola,', nombre,'. Tienes',edad,'años')

print('Hola, ' + nombre + '. Tienes ' + edad_cadena + ' años.')

# hoy = datetime.date.today()
hoy = date.today()

año_actual = hoy.year
año_nacimiento = año_actual - edad

print(nombre + ", naciste en " + str(año_nacimiento) + '.')

