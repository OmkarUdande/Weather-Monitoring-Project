import requests
from django.conf import settings
from django.shortcuts import render
from .models import WeatherData
from datetime import datetime

def fetch_weather(city):
    API_KEY = settings.OPENWEATHERMAP_API_KEY
    BASE_URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    response = requests.get(BASE_URL)
    
    if response.status_code == 200:
        data = response.json()
        temperature_celsius = data['main']['temp'] - 273.15
        feels_like_celsius = data['main']['feels_like'] - 273.15
        weather_main = data['weather'][0]['main']
        timestamp = datetime.utcfromtimestamp(data['dt'])

        weather_data = WeatherData(
            city=city,
            temperature=temperature_celsius,
            feels_like=feels_like_celsius,
            weather_main=weather_main,
            timestamp=timestamp
        )
        weather_data.save()
    else:
        print(f"Error fetching data for {city}: {response.status_code}")

def display_weather(request):
    cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad']
    
    for city in cities:
        fetch_weather(city)

    weather_data = WeatherData.objects.all().order_by('-timestamp')[:10]
    return render(request, 'weather/weather_display.html', {'weather_data': weather_data})
