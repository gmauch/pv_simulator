from output.output_formatter import pv_output_formatter
from output.outputter import outputter

'''
Implmentation of outputter class that writes message to a file in the underlying file system
'''
class file_outputter(outputter):
    def __init__(self, path):
        self.path = path
        self.formatter = pv_output_formatter()

    def write(self, meter_value, pv_value):
        with open(self.path, 'a') as out_file:
            out_file.write(self.formatter.format_meter_and_pv_value_to_message(meter_value, pv_value))
