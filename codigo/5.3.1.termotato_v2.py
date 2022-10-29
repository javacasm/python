# termostato v2

while True:
    temperatura = int(input("temperatura? "))
 
    if temperatura > 25:
        print('Encendido AC')
    else:   # Es menor o igual que 25
        print('Apago AC')
        
        if temperatura < 18:
            print('Enciendo CC')
        else: # t entre 18 y 25
            print('Apago CC')
            print('Temperatura adecuada',temperatura)
