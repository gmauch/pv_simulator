from unittest import TestCase

from meter.meter import meter

from mockito import unstub

class TestMeter(TestCase):
    def test_should_raise_ValueError_with_negative_initial_consumption(self):
        with self.assertRaises(ValueError):
            meter(-1, 10)

    def test_should_raise_ValueError_with_invalid_initial_consumption_greater_than_max(self):
        with self.assertRaises(ValueError):
            meter(11, 10)

    def test_generate_consumption_should_be_between_ranges(self):
        # GIVEN a meter with initial_consumption of 0 and max of 10000
        lower_boundary = 0
        upper_boundary = 10
        how_many_iterations = 100000
        ameter = meter(lower_boundary, upper_boundary)

        # WHEN consumption is generated a lot of times (lot == 10000)
        # each consumption value should be within the defined boundaries
        for i in range(how_many_iterations):
            consumption = ameter.generate_consumption()
            if consumption < lower_boundary or consumption > upper_boundary:
                self.assertFalse('Found consumption of {}. Should be between {} and {}'
                                 .format(consumption, lower_boundary, upper_boundary))
        # THEN
        self.assertTrue('Ran {} iterations without non-conformances in meter.generate_consumption()')
        unstub()
