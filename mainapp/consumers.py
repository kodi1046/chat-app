import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'you are now connected',
        }))
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data) # konvertera tillbaka till json
        message = text_data_json['message']
        print(message)