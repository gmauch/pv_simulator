from rabbit.rabbit_base import rabbit_base

'''
Class that extends functionalities of the rabbit_base class to provide methods for a RabbitMQ publisher.
'''
class rabbit_publisher(rabbit_base):
    def __init__(self, broker_address):
        rabbit_base.__init__(self, broker_address)

    def publish_meter(self, meter_value):
        self.channel.basic_publish(exchange='',
                                   routing_key=self.QUEUE_NAME,
                                   body=str(meter_value))
