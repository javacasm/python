# deletrea una cadena

palabra = input('Introduce una palabra: ')

for letra in palabra:
    print(letra.capitalize())
print(f'"{palabra}" tiene {len(palabra)} caracteres')