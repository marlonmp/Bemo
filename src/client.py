from discord.ext.commands.context import Context as Ctx
from discord import Intents, Member, Message
from discord.member import VoiceState
from discord.ext import commands


from src.lib.vc_manager import VC
from src.lib.temp_pl import TP
from src.lib.cache import DB

from dotenv import load_dotenv

import os

## constants

load_dotenv()

_GUILD_ID = int(os.environ.get('GUILD_ID'))
_CHAN_ID = int(os.environ.get('CHAN_ID'))

### ------ client ------

class Client(commands.Bot):

## constructor

    def __init__(self):

        super().__init__(command_prefix='!', description='None !!Desc', intents=Intents.all())

##

    def load_cogs(self):

        """This function load all cogs from ./src/cogs"""

        for filename in os.listdir('./src/cogs'):
            if '_cog.py' in filename:
                self.load_extension(f'src.cogs.{filename[:-3]}')

## Events

    async def on_ready(self):

        # self.load_cogs()

        self.__set_commands()

        print(f'[EVENT] Bot ready as {self.user.name}')


    async def on_message(self, message: Message):
        
        guild = self.get_guild(_GUILD_ID)
        chan = self.get_channel(_CHAN_ID)

        is_valid_guild = (guild.id == message.guild.id) or (_GUILD_ID == 0)
        is_valid_chan = (chan.id == message.channel.id) or (_CHAN_ID == 0)

        if is_valid_guild and is_valid_chan:
            await self.process_commands(message)


    async def on_command_error(self, ctx: Ctx, _): pass


    async def on_voice_state_update(self, member: Member, before: VoiceState, after: VoiceState):

        await VC.vs_member_event(member, before, after)

## Commands

    def __set_commands(self):

## voice client commands

        @self.command()
        async def join(ctx: Ctx):

           res = await VC.join(ctx.author)

           if res:
               await ctx.reply(res)


        @self.command()
        async def link(ctx: Ctx):

            res = await VC.link(ctx.author)

            if res:
               await ctx.reply(res)
                    

        @self.command()
        async def unlink(ctx: Ctx):

            res = await VC.unlink(ctx.author)

            if res:
               await ctx.reply(res)


        @self.command()
        async def leave(ctx: Ctx):

            res = await VC.leave(ctx.author)

            if res:
               await ctx.reply(res)

## DB commands

        @self.command()
        async def show(ctx: Ctx):
            
            embeds = DB.show_pl()

            for embed in embeds:

                await ctx.send(embed=embed)


        @self.command()
        async def list(ctx: Ctx, *, prefix: str = ''):
            
            if prefix:

                embeds = DB.list_songs(prefix)

                for embed in embeds:
                    await ctx.send(embed=embed)


        @self.command()
        async def new(ctx: Ctx, title: str):

            res = DB.new_pl(title, ctx.author.id)

            if res:
                await ctx.reply(res)


        @self.command()
        async def update(ctx: Ctx, prefix: str, new_title: str):
            res = DB.update_title(prefix, new_title)

            if res:
                await ctx.reply(res)


        @self.command()
        async def delete(ctx: Ctx, pl_id: int):
            res = DB.delete_pl(pl_id)

            if res:
                await ctx.reply(res)


        @self.command()
        async def add(ctx: Ctx, prefix: str, url: str):
            res = DB.add_song(prefix, url)

            if res:
                await ctx.reply(res)


        @self.command()
        async def remove(ctx: Ctx, prefix: str, song_id: int):
            res = DB.remove_song(prefix, song_id)

            if res:
                await ctx.reply(res)
        

        @self.command()
        async def save(ctx: Ctx):

            DB.save()

            await ctx.reply('Db is saved')

## playing commands

        @self.command()
        async def start(ctx: Ctx, pl_id: int, song_id: int = 0):
            res = TP.start(pl_id, song_id)

            if res:
                await ctx.reply(res)


        @self.command()
        async def play(ctx: Ctx, song_id: int):
            res = TP.play(song_id)

            if res:
                await ctx.reply(res)


        @self.command()
        async def replay(ctx: Ctx):
            res = TP.replay()

            if res:
                await ctx.reply(res)


        @self.command()
        async def previus(ctx: Ctx):
            res = TP.previus()

            if res:
                await ctx.reply(res)


        @self.command()
        async def pause(ctx: Ctx, song_id: int = 0):
            res = TP.pause()

            if res:
                await ctx.reply(res)


        @self.command()
        async def resume(ctx: Ctx):
            res = TP.resume()

            if res:
                await ctx.reply(res)


        @self.command()
        async def next(ctx: Ctx):
            res = TP.next()

            if res:
                await ctx.reply(res)


        # @self.command()
        async def loop(ctx: Ctx):
            res = TP.loop()

            if res:
                await ctx.reply(res)


        @self.command()
        async def shuffle(ctx: Ctx):
            res = TP.shuffle()

            if res:
                await ctx.reply(res)


        @self.command()
        async def normalize(ctx: Ctx):
            res = TP.normalize()

            if res:
                await ctx.reply(res)

