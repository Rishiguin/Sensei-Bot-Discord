from discord import Game
from discord.ext import commands
from discord import Client

bot = commands.Bot(command_prefix='+')
initial_extensions = [
    'cogs.music',
    'cogs.chat',
    'cogs.logs',
]

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event #h
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}')
    await bot.change_presence(activity=Game(name='+info'))
    print(f'Bot is ready!')


bot.run('NzMyMzQyODE5NTEwODEyNzEz.Xw1TFw.EuCDtfSgWM9MJBJFdZr4dEqc3MI', bot=True, reconnect=True)
