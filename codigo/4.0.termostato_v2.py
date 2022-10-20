"""
Termostato

1. Pedimos la temperatura al usuario
2. Comparamos con la temperatura minima
    * Si es mayor -> Enciendo aire acondicionado
    * Si es mnor  <- Enciendo la calefaccion

"""

temperatura = int(input("¿Que temperatura hay? "))

umbralAA = 25
umbralCal = 18


if temperatura > umbralAA:
    print('Encendemos AA')
elif temperatura < umbralCal:  # elif = else if
    print('Enciendo Calefaccion')
else:
    print('apago AA y CA')
    

    