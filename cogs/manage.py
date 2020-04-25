import os
import random
import discord
import datetime as dt
from discord.ext import commands

##########################
# Manage Commands
##########################
class Manage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('... Added Manage Cog ...')
    
    @commands.command()
    async def logout(self, ctx):
        await ctx.send("Powering off")
        await self.bot.logout()

def setup(bot):
    bot.add_cog(Manage(bot))
    