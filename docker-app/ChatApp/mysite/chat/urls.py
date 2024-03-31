# chat/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),    
    path("<str:room_name>/", views.room, name="room"),
    path('get_users_in_room/<str:room_name>/', views.get_users_in_room, name='get_users_in_room'),
]