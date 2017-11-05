import yaml

from photovoltaic.pv_simulator import pv_simulator

'''
Factory for pv_simulator objects.
'''
class pv_simulator_factory:
    def __init__(self, logger, path):
        self.logger = logger
        self.path = path

    def create_consumer(self):
        with open(self.path) as data:
            pv_data_map = yaml.load(data)

        return pv_simulator(self.logger, pv_data_map)
