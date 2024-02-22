# views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def chatpage(request):
    return render(request, 'chatpage.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
