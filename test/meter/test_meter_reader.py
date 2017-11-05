import logging
import time
from unittest import TestCase

from mockito import mock, when, verify, unstub

from meter.meter import meter
from meter.meter_reader import meter_reader
from rabbit.rabbit_publisher import rabbit_publisher


class TestMeter_reader(TestCase):
    def test_running_meter_reader_should_call_meter_generate_consumption_and_rabbit_publisher_publish(self):
        # GIVEN
        mocked_log = mock(logging)
        mocked_meter = mock(meter, strict=False)
        mocked_rabbit_publisher = mock(rabbit_publisher, strict=False)
        SHORT_INTERVAL = 1
        DEFAULT_INTERVAL = 2
        DEFAULT_CONSUMPTION = 100
        when(mocked_meter).generate_consumption().thenReturn(DEFAULT_CONSUMPTION)
        ameter_reader = meter_reader(mocked_log, mocked_meter, DEFAULT_INTERVAL, mocked_rabbit_publisher)

        # WHEN
        ameter_reader.start()
        time.sleep(SHORT_INTERVAL)

        # THEN
        verify(mocked_rabbit_publisher).publish_meter(DEFAULT_CONSUMPTION)
        verify(mocked_meter).generate_consumption()
        unstub()
