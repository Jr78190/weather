from django.shortcuts import render
import requests
import datetime

def index(request):
    if 'ville' in request.POST:
        ville = request.POST['ville']
    else:
        ville = 'Paris'
    appid = '3c6dbf0dbebcf67f23f493c1dae4e3f8'
    URL = 'http://api.openweathermap.org/data/2.5/forecast'
    PARAMETRE = {'q': ville, 'appid': appid, 'units': 'metric'}

    r = requests.get(url=URL, params=PARAMETRE)
    res = r.json()

    if 'list' in res:
        forecast_data = {}
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=7)

        for forecast in res['list']:
            forecast_date = datetime.datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S').date()
            if today <= forecast_date < end_date:
                forecast_day = forecast_date.strftime('%A')
                if forecast_day not in forecast_data:
                    temp = forecast['main'].get('temp')
                    temp_min = forecast['main'].get('temp_min')
                    temp_max = forecast['main'].get('temp_max')
                    humidity = forecast['main'].get('humidity')
                    description = forecast['weather'][0]['description']
                    icon = forecast['weather'][0]['icon']

                    forecast_data[forecast_day] = {
                        'day': forecast_day,
                        'temp': temp,
                        'temp_min': temp_min,
                        'temp_max': temp_max,
                        'humidity': humidity,
                        'description': description,
                        'icon': icon
                    }
    else:
        forecast_data = None

    return render(request, 'listings/index.html', {'forecast_data': forecast_data, 'ville': ville})


from django.shortcuts import render
import requests
import datetime

def index(request):
    if 'ville' in request.POST:
        ville = request.POST['ville']
    else:
        ville = 'Paris'
    
    appid = '3c6dbf0dbebcf67f23f493c1dae4e3f8'
    URL = 'http://api.openweathermap.org/data/2.5/forecast'
    PARAMETRE = {'q': ville, 'appid': appid, 'units': 'metric'}

    r = requests.get(url=URL, params=PARAMETRE)
    res = r.json()

    if 'list' in res:
        forecast_data = {}
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=7)

        for forecast in res['list']:
            forecast_date = datetime.datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S').date()
            if today <= forecast_date < end_date:
                forecast_day = forecast_date.strftime('%A')
                if forecast_day not in forecast_data:
                    temp = forecast['main'].get('temp')
                    temp_min = forecast['main'].get('temp_min')
                    temp_max = forecast['main'].get('temp_max')
                    humidity = forecast['main'].get('humidity')
                    description = forecast['weather'][0]['description']
                    icon = forecast['weather'][0]['icon']

                    activities = get_activities(temp, description)

                    forecast_data[forecast_day] = {
                        'day': forecast_day,
                        'temp': temp,
                        'temp_min': temp_min,
                        'temp_max': temp_max,
                        'humidity': humidity,
                        'description': description,
                        'icon': icon,
                        'activities': activities
                    }
    else:
        forecast_data = None

    return render(request, 'listings/index.html', {'forecast_data': forecast_data, 'ville': ville})


def get_activities(temp, description):
    if temp and temp > 25 or 'clear' in description:
        activities = ['Randonnée', 'Natation', 'Pique-nique']
    elif temp and temp <= 25 or 'rain' in description:
        activities = ['Cinéma', 'Musées', 'Lecture d\'un livre']
    else:
        activities = []
    
    return activities
