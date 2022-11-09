# lectura de fichero de texto

f = open('prueba/convert.txt','rt',encoding='utf8') # abrimos para lectura el fichero en fromato texto

for linea in f.readlines():
    print(linea)
    
f.close()