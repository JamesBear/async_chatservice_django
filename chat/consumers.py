# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from . import name_allocator
from . import chatbot
import asyncio
import time

MAX_REPLY_TIME = 5
SLEEP_INTERVAL = 0.5

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.nickname = name_allocator.random_name()

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']


        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender' : self.nickname
            }
        )
        
        msg_obj = [self.nickname, message, None]
        chatbot.push_message(msg_obj)

        await self.get_bot_reply(msg_obj)
        reply = msg_obj[2]

        if reply != None:
            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': reply,
                    'sender' : 'bot'
                }
            )
    
    async def get_bot_reply(self, message_object):
        start_time = time.time()
        while True:
            await asyncio.sleep(SLEEP_INTERVAL)
            if message_object[2] != None:
                break
            elapsed = time.time() - start_time
            if elapsed > MAX_REPLY_TIME:
                print(self.get_name() + ': chatbot reply time out')
                break

    def get_name(self):
        return self.nickname

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': sender + ': ' + message
        }))