from discord import Embed, FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get
import random
from youtube_dl import YoutubeDL
from asyncio import run_coroutine_threadsafe
import requests
import discord
import spotipy
import spotipy.util as util
import sys
from spotipy.oauth2 import SpotifyClientCredentials

clm=SpotifyClientCredentials(client_id='8fc65af3d87a44f7b9cd241c4e967e13',client_secret='8015fab9a7384427b4eefa5886403ebf')
sp=spotipy.Spotify(client_credentials_manager=clm)

items={
  'rock':['37i9dQZF1DWXRqgorJj26U'],
  'hiphop':['1tIioq32KjWlt5vvk5rhqX'],
  'classicalindian':['5tX4GrnMulZfRUN49zxkW1'],
  'classical':['37i9dQZF1DWV0gynK7G6pD'],
  'r&b':['37i9dQZF1DX2UgsUIg75Vg','37i9dQZF1DX7yRWDZJQ3Yz','37i9dQZF1DWYmmr74INQlb'],
  'heavymetal':['37i9dQZF1DX9qNs32fujYe'],
  'jazz':['37i9dQZF1DXbITWG1ZJKYt'],
  'edm':['3Di88mvYplBtkDBIzGLiiM','5Y9eVQ3u5rBAfL61OmsvDZ'],
  'rap':['1k2kVgwVqQknegkmpXEA17','37i9dQZF1DX0XUsuxWHRQd'],
  'funk':['4nmgmuVJSMDit2bpRNVDO2'],
  'lofi':['37i9dQZF1DWWQRwui0ExPn'],
  'gaming':['37i9dQZF1DWTyiBJ6yEqeu'],
  'C418':['37i9dQZF1DZ06evO2DcVFr','37i9dQZF1E4keRh2SuErl0'],
  'kpop':['37i9dQZF1DWTY99d0AYptp','37i9dQZF1DX2cVoXMHpaD1'],
  'bollywood':['37i9dQZF1DXd8cOUiye1o2','37i9dQZF1DX0XUfTFmNBRM'],
  'random':['1PIhV6X7PV4TjAQb7unitN','37i9dQZEVXbLiRSasKsNU9'],
  'sleep':['37i9dQZF1DWZd79rJ6a7lp'],

  'happy':['37i9dQZF1DX3rxVfibe1L0','37i9dQZF1DX9XIFQuFvzM4'],
  'alone':['37i9dQZF1DWX83CujKHHOn','37i9dQZF1DX2pSTOxoPbx9'],
  'comfort':['37i9dQZF1DWSRc3WJklgBs'],
  'sad':['37i9dQZF1DWVrtsSlLKzro','37i9dQZF1DX3YSRoSdA634'],
  'badass':['37i9dQZF1DX1tyCD9QhIWF']

}


