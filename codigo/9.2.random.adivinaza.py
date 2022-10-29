from random import randrange

numero = randrange(1,10)
contador = 0
while True:
    prueba = int(input('Adivina un numero entre 1 y 10: '))
    contador += 1
    if prueba == numero:
        print('Has acertado!! en',contador,'intentos. Era el',numero)
        break