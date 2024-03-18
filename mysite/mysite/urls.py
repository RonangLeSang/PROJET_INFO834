"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import index, chatpage, login_page, logout_user, signup_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'),
    path('chatpage', chatpage, name='chatpage'),
    path("chat/", include("chat.urls")),
    path('register/', signup_page, name='register'),
    path('admin/', admin.site.urls),
    path('logout/', logout_user, name='logout'),
    path('connexion', login_page, name='login'),
]
