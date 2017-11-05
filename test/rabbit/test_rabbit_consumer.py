import logging

from unittest import TestCase

from mockito import mock, when, verify, unstub
from mockito.matchers import any

from photovoltaic.pv_simulator import pv_simulator
from photovoltaic.pv_simulator_factory import pv_simulator_factory
from output.file_outputter import file_outputter
from rabbit.rabbit_consumer import rabbit_consumer

class TestRabbit_consumer(TestCase):
    def test_consumer_callback_should_call_outputter_write_and_pv_simulator_generate(self):
        # GIVEN
        ADDRESS = '127.0.0.1'
        PATH = '/'
        EMPTY_DICT = dict()
        CONSUMER_CALLBACKED_VALUE = 0.1234
        MOCKED_PV_GENERATED_VALUE = 0.5678

        mocked_log = mock(logging, strict=False)
        mocked_pv_simulator = mock(pv_simulator(mocked_log, EMPTY_DICT), strict=False)
        when(mocked_pv_simulator).generate(any).thenReturn(MOCKED_PV_GENERATED_VALUE)
        factory = mock(pv_simulator_factory(mocked_log, PATH), strict=False)
        when(factory).create_consumer().thenReturn(mocked_pv_simulator)
        outputter = mock(file_outputter(PATH), strict=False)
        consumer = rabbit_consumer(ADDRESS, factory, outputter)

        # WHEN
        consumer.callback('channel', 'method', 'properties', CONSUMER_CALLBACKED_VALUE)

        # THEN
        verify(outputter).write(CONSUMER_CALLBACKED_VALUE, MOCKED_PV_GENERATED_VALUE)
        verify(mocked_pv_simulator).generate(any) # Can't specify when this test is going to run
        unstub()
