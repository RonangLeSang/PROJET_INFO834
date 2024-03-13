from PymongoReq import create_account
from django.shortcuts import render, redirect

def create_ac(request):
    if request.login  is None and request.login is None:
        raise ValueError("espéce de tamanoir t'a  rien mis")
    elif request.password != request.repeat_password:
        raise ValueError("espèce de poisson rouge tu te souviens même pas de ce que tu viens de taper!!!!!!!!!")
    else:
        create_account(request.login, request.password)
        redirect("login.html")
    render(request, "register.html")
        