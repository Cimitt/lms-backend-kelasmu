import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chat.models import ClassChatMessage, DirectChatMessage
from api.chat.serializers import ClassChatMessageSerializer, DirectChatMessageSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class ClassChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']
        if user.is_anonymous:
            await self.close()
            return

        self.material_id = self.scope['url_route']['kwargs']['material_id']
        self.room_group_name = f'class_chat_{self.material_id}'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')
        user = self.scope['user']

        chat_message = await self.create_message(user.id, self.material_id, message)
        serializer = ClassChatMessageSerializer(chat_message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': serializer.data
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event['message']))

    @database_sync_to_async
    def create_message(self, user_id, material_id, message):
        return ClassChatMessage.objects.create(
            sender_id=user_id,
            material_id=material_id,
            content=message
        )

class DirectChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']
        if user.is_anonymous:
            await self.close()
            return

        self.user_id = int(self.scope['url_route']['kwargs']['user_id'])
        self.room_group_name = f'direct_chat_{min(user.id, self.user_id)}_{max(user.id, self.user_id)}'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')
        sender = self.scope['user']

        chat_message = await self.create_message(sender.id, self.user_id, message)
        serializer = DirectChatMessageSerializer(chat_message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': serializer.data
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event['message']))

    @database_sync_to_async
    def create_message(self, sender_id, recipient_id, message):
        return DirectChatMessage.objects.create(
            sender_id=sender_id,
            recipient_id=recipient_id,
            content=message
        )
