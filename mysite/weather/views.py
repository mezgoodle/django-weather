from django.shortcuts import render
from dotenv import load_dotenv
import os
import requests
load_dotenv()

def index(request):
    appid = os.getenv('API_KEY')
    city = 'Kyiv'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}'
    res = requests.get(url)
    print(res.text)
    template_name = 'weather/index.html'
    return render(request, template_name)
