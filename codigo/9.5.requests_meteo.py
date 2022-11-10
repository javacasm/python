import requests



## Recuerda cambiar APIKEY por tu clave
## La puedes obtener dándote de alta en https://openweathermap.org

requests.get('https://api.openweathermap.org/data/2.5/weather?lat=39.31&lon=-74.5&appid=APIKEY')
# <Response [200]>
r = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=39.31&lon=-74.5&appid=APIKEY')
r.status_code
# 200
requests.get('https://api.openweathermap.org/data/2.5/weather?lat=39.31&lon=-74.5&appid=APIKEY_ERROR')
# <Response [401]>
r.json()
# {'coord': {'lon': -74.5, 'lat': 39.31}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 285.9, 'feels_like': 284.93, 'temp_min': 285.26, 'temp_max': 287.06, 'pressure': 1034, 'humidity': 65}, 'visibility': 10000, 'wind': {'speed': 4.63, 'deg': 70}, 'clouds': {'all': 100}, 'dt': 1668016143, 'sys': {'type': 2, 'id': 2006197, 'country': 'US', 'sunrise': 1667993692, 'sunset': 1668030532}, 'timezone': -18000, 'id': 4502904, 'name': 'Margate City', 'cod': 200}

for clave,valor in r.json().items():
    print(clave,valor)
    
"""
coord {'lon': -74.5, 'lat': 39.31}
weather [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]
base stations
main {'temp': 285.9, 'feels_like': 284.93, 'temp_min': 285.26, 'temp_max': 287.06, 'pressure': 1034, 'humidity': 65}
visibility 10000
wind {'speed': 4.63, 'deg': 70}
clouds {'all': 100}
dt 1668016143
sys {'type': 2, 'id': 2006197, 'country': 'US', 'sunrise': 1667993692, 'sunset': 1668030532}
timezone -18000
id 4502904
name Margate City
cod 200
"""

info_tiempo=r.json()['main']
info_tiempo
# {'temp': 285.9, 'feels_like': 284.93, 'temp_min': 285.26, 'temp_max': 287.06, 'pressure': 1034, 'humidity': 65}
info_tiempo['temp']
# 285.9
info_tiempo['temp'] - 273
# 12.899999999999977
info_tiempo['humidity']
# 65


requests.get('https://api.openweathermap.org/data/2.5/weather?q=Granada&appid=APIKEY')
# <Response [200]>
requests.get('https://api.openweathermap.org/data/2.5/weather?q=Granada&units=matric&appid=APIKEY')
# <Response [200]>
r_granada = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Granada&units=matric&appid=APIKEY')
data_granada=r_granada.json()
r_granada = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Granada&units=metric&appid=APIKEY')
data_granada=r_granada.json()
data_granada['main']
# {'temp': 10.46, 'feels_like': 9.78, 'temp_min': 9.61, 'temp_max': 12.7, 'pressure': 1022, 'humidity': 85, 'sea_level': 1022, 'grnd_level': 887}
r_pro_granada = requests.get('https://api.openweathermap.org/data/2.5/forecast?q=Granada&units=metric&appid=APIKEY')
r_pro_granada.status_code
# 200

prevision = r_pro_granada.json()['list']
for p in prevision:
    print(p)

"""    
{'dt': 1668027600, 'main': {'temp': 9.61, 'feels_like': 9.61, 'temp_min': 7.9, 'temp_max': 9.61, 'pressure': 1022, 'sea_level': 1022, 'grnd_level': 888, 'humidity': 89, 'temp_kf': 1.71}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 60}, 'wind': {'speed': 0.58, 'deg': 114, 'gust': 0.6}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2022-11-09 21:00:00'}
....
{'dt': 1668448800, 'main': {'temp': 10.21, 'feels_like': 8.83, 'temp_min': 10.21, 'temp_max': 10.21, 'pressure': 1019, 'sea_level': 1019, 'grnd_level': 885, 'humidity': 59, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.22, 'deg': 296, 'gust': 1.62}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2022-11-14 18:00:00'}
"""

for p in prevision:
    print(p['dt_txt'],p['main']['temp'])
"""    
2022-11-09 21:00:00 9.61
2022-11-10 00:00:00 8.36
.....
2022-11-14 18:00:00 10.21

"""

