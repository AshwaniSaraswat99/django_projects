from django.shortcuts import render, redirect 
from django.contrib import admin, messages
import json
import requests
from decouple import config
Weather_API = config('Weather_API')
# Create your views here.
def index(request): 
    weather=None
    city = ''
    if request.method == "POST":
        city = request.POST['city']
        response=requests.get(f'https://api.weatherapi.com/v1/current.json?key={Weather_API}&q={city}&aqi=no').json()
        if not city or "error" in response:
            messages.error(request, "Please enter a valid city name.")
            return redirect('index.html')
        weather={
            'city':city,
            "country": response["location"]["country"],
            "time": response["location"]["localtime"],
            "temp_c": response["current"]["temp_c"],
            "condition": response["current"]["condition"]["text"],
            "icon": response["current"]["condition"]["icon"],
            "wind_kph": response["current"]["wind_kph"],
            "humidity": response["current"]["humidity"],
        }
    else:
        city = ''
    return render(request, 'index.html',{'weather':weather})