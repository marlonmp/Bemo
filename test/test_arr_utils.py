import os
import unittest

from src.lib import arr_utils

class test_arr_utils(unittest.TestCase):

    def setUp(self):
        self.arr = ['num', 'str', 'class', 'def', 'vars', 'foo', 'bar']

    def test_filter(self):

        filtereds = arr_utils.filter(self.arr, lambda item: len(item) == 3)

        self.assertEqual(len(filtereds), 5)

        filtereds = arr_utils.filter(self.arr, lambda item: len(item) == 20)

        self.assertEqual(len(filtereds), 0)


    def test_find_index(self):

        index = arr_utils.find_index(self.arr, lambda item: item == 'str')

        self.assertEqual(index, 1)

        index = arr_utils.find_index(self.arr, lambda item: item == 'function')

        self.assertEqual(index, -1)


    def test_find_item(self):

        item = arr_utils.find_item(self.arr, lambda item_: 'c' in item_ )

        self.assertEqual(item, 'class')

        item = arr_utils.find_item(self.arr, lambda item_: 'x' in item_)

        self.assertEqual(item, None)
    

    def test_shuffle(self):

        shuffleds_arrs = 0

        for i in range(20):

            shuffled_arr = arr_utils.shuffle(self.arr)

            if shuffled_arr != self.arr:
                shuffleds_arrs += 1
        
        self.assertNotEqual(shuffleds_arrs, 0)


