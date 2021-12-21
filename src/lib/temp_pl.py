## temporal_playlist.py
from discord import FFmpegPCMAudio

from src.lib.vc_manager import VC
from src.lib.cache import DB

from src.model.playlist import Playlist
from src.model.song import Song

from src.lib import arr_utils as arr_u

from copy import copy


_FFMPEG_OPTS = { 'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn' }


class _temp_playlist:

    __playlist: Playlist

    __song_playing:   int

    __bucle:    int

    __songs: list[Song]

## constructor

    def __init__(self):

        self.__playlist = None

        self.__song_playing = -1

        self.__bucle = 0

        self.__songs = []

##

    def __clone_songs(self):

        self.__songs = self.__playlist.get_songs_copy()

##

    def __get_song_by_id(self, song_id: int):
        return arr_u.find_index(self.__songs, lambda song: song.get_id() == song_id)


    def __get_song_playing_index(self):
        return self.__get_song_by_id(self.__song_playing)

##

    # cmd - start
    def start(self, pl_id: int, song_id: int = 0) -> str:
        pl = DB.get_pl(by_id=pl_id)

        if pl:
            self.__playlist = copy(pl)

            self.__songs = pl.get_songs_copy()

            songs_len = len(self.__songs)

            if songs_len > 0:

                index = self.__get_song_by_id(song_id)

                index = 0 if index < 0 else index

                self.__play_index(index)

            return ''

        return 'No playlist found'


    def __play_index(self, song_index: int):
        
        song = self.__songs[song_index]

        print('song', song.get_title())

        if VC.voice_client:

            source = song.get_source()

            self.__song_playing = song.get_id()

            if VC.voice_client.is_playing():
                VC.voice_client.pause()

            VC.voice_client.play(FFmpegPCMAudio(source, **_FFMPEG_OPTS), after=self.next)

    # cmd - play
    def play(self, song_id: int) -> str:

        index = self.__get_song_by_id(song_id)

        if index >= 0:

            self.__play_index(index)
            return 'Playing song'

        return 'Song not found'

    # cmd - replay
    def replay(self):

        index = self.__get_song_playing_index()

        if index >= 0:

            self.__play_index(index)


    def __get_previus(self):

        songs_len = len(self.__songs) -1

        index = self.__get_song_playing_index()

        previus_song = songs_len if (index  == 0) else index  -1

        return previus_song
    
    # cmd - previus
    def previus(self):

        songs_len = len(self.__songs)

        if songs_len > 0:

            index = self.__get_previus()

            self.__play_index(index)

    # cmd - pause
    def pause(self):

        if VC.voice_client and VC.voice_client.is_playing():

            VC.voice_client.pause()

    # cmd - resume
    def resume(self):

        if VC.voice_client and VC.voice_client.is_paused():

            VC.voice_client.resume()


    def __get_next(self):

        songs_len = len(self.__songs) -1

        index = self.__get_song_playing_index()

        next_song = 0 if (index == songs_len) else index +1

        return next_song

    # cmd - next
    def next(self, e = None):

        songs_len = len(self.__songs)

        if songs_len > 0:

            index = self.__get_next()

            self.__play_index(index)

    # cmd - loop
    def loop(self): pass

    # cmd - shuffle
    def shuffle(self):

        self.__clone_songs()

        shuffled_arr: list[Song] = []

        index = self.__get_song_playing_index()

        if index >= 0:

            item = self.__songs.pop(index)

            shuffled_arr.append(item)


        shuffled_arr += arr_u.shuffle(self.__songs)

        self.__songs = shuffled_arr

        self.__song_playing = self.__songs[0].get_id()

    # cmd - normalize
    def normalize(self):
        self.__clone_songs()


TP = _temp_playlist()