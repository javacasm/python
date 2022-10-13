from dateutil.parser import parse
from datetime import datetime

str_cumple = input("Introduce el dia y la hora de tu cumpleaños en formato dd/mm/yyyy hh:mm:ss")

# str_cumple = '25/12/1970 15:00:00'

fecha_cumple = parse(str_cumple)
# print(fecha_cumple)

ahora = datetime.now()

edad = ahora-fecha_cumple

horas = edad.seconds // 3600 # segundos que tiene 1 hora
restoSegundos = edad.seconds - horas * 3600
minutos = restoSegundos // 60
segundos = restoSegundos - minutos * 60

años = edad.days// 365 # se puede mejorar calculando los bisiestos entre las fechas
restoDias = edad.days % 365

meses = restoDias // 30 # tomamos el mes medio

restoDias = edad.days - años*365 - meses*30

print(f'tienes {años} años, {meses} meses, {restoDias} días, {horas} horas, {minutos} minutos y {segundos} segundos')
