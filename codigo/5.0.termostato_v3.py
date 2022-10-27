# termostato v3

while True:
    
    try:
        temperatura = int(input("temperatura? (valor entero) "))
        
    except:
        print('La temperatura ha de ser un numero entero')
        continue # reinicia el bucle
    
    if temperatura > 25:
        print('Encendido AC')
    else:   # Es menor o igual que 25
        print('Apago AC')
          
    if  18 <= temperatura <= 25:   # temperatura >= 18 and temperatura <= 25:
        print('Temperatura adecuada',temperatura)
        
    if temperatura < 18:
        print('Enciendo CC')
    else: # es mayor o igual que 18
        print('Apago CC')        
