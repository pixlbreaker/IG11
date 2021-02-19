import discord
import os
import json

from discord.ext import commands

f = open("login.json")
data = json.load(f)
TOKEN = data['TOKEN']
cogs = ['cogs.manage', 'cogs.soundboard', 'cogs.music']

bot = commands.Bot(command_prefix="!")

# Load function for extensions
@bot.command
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

# Unloads function for extension
@bot.command
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.event
async def on_ready():
    for cog in cogs:
        bot.load_extension(cog)

# for filename in os.listdir('./cogs'):
#     if filename.endswith('.py'):
#         bot.load_extension(f'cogs.{filename[:-3]}')

# Run the bot
bot.run(TOKEN)