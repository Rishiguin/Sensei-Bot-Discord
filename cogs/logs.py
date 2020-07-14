from discord import Embed
from discord.ext import commands

from datetime import datetime
from json import loads, dumps

class Logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guilds = {}

    @commands.Cog.listener()
    async def on_ready(self):
        with open('guilds.json', 'r') as file:
            data = file.read()
            self.guilds = loads(data)

    @commands.command(brief='!log', hidden=True)
    async def log(self, ctx):
        await ctx.message.delete()
        try:
            if self.guilds[str(ctx.guild.id)]:
                self.guilds[str(ctx.guild.id)] = False
                await ctx.send("Les logs sont désactivés", delete_after=5.0)
            else:
                self.guilds[str(ctx.guild.id)] = True
                await ctx.send("Les logs sont activés", delete_after=5.0)
        except:
            self.guilds[str(ctx.guild.id)] = True
            await ctx.send("Les logs sont activés", delete_after=5.0)
        with open('guilds.json', 'w') as file:
            print(self.guilds)
            file.write(dumps(self.guilds)) 

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            msg = f'You must input those arguments: {error.param.name}'
        elif isinstance(error, commands.CommandNotFound):
            msg = 'Command not found!'
        elif isinstance(error, commands.MissingPermissions):
            msg = "You're not allowed to use this command!"
        elif isinstance(error, commands.BotMissingPermissions):
            perms = ', '.join(error.missing_perms)
            msg = f'I need those permissions to execute this command: {perms}!'
        elif isinstance(error, commands.BadArgument):
            if 'int' in str(error):
                msg = 'You must input an integer!'
            elif 'Member' in str(error):
                msg = "Membre introuvable !"
        elif isinstance(error, commands.CommandInvokeError):
            if 'index' in str(error):
                msg = "Argument's too big!"
            elif 'NoneType' in str(error):
                msg = "I'm not connected to any channel!" if 'is_playing' in str(error) else "You're not connected to any channel!"
            elif ('ValueError' or 'KeyError') in str(error):
                msg = 'Some arguments are invalid!'
            elif 'Missing Permissions' in str(error):
                msg = "Je n'ai pas la permission de faire ça !"
            else:
                print(str(error))
                return
        else:
            print(str(error))
            return
 
        embed = Embed(title="❌ Something went wrong:", description=msg, color=0xe74c3c)
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=5.0)

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        for channel in ctx.guild.text_channels:
            try:
                if channel.name == "logs" and self.guilds[str(ctx.guild.id)]:
                    command = f"{ctx.author.mention}: !{ctx.command.name}{ctx.message.content[(len(ctx.command.name)+1):]}"
                    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    embed = Embed(title=':pager: Commande exécutée :', description=command, color=0x3498db)
                    embed.add_field(name='\u200b', value=now)
                    await channel.send(embed=embed)
            except:
                pass


def setup(bot):
    bot.add_cog(Logger(bot))
