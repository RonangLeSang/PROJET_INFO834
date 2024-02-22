# views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def chatpage(request):
    return render(request, 'chatpage.html')