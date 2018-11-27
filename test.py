from datetime import datetime
import os
import pytz
import requests
import math
import pprint
API_KEY = 'caaa75ae5627d27d7bde3bc14dc9c91c'
API_URL = ('http://api.openweathermap.org/data/2.5/forecast?id={}&mode=json&units=metric&lang=pl&appid={}') #cała prognoza
#API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')  #org
#API_URL = ('http://api.openweathermap.org/data/2.5/weather?id={}&mode=json&units=metric&lang=pl&appid={}') #test
city_id = '3088171'
def query_api(city):
    try:
        #print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
        #pprint.pprint(data)
    except Exception as exc:
        print(exc)
        data = None
    return data

def date2string(date):
    try:
        datastr = pytz.utc.localize(datetime.utcfromtimestamp(date)).strftime("%Y-%m-%d %H:%M")
    except Exception as exc:
        print(exc)
        datastr = None
    return datastr

if __name__ == '__main__':
    forecast = query_api(city_id)
    for item in forecast['list']:
        print(date2string(item['dt'])) #time
        print(item['main']['temp']) # temp
        print(item['main']['temp_min']) # temp min
        print(item['main']['temp_max']) # temp max
        print(item['main']['pressure']) # pressure
        print(item['main']['humidity']) # humidity
        print(item['weather'][0]['main']) # 
        print(item['weather'][0]['description']) # 
        print(item['weather'][0]['icon']) # 
        print(item['clouds']['all']) #
        print(item['wind']['speed']) #
    #print('1543158000')
    #print(dir(pytz))
    #print(pytz.utc.localize(datetime.utcfromtimestamp(1543168800)).strftime("%Y-%m-%d %H:%M"))
    #print(date2string(1543168800))
