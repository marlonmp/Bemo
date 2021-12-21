from src.lib import time_format
from src.lib import video_info

class Song:

    __id: int
    __video_id: str
    __title: str
    __duration: int

## constructor

    def __init__(self, *, set_from_db: dict = {}, set_from_url: str = ''):
        
        self.__id = 0

        if set_from_db: self.__build_from_db(set_from_db)

        elif set_from_url: self.__build_from_url(set_from_url)

## build functions

    def __build_from_db(self, dict_: dict):

        self.__id = dict_['id']

        self.__video_id = dict_['video_id']

        self.__title = dict_['title']

        self.__duration = dict_['duration']

    
    def __build_from_url(self, url: str):

        info = video_info.get(url)

        self.__video_id = info['id']

        self.__title = info['title']

        self.__duration = info['duration']

## setters

    def set_id(self, id: int):
        self.__id = id

## getters

    def get_id(self):
        return self.__id


    def get_video_id(self):
        return self.__video_id


    def get_title(self):
        return self.__title


    def get_cover_url(self):
        return 'https://i3.ytimg.com/vi/' + self.__video_id + '/maxresdefault.jpg'


    def get_video_url(self):
        return 'https://youtu.be/' + self.__video_id


    def get_duration(self):
        return self.__duration


    def get_duration_fmt(self):
        return time_format.format(self.__duration)


    def get_source(self):

        info = video_info.get(self.get_video_url())

        return info['formats'][0]['url']

## fmt

    def to_dict(self):

        return {
            'id': self.__id,
            'video_id': self.__video_id,
            'title': self.__title,
            'duration': self.__duration
        }