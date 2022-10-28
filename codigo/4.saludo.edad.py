# Programa que pide el nombre al usurario y lo saluda

nombre = input("Dime tu nombre: ")

print('Hola', nombre)

edad = int(input('¿Cual es tu edad? '))  # convierte de cadena a entero

print('Hola, ' + nombre + '. Tienes ' + str(edad) + ' años')

año_actual = 2022
año_nacimiento = año_actual    -   edad

print(nombre + " naciste en " + str(año_nacimiento)+'.')

if edad >= 65:  # sentencia condicional
    print(nombre + ' estas jubilado.')
    print('¡¡Disfruta!!')
else:
    if 18 < edad <= 30:  # comparacion con un rango
        print('Estas en la flor de la vida')
    elif 30 < edad and edad <= 50:
        print('Estas en una etapa estupenda')
    elif edad <= 18:  
        print(nombre + ' eres un jovenzuelo')
    if edad >= 50:    
        años_para_jubilacion = 65 - edad
        print('Te faltan ' + str(años_para_jubilacion) + ' años.')
    
print('Adios!!')




