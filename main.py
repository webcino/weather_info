import requests
from pprint import pprint

API_KEY = '0d8e64dd45bc42ded023908562f1cf25'
city = input('Enter a city: ')

base_url = 'http://api.openweathermap.org/data/2.5/weather?appid='+API_KEY+'&q='+city

weather_data = requests.get(base_url).json()

pprint(weather_data)