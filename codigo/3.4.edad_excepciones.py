# manejo de excepciones

while True:
    try:
        edad = int(input('¿edad?'))
        if 0 <= edad < 150:
            print('edad:',edad)
            break
        else:
            print('la edad debe estar entre 0 y 150')
    except :
        print('La edad no es valida')
