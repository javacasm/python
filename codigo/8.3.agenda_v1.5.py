# agenda v1
# guardar una lista de amigos

lista_amigos = []
lista_edades = []

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

def mostrarAmigosYEdades():
    """ Muestra todos los amigos y sus edades
        Utiliza las variables globales lista_edades y lista_amigos
    """
    global lista_amigos, lista_edades
    print('\nLista de amigos y edades') # \n = salto de linea
    print('--------------------------')
    for i in range (len(lista_amigos)):
        print(lista_amigos[i],'tiene',lista_edades[i],'años')    

def añadirAmigos():
    """ Añade amigos y sus edades a la lista
        Pulsamos Enter '' para terminar
    """
    while True:
        amigo = input('Nombre del amigo: (Enter para terminar) ')
        if amigo == '':
            break  # salimos del bucle
        if amigo in lista_amigos:
            print(amigo,' ya esta en la lista')
            continue # volvemos a empezar el bucle

        lista_amigos.append(amigo)
        edad = int(input('Edad de ' + amigo+': '))
        lista_edades.append(edad)
        print('Tienes', len(lista_amigos), 'amigos')

def guardarAgenda():
    """ Guardamos la agenda de amigos y edades
        en un fichero de txto en formato CSV
        Cada linea tendra nombre;edad
    """
    f = open('agenda.csv','wt', encoding="utf8")
    
    for i in range (len(lista_amigos)): # range(0,len(..),1)
        linea = lista_amigos[i] + ';' + str(lista_edades[i]) + '\n'
        f.write(linea)
    
    f.close()

def cargarAgenda():
    """ Recupera la agenda
    """
    f = open('agenda.csv','rt',encoding="utf8")
    numero_lineas = 0
    for linea in f.readlines():
        try:  # por si hay algun error en el formato
            valores=linea.split(';')  # divido la linea por ";"
            nombre= valores[0]        # 1º nombre
            edad = int(valores[1])    # 2º edad
            lista_amigos.append(nombre)
            lista_edades.append(edad)
            numero_lineas += 1
        except:
            print('Error recuperando linea:',linea)
    f.close()
    print('Recuperados',numero_lineas,'amigos')


cargarAgenda()
añadirAmigos()
mostrarAmigosYEdades()
guardarAgenda()