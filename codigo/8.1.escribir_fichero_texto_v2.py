# escribmos en un fichero de texto

f = open('prueba/convert.txt', 'wt',encoding='utf8')
f.write('Hola, estoy escribiendo en un fichero de texto\n')

f.write('Una linea\n')

f.write('Y otra linea\n')

f.close()
# añadimos una linea al final

f = open('prueba/convert.txt', 'at',encoding='utf8')
f.write('Una linea añadida al final')
f.close()