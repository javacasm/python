

def saludo():
    print('Hola Mundo')

def saludaPersona(nombre):
    saludosVarios('Hola',nombre)
    # print('Hola', nombre)

def saludosVarios(saludo,nombre):
    print(saludo,nombre)
    
def variosSaludosPersona(nombre,numeroVeces):
    for i in range(numeroVeces):
        saludaPersona(nombre)
    


saludo()

saludaPersona('Pepe')
saludaPersona('Mª Jesus')

variosSaludosPersona('Fernando',100)
