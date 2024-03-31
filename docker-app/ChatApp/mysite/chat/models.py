import uuid
from django.db import models


class ChatRoom(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)


class Message(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField(editable=True)
    room_id = models.UUIDField(editable=True)
    content = models.CharField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
