import os
import unittest

from src.lib import JSON

class test_JSON(unittest.TestCase):

    def setUp(self):
        self.dict = {
            'name': 'marlo',
            'age': 18
        }

        self.path = 'dict.json'

    def test_stringify_file(self):

        JSON.stringify_file(self.path, self.dict)

    def test_parse(self):
        
        file_dict = JSON.parse_file(self.path)

        os.remove(self.path)

        self.assertEqual(self.dict, file_dict)