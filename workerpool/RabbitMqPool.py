from workerpool.interface import MetaWorkerPool
import pika

def callback(ch, method, properties, body):
    print(f"processing file path {body}")
    

class RabbitMqPool(MetaWorkerPool):
    def __init__(self, host:str,queue_name:str):
        self.queue_name=queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)
        self.channel.basic_consume(queue=queue_name,
                      auto_ack=True,
                      on_message_callback=callback)


    def start_pooling(self):
        self.channel.start_consuming()
