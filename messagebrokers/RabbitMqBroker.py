from typing import Dict
from messagebrokers.interface import MetaBroker
import pika

class RabbitMqBroker(MetaBroker):
    def __init__(self, host:str, queue_name:str):
        self.queue_name=queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)
    
    def add_task(self, data: Dict):
        print(f"data to send {data}")
        file_path = data["path"]
        self.channel.basic_publish(exchange='',
                      routing_key=self.queue_name,
                      body=file_path)


