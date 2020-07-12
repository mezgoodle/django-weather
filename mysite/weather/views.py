from django.shortcuts import render
from .models import City
from dotenv import load_dotenv
import os
import requests
load_dotenv()

def index(request):
    appid = os.getenv('API_KEY')
    cities = City.objects.all()[:5]
    info = []
    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city.name}&units=metric&appid={appid}'
        res = requests.get(url).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }
        info.append(city_info)
    context = {'info': info}
    template_name = 'weather/index.html'
    return render(request, template_name, context)
