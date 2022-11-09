# agenda de contactos v1.5

from os import listdir

lista_amigos = []
lista_edades = []

nombre_agenda = 'agenda.csv'
separador_campos = ';'

def saludosAmigos():
    """ Funcion que saluda a todos los amigos
        Usa la variable global lista_amigos
    """
    global lista_amigos
    for amigo in lista_amigos:
        print('Hola',amigo)

def mostrarAmigos_v1():
    """ Muestra todos los amigos
        Utiliza la variable global lista_amigos
    """     
    global lista_amigos
    for i in range (len(lista_amigos)): # range(0,len(..),1)
        print(lista_amigos[i])

def mostrarAmigos_v2():
    """ Muestra todos los amigos
        Utiliza la variable global lista_amigos
    """    
    global lista_amigos
    for amigo in lista_amigos:
        print(amigo)

def mostradAmigosYEdad():
    """ Funcion que muestra todos los amigos
        y sus edades
        Usa las variables globales
            lista_amigos y lista_edades
    """
    global lista_amigos, lista_edades
    for i in range(len(lista_amigos)):
        amigo = lista_amigos[i]
        edad = lista_edades[i]
        print('Mi amigo',amigo,'tiene',edad,'años')

def añadirAmigos():
    """ Funcion que permite añadir amigos y sus edades
        Se detiene al entrar un nombre vacio ""
        Usa las variables globales
            lista_amigos y lista_edades

    """
    global lista_amigos, lista_edades
    while True:
        amigo = input('Nombre de amigo: (Enter para salir) ')
        
        if amigo == "": # han pulsado enter
            break # salimos del bucle
        
        # if lista_amigos.count(amigo) != 0: # ya esta
        if amigo in lista_amigos:
            print(amigo,' ya estan la lista')
            continue
        # fin del if
        
        lista_amigos.append(amigo)

        edad = int(input('¿que edad tiene? '))
        
        lista_edades.append(edad)

        print('Ahora tienes',len(lista_amigos),'amigos')
        

def guardarAmigos():
    global nombre_agenda, separador_campos
    f = open(nombre_agenda, 'wt', encoding='utf8') # siempre guardamos la agenda completa
    for i in range(len(lista_amigos)):
        linea = lista_amigos[i] + separador_campos + str(lista_edades[i]) + '\n'
        f.write(linea)
    f.close()
    print('Se han guardado '+str(len(lista_amigos)))

def cargarAmigos():
    global nombre_agenda, separador_campos
    if nombre_agenda in listdir():
        f = open(nombre_agenda, 'rt', encoding='utf8')
        for linea in f.readlines():
            valores = linea.split(separador_campos)
            lista_amigos.append(valores[0])
            lista_edades.append(int(valores[1]))
        print('Se ha recuperado '+str(len(lista_amigos))+' amigos')
    else:
        print('No se ha encontrado el fichero de la agenda')

cargarAmigos()
añadirAmigos()
guardarAmigos()
mostradAmigosYEdad()
    