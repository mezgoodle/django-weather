from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
from dotenv import load_dotenv
import os
import requests
load_dotenv()


def index(request, id=None):
    msg = {}
    if id:
        city = City.objects.get(id=id)
        city.delete()
        return redirect('index')
    if(request.method == 'POST'):
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            msg['text'] = 'Your city has been added'
            msg['class'] = 'alert alert-success'
        else:
            msg['text'] = 'Error has been encountered'
            msg['class'] = 'alert alert-danger'

    form = CityForm()
    appid = os.getenv('API_KEY')
    CITY_LIMIT = 7
    cities = City.objects.all()[:CITY_LIMIT]
    info = []
    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city.name}&units=metric&appid={appid}'
        res = requests.get(url).json()
        city_info = {
            'city': city.name,
            'id': city.id,
            'temp': res['main']['temp'],
            'wind_speed': res['wind']['speed'],
            'clouds': res['clouds']['all'],
            'icon': res['weather'][0]['icon'],
        }
        info.append(city_info)

    context = {
        'info': info,
        'form': form,
        'msg': msg,
    }
    template_name = 'weather/index.html'
    return render(request, template_name, context)
