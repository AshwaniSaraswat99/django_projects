from django.shortcuts import render, redirect 
from django.contrib import admin

# Create your views here.
def index(request): 
    if request.method == "POST":
        city = request.POST['city']
    else:
        city = ''
    return render(request, 'index.html',{'city':city})