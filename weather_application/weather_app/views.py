import datetime

import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    API_KEY = open("API_KEY", "r").read()
    weather_url = "https://api.openweathermap.org/data/3.0/weather?q={}&appid={}"
    forecast_url = "https://api.api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}"
    
    if request.method == 'POST':
        city = request.POST['city']
    else:
        return render(request, "pages/index.html")
    
    

def fetch_weather_forecast_info(city, api_key, weather_url, forecast_url):
    response = requests.get(weather_url.format(city, api_key)).json()
    lat, lon = response['coord']['lat'], response['coord']['lon']
    forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()
    
    weather_url = {
        "city" : city,
        "temperature": round(response['main']['temp'] - 273.15 , 2),
        "description": response['weather'][0]['description'],
        "icon": response['weather'][0]['icon']
    }
    
    daily_forecasts = []
    for daily_data in forecast_response['daily'][:5]:
        daily_forecasts.append({
            "day": datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
            "min_temp": round(daily_data['temp']['min'] - 273.15 , 2),
            
        })