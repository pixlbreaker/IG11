import discord
import pafy
import youtube_dl
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
    
    def __playaudio__(self, ctx, audio_path):
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio(audio_path)

        #self.songs.append(audio_source)
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
        else:
            voice_client.pause()
            voice_client.play(audio_source, after=None)
    
    def __join__(self, ctx):
        """Joins the users channel"""
        try:
            channel = ctx.message.author.voice.channel
            voice = get(self.bot.voice_clients, guild=ctx.guild)
            if voice and voice.is_connected():
                voice.move_to(channel)
                ctx.send("Moved channel")
            else:
                voice = channel.connect()
                ctx.send("Joined channel")
        except:
            ctx.send("You are not connected to a channel")

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
        self.__join__(ctx)
        self.__playaudio__(ctx, audio_path)
        
    
    # @commands.command(pass_context=True)
    # async def join(self, ctx):
    #     """Joins the users channel"""
    #     try:
    #         channel = ctx.message.author.voice.channel
    #         voice = get(self.bot.voice_clients, guild=ctx.guild)
    #         if voice and voice.is_connected():
    #             await voice.move_to(channel)
    #             await ctx.send("Moved channel")
    #         else:
    #             voice = await channel.connect()
    #             await ctx.send("Joined channel")
    #     except:
    #         await ctx.send("You are not connected to a channel")
    
        


def setup(bot):
    bot.add_cog(Soundboard(bot))