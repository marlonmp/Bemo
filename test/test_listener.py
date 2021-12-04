import unittest

from src.lib.listener import Listener

class test_Listener(unittest.TestCase):

    def setUp(self):
        self.listener = Listener()

        self.msg = '[EVENT] starting'

        self.num = 0

        def on_start_1():
            print(self.msg)

        def on_start_2():
            self.num += 2

        def on_start_3():
            print('[EVENT_MSG] ', self.msg)
            
        def on_start_4():
            self.num += 4

        self.funcs = [on_start_1, on_start_2]
            

        self.listener.add('start', on_start_1, on_start_2, on_start_1, on_start_3, on_start_4, on_start_1)

        print('listener events:', self.listener._events)


    def test_dispatch_event(self):

        self.listener.dispatch('start')

        self.assertEqual(self.num, 6)


    def test_remove_listener(self):
        
        self.listener.remove('start', *self.funcs)

        self.listener.dispatch('start')

        self.assertEqual(self.num, 4)