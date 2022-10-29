import random

numero_pensado = random.randint(0,10+1)

print('He pensado un numero entre 0 y 10')

intentos = 1
while True:
    guess = int(input('Di un numero:'))
    if guess == numero_pensado:
        print(f'Es el {numero_pensado} ¡¡Acertaste en {intentos} intentos!!')
        break
    intentos += 1
    