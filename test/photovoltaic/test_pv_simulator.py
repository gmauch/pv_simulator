import logging
import datetime
from unittest import TestCase

from mockito import mock, unstub

from photovoltaic.pv_simulator import pv_simulator


class TestPv_simulator(TestCase):
    def test_pv_simulator_should_use_injected_dict_as_source_for_generation(self):
        # GIVEN
        mocked_log = mock(logging, strict=False)
        TEN_O_CLOCK_PRODUCTION = 50
        ELEVEN_O_CLOCK_PRODUCTION = 50
        power_data = {'10:00' : TEN_O_CLOCK_PRODUCTION, '11:00' : ELEVEN_O_CLOCK_PRODUCTION}
        pv = pv_simulator(mocked_log, power_data)
        test_date = datetime.datetime(2017, 11, 4, 10, 00)

        # WHEN
        generated_value = pv.generate(test_date)

        # THEN
        self.assertEqual(TEN_O_CLOCK_PRODUCTION, generated_value)
        unstub()

    def test_pv_simulator_should_consider_0_for_nonexistent_times_in_power_data(self):
        # GIVEN
        mocked_log = mock(logging, strict=False)
        TEN_O_CLOCK_PRODUCTION = 50
        ELEVEN_O_CLOCK_PRODUCTION = 50
        power_data = {'10:00': TEN_O_CLOCK_PRODUCTION, '11:00': ELEVEN_O_CLOCK_PRODUCTION}
        pv = pv_simulator(mocked_log, power_data)
        test_date = datetime.datetime(2017, 11, 4, 12, 00)

        # WHEN
        generated_value = pv.generate(test_date)

        # THEN
        self.assertEqual(0, generated_value)
        unstub()
