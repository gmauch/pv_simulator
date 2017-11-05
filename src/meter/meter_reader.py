import threading
import time

'''
Class that coordinates a meter class to generate simulated home power readings with a RabbitMQ publisher.
'''
class meter_reader(threading.Thread):

    def __init__(self, log, meter, interval, rabbit_publisher):
        threading.Thread.__init__(self)
        self.logger = log
        self.meter = meter
        self.producer_interval = interval
        self.rabbit_publisher = rabbit_publisher

    def run(self):
        self.rabbit_publisher.initialize_queue()
        try:
            while True:
                self.rabbit_publisher.publish_meter(self.meter.generate_consumption())
                time.sleep(self.producer_interval)
        except:
            pass
        finally:
            self.rabbit_publisher.close()