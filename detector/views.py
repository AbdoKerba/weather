from django.shortcuts import render,HttpResponse
import json
import urllib.request
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        try:
            req = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=594708214e839c9292443ce74ab32272").read()
            json_data = json.loads(req)
            data = {
                'country': json_data['sys']['country'],
                'temp': round(json_data['main']['temp'] - 272.15),
                'description': json_data['weather'][0]['description'],
                'pressure': json_data['main']['pressure'],
                'wind': json_data['wind']['speed'],
                'city': city
            }
        except:
            return HttpResponse("Invalid city")
    else:
        data = {}
    return render(request, 'index.html', data)