import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):

    user_id = None

    def connect(self):
        self.room_group_name = "test"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        self.accept()
    
    def receive(self, text_data):

        text_data_json = json.loads(text_data) # converts back to json

        if text_data_json['type'] == 'text':

            message = text_data_json['message']
            user_id = text_data_json['id']

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type':'chat_message',
                    'message':message,
                    'id':user_id,
                }
            )
        
        elif text_data_json['type'] == 'image':

            image = text_data_json['image']
            user_id = text_data_json['id']

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type':'chat_image',
                    'image':image,
                    'id':user_id,
                }
            )
    
    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type':'chat_messagechat',
            'message':message,
            'id': event['id'],
        }))

        

    def chat_image(self, event):
        image = event['image']
        self.send(text_data=json.dumps({
            'type':'chat_messageimage',
            'image':image,
            'id': event['id'],
        }))

