from discord import Embed
from discord.ext import commands
import requests
import json
from requests import get

genres=[
  'rock',
  'hiphop',
  'metal',
  'epic',
  'synthwave'
  '90s'
  'classical',
  'r&b',
  'heavymetal',
  'jazz',
  'edm',
  'rap',
  'funk',
  'lofi',
  'gaming',
  'focus',
  'kpop',
  'bollywood',
  'anime',
  'random',
  'sleep'
]
moods=[
    'happy',
    'alone',
    'comfort',
    'sad',
    'angry',
    'badass'
]
class chat(commands.Cog):
    
    def __init__(self, bot): 
        self.bot = bot
    
    @commands.command(brief='+info')
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
        embed.add_field(name='`+song or +s [genre/mood]`',value='get a song recommended by Music Sensei along with the Spotify link',inline=False)
        embed.add_field(name='`+songplay or +sp [genre/mood]`',value='play a song recommended by Music Sensei',inline=False)
        embed.add_field(name='`+listening [song/artist]`',value='Get a list of all the people in your server listening to that song/artist',inline=False)
        embed.add_field(name='`+listeningall or +la`',value='Get a list of all the members in your server currently listening to songs',inline=False)
        embed.add_field(name='`+genres`',value='get a list of genres that Music Sensei supports',inline=False)
        embed.add_field(name='`+moods`',value='get a list of moods that Music Sensei supports',inline=False)
        embed.add_field(name='`+play [youtube url/song name]`',value='play any song of your choice',inline=False)
        embed.add_field(name='`+pause`',value='pause the music',inline=False)
        embed.add_field(name='`+resume`',value='resume the music',inline=False)
        embed.add_field(name='`+skip`',value='skip the current currently playing song',inline=False)
        embed.add_field(name='`+remove [index in queue]`',value='remove a song from the queue',inline=False)
        embed.add_field(name='`+bye`',value='leaves voice channel',inline=False)
        embed.add_field(name='-',value=f"[invite me](https://discord.com/api/oauth2/authorize?client_id=732342819510812713&permissions=37223488&scope=bot)",inline=True)
        embed.add_field(name='-',value=f"[support server](https://discord.gg/EYQrwpy)",inline=True)
        await ctx.message.delete()
        await ctx.send(embed=embed)#hello


    @commands.command(brief='+genres')
    async def genres(self, ctx):
        embed = Embed(color=0x9240FF, title='Genres : ')
        m=''
        embed.add_field(name='`+songplay or +sp [genre]` :get a song played of the genre by music sensei',value='Example : +songplay heavymetal',inline=False)
        embed.add_field(name='`+song or +s [genre]` :get a song recommended of the genre by Music Sensei',value='Example : +song heavymetal',inline=True)
        for i in range(0,len(genres)):
          m=m+' `{}`, '.format(genres[i])
        embed.description=m
        embed.set_footer(text='more to be added soon...')
        await ctx.message.delete()
        await ctx.send(embed=embed,delete_after=45.0)

    @commands.command(brief='+moods')
    async def moods(self,ctx):
        embed = Embed(color=0x9240FF, title='Moods : ')
        embed.add_field(name='`+songplay or +sp [mood]` :get a song played of the mood by Music Sensei',value='Example : +songplay happy')
        embed.add_field(name='`+song or +s [mood]` :get a song recommended of the mood by Music Sensei',value='Example : +song happy')
        n=''
        for i in moods:
          n=n+' `{}`, '.format(i)
        embed.description=n
        embed.set_footer(text='more to added soon...')
        await ctx.message.delete()
        await ctx.send(embed=embed)
    @commands.command(brief='+urban [word] | (gives the meaning of the word from urban dictionary)')
    async def urban(self,ctx):
        word1 = ctx.message.content.replace('+urban','')
        word  =word1.strip().lower()

        embed = Embed(color=0xfcba03, title=f'{word.upper()}')

        url="https://mashape-community-urban-dictionary.p.rapidapi.com/define"

        querystring={"term":f"{word}"}
        
        headers = {
            'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
            'x-rapidapi-key': "4506e5dc85msh57cad0977206ed3p1e19e7jsn0f0af8f6be4e"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        
        embed.add_field(name='Definitions : ',value='_______________',inline=False)
        for i in range (0,2):
         try:
           d=data['list'][i]['definition'].replace('[','').replace(']','')
           print(d)
           embed.add_field(name=f'{i+1}.',value=d, inline=False)
         except Exception as e:
           print (e)
           continue

        embed.add_field(name='Examples : ',value='___________',inline=False)

        for i in range (0,2):
         try:
           d=data['list'][i]['example'].replace('[','').replace(']','')
           print(d)
           embed.add_field(name=f'{i+1}.',value=d, inline=False)
         except Exception as e:
           print (e)
           continue
        await ctx.send(embed=embed)

    @commands.command(brief='~ideapls')
    async def idea(self,ctx):
        embed = Embed(color=0xF5A623)  
        e2 = Embed(color=0xC52430)
        e2.set_author(name='Thinking',icon_url='https://media.giphy.com/media/xTkcEQACH24SMPxIQg/giphy.gif') 
        msg = await ctx.send(embed=e2)
        time.sleep(2)
        res=requests.get(url='http://itsthisforthat.com/api.php?text')
        adv=res.text
        embed.description='I have an idea. '+adv
        await msg.edit(embed=embed)

        
#    @commands.command(brief='+poll [question] [answers]')
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

#    @commands.command(brief='+meme')
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
