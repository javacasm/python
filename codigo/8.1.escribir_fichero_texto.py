# escritura de fichero de texto

f = open('prueba.txt', "wt", encoding="utf8")
f.write('Hola mundo!')
f.close()

f = open('prueba.txt', "at") # añade al final
f.write('12345')
f.close()

f = open('prueba.txt', "at") # añade al final
f.write('Es el final\n')
f.close()