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

city = "burlingame"

def get_weather(city) -> str:
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(weather_url).json()
    temp_kelvin = response['main']['temp']
    temp_fahren = "{:.2f}".format(temp_conversion(temp_kelvin))
    #time = dt.datetime.utcfromtimestamp(response['dt'] + response['timezone'])
    print(response)
    return temp_fahren
    #print(time)


