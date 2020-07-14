from discord import Embed
from discord.ext import commands

import json
from requests import get

genres=[
  'rock',
  'hiphop',
  'classicalindian',
  'classical',
  'r&b',
  'heavymetal',
  'jazz',
  'edm',
  'rap',
  'funk',
  'lofi',
  'gaming',
  'C418',
  'kpop',
  'bollywood',
  'random',
  'sleep'
]
moods=[
    'happy',
    'alone',
    'comfort',
    'sad',
    'badass'
]
class chat(commands.Cog):
    
    def __init__(self, bot): 
        self.bot = bot
    
    @commands.command(brief='!info')
    async def info(self, ctx):
        k=0
        embed = Embed(color=0x9240FF, title='List of commands : ')
#        for cog in self.bot.cogs:
#            if self.bot.get_cog(cog).get_commands():
#                temp = []
#                for cmd in self.bot.get_cog(cog).get_commands():
#                    if not cmd.hidden:
#                        temp.append(f"{cmd.brief}\n")
#                if temp:
#                    embed.add_field(name=f'**{cog} :**', value=f"{'-> '.join(temp)}", inline=False)
        embed.add_field(name='`!songplay or !sp [genre/mood]`',value='play a song recommended by music sensei',inline=False)
        embed.add_field(name='`!song or !s [genre/mood]`',value='get a song recommended by music sensei along with the spotify link',inline=False)
        embed.add_field(name='`!genres`',value='get a list of genres that Music Sensei supports',inline=False)
        embed.add_field(name='`!moods`',value='get a list of moods that Music Sensei supports',inline=False)
        embed.add_field(name='`!play [youtube url/song name]`',value='play any song of your choice',inline=False)
        embed.add_field(name='`!pause`',value='pause the music',inline=False)
        embed.add_field(name='`!skip`',value='skip the current currently plating song',inline=False)
        embed.add_field(name='`!remove [index in queue]`',value='remove a song from queue',inline=False)
        await ctx.message.delete()
        await ctx.send(embed=embed)


    @commands.command(brief='!genres')
    async def genres(self, ctx):
        embed = Embed(color=0x9240FF, title='List of genres : ')
        m=[]
        for i in range(0,len(genres)):
          embed.add_field(name='`{}`'.format(genres[i]),value='-',inline=True)
        embed.set_footer(text='more to added soon...')
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(brief='!moods')
    async def moods(self,ctx):
        embed = Embed(color=0x9240FF, title='List of moods : ')
        for i in moods:
          embed.add_field(name='`{}`'.format(i),value='-',inline=True)
        embed.set_footer(text='more to added soon...')
        await ctx.message.delete()
        await ctx.send(embed=embed)

#    @commands.command(brief='!poll [question] [answers]')
#    async def poll(self, ctx, *items):
#        question = items[0]
#        answers = '\n'.join(items[1:])
#        embed = Embed(title='Nouveaux sondage :', description=f":grey_question: __{question}__", color=0x3498db)
#        embed.set_footer(text=f'Asked by {ctx.author}')
#        for i in range(1, len(items)):
#            embed.add_field(name=f"Option n°{i}", value=items[i], inline=False)
#        await ctx.message.delete()
#        message = await ctx.channel.send(embed=embed)
#        reactions = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
#
#        for i in range(len(items[1:])):
#            await message.add_reaction(reactions[i])

#    @commands.command(brief='!meme')
#    async def meme(self, ctx):
#        data = get('https://meme-api.herokuapp.com/gimme').json()
#        embed = (Embed(title=f":speech_balloon: r/{data['subreddit']} :", color=0x9240FF)
#                .set_image(url=data['url'])
#                .set_footer(text=data['postLink']))
#        await ctx.send(embed=embed)

#    @commands.command(brief='twitch [game] [key-words (optional)]')
#    async def twitch(self, ctx, game, *keys, streams=[]):
#        headers = {
#            'Client-ID': "j3abopdoj1fi9hshxtli9jlnkyruof",
#            'Authorization':  "skwhgj2gzbf6aeae84hedfzb1b2hyp"
#        }
#        topgames = get(f"https://api.twitch.tv/helix/games/top?first=100", headers=headers).json()
#        for category in topgames['data']:
#            if game.lower() in category['name'].lower():
#                embed = Embed(title=f":desktop: Streams ({category['name']}):", color=0x3498db)
#                stream_nb = 100 if keys else 20
#                response = get(f"https://api.twitch.tv/helix/streams?game_id={category['id']}&first={stream_nb}", headers=headers).json()
#                for stream in response['data']:
#                    if keys:
#                        for key in keys:
#                            if key.lower() in stream['title'].lower() and not stream in streams:
#                                streams.append(stream)
#                                embed.add_field(name=f"{stream['user_name']}", value=f"[{stream['title']}](https://twitch.tv/{stream['user_name']})")
#                    else:
#                        embed.add_field(name=f"{stream['user_name']}", value=f"[{stream['title']}](https://twitch.tv/{stream['user_name']})")
#                await ctx.send(embed=embed)
#                return
#        embed = Embed(title=f"❌ Something went wrong:", description="No matching streams found", color=0xe74c3c)
#        await ctx.send(embed=embed) 


def setup(bot):
    bot.add_cog(chat(bot))
