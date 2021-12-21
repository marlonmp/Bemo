from typing import Union
from discord.voice_client import VoiceClient
from discord.channel import VoiceChannel
from discord.member import VoiceState
from discord import Member, User

from asyncio.locks import Lock

class __vc_manager:

    linked_user_id: int
    voice_client:   VoiceClient

    __blocker: Lock

## constructor

    def __init__(self):

        self.linked_user_id = 0
        self.voice_client: VoiceClient = None

        self.__blocker = Lock()

## voice client actions

    async def set_conn(self, voice_chan: VoiceChannel):

        await self.__blocker.acquire()

        if self.voice_client != None:

             if self.voice_client.channel.id != voice_chan.id:

                is_playing = self.voice_client.is_playing()

                await self.voice_client.move_to(voice_chan)

                if is_playing:
                    self.voice_client.resume()

        else:
            self.voice_client = await voice_chan.connect()
        
        self.__blocker.release()
    

    async def disconnect(self):

        await self.__blocker.acquire()

        await self.voice_client.disconnect()

        self.voice_client = None

        self.__blocker.release()
    
## voice state event

    async def vs_member_event(self, member: Member, before: VoiceState, after: VoiceState):

        if member.id == self.linked_user_id:

            # member join
            if (before.channel == None) and (after.channel != None):

                await self.set_conn(after.channel)

            # member leave
            elif (after.channel == None) and (before.channel != None):

                await self.disconnect()

            # member move
            else:

                await self.set_conn(after.channel)

## msg

    def __linked_user_msg(self):
        return 'I\'m linked with <@' + self.linked_user_id + '>'


    def __require_chan_msg(self):
        return 'You need to be on a voice channel 7-7'


    def __arleady_linked_msg(self):
        return 'You are already linked'


    def __no_linked_msg(self):
        return 'I\'m not linked with someone'
    

    def __not_on_a_chan_msg(self):
        return 'I\'m not on a voice channel'

## bot actions in channel

    # cmd - join
    async def join(self, author: Union[User, Member]) -> str:

        if self.linked_user_id and (self.linked_user_id != author.id):

            return self.__linked_user_msg()
        
        if author.voice:

            voice_chan: VoiceChannel = author.voice.channel

            await self.set_conn(voice_chan)

        else:
            return self.__require_chan_msg()
        
        return 'joined'

    # cmd - link
    async def link(self, author: Union[User, Member]) -> str:

        if self.linked_user_id:

            if self.linked_user_id == author.id:
                return self.__arleady_linked_msg()
            
            else:
                return self.__linked_user_msg()
        
        else:

            await self.__blocker.acquire()

            self.linked_user_id = author.id

            self.__blocker.release()

            if author.voice != None:

                voice_chan: VoiceChannel = author.voice.channel

                await self.set_conn(voice_chan)

        return 'linked'
                
    # cmd - unlink
    async def unlink(self, author: Union[User, Member]):

        if self.linked_user_id:

            if self.linked_user_id == author.id:
                await self.__blocker.acquire()

                self.linked_user_id = 0

                self.__blocker.release()
            
            else:
                return self.__linked_user_msg()

        else:
            return self.__no_linked_msg()
        
        return 'unlinked'

    #cmd - leave
    async def leave(self, author: Union[User, Member]):

        if self.voice_client:
            
            if self.linked_user_id:
                
                if self.linked_user_id != author.id:
                    return self.__linked_user_msg()

            if self.voice_client.is_connected():

                await self.disconnect()

                return 'I\'m leave'
        
        return self.__not_on_a_chan_msg()


VC = __vc_manager()