import requests
import datetime
from django.shortcuts import render

def index(request):
    API_KEY = '216dfed2f886cc6ec8f5d76d3089833a'
    
    if request.method == 'POST':
        city = request.POST.get('city')
        
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
        
        try:
            weather_info, daily_forecasts = fetch_weather_forecast_info(city, API_KEY, weather_url, forecast_url)
        except Exception as e:
            print(f"Error fetching weather forecast info: {e}")
            weather_info, daily_forecasts = None, None
        
        context = {
            "weather_data": weather_info,
            "daily_forecast": daily_forecasts
        }
        
        return render(request, 'weather_app/index.html', context)
    else:
        return render(request, 'weather_app/index.html')

def fetch_weather_forecast_info(city, api_key, weather_url, forecast_url):
    # Fetch current weather
    response = requests.get(weather_url).json()

    if response.get('cod') != 200:
        print(f"Error fetching weather info: {response.get('message')}")
        return None, None

    # Extract coordinates
    coord = response.get('coord', {})
    lat, lon = coord.get('lat'), coord.get('lon')

    if lat is None or lon is None:
        print("Error: 'coord' key is missing or has missing values.")
        return None, None

    # Fetch 5-day forecast
    forecast_response = requests.get(forecast_url).json()
    
    if 'list' not in forecast_response:
        print("Error: 'list' key is missing in the forecast response.")
        return weather_info, []

    # Extract weather info
    weather_info = {
        "city": city,
        "temperature": round(response['main']['temp'] - 273.15, 2),
        "description": response['weather'][0]['description'],
        "icon": response['weather'][0]['icon']
    }
    
    # Extract daily forecasts
    daily_forecasts = []
    daily_data_list = forecast_response.get('list', [])
    
    # Process forecast data for 5 days
    # Note: 'list' contains data every 3 hours, so we need to aggregate this into daily data.
    for i in range(0, len(daily_data_list), 8):  # 8 data points for each day
        daily_data = daily_data_list[i]
        date = datetime.datetime.fromtimestamp(daily_data['dt'])
        daily_forecasts.append({
            "day": date.strftime("%A"),
            "min_temp": round(daily_data['main']['temp_min'] - 273.15, 2),
            "max_temp": round(daily_data['main']['temp_max'] - 273.15, 2),
            "description": daily_data['weather'][0]['description'],
            "icon": daily_data['weather'][0]['icon']
        })
        if len(daily_forecasts) >= 5:  # Limit to 5 days
            break
    
    return weather_info, daily_forecasts