import argparse
import logging as log

from meter.meter import meter
from photovoltaic.pv_consumer import pv_consumer

from meter.meter_reader import meter_reader
from output.file_outputter import file_outputter
from photovoltaic.pv_simulator_factory import pv_simulator_factory
from rabbit.rabbit_consumer import rabbit_consumer
from rabbit.rabbit_publisher import rabbit_publisher

'''
Class that defines, configures and reads user-supplied arguments.
'''
class arguments:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='PV Simulator. This application solves the problem described in ./docs/PV Simulator Challenge.pdf')

    def check_positive(self, value):
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
        return ivalue

    def _configure_command_args(self):
        self.parser.add_argument('-b', '--broker_address',
                                 help='Address of the RabbitMQ Broker to be used to exchange messages.'
                                      ' Defaults to localhost.',
                                 type=str,
                                 default='localhost')
        self.parser.add_argument('-p', '--power_data_file',
                                 help='Path to a yaml file containing power data associated to time of day.'
                                      ' Defaults to ../input/default.yaml.',
                                 type=str,
                                 default='../input/default.yaml')
        self.parser.add_argument('-pi', '--producer_interval',
                                 help='Interval in seconds between producer samples are generated. Defaults to 2.',
                                 type=int,
                                 default=2)
        self.parser.add_argument('-i', '--initial_meter',
                                 help='Initial value for meter consumption. Defaults to 0.',
                                 type=int,
                                 default=0)
        self.parser.add_argument('-m', '--max_meter',
                                 help='Max value for meter consumption. Defaults to 900.',
                                 type=int,
                                 default=900)
        self.parser.add_argument('-o', '--output_path',
                                 help='Path for output file generated during program execution. Defaults to output/results.out.',
                                 type=str,
                                 default='../output/results.out')
        self.parser.add_argument("-l", "--logging_path",
                                 help="Path to output application logs. Defaults to output/output.log.",
                                 type=str,
                                 default='../output/output.log')
        self.parser.add_argument("-ll", "--logging_level",
                                 help="Level for logging statements. Defaults to INFO.",
                                 type=str.upper,
                                 choices=["INFO", "DEBUG", "WARN", "ERROR"],
                                 default="INFO")

    def _parse_command_arguments(self):
        args = self.parser.parse_args()
        self.broker_address = args.broker_address
        self.power_data_file = args.power_data_file
        self.producer_interval = args.producer_interval
        self.initial_meter = args.initial_meter
        self.max_meter = args.max_meter
        self.output_path =  args.output_path
        self.logging_path = args.logging_path
        self.logging_level = args.logging_level

'''
Main class of the project. Orchestrates the creation and execution of objects.
'''
class pv_simulator:
    def process_input_arguments(self):
        args = arguments()
        args._configure_command_args()
        args._parse_command_arguments()
        return args

    def create_logging(self, args):
        log.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=args.logging_level,
                        filename=args.logging_path)

    def start_meter_reading(self, args):

        reader = meter_reader(log, meter(args.initial_meter, args.max_meter),
                              args.producer_interval, rabbit_publisher(args.broker_address))
        reader.start()

    def start_pv_readings(self, args):
        factory = pv_simulator_factory(log, args.power_data_file)
        outputter = file_outputter(args.output_path)
        rabbit = rabbit_consumer(args.broker_address, factory, outputter)
        consumer = pv_consumer(log, rabbit)
        consumer.start()

if __name__ == '__main__':
    pv_simulator = pv_simulator()
    arguments = pv_simulator.process_input_arguments()
    pv_simulator.start_meter_reading(arguments)
    pv_simulator.start_pv_readings(arguments)
