import threading



'''
This class wraps a rabbit_consumer and starts it to consume messages.
'''


class pv_consumer(threading.Thread):
    def __init__(self, logger, rabbit_consumer):
        threading.Thread.__init__(self)
        self.logger = logger
        self.rabbit_consumer = rabbit_consumer

    def run(self):
        self.rabbit_consumer.initialize_queue()
        self.rabbit_consumer.start_consuming()
