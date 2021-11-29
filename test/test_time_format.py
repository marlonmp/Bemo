import unittest

from src.lib import time_format

class test_time_format(unittest.TestCase):

    def setUp(self):
        
        self.time_sec = 2352
        self.time_formated = '39:12'
    
    def test_format(self):

        time_formated = time_format.format(self.time_sec)

        self.assertEqual(time_formated, self.time_formated)