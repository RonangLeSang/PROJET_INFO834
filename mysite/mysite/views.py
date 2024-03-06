# views.py
from django.contrib.auth import authenticate
from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'index.html')


def chatpage(request):
    return render(request, 'chatpage.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'login.html', context={'form': form, 'message': message})
