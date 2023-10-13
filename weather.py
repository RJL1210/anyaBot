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






def get_weather(city):
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(weather_url).json()
    print(response)
    if response['cod'] == '404':
        return "No City Found"
    
    sub_weather = response['weather'][0]['description']
    main_weather = response['weather'][0]['main']
    #so many different subtypes of cloudy weather, the description is more important in this case
    if (main_weather == 'Clouds'):
        main_weather = sub_weather
    print(main_weather)
    temp_kelvin = response['main']['temp']
    temp_fahren = "{:.2f}".format(temp_conversion(temp_kelvin))

    return (temp_fahren, main_weather)

def get_time(city) -> str:
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(weather_url).json()

    if response['cod'] == '404':
        return "No City Found"
    
    return "Time: " + str(dt.datetime.utcfromtimestamp(response['dt'] + response['timezone']))
