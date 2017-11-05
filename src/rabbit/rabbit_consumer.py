import datetime

from rabbit.rabbit_base import rabbit_base

'''
Class that extends functionalities of the rabbit_base class to provide methods for a RabbitMQ consumer.
'''
class rabbit_consumer(rabbit_base):
    def __init__(self, broker_address, factory, outputter):
        rabbit_base.__init__(self, broker_address)
        self.pv = factory.create_consumer()
        self.outputter = outputter

    def start_consuming(self):
        self.channel.basic_consume(self.callback,
                                   queue=self.QUEUE_NAME,
                                   no_ack=True)
        self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)
        self.outputter.write(float(body), self.pv.generate(datetime.datetime.now()))
