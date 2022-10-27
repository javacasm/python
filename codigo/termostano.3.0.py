# termostato con bucle while

while True:
    temperatura = int(input('¿Temperatura?'))
    if temperatura > 25:
        print('endiende el AC')
    else:
        print('apaga el AC')
    if temperatura < 18:
        print('enciende calefaccion')
    else:
        print('apago calefaccion')
        
    if 18 <= temperatura <= 25:  # temperatura >= 18 and temperatura <= 25:
        print('temperatura optima')
    
print('Fuera del bucle')