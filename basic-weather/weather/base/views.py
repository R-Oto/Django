from django.shortcuts import render
import json 
import urllib.request
# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST['city']
        req = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q'+city+'&appid=1b88f27e8c9f835364dc37e8486c83d8')
    else:
        city = ''
    return render(request, 'index.html', {'city':city})