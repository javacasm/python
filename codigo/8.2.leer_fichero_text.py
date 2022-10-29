f = open("prueba.txt",'rt', encoding="utf8")

for linea in f.readlines():
    print(linea)

f.close()