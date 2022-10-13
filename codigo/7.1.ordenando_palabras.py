dias2days = {'lunes':'monday','martes':'tuesday','miercoles':'wednesday','jueves':'thursday','viernes':'friday','sabado':'saturday','domingo':'sunday'}

while True:
    dia = input('Introduce un dia de la semana: ("" para terminar)')
    if dia == '':
        print('bye')
        break
    try:
        day = dias2days[dia]
        
        print(f'{dia} -> {day}')
    except  Exception as e:
        print('Error: ',e)