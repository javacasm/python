"""
Termostato

1. Pedimos la temperatura al usuario
2. Comparamos con la temperatura minima
    * Si es mayor -> Enciendo aire acondicionado
    * Si es mnor  <- Enciendo la calefaccion

"""

temperatura = int(input("¿Que temperatura hay?"))

umbral = 25

if temperatura < umbral :
    print('Enciendo la calefaccion')
    print('Apago el AA')
else:
    print('Enciendo el AA')
    print('Apago la calefaccion')
    
    
    
