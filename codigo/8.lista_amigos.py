# agenda de contactos v1

lista_amigos = []
lista_edades = []

def saludosAmigos():
    """ Funcion que saluda a todos los amigos
        Usa la variable global lista_amigos
    """
    global lista_amigos
    for amigo in lista_amigos:
        print('Hola',amigo)
    
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
        
añadirAmigos()

mostradAmigosYEdad()