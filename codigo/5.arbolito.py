# dibujando arbolitos

filas = int(input('¿cuantas filas quieres que tenga tu arbol'))

for i in range(1,filas+1):
    dibujo = "#" * i
    print(dibujo)
for i in range(filas,0,-1):
    dibujo = "#" * i
    print(dibujo)    