from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from chat.models import ChatRoom


@login_required
def index(request):
    return render(request, "chat/selectRoom.html")


@login_required
def room(request, room_name):
    chat_room, created = ChatRoom.objects.get_or_create(name=room_name)
    if created:
        chat_room.save()
    return render(request, "chat/room.html", {"room_name": room_name})
