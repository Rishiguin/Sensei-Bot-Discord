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
import time
from discord import Spotify

import os
from gtts import gTTS
import pyttsx3

clm=SpotifyClientCredentials(client_id='8fc65af3d87a44f7b9cd241c4e967e13',client_secret='8015fab9a7384427b4eefa5886403ebf')
sp=spotipy.Spotify(client_credentials_manager=clm)

items={
  'rock':['37i9dQZF1DWXRqgorJj26U'],
  'hiphop':['1tIioq32KjWlt5vvk5rhqX'],
  'classical':['37i9dQZF1DWV0gynK7G6pD'],#info
  'epic':['3djwi67c1QC3MQlVlRMlc7'],
  'r&b':['37i9dQZF1DX2UgsUIg75Vg','37i9dQZF1DX7yRWDZJQ3Yz','37i9dQZF1DWYmmr74INQlb'],
  'synthwave':['5GBJpEiKMiFy3cBPKR2TaH','3gWAZPuNWpELIhKNbnpfwk'], 
  'heavymetal':['37i9dQZF1DX9qNs32fujYe'],
  'jazz':['37i9dQZF1DXbITWG1ZJKYt'],
  'edm':['3Di88mvYplBtkDBIzGLiiM','5Y9eVQ3u5rBAfL61OmsvDZ'],
  'rap':['1k2kVgwVqQknegkmpXEA17','37i9dQZF1DX0XUsuxWHRQd'],
  'metal':['37i9dQZF1DWTcqUzwhNmKv'],
  '90s':['37i9dQZF1DWXqpDKK4ed9O'],
  'funk':['4nmgmuVJSMDit2bpRNVDO2'],
  'lofi':['37i9dQZF1DWWQRwui0ExPn'],
  'gaming':['37i9dQZF1DWTyiBJ6yEqeu'],
  'kpop':['37i9dQZF1DWTY99d0AYptp','37i9dQZF1DX2cVoXMHpaD1'],
  'bollywood':['37i9dQZF1DXd8cOUiye1o2','37i9dQZF1DX0XUfTFmNBRM'],
  'random':['1PIhV6X7PV4TjAQb7unitN','37i9dQZEVXbLiRSasKsNU9'],
  'sleep':['37i9dQZF1DWZd79rJ6a7lp'],
  'focus':['37i9dQZF1DWZeKCadgRdKQ','37i9dQZF1DWXLeA8Omikj7'],
  'happy':['37i9dQZF1DX3rxVfibe1L0','37i9dQZF1DX9XIFQuFvzM4'],
  'alone':['37i9dQZF1DWX83CujKHHOn','37i9dQZF1DX2pSTOxoPbx9'],
  'comfort':['37i9dQZF1DWSRc3WJklgBs'],
  'sad':['37i9dQZF1DWVrtsSlLKzro','37i9dQZF1DX3YSRoSdA634'],
  'badass':['37i9dQZF1DX1tyCD9QhIWF'],
  'angry':['71Xpaq3Hbpxz6w9yDmIsaH'],
  'anime':['37i9dQZF1DX6XceWZP1znY','0Efxy2V32pxFXTRKcA6zpp']

}
gifs={
  'anime':['https://media.giphy.com/media/dSdSQmzlJopuqueF2i/giphy.gif','https://media.giphy.com/media/1fnu914Z79qQpVi2xZ/giphy.gif','https://media.giphy.com/media/1zgzISaYrnMAYRJJEr/giphy.gif','https://media.giphy.com/media/ORjDJ8ZRAEjPyPhUu2/giphy.gif','https://media.giphy.com/media/ZyFCksxxD9tmLYfGJo/giphy.gif'],
  'synthwave':['https://media.giphy.com/media/wKnqovL33x9in9ci6X/giphy.gif','https://media.giphy.com/media/hSpRpdP46ETIXXWajD/giphy.gif','https://media.giphy.com/media/h58dtf5vTpjulO4M5o/giphy.gif','https://media.giphy.com/media/RMwccgrk3FvU9G7su4/giphy.gif','https://media.giphy.com/media/vMSXa7KFGx49aeeXhe/giphy.gif','https://media.giphy.com/media/l0MYJAzu5RTVSGeiY/giphy.gif'],
  'lofi':['https://media.giphy.com/media/j5zqQSABpeHCU8EpO3/giphy.gif','https://media.giphy.com/media/ZyFCksxxD9tmLYfGJo/giphy.gif','https://media.giphy.com/media/1fnu914Z79qQpVi2xZ/giphy.gif','https://media.giphy.com/media/MU56lYT1Ov07fVTsnM/giphy.gif','https://media.giphy.com/media/c9IdCLK8TDv1e/giphy.gif','https://media.giphy.com/media/vMSXa7KFGx49aeeXhe/giphy.gif'],
  '90s':['https://media.giphy.com/media/OeEVCJ2UqMQNO/giphy.gif','https://media.giphy.com/media/l41m2P3MMhMcmGbYY/giphy.gif','https://media.giphy.com/media/vMSXa7KFGx49aeeXhe/giphy.gif','https://media.giphy.com/media/14iK5HgJO2hJfi/giphy.gif'],
  'rock':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/VnIoecjQ3caw8/giphy.gif','https://media.giphy.com/media/xThtayqRC9fCEZ9P6U/giphy.gif'],
  'hiphop':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/14iK5HgJO2hJfi/giphy.gif','https://media.giphy.com/media/J5qQHCpkBiMXsoxDdA/giphy.gif'],
  'classical':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/26tn9547icxKKsAko/giphy.gif','https://media.giphy.com/media/J5qQHCpkBiMXsoxDdA/giphy.gif'],
  'epic':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/26tn9547icxKKsAko/giphy.gif'],
  'r&b':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/MU56lYT1Ov07fVTsnM/giphy.gif','https://media.giphy.com/media/14iK5HgJO2hJfi/giphy.gif','https://media.giphy.com/media/VnIoecjQ3caw8/giphy.gif'],
  'heavymetal':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/xThtayqRC9fCEZ9P6U/giphy.gif','https://media.giphy.com/media/26tn9547icxKKsAko/giphy.gif'],
  'jazz':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/26tn9547icxKKsAko/giphy.gif'],
  'edm':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/xThtayqRC9fCEZ9P6U/giphy.gif','https://media.giphy.com/media/VnIoecjQ3caw8/giphy.gif'],
  'rap':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/xThtayqRC9fCEZ9P6U/giphy.gif','https://media.giphy.com/media/26tn9547icxKKsAko/giphy.gif'],
  'metal':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/xThtayqRC9fCEZ9P6U/giphy.gif','https://media.giphy.com/media/26tn9547icxKKsAko/giphy.gif'],
  'funk':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/VnIoecjQ3caw8/giphy.gif'],
  'gaming':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/ORjDJ8ZRAEjPyPhUu2/giphy.gif','https://media.giphy.com/media/l0MYJAzu5RTVSGeiY/giphy.gif'],
  'kpop':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/26tn9547icxKKsAko/giphy.gif'],
  'bollywood':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/26tn9547icxKKsAko/giphy.gif','https://media.giphy.com/media/WtgwBP21Gujtu/giphy.gif'],
  'random':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/26tn9547icxKKsAko/giphy.gif','https://media.giphy.com/media/WtgwBP21Gujtu/giphy.gif'],
  'sleep':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/26tn9547icxKKsAko/giphy.gif','https://media.giphy.com/media/3o6ZsWqOrPRbtQoHG8/giphy.gif'],
  'focus':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/VnIoecjQ3caw8/giphy.gif','https://media.giphy.com/media/3o6ZsWqOrPRbtQoHG8/giphy.gif','https://media.giphy.com/media/l0MYQUIaqh223Ij8Q/giphy.gif'],
  'happy':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/VnIoecjQ3caw8/giphy.gif','https://media.giphy.com/media/RMwccgrk3FvU9G7su4/giphy.gif','https://media.giphy.com/media/l0MYQUIaqh223Ij8Q/giphy.gif'],
  'alone':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/ORjDJ8ZRAEjPyPhUu2/giphy.gif','https://media.giphy.com/media/3o6ZsWqOrPRbtQoHG8/giphy.gif'],
  'comfort':['https://media.giphy.com/media/3gTmgzy7wYJfyaGRHQ/giphy.gif','https://media.giphy.com/media/d2NfTnGMMBT8ORweXA/giphy.gif','https://media.giphy.com/media/ORjDJ8ZRAEjPyPhUu2/giphy.gif'],
  'sad':['https://media.giphy.com/media/d2NfTnGMMBT8ORweXA/giphy.gif','https://media.giphy.com/media/UUHUfrG6NsXzG/source.gif','https://media.giphy.com/media/ORjDJ8ZRAEjPyPhUu2/giphy.gif'],
  'badass':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/RMwccgrk3FvU9G7su4/giphy.gif','https://media.giphy.com/media/26tn9547icxKKsAko/giphy.gif','https://media.giphy.com/media/WtgwBP21Gujtu/giphy.gif'],
  'angry':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://media.giphy.com/media/RMwccgrk3FvU9G7su4/giphy.gif','https://media.giphy.com/media/26tn9547icxKKsAko/giphy.gif','https://media.giphy.com/media/WtgwBP21Gujtu/giphy.gif'],
  'allr':['https://media.giphy.com/media/l44QvKoQuUD3xPZKg/giphy.gif','https://tenor.com/9Tma.gif','https://media.giphy.com/media/xThtayqRC9fCEZ9P6U/giphy.gif','https://media.giphy.com/media/3o6ZsWqOrPRbtQoHG8/giphy.gif','https://media.giphy.com/media/WtgwBP21Gujtu/giphy.gif','https://media.giphy.com/media/3o7WILxziMaugB5Va8/giphy.gif','https://media.giphy.com/media/ei4OKs5ft9bmfkKSAk/giphy.gif','https://media.giphy.com/media/RMwccgrk3FvU9G7su4/giphy.gif','https://media.giphy.com/media/l0MYQUIaqh223Ij8Q/giphy.gif']
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
    def search(author, arg,x):
        with YoutubeDL(Music.YDL_OPTIONS) as ydl:
            try: requests.get(arg)
            except: info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
            else: info = ydl.extract_info(arg, download=False)
        try:
         embed = (Embed(title='🎵 Now playing :', description=f"[{info['title']}]({info['webpage_url']})", color=0x9240FF)
                    .add_field(name='Duration', value=Music.parse_duration(info['duration']))
                    .add_field(name='Requested by', value=author)
                    .add_field(name='Uploader', value=f"[{info['uploader']}]({info['channel_url']})")
                    .add_field(name="Queue", value=f"No song queued",inline=False)
                    .add_field(name='-',value=f"[invite me](https://discord.com/api/oauth2/authorize?client_id=732342819510812713&permissions=37223488&scope=bot)",inline=False)
                    .set_image(url=f'{x}')
                    .set_thumbnail(url=info['thumbnail'])
                    .set_footer(text=' this is the default music viewer for each music session.',icon_url='https://i.imgur.com/rFvaZrr.png'))
         return {'embed': embed, 'source': info['formats'][0]['url'], 'title': info['title']}
        except Exception as e:
            print(e)

    async def edit_message(self, ctx):
        try:
         embed = self.song_queue[ctx.guild][0]['embed']
         content = "\n".join([f"({self.song_queue[ctx.guild].index(i)}) {i['title']}" for i in self.song_queue[ctx.guild][1:]]) if len(self.song_queue[ctx.guild]) > 1 else "No song queued"
         embed.set_field_at(index=3, name="Queue :", value=content, inline=False)
         await self.message[ctx.guild].edit(embed=embed)
        except Exception as e:
            print(e)
            
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


    @commands.command(aliases=['sp'], brief='s-songplay [genre/mood] play a song recommended by Sensei of the mood/genre')
    async def songplay(self, ctx, *, ge: str):
        ur=''
        channel = ctx.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        print(ctx.author.mention)
        list_of_songs=[]
        if ge in gifs:
            gli=gifs[ge]
            ur=gli[random.randint(0,len(gli)-1)]
            print(ur)
        else:
            gli='allr'
            ur=gli[random.randint(0,len(gli)-1)]
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
             embed.add_field(name='Artist : ',value=artist1,inline=False)
             embed.add_field(name='-',value=f"[invite me](https://discord.com/api/oauth2/authorize?client_id=732342819510812713&permissions=37223488&scope=bot)",inline=True)
             embed.add_field(name='-',value=f"[support server](https://discord.gg/EYQrwpy)",inline=True)
             embed.set_footer(text='New features coming soon...')
             await ctx.send('Checkout now playing section', delete_after=5.0)
             await ctx.channel.send(embed=embed,delete_after=6.0)
             song = Music.search(ctx.author.mention,(songname1+' '+artist1),ur)
        else:
             await ctx.send('`❌ Genre/Mood not found, type s-genres or s-moods for list of genres/moods`',delete_after=6.0)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()     
        print(song)
        if not voice.is_playing():
            self.song_queue[ctx.guild] = [song]
            self.message[ctx.guild] = await ctx.send(embed=song['embed'])
            try:
             await ctx.message.delete()
            except:
              pass


            voice.play(FFmpegPCMAudio(song['source'], **Music.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
            voice.is_playing()
        else:
            self.song_queue[ctx.guild].append(song)
            await self.edit_message(ctx)
        try:
             await ctx.message.delete()
        except:
               pass
   
    @commands.command(aliases=['s'], brief='s-song [genre/mood] : receive a recommendation from Music Sensei for a particular genre. Type s-genre or s-mood for list of genres/moods available.')
    async def song(self, ctx, *, ge: str):
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
             embed = discord.Embed(color=0x4400ff)
             embed.description = 'Check this song  out {}'.format(ctx.author.mention)
             embed.add_field(name='Song : ',value=songname1,inline=True)
             embed.add_field(name='Artist : ',value=artist1,inline=True)
             embed.add_field(name='Spotify link : ',value=link1,inline=False)
             embed.add_field(name='-',value=f"[invite me](https://discord.com/api/oauth2/authorize?client_id=732342819510812713&permissions=37223488&scope=bot)",inline=True)
             embed.add_field(name='-',value=f"[support server](https://discord.gg/EYQrwpy)",inline=True)
             embed.set_footer(text='New features coming soon...')
             await ctx.send(embed=embed)
             try:
               await ctx.message.delete()
             except:
               pass
   

        else:
             await ctx.send('`❌ Genre/Mood not found, type s-genres or s-moods for list of genres/moods`',delete_after=6.0)
             
    @commands.command(aliases=['p'], brief='s-play [play any youtube url/songname] : play a songname/YT url')
    async def play(self, ctx, *, video: str):
        channel = ctx.author.voice.channel
        gli='allr'
        ur=gifs[gli][random.randint(0,len(gifs[gli])-1)]
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        print(ctx.author.mention)
        print(video)
        try :
         song = Music.search(ctx.author.mention, video,ur)
        except:
            song=Music.search(ctx.author.mention, video,ur)
        print(song)
        await ctx.send('Added to queue checkout now playing section', delete_after=6.0)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()     
           
        if not voice.is_playing():
            self.song_queue[ctx.guild] = [song]
            self.message[ctx.guild] = await ctx.send(embed=song['embed'])
            try:
               await ctx.message.delete()
            except:
                pass
   

            
            voice.play(FFmpegPCMAudio(song['source'], **Music.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
            voice.is_playing()
        else:
            self.song_queue[ctx.guild].append(song)
            await self.edit_message(ctx)
        time.sleep(4)
        try:
             await ctx.message.delete()
        except:
               pass
   
    @commands.command(aliases=['resume'],brief='s-resume : resume music ')
    async def pause(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            try:
              await ctx.message.delete()
            except:
               pass
   

            if voice.is_playing():
                await ctx.send('⏸️ Music paused', delete_after=5.0)
                voice.pause()
            else:
                await ctx.send('⏯️ Music resumed', delete_after=5.0)
                voice.resume()

    @commands.command(aliases=['pass'], brief='s-skip : skip a song')
    async def skip(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            try:
              await ctx.message.delete()
            except:
               pass
   

            await ctx.send('⏭️ Music skipped', delete_after=5.0)
            voice.stop()

    @commands.command(brief='s-remove [index no.] : removes song from the queue with the specified index no. ')
    async def remove(self, ctx, *, num: int):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            del self.song_queue[ctx.guild][num]
            try:
               await ctx.message.delete()
            except:
               pass
   

            await self.edit_message(ctx)

    @commands.command(brief='s-spotify [@member] : shows what the mentioned member is listening to')
    async def spotify(self,ctx, user: discord.Member=None):
        user = user or ctx.author
        k=0
        for activity in user.activities:
            if isinstance(activity, Spotify):
                k=k+1
                await ctx.send(f"{user} is listening to {activity.title} by {activity.artist}")
        if(k==0):
            await ctx.send("User is not listening to anything on Spotify.")
            
    @commands.command(aliases=['dis','leave','bye'], brief='s-disconnect : leaves voice channel currently playing in')
    async def disconnect(self, ctx):
        server = ctx.message.guild.voice_client
        await ctx.send(':wave: see you later',delete_after=5.0)
        await server.disconnect()

    @commands.command(aliases=['l'],brief='s-listening [song/artist] : gets a list of members listening to that particular song/artist')
    async def listening(self,ctx,arso: str):
        q=ctx.message.content.replace('s-listening','').strip().lower()
        n=[]
        ns=0
        for i in ctx.guild.members:
            for activity in i.activities:
                if isinstance(activity,Spotify):
                   ns+=1
                   if((q in activity.title.lower()) or (q in activity.artist.lower())):
                    n.append([f'{i}',f'{activity.title}',f'{activity.artist}'])
        print(n)
        if(ns==0):
            await ctx.send('No one in this server is listening to songs on Spotify right now.')
        else:
          if(ns==1):
              pre='person is'
          else:
              pre='people are'
          embed = discord.Embed(color=0x4400ff)
          embed.description=(str(ns)+f' {pre} '+'listening to songs on Spotify in this server right now')
          embed.add_field(name=f'No of people listening to {q} : ',value=len(n),inline=False)
          if(len(n)==0):
              await ctx.send(embed=embed)
          else:
              for item in n:
                  user=item[0]
                  name=item[1]
                  artist=item[2]
                  embed.add_field(name='Member :',value=f'{user}',inline=True)
                  embed.add_field(name='Listening to :',value=f'{name} by {artist}',inline=True)
              await ctx.send(embed=embed)

    @commands.command(aliases=['la'],brief='s-listeningall : gets a list of all the members in the server currently listening to music')
    async def listeningall(self,ctx):
        n=[]
        ns=0
        for i in ctx.guild.members:
            for activity in i.activities:
                if isinstance(activity,Spotify):
                   ns+=1
                   n.append([f'{i}',f'{activity.title}',f'{activity.artist}'])
        print(n)
        if(ns==0):
            await ctx.send('No one in this server is listening to songs on Spotify right now.')
        else:
          if(ns==1):
              pre='person is'
          else:
              pre='people are'
          embed = discord.Embed(color=0x4400ff)
          embed.description=(str(ns)+f' {pre} '+'listening to songs on Spotify in this server right now')
          if(len(n)==0):
              await ctx.send(embed=embed)
          else:
              for item in n:
                  user=item[0]
                  name=item[1]
                  artist=item[2]
                  embed.add_field(name=(f'{user}'+' is listening to '),value=f'{name} by {artist}',inline=False)
              await ctx.send(embed=embed)

#    @commands.command()
#    async def tts(self,ctx,d,tex):
#        voice = get(self.bot.voice_clients, guild=ctx.guild)
#        # Gets voice channel of message author
#        voice_channel = ctx.author.voice.channel
#        channel = ctx.author.voice.channel
#
#        file = open("counter.txt","r")
#        Counter = 0
#        # Reading from file 
#        Content = file.read()
#        CoList = Content.split("\n")
#  
#        for i in CoList: 
#            if i:
#                Counter += 1
#        file.close()
#        k=Counter
#
#        di=d.strip().lower()
#        tex1=ctx.message.content.replace(d,'').replace('+tts','')
#        print('text : ',tex1)
#        print('d : ',d)
#        #text_to_read = "teri gaand maar dunga madarchod"
#        try:
#         if voice.is_playing():
#          self.tts_queue[ctx.guild].append(f'my_file{str(k)}.mp3')
#          while voice.is_playing():
#            time.sleep(.1)
#        except:
#            pass
#        #os.remove(f'my_file{str(k)}.mp3')
#        k2=k+1
#        print('k2=a+1 = ',k2)
#        filename = f'my_file{str(k2)}.mp3'
#
#        file=open('counter.txt','a')
#        file.write('a \n')
#        file.close()
#        
#        def female(text,dia):
#            language = f'en{dia}'
#            slow_audio_speed = False
#            audio_created = gTTS(text=text, lang=language,
#                                 slow=slow_audio_speed)
#            audio_created.save(filename)
#        
#        def male(text):
#            engine=pyttsx3.init()
#            voices = engine.getProperty('voices')
#            engine.setProperty('voice', voices[0].id)
#            engine.save_to_file(text, filename)
#            engine.runAndWait()
#        
#        if(di.startswith('f-')):
#            da=di.split('-')
#            if len(da)>0:
#              dial='-'+da[1]
#            else:
#              dial=''
#            print(tex1,' ',dial)
#            female(tex1,dial)
#
#        elif(di=='m'):
#            male(tex1)
#
#
#        if voice and voice.is_connected():
#            await voice.move_to(channel)
#        else:
#            voice = await channel.connect()  
#
#        song=filename
#        if not voice.is_playing():
#            self.tts_queue[ctx.guild] = [song]
#            voice.play(FFmpegPCMAudio(song), after=lambda e: self.play_next_tts(ctx))
#            voice.is_playing()
#        else:
#            self.tts_queue[ctx.guild].append(song)
#          
#        '''
#        if voice_channel != None:
#            channel = voice_channel.name
#            vc = await voice_channel.connect()
#            vc.play(discord.FFmpegPCMAudio('my_file.mp3'))
#            # Sleep while audio is playing.
#            while vc.is_playing():
#                time.sleep(.1)
#            await vc.disconnect()
#        else:
#            await ctx.send(str(ctx.author.name) + "is not in a channel.")
#        # Delete command after the audio is done playing.
#        await ctx.message.delete()
#       '''

    

       

        #voice = get(self.bot.voice_clients, guild=ctx.guild)
        #run_coroutine_threadsafe(voice.disconnect())

def setup(bot):
    bot.add_cog(Music(bot))
