from django.shortcuts import render
from .models import WeatherData
from . forms import WeatherLocationForm
from . tasks import fetch_weather


def weather_view(request):
    if request.method == 'POST':
        form = WeatherLocationForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            
            # Replace 'user_api_key' with the actual user's API key.
            api_key = 'user_api_key'
            
            result = fetch_weather.apply_aync((location, api_key))
    else:
        form = WeatherLocationForm
        result = None
    weather_data = WeatherData.objects.all().order_by('-timestamp')[:10]

    return render(request, 'weather/weather.html', {'form': form, 'result': result, 'weather_data': weather_data})    
