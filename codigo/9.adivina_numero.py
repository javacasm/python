# Adivina el numero aleatorio que he pensado

from random import randrange

print('Adivina el numero aleatorio que he pensado entre 0 y 9')

numero_aleatorio = randrange(0,10)
numero_intentos = 1
while True:
    numero = int(input('¿que numero he pensado?'))
    if numero == numero_aleatorio:
        print('¡¡Lo has adivinado!! ')
        print('Era el '+str(numero_aleatorio))
        if numero_intentos == 1:
            print('¡Enhorabuena! Has necesitado solo 1 intento')
        else:
            print('Has necesitado '+str(numero_intentos)+' intentos')
        break
    else:
        # numero_intentos = numero_intentos  + 1
        numero_intentos += 1 