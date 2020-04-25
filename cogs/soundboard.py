import discord
from discord.ext import commands

############################
#   Soundboard Cog
############################

class Soundboard(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('... Added Soundboard Cog...')
    
    @commands.command(pass_context=True)
    async def bitconnect(self, ctx):
        """
        Plays the bitconnect sound
        """
        await ctx.send("Bitconnect")
        
    
    @commands.command(pass_context=True)
    async def join(self, ctx):
        """Joins the users channel"""
        try:
            channel = ctx.message.author.voice.channel
            voice = get(self.bot.voice_clients, guild=ctx.guild)
            if voice and voice.is_connected():
                await voice.move_to(channel)
                await ctx.send("Moved channel")
            else:
                voice = await channel.connect()
                await ctx.send("Joined channel")
        except:
            await ctx.send("You are not connected to a channel")
        


def setup(bot):
    bot.add_cog(Soundboard(bot))