import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    #Função de conexão antiga
    #def connect(self):
    #    self.room_group_name = 'test'

     #   async_to_sync(self.channel_layer.group_add)(
      #      self.room_group_name,
       #     self.channel_name
        #)

        #self.accept()
    def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print('VC FOI CONECTADO A SALA: ' + self.room_name)
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        print('VC FOI DESCONECTADO DA SALA: ' + self.room_name)
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'sender': sender
            }
        )

    def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        self.send(text_data=json.dumps({
            #'type':'chat',
            'message':message,
            'sender': sender
        }))