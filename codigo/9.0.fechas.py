# calculo de edad

import datetime # tiene lo relacionado con fechas 
fecha = datetime.date.today()
año_actual = fecha.year
edad = int(input('¿edad? '))
año_nacimiento = año_actual - edad
print('Naciste en',año_nacimiento)
