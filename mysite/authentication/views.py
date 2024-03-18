from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from mysite.mysite.forms import RegisterForm, LoginForm


# def register(request):
#     if request.method == 'GET':
#         form = RegisterForm()
#         return render(request, 'register.html', {'form': form})
#
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             messages.success(request, 'You have singed up successfully.')
#             # login(request, user)
#             print(user.username + "   " + user.password)
#             return redirect('index')
#         else:
#             return render(request, 'register.html', {'form': form})
#
#
# def login_page(request):
#     form = LoginForm()
#     message = ''
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 message = f'Bonjour, {user.username}! Vous êtes connecté.'
#             else:
#                 message = 'Identifiants invalides.'
#     return render(
#         request, 'authentication/login.html', context={'form': form, 'message': message})
