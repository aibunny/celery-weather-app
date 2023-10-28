from celery import Celery
import requests

app = Celery('weather',broker='redis://localhost:6379/0')

@app.task
def fetch_weather(location, api_key):
    # Replace 'your_api_key' and use the correct endpoint for your chosen weather API.
    WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': location,  # Example: 'Nairobi,KE'
        'appid': api_key,  # Replace with your actual API key
    }

    response = requests.get(WEATHER_API_URL, params=params)
    
    if response.status_code == 200:
        return weather_data 
    else:
        return {'error' : 'Unable to fetch weather data'}
    