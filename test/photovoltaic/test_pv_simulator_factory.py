import logging
import yaml
from mockito import mock, unstub
from unittest import TestCase
from photovoltaic.pv_simulator_factory import pv_simulator_factory

class TestPv_simulator_factory(TestCase):
    def test_create_consumer_should_use_suuplied_file_as_power_data(self):
        # GIVEN
        mocked_log = mock(logging, strict=False)
        PATH_TO_TEST_DICT = 'photovoltaic/test_dict.txt'
        with open(PATH_TO_TEST_DICT) as data:
            test_data_map = yaml.load(data)

        factory = pv_simulator_factory(mocked_log, PATH_TO_TEST_DICT)

        # WHEN
        consumer = factory.create_consumer()

        # THEN
        consumer.power_data == test_data_map
        unstub()
