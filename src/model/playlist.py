from src.lib import time_format

def _set_duration(playlist: dict):

    playlist['duration'] = 0

    for song in playlist['songs']:
        playlist['duration'] += song['duration']

    playlist['duration'] = time_format.format(playlist['duration'])


def _format_author(playlist: dict):

    playlist['author'] = '<@' + playlist['author'] + '>'


def _set_songs_quantity(playlist: dict):

    playlist['songs_quantity'] = len(playlist['songs'])


def set_format(playlist: dict):

    _set_duration(playlist)

    _format_author(playlist)

    _set_songs_quantity(playlist)


def build():
    pass