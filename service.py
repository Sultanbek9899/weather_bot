import requests
import json
from config import API_KEY
from datetime import datetime


def make_request(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
    r = requests.get(url)
    return r.content

def get_weather(city):
    response = make_request(city)
    weather_data = json.loads(response)
    temp_f = weather_data['main']['temp']
    time = int(weather_data['dt'])
    time = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
    temp_c = round(temp_f - 273.15) # конвертация в цельсии из Келвин
    data = {
        "time":time, 
        'temp_c':temp_c,
    }
    return  data