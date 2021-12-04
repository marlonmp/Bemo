import unittest

from src.lib.listener import Listener

class test_Listener(unittest.TestCase):

    def setUp(self):
        self.listener = Listener()

        self.start_event = {
            'type': 'start',
            'content': {
                'num_1': 2,
                'num_2': 4,
                'cancel': True
            }
        }

        self.num = 0

        def on_start_1(event: dict):
            print('\n\nEvent:',event, '\n\n')
            self.num += event['content']['num_1']

            if event['content']['cancel']:
                return False
            
        def on_start_2(event: dict):
            self.num += event['content']['num_2']

        self.listener_to_remove = on_start_1
            

        self.listener.add('start', on_start_1, on_start_2, on_start_1)

        print('listener events:', self.listener._events)


    def test_dispatch_event_cancel(self):

        self.listener.dispatch(self.start_event)

        self.assertEqual(self.num, 2)


    def test_dispatch_event_no_cancel(self):

        self.start_event['content']['cancel'] = False

        self.listener.dispatch(self.start_event)

        self.assertEqual(self.num, 8)


    def test_remove_listener(self):

        self.start_event['content']['cancel'] = False
        
        self.listener.remove('start', self.listener_to_remove)

        self.listener.dispatch(self.start_event)

        self.assertEqual(self.num, 6)