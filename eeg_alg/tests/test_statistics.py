from unittest import TestCase

from statistics import *


class TestStatistics(TestCase):
    def test_relative_frequency(self):
        data = [6, 12, 8, 4]
        r = relative_frequency(data)

TestStatistics().test_relative_frequency()
