from datetime import datetime
import os
import pytz
import requests
import math
API_KEY = 'caaa75ae5627d27d7bde3bc14dc9c91c'
#API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')
API_URL = ('http://api.openweathermap.org/data/2.5/forecast?id={}&mode=json&units=metric&lang=pl&appid={}') #cała prognoza
def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data
