from django.shortcuts import render
import requests
import json

# Create your views here.

def get_weather(city):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = '934dea40177029c801ed5c95c1e6830c'
    parameters = {
        'q' : city,
        'appid' : api_key,
        'units' : 'metric'
        
    }
    response = requests.get(base_url, params=parameters)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        return None

def homePage(request):
    city = request.GET.get('city')
    icon_url  = 'https://openweathermap.org/img/wn/09d@2x.png'
    if city:
        weather_data_result = get_weather(city)
        
        if weather_data_result is not None:
            icon_id = weather_data_result['weather'][0]['icon']
            icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
            weather_data = json.dumps(weather_data_result,indent=4)
            print(weather_data)
            
            # extracting details
            weather = weather_data_result['weather'][0]['main']
            weather_description = weather_data_result['weather'][0]['description']
            city = weather_data_result['name']
            country = weather_data_result['sys']['country']
            wind_speed = weather_data_result['wind']['speed']
            pressure = weather_data_result['main']['pressure']
            humidity = weather_data_result['main']['humidity']
            temperature = weather_data_result['main']['temp']
        else:
            return render(request,'index.html')
    return render(request, 'index.html', {
        'icon_url' : icon_url,
        'weather' : weather,
        'weather_description' : weather_description,
        'city' : city,
        'wind_speed' : wind_speed,
        'pressure' : pressure,
        'humidity' : humidity,
        'temperature' : temperature
        
    })
            
    # return render(request, 'index.html')