import unittest

from src.lib import video_info

class test_video_info(unittest.TestCase):

    def setUp(self):
        
        self.url = 'https://youtu.be/6tNS--WetLI'
        self.id = '6tNS--WetLI'
    
    def test_get(self):

        video = video_info.get(self.url)

        self.assertEqual(self.id, video['id'])