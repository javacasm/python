# calculadora

visualizarDatoIntermedios = True # booleana True o False

def suma(a,b):
    global visualizarDatoIntermedios
    resultado = a + b  # variables locales
    if visualizarDatoIntermedios == True:
        print(resultado)
    return resultado

def resta(a,b):
    global visualizarDatoIntermedios
    resultado = a - b
    if visualizarDatoIntermedios == True:
        print(resultado)    
    return resultado

sumaAmasB = suma(10,20)
print(sumaAmasB)

restaAmenosB = resta(20,5)
print(restaAmenosB)