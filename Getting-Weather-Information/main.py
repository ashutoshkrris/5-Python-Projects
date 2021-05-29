import requests
from pprint import pprint

API_KEY = ''
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'


def get_weather_condition(city):
    query_params = {
        'appid': API_KEY,
        'q': city
    }
    res = requests.get(BASE_URL, params=query_params).json()
    pprint(res)


if __name__ == "__main__":
    city = input("Enter city name : ")
    get_weather_condition(city)
