from src.model.song import Song


from src.lib import arr_utils as arr_u
from src.lib import time_format


from re import match as re_match
from copy import copy

##

class Playlist:

    __id:       int
    __owner:    int
    __title:    str
    __songs:    list[Song]
    __duration: int

## constructor

    def __init__(self, *, set_from_db: dict = {}, new_: dict = {}):
        
        self.__id = 0

        if set_from_db: self.__build_from_dict(set_from_db)

        elif new_: self.__build_a_new_one(new_)

## build functions

    def __build_from_dict(self, dict_: dict[str, list[dict]]):

        self.__id = dict_['id']

        self.__owner = dict_['owner']

        self.__title = dict_['title']

        self.__songs = [Song(set_from_db= song) for song in dict_['songs']]

        self.__duration = 0

        for song in self.__songs:

            self.__duration += song.get_duration()


    def __build_a_new_one(self, dict_: dict):
        
        self.__owner = dict_['owner']

        self.__title = dict_['title']

        self.__duration = 0

        self.__songs = []

## search

    def get_song_index(self, song_id: int):
      
        return arr_u.find_index(self.__songs, lambda song: song.get_id() == song_id)

    def get_song(self, song_id: int):

        song_index = self.get_song_index(song_id)

        return self.__songs[song_index]

## update

    def add_song(self, song: Song):

        index = arr_u.find_index(self.__songs, lambda song_: song_.get_video_id() == song.get_video_id())

        if index >= 0:
            return False

        songs_len = len(self.__songs)

        # new_id = last song id + 1
        new_id = self.__songs[-1].get_id() + 1 if songs_len > 0 else 1

        new_song = copy(song)

        new_song.set_id(new_id)

        self.__songs.append(new_song)

        return True

## delete song

    def delete_song(self, song_id: int):

        song_index = self.get_song_index(song_id=song_id)

        if song_index >= 0:
            self.__songs.pop(song_index)
            return True
        
        return False

## setters

    def set_id(self, id: int):
        self.__id = id


    def set_title(self, title: str):
        self.__title = title

## getters

    def get_id(self):
        return self.__id


    def get_owner(self):
        return f'<@{self.__owner}>'


    def get_title(self):
        return self.__title


    def get_songs(self):
        return self.__songs


    def get_songs_copy(self):
        return self.__songs[:]


    def get_songs_quantity(self):
        return len(self.__songs)
    

    def get_duration_fmt(self):
        return time_format.format(self.__duration)

## fmt

    def load_songs(self, data: list[dict]):

        for dict_ in data:
            song = Song(set_from_db=dict_)
            self.__songs.append(song)


    def to_dict(self):

        return {
            'id':self.__id,
            'owner':self.__owner,
            'title':self.__title,
            'songs': [ song.to_dict() for song in self.__songs ]
        }