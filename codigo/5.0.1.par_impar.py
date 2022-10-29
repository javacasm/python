# numeros pares o impares del 0 al 100

for n in range(0,101,1): 
    if n%2 == 1:
        print(str(n) + ' es impar')
    else:
        print(str(n) + ' es par')
    