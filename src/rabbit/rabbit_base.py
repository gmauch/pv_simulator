import pika

'''
Generic class to wrap a RabbitMQ broker and provide useful methods for publishers and consumers.
'''
class rabbit_base:
    QUEUE_NAME = 'pv_queue'

    def __init__(self, broker_address):
        self.broker_address = broker_address

    def initialize_queue(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.broker_address))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.QUEUE_NAME)

    def close(self):
        self.connection.close()