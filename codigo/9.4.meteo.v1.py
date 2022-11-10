
# Ejemplo de resultado
r_NY = {  "lat": 39.31,  "lon": -74.5,
       "timezone": "America/New_York",
       "timezone_offset": -18000,
       "current": {
            "dt": 1646318698,
            "sunrise": 1646306882,
            "sunset": 1646347929,
            "temp": 282.21,
            "feels_like": 278.41,
            "pressure": 1014,
            "humidity": 65,
            "dew_point": 275.99,
            "uvi": 2.55,
            "clouds": 40,
            "visibility": 10000,
            "wind_speed": 8.75,
            "wind_deg": 360,
            "wind_gust": 13.89 }
       }

r_NY['current']  # tiempo actual
r_NY['current']['temp']-273  # temperatura
r_NY['current']['clouds']    # % de nubes
r_NY['current']['humidity']  # humedad

# peticion usando mi API-KEY

import requests

## RECUERDA CAMBIAR APIKEY POR TU CLAVE DEL SERVICIO OpenWeatherMap

# peticion de tiempo actual en Granada
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Granada&appid=APIKEY')

if r.status_code == 200: # todo fue bien
    print('datos ok')
elif r.status_code == 401: # problema con la APIKey o licencia
    print('revisa tu suscripcion y el APIKey usada')
else:
    print('Error',r.status_code,'consulta https://openweathermap.org/faq#error401')


data = r.json() # lo trata como json y lo convierte en un diccionario

for clave,valor in data.items(): # vemos los elementos del diccionario
    print(clave,valor)

data['coord'] # coordenadas del resultado

data['name']  # nombre de la estacion

data['weather'] # tiempo actual

data['main']

data['main']['temp'] -273

data['main']['humidity']

# peticion de pronostico
r_pro = requests.get('http://api.openweathermap.org/data/2.5/forecast?lat=37.25&lon=-3.25&appid=APIKEY')
data_pro = r_pro.json()

data_pro['list'] # previsiones

for prev in data_pro['list']:
    fecha_prev = datetime.datetime.fromtimestamp(prev['dt'])
    desc_prev = prev['weather'][0]['main']
    temp = prev['main']['temp'] -273
    print(fecha_prev,desc_prev,temp)
    
