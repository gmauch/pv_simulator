import datetime
'''
Class that formats a message from a photovoltaic value and meter reading (home power consumption) according in the
format defined in the instructions of this application.
'''
class pv_output_formatter:
    def format_meter_and_pv_value_to_message(self, meter_value, pv_value):
        return "[{}] meter: {} pv: {}, sum of powers: {}\n".format(datetime.datetime.now(),
                                                                           meter_value,
                                                                           pv_value,
                                                                           meter_value + pv_value)
