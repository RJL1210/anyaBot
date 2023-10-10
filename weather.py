import datetime as dt
import requests
import json

tokens = open('config.json')
json_contents = json.load(tokens)
api_key = json_contents['weatherToken']

def temp_conversion(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit


#print(response)



def get_weather(city) -> str:
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(weather_url).json()

    if response['cod'] == '404':
        return "No City Found"
    
    temp_kelvin = response['main']['temp']
    temp_fahren = "{:.2f}".format(temp_conversion(temp_kelvin))

    return 'Degrees: ' + temp_fahren

def get_time(city) -> str:
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(weather_url).json()

    if response['cod'] == '404':
        return "No City Found"
    
    return "Time: " + str(dt.datetime.utcfromtimestamp(response['dt'] + response['timezone']))
