# bucle entre 1  y 100

# range(inicial, final, paso)

for i in range(1,100+1,5): # == significa comparacion
    if i%2 == 0:  #  % operador modulo = resto de la divison
        print(i, 'es par')
    else:
        print(i, "es impar")