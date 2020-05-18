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
    
    async def __playaudio__(self, ctx, audio_path):

        # Gets the channel and the voice information
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        # Guild and voice client
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)

        # The audio source
        audio_source = discord.FFmpegPCMAudio(audio_path)

        # Plays the audio
        await ctx.send("Playing audio")
        voice_client.play(audio_source, after=None)
    

    @commands.Cog.listener()
    async def on_ready(self):
        print('... Added Soundboard Cog...')
    

    @commands.command(pass_context=True)
    async def p(self, ctx, name):
        """
        Lets you play a soundclip. Use '!p soundname' to play the sound in the audio chat.
        """
        try:
            # Finds the audio clip from the name
            l = os.listdir('./sound')
            li=[x.split('.')[0] for x in l]
            i = li.index(name)
            audio_path = "sound/" + l[i]
            await self.__playaudio__(ctx, audio_path)
        except:
            await ctx.send("The audio clip does not exist.")
        

    
    @commands.command(pass_context=True,)
    async def soundlist(self, ctx):
        """
        Gives a list of all the sound files for the soundboard
        """
        await ctx.send("This is a list of all the avaiable sounds:")
        await ctx.send("Please wait ... ")
        sounds = "```"
        for filename in os.listdir('./sound'):
            sounds = sounds + filename + "\n"
        sounds = sounds + "```"

        await ctx.send(sounds)
        
        
    
    @commands.command(pass_context=True)
    async def addsound(self, ctx):
        """
        Adds a new sound to the soundboard. Uses only .mp3, .wav, .ogg
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