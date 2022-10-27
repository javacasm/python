
contadorSaludos = 0   # variable global

def saludo():
    global contadorSaludos
    print('Hola Mundo')
    contadorSaludos += 1
    
def saludoPersonas(nombre): # nombre es un argumento/parametro
    global contadorSaludos
    # la variable nombre es interna a la funcion = locales
    print('Hola',nombre)
    contadorSaludos += 1

def saludosVarios(saludo, nombre):
    global contadorSaludos
    print(saludo,nombre)
    contadorSaludos += 1

def repiteSaludosVarios(saludo, nombre, numeroVeces):
    # no necesito incrementar contadorSaludos porque lo hace saludosVarios
    for i in range(numeroVeces):
        saludosVarios(saludo, nombre)
        



# ya esta fuera de la funcion


repiteSaludosVarios('Adios','Laura',5)

print('Saludos:',contadorSaludos)

saludosVarios('Hola','Pepe')
print('Saludos:',contadorSaludos)
saludo()
print('Saludos:',contadorSaludos)
saludoPersonas('Pepe')
print('Saludos:',contadorSaludos)
saludoPersonas('Juan')
print('Saludos:',contadorSaludos)