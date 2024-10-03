from django.shortcuts import render
import json 
import urllib.request

def index(request):
    data = {}
    city = ''
    
    if request.method == "POST":
        city = request.POST.get('city', '')
        try:
            api_key = '1b88f27e8c9f835364dc37e8486c83d8'  # Make sure to secure your API key
            res = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric').read()
            json_data = json.loads(res)
            
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": f"{json_data['coord']['lon']} {json_data['coord']['lat']}",
                "temp": f"{json_data['main']['temp']} °C",  # Display temperature in Celsius
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity'])
            }
        except Exception as e:
            data = {"error": "Could not retrieve data for that city. Please check the city name."}

    return render(request, 'index.html', {'data': data, 'city': city})
