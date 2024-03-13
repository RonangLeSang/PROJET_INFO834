# views.py
from django.shortcuts import render
from login import login_view
from createAccount import create_ac

def index(request):
    return render(request, 'index.html')

def chatpage(request):
    return render(request, 'chatpage.html')

def login(request):
    login_view(request)

def register(request):
    create_ac(request)
