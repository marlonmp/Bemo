from discord import Embed

from src.model.playlist import Playlist
from src.model.song import Song


from src.lib import arr_utils as arr_u
from src.lib import embeds
from src.lib import JSON


from re import match as re_match
from copy import copy

from dotenv import load_dotenv

import os

## constants

load_dotenv()

_DB_PATH = os.environ.get('DB_PATH')

##

class __DB:

    __data: list[Playlist]

## constructor

    def __init__(self):

        self.__data = []

        self.load()

## filters

    def __get_pl_by_id(self, id: int):

        return arr_u.find_index(self.__data, lambda pl: pl.get_id() == id)


    def __get_pl_by_title(self, title: str):

        regexp = '^' + title

        return arr_u.find_index(self.__data, lambda pl: re_match(regexp, pl.get_title()))


    def get_pl_index(self, *, by_id: int = -1, by_title: str = ''):
      
        if by_id > -1:
            return self.__get_pl_by_id(by_id)
        
        elif by_title:
            return self.__get_pl_by_title(by_title)
        
        return -1
    

    def get_pl(self, *, by_id: int = -1, by_title: str = ''):

        pl_index = self.get_pl_index(by_id=by_id, by_title=by_title)

        return self.__data[pl_index] if pl_index > -1 else None


    def get_pl_from_prefix(self, prefix: str):
        
        pl = None

        if self.__is_valid_title(prefix):
            pl = self.get_pl(by_title=prefix)

        elif self.__is_valid_id(prefix): 
            pl = self.get_pl(by_id=int(prefix))
        
        return pl


## validators

    def __is_valid_title(self, title: str):

        regexp = '^[a-z\d\_\-]{3,20}$'

        return True if re_match(regexp, title) else False
    

    def __is_valid_id(self, id: str):
        
        regexp = '^\d+$'

        return True if re_match(regexp, id) else False


    def __validate_new_title(self, title: str) -> str:

        is_valid_title = self.__is_valid_title(title)

        if not is_valid_title:
            return 'Title no valid'

        index = self.__get_pl_by_title(title)

        if index >= 0:
            return 'This title is already in use'
        
        return ''

## CRUD

    # cmd - show
    def show_pl(self):

        embeds_arr: list[Embed] = []

        data_len = len(self.__data)

        if data_len == 0:
            embeds_arr.append(embeds.red(description='No playlist in data base'))
            
        else:

            for playlist in self.__data:
                
                embed = embeds.green()                

                embed.add_field(name='id', value=playlist.get_id(), inline=True)
                embed.add_field(name='Title', value=playlist.get_title(), inline=True)
                embed.add_field(name='Author', value=playlist.get_owner(), inline=True)
                embed.add_field(name='Songs', value=playlist.get_songs_quantity(), inline=True)
                embed.add_field(name='Duration', value=playlist.get_duration_fmt(), inline=True)

                embeds_arr.append(embed)
        
        return embeds_arr

    # cmd - list
    def list_songs(self, prefix: str):

        embeds_arr: list[Embed] = []

        pl = self.get_pl_from_prefix(prefix)

        if pl:

            songs = pl.get_songs()

            songs_len = len(songs)

            if songs_len > 0:

                for song in songs:

                    embed = embeds.green(title='Song')

                    embed.set_thumbnail(url=song.get_cover_url())

                    embed.add_field(name='Id', value=song.get_id(), inline=True)
                    embed.add_field(name='Title', value=f'[{song.get_title()}]({song.get_video_url()})', inline=True)
                    embed.add_field(name='Duration', value=song.get_duration_fmt(), inline=True)

                    embeds_arr.append(embed)

            else:
                embed = embeds.red(description='This playlist is empty')

                embeds_arr.append(embed)

        else:
            embed = embeds.red(description='No playlist found')

            embeds_arr.append(embed)

        return embeds_arr

    # cmd - new
    def new_pl(self, title: str, owner: int) -> str:

        err = self.__validate_new_title(title)

        if err:
            return err

        pl = Playlist(new_={'title': title, 'owner': owner})

        data_len = len(self.__data)

        # new_id = last playlist id + 1
        new_id = self.__data[-1].get_id() + 1 if data_len > 0 else 1

        new_pl = copy(pl)

        new_pl.set_id(new_id)

        self.__data.append(new_pl)

        return 'Playlist created'

    # cmd - update
    def update_title(self, prefix: str, title: str) -> str:

        err = self.__validate_new_title(title)

        if err:
            return err

        pl = self.get_pl_from_prefix(prefix)

        if pl:

            pl.set_title(title)

            return 'Playlist updated'
        
        return 'No playlist found'

    # cmd - delete
    def delete_pl(self, pl_id: int) -> str:

        pl_index = self.__get_pl_by_id(pl_id)

        if pl_index >= 0:
            self.__data.pop(pl_index)

            return 'Playlist deleted'
        
        return 'No playlist found'

    # cmd - add
    def add_song(self, prefix: str, url: str) -> str:

        song = Song(set_from_url=url)

        pl = self.get_pl_from_prefix(prefix)

        if pl:

            if pl.add_song(song):
                return 'Song added'
            
            return 'Song is already into playlist'
        
        return 'Playlist not found'

    # cmd - remove
    def remove_song(self, prefix: str, song_id: int) -> str:

        pl = self.get_pl_from_prefix(prefix)

        if pl:

            if pl.delete_song(song_id):
                return 'Song removed'
        
            return 'Song not found'
        
        return 'Playlist not found'

##

    def to_dict(self):

        return {
            'playlist': [pl.to_dict() for pl in self.__data]
        }

## load and save

    def load(self):

        db = JSON.parse_file(_DB_PATH, '{"playlist":[]}')

        for dict_ in db['playlist']:

            pl = Playlist(set_from_db=dict_)

            self.__data.append(pl)
    

    def save(self):

        JSON.stringify_file(_DB_PATH, self.to_dict())
    

DB = __DB()