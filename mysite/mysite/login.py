from django.shortcuts import render, redirect
from django.contrib.auth import  login
from PymongoReq import connect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = connect(username, password)
        if user is not None:
            login(request, user)
            # Rediriger l'utilisateur vers une autre page après la connexion réussie
            return redirect('accueil')
        else:
            # Gérer le cas où l'authentification échoue
            # Par exemple, afficher un message d'erreur
            pass
    return render(request, 'login.html')
