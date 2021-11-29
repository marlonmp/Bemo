from discord.voice_client import VoiceClient as Conn
from discord.ext.commands.context import Context
from discord import VoiceChannel, utils, FFmpegPCMAudio
from discord.ext import commands

from youtube_dl import YoutubeDL

client = commands.Bot(command_prefix='!')

def get(url: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': 'True',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }
        ]
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return (info, info['formats'][0]['url'])

@client.command()
async def play(ctx: Context, url: str):

    voice = utils.get(client.voice_clients, guild=ctx.guild)
    voiceChan: VoiceChannel = utils.get(ctx.guild.voice_channels, name='General')

    conn: Conn = await voiceChan.connect()

    FFMPEG_OPTS = { 'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn' }

    video, source = get(url)
    conn.play(FFmpegPCMAudio(source, **FFMPEG_OPTS), after=lambda e: print('done', e))
    conn.is_playing()

client.run('')