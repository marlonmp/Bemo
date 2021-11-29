import re

from ..lib.video_info import get
from ..lib.time_format import format

class Song:

    id: str
    title: str
    duration: int

    def __init__(self, url='', dict={}):

        if url != '':
            self.__get_from_url(url)

        elif dict != {}:
            self.__get_from_dict(dict)

    def __get_from_url(self, url: str):

        video= get(url)

        self.id = video['id']
        self.title = video['title']

        # time in seconds
        self.duration = video['duration']

    def __get_from_dict(self, dict: dict):
        
        self.id = dict['id']
        self.title = dict['title']
        self.duration = dict['duration']

    def get_duration_formated(self):
        return format(self.duration)

    def to_dict(self) -> dict:
        
        return {
            'id': self.id,
            'title': self.title,
            'duration': self.duration
        }
        