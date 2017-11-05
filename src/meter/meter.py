import random

'''
Class that models a home power consumption.
ASSUMPTIONS:
As the idea for this class is to simulate a home power consumption, I thought that generating a random value for
instantaneous consumption would be strange, since I ASSUMED it can not be erratic. For instance, if the generation was
random, then in one second there could a consumption of 10 watts, then 800, then back to 10, then 700, which does not
seem to me like a typical home consumption. Instead, I created a variable to store the last measured consumption and the
next value is a randomic variation limited to 10% of the total. This way the variation between consecutive reads will be
a slight increase or decrease in relation to the previously read value, which, IN MY ASSUMPTION, is a better model for a
home power consumption than just any possible value between the min and max values.
'''
class meter:
    VARIATION_LOWER_LIMIT = -0.1
    VARIATION_UPPER_LIMIT = 0.1

    def __init__(self, initial_consumption, max_consumption):
        self._check_intervals(initial_consumption, max_consumption)
        self.current_consumption = initial_consumption
        self.max_consumption = max_consumption

    def generate_consumption(self):
        variation = random.uniform(self.VARIATION_LOWER_LIMIT, self.VARIATION_UPPER_LIMIT) * self.max_consumption
        self.current_consumption = self._enforce_boundaries(variation)

        return self.current_consumption

    def _enforce_boundaries(self, variation):
        total = self.current_consumption + variation
        if total < 0:
            return 0
        elif total > self.max_consumption:
            return self.max_consumption
        else:
            return total

    def _check_intervals(self, initial_consumption, max_consumption):
        if not 0 <= initial_consumption <= max_consumption:
            raise ValueError('Initial consumption must be between 0 and {}, but {} was supplied'
                             .format(max_consumption, initial_consumption))