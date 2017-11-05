'''
Class that models a photo-voltaic generator.
The class uses a dict that associates a time of day to for the power values as source.
'''
class pv_simulator:
    def __init__(self, logger, power_data):
        self.logger = logger
        self.power_data = power_data

    def generate(self, time):
        return float(self.power_data.get(self._extract_power_data_key_from_datetime(time), 0))

    def _extract_power_data_key_from_datetime(self, when):
        try:
            return "{:02d}:{:02d}".format(when.hour, when.minute)
        except:
            self.logger.error("Error extracting hour and minute from {}".format(when))
            return "00:00"
