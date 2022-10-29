# Termostato 

try:
    temperatura = float(input("¿Que temperatura hace? "))
    if temperatura > 30:
        print("Hace calor")
    elif temperatura < 15:
        print("Hace frio")
    else:
        print("Temperatura agradable")
except Exception as e:
    print("Error: ",e)        