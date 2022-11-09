import json
import os

contacto = {}

lista_contactos = []

nombre_fichero_datos = 'agenda_v2.json'

def addContactos():

    while True:
        contacto = {}
        nombre = input ('Nombre: (Enter para terminar) ')
        if nombre == '':
            break
        contacto['nombre'] = nombre
        contacto['email'] = input('email: ')
        contacto['telefono'] = input('telefono: ')

        lista_contactos.append(contacto)
    
def printContactos():
    print('\nHay '+str(len(lista_contactos))+ ' contactos')
    print('-'*50)
    for contacto in lista_contactos:
        for nombre_dato,dato in contacto.items():
            print(nombre_dato + ': ' + dato)

def guardarContactos():
    f = open(nombre_fichero_datos,'wt',encoding='utf8')
    for contacto in lista_contactos:
        linea = json.dumps(contacto)+'\n'
        f.write(linea)
    f.close()
    print('Guardados',len(lista_contactos),'contactos')
    
def leeContactos():
    if nombre_fichero_datos in os.listdir():
        f = open(nombre_fichero_datos,'rt',encoding='utf8')
        for linea in f.readlines():
            contacto = json.loads(linea)
            print(contacto)
            print(contacto['nombre'])
            lista_contactos.append(contacto)
        f.close()
        print('Leidos',len(lista_contactos),'contactos')
    else:
        print('No hay datos anteriores')
    
leeContactos()

printContactos()

addContactos()

printContactos()

guardarContactos()