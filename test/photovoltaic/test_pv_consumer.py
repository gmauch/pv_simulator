import logging
from unittest import TestCase

from mockito import mock, verify, unstub

from output.file_outputter import file_outputter
from photovoltaic.pv_consumer import pv_consumer
from photovoltaic.pv_simulator_factory import pv_simulator_factory
from rabbit.rabbit_consumer import rabbit_consumer

class TestPv_consumer(TestCase):
    def test_running_pv_consumer_should_call_rabbit_consumer_initialize_queue_and_start_consuming(self):
        # GIVEN
        ADDRESS = '127.0.0.1'
        PATH = '/'
        mocked_log = mock(logging, strict=False)
        factory = mock(pv_simulator_factory(mocked_log, PATH), strict=False)
        outputter = mock(file_outputter(PATH), strict=False)
        mocked_rabbit_consumer = mock(rabbit_consumer(ADDRESS, factory, outputter), strict=False)
        consumer = pv_consumer(mocked_log, mocked_rabbit_consumer)

        # WHEN
        consumer.start()

        # THEN
        verify(mocked_rabbit_consumer).initialize_queue()
        verify(mocked_rabbit_consumer).start_consuming()
        unstub()
