from discord import Game
from discord.ext import commands
from discord import Client
from discord.ext import tasks
from discord.utils import get
from discord import Embed
import sqlite3
from config import botkey
from cogs.reaction import reaction_func

bot = commands.Bot(command_prefix='-', help_command=None)
initial_extensions = [
    'cogs.music',
    'cogs.chat',
    'cogs.logs',
]

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}')
    await bot.change_presence(activity=Game(name='s-help'))
    print(f'Bot is ready!')


@bot.event
async def on_raw_reaction_add(ctx):
    await reaction_func


bot.run(config.BOTKEY)
