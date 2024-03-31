from django.contrib.auth.decorators import login_required
from authentication.models import User

from django.shortcuts import render
# do not change this
from chat.models import ChatRoom
from django.http import JsonResponse
from .models import Message
from chat.consumers import ChatConsumer


@login_required
def index(request):
    return render(request, "chat/selectRoom.html")


@login_required
def room(request, room_name):
    chat_room, created = ChatRoom.objects.get_or_create(name=room_name)
    if created:
        chat_room.save()
    messages_req = Message.objects.filter(room_id= chat_room._id)
    messages_db = []
    for message in messages_req:
        user = User.objects.get(_id=message.user_id)
        messages_db.append( {"username" : user.username, "content": message.content} )
    return render(request, "chat/room.html", {"room_name": room_name, "messages_db": messages_db})


@login_required
def save_message(request):
    if request.method == 'POST':
        message_content = request.POST.get('message', '')
        if message_content:
            # Save the message to the database
            Message.objects.create(content=message_content)
            

def get_users_in_room(request, room_name):
    # Utilisez votre fonction get_users_in_room pour récupérer la liste des utilisateurs dans la salle
    users = ChatConsumer.get_users_in_room(room_name)
    return JsonResponse(users, safe=False)

