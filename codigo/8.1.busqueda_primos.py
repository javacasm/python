import os

fichero_primos = 'primos.txt'

numero_buscar = 2


def esPrimo(numero):
    for i in range(2,numero//2 +1):
        if numero%i == 0: # resto=0 -> es divisible
            return False # No hay que probar mas
    return True # ningun numero es divisor
            
def escribePrimo(numero):
    f = open(fichero_primos, "at")
    f.write(str(numero)+'\n')
    f.close()

if fichero_primos in os.listdir():
    f = open(fichero_primos, "rt")
    while True:
        linea = f.readline()
        if not linea: # la linea es nula, hemos terminado
            break
        numero_buscar = int(linea)
  
numero_buscar += 1 # empezamos a buscar en el siguiente
print(f'Empezaremos por {numero_buscar}')
while True:
    if esPrimo(numero_buscar):
        print(f'encontrado {numero_buscar}', end = '\r')
        escribePrimo(numero_buscar)
    numero_buscar += 1
    