class Music(commands.Cog, name='Music'):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    def __init__(self, bot):
        self.bot = bot
        self.song_queue = {}
        self.message = {}

    @staticmethod
    def parse_duration(duration):
        result = []
        m, s = divmod(duration, 60)
        h, m = divmod(m, 60)
        return f'{h:d}:{m:02d}:{s:02d}'

    @staticmethod
    def search(author, arg):
        with YoutubeDL(Music.YDL_OPTIONS) as ydl:
            try: requests.get(arg)
            except: info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
            else: info = ydl.extract_info(arg, download=False)

        embed = (Embed(title='🎵 Now playing :', description=f"[{info['title']}]({info['webpage_url']})", color=0x9240FF)
                .add_field(name='Duration', value=Music.parse_duration(info['duration']))
                .add_field(name='Requested by', value=author)
                .add_field(name='Uploader', value=f"[{info['uploader']}]({info['channel_url']})")
                .add_field(name="Queue", value=f"No song queued")
                .set_thumbnail(url=info['thumbnail']))

        return {'embed': embed, 'source': info['formats'][0]['url'], 'title': info['title']}

    async def edit_message(self, ctx):
        embed = self.song_queue[ctx.guild][0]['embed']
        content = "\n".join([f"({self.song_queue[ctx.guild].index(i)}) {i['title']}" for i in self.song_queue[ctx.guild][1:]]) if len(self.song_queue[ctx.guild]) > 1 else "No song queued"
        embed.set_field_at(index=3, name="Queue :", value=content, inline=False)
        await self.message[ctx.guild].edit(embed=embed)

    def play_next(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if len(self.song_queue[ctx.guild]) > 1:
            del self.song_queue[ctx.guild][0]
            run_coroutine_threadsafe(self.edit_message(ctx), self.bot.loop)
            voice.play(FFmpegPCMAudio(self.song_queue[ctx.guild][0]['source'], **Music.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
            emb=discord.Embed()
            voice.is_playing()
        else:
            run_coroutine_threadsafe(voice.disconnect(), self.bot.loop)
            run_coroutine_threadsafe(self.message[ctx.guild].delete(), self.bot.loop)


    @commands.command(aliases=['sp'], brief='!songplay [genre]')
    async def songplay(self, ctx, *, ge: str):
        channel = ctx.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        print(ctx.author.mention)
        list_of_songs=[]
        if ge in items:
          
             pli=items[ge]
             print(pli)
             inde=random.randint(0,len(pli)-1)
             print(inde)
             play_id=pli[inde]
             print(play_id)
             t=sp.playlist_tracks(playlist_id='{}'.format(play_id),limit=70)
             for item in t['items']:
                 urls=item['track']['external_urls']
                 track = item['track']
                 print(track['name'] + ' - ' + track['artists'][0]['name']+' - '+urls['spotify'])
                
                 songname=track['name']
                 artist=track['artists'][0]['name']
                 link=urls['spotify']
                  
                 ar=[['{}'.format(songname),'{}'.format(artist),'{}'.format(link)]]
                 print(ar)
                 list_of_songs.append(ar)
        
           
             print(list_of_songs)
             grp= list_of_songs[random.randint(0,len(list_of_songs)-1)]
             print(grp)
             songname1=grp[0][0]
             artist1=grp[0][1]
             link1=grp[0][2]
             embed = discord.Embed(color=0x9240FF)
             embed.description = 'Adding this song to queue - '
             embed.add_field(name='Song : ',value=songname1,inline=True)
             embed.add_field(name='Artist : ',value=artist1,inline=True)
             embed.set_footer(text='New features coming soon...')
             await ctx.send('Checkout now playing section', delete_after=5.0)
             await ctx.channel.send(embed=embed,delete_after=6.0)
             song = Music.search(ctx.author.mention,(songname1+' '+artist1))
        else:
             await ctx.send('`Genre not found`',delete_after=5.0)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()     

        if not voice.is_playing():
            self.song_queue[ctx.guild] = [song]
            self.message[ctx.guild] = await ctx.send(embed=song['embed'])
            await ctx.message.delete()
            voice.play(FFmpegPCMAudio(song['source'], **Music.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
            voice.is_playing()
        else:
            self.song_queue[ctx.guild].append(song)
            await self.edit_message(ctx)
        await ctx.message.delete()
    @commands.command(aliases=['s'], brief='!song [genre] ( receive a recommendation from Music Sensei for a particular genre. Type !genre for list of genres available.)')
    async def song(self, ctx, *, ge: str):
        channel = ctx.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        print(ctx.author.mention)
        list_of_songs=[]
        if ge in items:
          
             pli=items[ge]
             print(pli)
             inde=random.randint(0,len(pli)-1)
             print(inde)
             play_id=pli[inde]
             print(play_id)
             t=sp.playlist_tracks(playlist_id='{}'.format(play_id),limit=70)
             for item in t['items']:
                 urls=item['track']['external_urls']
                 track = item['track']
                 print(track['name'] + ' - ' + track['artists'][0]['name']+' - '+urls['spotify'])
                
                 songname=track['name']
                 artist=track['artists'][0]['name']
                 link=urls['spotify']
                  
                 ar=[['{}'.format(songname),'{}'.format(artist),'{}'.format(link)]]
                 print(ar)
                 list_of_songs.append(ar)
           
             print(list_of_songs)
             grp= list_of_songs[random.randint(0,len(list_of_songs)-1)]
             print(grp)
             songname1=grp[0][0]
             artist1=grp[0][1]
             link1=grp[0][2]
             embed = discord.Embed(color=0x9240FF)
             embed.description = 'Check this song  out '
             embed.add_field(name='Song : ',value=songname1,inline=True)
             embed.add_field(name='Artist : ',value=artist1,inline=True)
             embed.add_field(name='Spotify link : ',value=link1,inline=True)
             embed.set_footer(text='New features coming soon...')
             await ctx.send(embed=embed)
             await ctx.message.delete()
             
    @commands.command(aliases=['p'], brief='!play [play any youtube url/songname]')
    async def play(self, ctx, *, video: str):
        channel = ctx.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        print(ctx.author.mention)
        print(video)
        song = Music.search(ctx.author.mention, video)
        await ctx.send('Added to queue checkout now playing section', delete_after=6.0)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()     
           
        if not voice.is_playing():
            self.song_queue[ctx.guild] = [song]
            self.message[ctx.guild] = await ctx.send(embed=song['embed'])
            await ctx.message.delete()
            
            voice.play(FFmpegPCMAudio(song['source'], **Music.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
            voice.is_playing()
        else:
            self.song_queue[ctx.guild].append(song)
            await self.edit_message(ctx)
        
    @commands.command(brief='!pause')
    async def pause(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await ctx.message.delete()
            if voice.is_playing():
                await ctx.send('⏸️ Music paused', delete_after=5.0)
                voice.pause()
            else:
                await ctx.send('⏯️ Music resumed', delete_after=5.0)
                voice.resume()

    @commands.command(aliases=['pass'], brief='!skip')
    async def skip(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            await ctx.message.delete()
            await ctx.send('⏭️ Music skipped', delete_after=5.0)
            voice.stop()

    @commands.command(brief='!remove')
    async def remove(self, ctx, *, num: int):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            del self.song_queue[ctx.guild][num]
            await ctx.message.delete()
            await self.edit_message(ctx)


def setup(bot):
    bot.add_cog(Music(bot))
