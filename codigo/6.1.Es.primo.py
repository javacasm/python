def esPrimo(numero):
    for i in range(2,numero//2 +1):
        if numero%i == 0: # resto=0 -> es divisible
            return False # No hay que probar mas
    return True # ningun numero es divisor
            

n = int(input("Introduce un numero: "))

if esPrimo(n):
    print(f'{n} es primo')
else:
    print(f'{n} NO es primo')