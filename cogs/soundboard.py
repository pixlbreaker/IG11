import discord
import pafy
import youtube_dl
import os
from urllib.request import Request, urlopen
from discord.ext import tasks, commands
from discord import FFmpegPCMAudio
from discord.utils import get

############################
#   Soundboard Cog
############################

class Soundboard(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        #self.play_queue.start()
    
    async def __playaudio__(self, ctx, audio_path):
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio(audio_path)

        await ctx.send("Playing audio")
        voice_client.play(audio_source, after=None)
    

    @commands.Cog.listener()
    async def on_ready(self):
        print('... Added Soundboard Cog...')

    @tasks.loop(seconds=5.0)
    async def play_queue(self):
        # Checks if the bot is playing music
        voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients)
        # if len(self.songs) > 0 and not voice_client.is_playing():

        #     # Plays the audio in the channel
        #     audio_info = self.songs.pop()
        #     self.__playsong__(audio_info[0], audio_info[1])
    
    @commands.command(pass_context=True)
    async def bitconnect(self, ctx):
        """
        Plays the bitconnect sound
        """
        await ctx.send("Bitconnect")
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        audio_path = "sound/bitconnect.mp3"
        await self.__playaudio__(ctx, audio_path)

    @commands.command(pass_context=True)
    async def p(self, ctx, name):
        """
        """
        l = os.listdir('./sound')
        li=[x.split('.')[0] for x in l]
        i = li.index(name)
        audio_path = "sound/" + l[i]
        await self.__playaudio__(ctx, audio_path)
        

    
    @commands.command(pass_context=True,)
    async def soundlist(self, ctx):
        """
        """
        await ctx.send("This is a list of all the avaiable sounds:")
        for filename in os.listdir('./sound'):
            await ctx.send(filename)
        
    
    @commands.command(pass_context=True)
    async def addsound(self, ctx):
        """
        """
        file_name = ctx.message.attachments[0].filename
        file_type = file_name.split(".")[-1]
        
        if file_type == "mp3" or file_type == "wav" or file_type == "ogg":
            # File information and writes it to the file
            file_loc = ctx.message.attachments[0].url
            req = Request(file_loc, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            file_write = open("sound\\" + file_name, "wb")
            file_write.write(webpage)
            file_write.close()

            name = file_name.split(".")[0]
            await ctx.send(name + " has been added")
        else:
            await ctx.send("You have not given the right file type.")


def setup(bot):
    bot.add_cog(Soundboard(bot))