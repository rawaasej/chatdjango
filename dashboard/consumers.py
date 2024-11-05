import json
from channels.generic.websocket import AsyncWebsocketConsumer
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['temperature_db']
collection = db['temperature_data']

class TemperatureConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Insérer les données dans MongoDB
        collection.insert_one({"message": message})

        # Envoyer un accusé de réception au client
        await self.send(text_data=json.dumps({
            'message': "Data saved to MongoDB"
        }))
