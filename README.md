# django-weather

[![Language](https://img.shields.io/badge/language-python-brightgreen?style=flat-square)](https://www.python.org/)

Django application that works with [OpenWeatherMapAPI](https://openweathermap.org/api).

## Table of contents

- [Table of contents](#table-of-contents)
- [Motivation](#motivation)
- [Build status](#build-status)
- [Badges](#badges)
- [Code style](#code-style)
- [Screenshots](#screenshots)
- [Tech/framework used](#techframework-used)
- [Features](#features)
- [Code Example](#code-example)
- [Installation](#installation)
- [Fast usage](#fast-usage)
- [Tests](#tests)
- [Contribute](#contribute)
- [Credits](#credits)
- [License](#license)

## Motivation

In summer I want to improve my skills with **Django**, so I made this project from the tutorial.

> For tutorial link look Credits section

## Build status

Here you can see build status of [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration):

[![Build Status](https://travis-ci.com/mezgoodle/django-weather.svg?branch=master)](https://travis-ci.com/mezgoodle/django-weather)

## Badges

[![Theme](https://img.shields.io/badge/Theme-API-brightgreen?style=flat-square)](https://uk.wikipedia.org/wiki/%D0%9F%D1%80%D0%B8%D0%BA%D0%BB%D0%B0%D0%B4%D0%BD%D0%B8%D0%B9_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BD%D0%B8%D0%B9_%D1%96%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81)
[![API](https://img.shields.io/badge/API-OpenWeatherMap-brightgreen?style=flat-square)](https://openweathermap.org/api)

## Code style

I'm using [Codacy](https://www.codacy.com/) for automate my code quality.

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/dccf7974d1354fe79aa320042a48b55b)](https://www.codacy.com/manual/mezgoodle/django-weather?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mezgoodle/django-weather&amp;utm_campaign=Badge_Grade)
 
## Screenshots

- Main page

![Screenshot 1](https://raw.githubusercontent.com/mezgoodle/images/master/django-weather1.png)

- City section

![Screenshot 1](https://raw.githubusercontent.com/mezgoodle/images/master/django-weather2.png)

## Tech/framework used

**Built with**

- [Django](https://www.djangoproject.com/)
- [requests](https://requests.readthedocs.io/en/master/)

## Features

On the page you can _add_ the city to database and find out what the **temperature** is there now, **wind speed**, **etc**. Also you can remove the _city_ from the list.

## Code Example

- main view

```python
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
```

## Installation

1. Clone this repository:

```bash
git clone https://github.com/mezgoodle/django-weather.git
```

2. Install packages with [pip](https://pip.pypa.io/en/stable/):

```bash
pip install -r requirements.txt
```

3. Rename `.env_sample` to `.env` and fill the variables like:

```bash
API_KEY="<YOUR_API_KEY>"
SECRET_KEY="<YOUR_SECRET_KEY>"
```

> API key from [OpenWeatherMap](https://openweathermap.org/).

## Fast usage

1. Make migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

2. Create superuser:

```python
python manage.py createsuperuser
```

3. Run development server:

```python
python manage.py runserver
```

## Tests

All tests are in this [file](https://github.com/mezgoodle/django-weather/blob/master/mysite/weather/tests.py). You can look [here](https://github.com/mezgoodle/Django-tutorial/wiki/Testing) how to make _unit-testing_ with **Django**.

## Contribute

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Credits

Link to [video](https://www.youtube.com/watch?v=lsAbq2RcWlQ), that helped me to built this project.

## License

MIT © [mezgoodle](https://github.com/mezgoodle)