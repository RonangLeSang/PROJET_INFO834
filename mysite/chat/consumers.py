import json
import redis
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from djongo import models

# Create a Redis connection
r = redis.Redis(host='localhost', port=6379, db=0)

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user_id = str(self.scope["user"])
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        # Add user ID to Redis set
        r.sadd(self.room_name, self.user_id)

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

        # Remove user ID from Redis set
        r.srem(self.room_name, self.user_id)

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        messageOnly = text_data_json["message"]
        message = self.user_id + " : " + messageOnly
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
        
    
    def get_users_in_room(room_name):
        userlist = r.smembers(room_name)
        return [str(user_id, 'utf-8') for user_id in userlist]







    