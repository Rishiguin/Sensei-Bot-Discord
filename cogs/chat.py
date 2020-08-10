from discord import Embed
from discord.ext import commands
import requests
import json
from requests import get
import discord
import urllib
from PIL import Image,ImageFont,ImageDraw,ImageFilter,ImageEnhance

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
        embed.add_field(name='`+song or +s [genre/mood]`',value='get a song recommended by Sensei along with the Spotify link',inline=False)
        embed.add_field(name='`+songplay or +sp [genre/mood]`',value='play a song recommended by Sensei',inline=False)
        embed.add_field(name='`+listening [song/artist]`',value='Get a list of all the people in your server listening to that song/artist',inline=False)
        embed.add_field(name='`+listeningall or +la`',value='Get a list of all the members in your server currently listening to songs',inline=False)
        embed.add_field(name='`+genres`',value='get a list of genres that Sensei supports',inline=False)
        embed.add_field(name='`+moods`',value='get a list of moods that Sensei supports',inline=False)
        embed.add_field(name='`+play [youtube url/song name]`',value='play any song of your choice',inline=False)
        embed.add_field(name='`+pause`',value='pause the music',inline=False)
        embed.add_field(name='`+resume`',value='resume the music',inline=False)
        embed.add_field(name='`+skip`',value='skip the current currently playing song',inline=False)
        embed.add_field(name='`+remove [index in queue]`',value='remove a song from the queue',inline=False)
        embed.add_field(name='`+bye`',value='leaves voice channel',inline=False)
        embed.add_field(name='-',value=f"[invite me](https://discord.com/api/oauth2/authorize?client_id=732342819510812713&permissions=37223488&scope=bot)",inline=True)
        embed.add_field(name='-',value=f"[support server](https://discord.gg/EYQrwpy)",inline=True)
        try:
          await ctx.message.delete()
        except:
            pass


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
        try:
            await ctx.message.delete()
        except:
            pass


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
        try:
           await ctx.message.delete()
        except:
            pass


        await ctx.send(embed=embed)




    @commands.command(brief='+urban [word] | (gives the meaning of the word from urban dictionary)')
    async def urban(self,ctx):
        #print(ctx.ctx.message.content)
        word=ctx.message.content.replace('s-urban ','').strip()
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




    @commands.command(brief='+idea')
    async def idea(self,ctx):
        print(ctx.message.content)
        import time
        embed = Embed(color=0xF5A623)  
        e2 = Embed(color=0xC52430)
        e2.set_author(name='Thinking',icon_url='https://media.giphy.com/media/xTkcEQACH24SMPxIQg/giphy.gif') 
        msg = await ctx.send(embed=e2)
        time.sleep(2)
        res=requests.get(url='http://itsthisforthat.com/api.php?text')
        adv=res.text
        embed.description='I have an idea. '+adv
        await msg.edit(embed=embed)




    @commands.command(brief='+joke')
    async def joke(self,ctx):
      import time
      d=requests.get('https://sv443.net/jokeapi/v2/joke/Any?type=twopart')
      req=d.json()
      print(req)

      setup=req['setup']
      deli=req['delivery']
  
      embed = Embed(color=0xfffb00, title=setup)
      e2 = Embed(color=0x42c42b, title=deli)
      embed.set_author(name='Sensei',icon_url='https://media.giphy.com/media/xT39DdjfMcxiu1lwk0/giphy.gif')
      e2.set_author(name='Sensei',icon_url='https://media.giphy.com/media/xT39DdjfMcxiu1lwk0/giphy.gif')
      msg= await ctx.send(embed=embed)
      time.sleep(6)
      await msg.edit(embed=e2)




    @commands.command(brief='+scanurl')
    async def scanurl(self,ctx):
      import time
      url=ctx.message.content.replace('s-scanurl','').strip()
      if not url.startswith('https://'):
        embed = Embed(title="❌ Enter a valid url", color=0xe74c3c)
        await ctx.send(embed=embed)
      else:
        e=mal(url)
        e2 = Embed(color=0xC52430)
        e2.set_author(name='Processing...',icon_url='https://media.giphy.com/media/5th8zFFsvNOuM6nGsq/giphy.gif') 
        msg = await ctx.send(embed=e2)
        time.sleep(3)
        await msg.edit(embed=e)

 


    @commands.command(brief='+poll ["question"] [answers separated by spaces]')
    async def poll(self, ctx, *items):
         question = items[0]     
         answers = '\n'.join(items[1:])
         embed = Embed(title='Poll :', description=f"__{question}__", color=0x3498db)
         embed.set_footer(text=f'Asked by {ctx.author}')
         for i in range(1, len(items)):
             embed.add_field(name=f"{i}", value=items[i], inline=False)
         #await ctx.message.delete()
         message = await ctx.channel.send(embed=embed)
         reactions = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
 
         for i in range(len(items[1:])):
             await message.add_reaction(reactions[i])
 



    @commands.command(brief='+meme')
    async def meme(self, ctx):
         data = get('https://meme-api.herokuapp.com/gimme').json()
         embed = (Embed(title=f":speech_balloon: r/{data['subreddit']} :", color=0x9240FF)
                 .set_image(url=data['url'])
                 .set_footer(text=data['postLink']))
         await ctx.send(embed=embed)




    @commands.command(brief='twitch [game] [key-words (optional)]',aliases=['tg','twitch game'])
    async def twitchgame(self, ctx, game, *keys, streams=[]):
      CLIENT_ID = 'j3abopdoj1fi9hshxtli9jlnkyruof'
      CLIENT_SECRET='ybud1f2qvv2u89s8ue8wpsdb7f88pc'
      
      def make_request(URL):
         header    = {"Client-ID": CLIENT_ID, "Authorization": f"Bearer {get_access_token()}" }
         req  = urllib.request.Request(URL, headers=header)
         recv = urllib.request.urlopen(req)
         print(recv)
         return json.loads(recv.read().decode("utf-8"))

      def get_access_token():  
          
          x = requests.post(f"https://id.twitch.tv/oauth2/token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&grant_type=client_credentials")
          print(x.text)
          print(json.loads(x.text)["access_token"])
          return json.loads(x.text)["access_token"]

      topgames = make_request(f"https://api.twitch.tv/helix/games/top?first=100")
      print(topgames)
      for category in topgames['data']:
          if game.lower() in category['name'].lower():
              embed = Embed(title=f"Streams ({category['name']}):", color=0x9834eb)
              stream_nb = 100 if keys else 20
              response = make_request(f"https://api.twitch.tv/helix/streams?game_id={category['id']}&first={stream_nb}")
              for stream in response['data']:
                  if keys:
                      for key in keys:
                          if key.lower() in stream['title'].lower() and not stream in streams:
                              streams.append(stream)
                              embed.add_field(name=f"{stream['user_name']}", value=f"[{stream['title']}](https://twitch.tv/{stream['user_name']})")
                  else:
                      embed.add_field(name=f"{stream['user_name']}", value=f"[{stream['title']}](https://twitch.tv/{stream['user_name']})")
              await ctx.send(embed=embed)
              return
      embed = Embed(title=f"❌ Something went wrong:", description="No streams found", color=0xe74c3c)
      await ctx.send(embed=embed) 





    @commands.command(brief='twitch [streamer] ',aliases=['ts'])
    async def twitchstreamer(self, ctx, streamer):
      print(streamer)
      CLIENT_ID = 'j3abopdoj1fi9hshxtli9jlnkyruof'
      CLIENT_SECRET='ybud1f2qvv2u89s8ue8wpsdb7f88pc'
      
      def make_request(URL):

         header    = {"Client-ID": CLIENT_ID, "Authorization": f"Bearer {get_access_token()}" }
         req  = urllib.request.Request(URL, headers=header)
         recv = urllib.request.urlopen(req)
         print(recv)
         return json.loads(recv.read().decode("utf-8"))

      def get_access_token():  
          
          x = requests.post(f"https://id.twitch.tv/oauth2/token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&grant_type=client_credentials")
          print(x.text)
          print(json.loads(x.text)["access_token"])
          return json.loads(x.text)["access_token"]

      streamers = make_request(f"https://api.twitch.tv/helix/search/channels?query={streamer.replace(' ','').lower().strip()}")
      streamer=streamers['data'][0]
      embed=Embed(color=0x9834eb)
      try:
         embed.title=streamer['display_name']
         thumb_url=streamer['thumbnail_url']
         embed.set_thumbnail(url=thumb_url)
         embed.add_field(name='Streamer id : ',value='{}'.format(streamer['id']),inline=False)
         if(streamer['is_live']==True):
           embed.add_field(name='Live now : ',value='✅',inline=False)
           embed.add_field(name='Watch live : ',value=f"[{streamer['title']}](https://twitch.tv/{streamer['display_name']})",inline=False)
           embed.add_field(name='Started at : ',value=f"{streamer['started_at'].replace('T',' ').replace('Z',' UTC')}",inline=False)
         else:
           embed.add_field(name='Live now : ',value='❌',inline=False)
         await ctx.send(embed=embed)
      except Exception as e:
       print(e)
       embed = Embed(title=f"❌ Something went wrong:", description="No streamers found", color=0xe74c3c)
       await ctx.send(embed=embed) 
  


    @commands.command(aliases=['help tts'])
    async def help_tts(self,ctx):
      emb=Embed(color=0x9240FF)
      dialects=[

        'f-us;English (US)',
        'f-in;English (India)',
        'f-ca;English (Canada)',
        'f-uk;English (UK)',
        'f-gb;English (UK)',
        'f-au;English (Australia)',
        'f-gh;English (Ghana)',
        'f-ie;English (Ireland)',
        'f-nz;English (New Zealand)',
        'f-ng;English (Nigeria)',
        'f-ph;English (Philippines)',
        'f-za;English (South Africa)',
      ]

      hagf=''

      for d in dialects :
        d1=d.split(';')
        print(d1)
        hagf=hagf+'*{}*'.format(d1[0])+' = '+d1[1]+' \n'
      print(hagf)
      emb.title='TTS'
      emb.description='1. ** +tts [gender] [text] ** \n\n gender: m for male , f for female \n example command : `+tts m hello there` \n\n -(optional) For **female** voice different dialects can be chosen \n\n Dialects : \n {} \n example: `+tts f-in hello there` \n\n **WARNING : Dialects are available only for female voice**'.format(hagf)
      await ctx.send(embed=emb)



    @commands.command()
    async def geturl(self,ctx,emoji: discord.Emoji):
     await ctx.send(emoji.url) 

    
    @commands.command()
    async def makenews(self,ctx):
      def news1(str2,ary):
        if len(str2)>93:
            return('k')
        else:
          if(len(str2)>29):
             ar=str2.split(' ')
             print(ar)
             wr=''
             for ind,i in enumerate(ar):
                print(i)
                wr=wr+i+' '
                if (len(wr) > 28):
                   if (len(wr) < 29) and ind==len(ar)-1:
                    ary.append(wr.strip())
                   ary.append(wr.strip())
                   print('b : ',ary)
                   wr=''
             print('----------------',ary)
             tf=ary[len(ary)-1]
             print(tf)
             inde=str2.find(tf)
             print(str2[inde+len(tf):])
             toadd=str2[inde+len(tf):]
             ary.append(toadd)
        
             for ind,w in enumerate(ary):
                 if len(w)>29: 
                    inde=w.rfind(' ')
                    word=w[:inde]
                    ary[ind]=word
                    ary.insert(ind+1,w[inde:len(w)])
                 else:
                     continue
          else:
             ary.append(str2)
                   
             print(ary)
        
          im=Image.open('abp.png')
          wid,hei=im.size
          print('wid ', wid)
          print('hei ',hei)
    
          out=im.convert('RGBA')
          out.save('abp.png')
          
          #time.sleep(20)
          #os.remove('some_image.jpg')
         
          
    
         
          dst=Image.open('abp.png')
    
         
          pointsize = 55
          fillcolor = "white"
          shadowcolor = "black"
    
          font=ImageFont.truetype('alfaslab.ttf',pointsize)
          w,h=font.getsize(str2)
    
          print('text height ',(h)*len(ary))
          th=(h)*len(ary)
          RED_HEIGHT=357
          RED_WIDTH=810
          xh=RED_HEIGHT-th
           
          xhf=int(xh/2)
         
          for ind,i in enumerate(ary):
           draw=ImageDraw.Draw(dst)
           w1,h1=font.getsize(i)
           x,y=(int((810-w1)/2)+80,(190+xhf+(h*ind)+10))
          # try:
          #  draw.text((x-1, y-1), i, font=font, fill=shadowcolor)
          #  draw.text((x+1, y-1), i, font=font, fill=shadowcolor)
          #  draw.text((x-1, y+1), i, font=font, fill=shadowcolor)
          #  draw.text((x+1, y+1), i, font=font, fill=shadowcolor)
          # except:
          #     pass
          
          # now draw the text over it
           draw.text((x, y), i.strip(), font=font, fill=fillcolor)
           #
           #draw.text(((300-w1)/2,((((h/2)+10))*ind)+out1.height-50),i,fill='orange',font=font)
          d_s=dst.filter(ImageFilter.SMOOTH).filter(ImageFilter.SMOOTH)
          dst.save('abp_edit.png')
          
          #out1.show()
          return('abp_edit.png')
      text=ctx.message.content.replace('s-makenews ','')
      if (ctx.message.content.startswith('s-makenews ')):
	      a4=[]
	      a=news1(text,a4)
	      if (a=='k'):
	 	       await ctx.send(f'**Limit : 93 characters**\nRemove {len(text)-93} characters.')
	      else :
	         await ctx.send(file=discord.File(a))










def setup(bot):
    bot.add_cog(chat(bot))


# %%
