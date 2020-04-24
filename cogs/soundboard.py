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


def setup(bot):
    bot.add_cog(Soundboard(bot))