from discord import Embed
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import json
from requests import get
import discord
import urllib
from PIL import Image,ImageFont,ImageDraw,ImageFilter,ImageEnhance
from discord import Game
import sqlite3

genres=[
  'rock',
  'hiphop',
  'metal',
  'epic',
  'synthwave',
  '90s',
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
    


    @commands.command(brief='s-help')
    async def help(self, ctx):
        k=0
        m,c,s='','',''

        embed1=Embed(color=0xff3053, title='List of commands : ')
        embed2 = Embed(color=0xff3053, title='Music - All the commands related to music')
        embed3=Embed(color=0xff3053, title='Chat - All the micellaneous commands')
        embed4=Embed(color=0xff3053, title='Starboard - Make your own server Starboard !')

        music1=['song','songplay','listening','listeningall','moods','genres','spotify','play','skip','resume','pause','disconnect','remove']
        chat1=['poll','urban','idea','joke','meme','makenews','twitchgame','twitchstreamer']
        starb=['starboard_add']

        for i1 in music1:
            m=m+'`{}`'.format(i1)+' | '
        for i2 in chat1:
            c=c+'`{}`'.format(i2)+' | '
        for i3 in starb:
            s=s+' | '+'`{}`'.format(i3)+' | '

        em={'music':embed2
        , 'chat':embed3
        , 'help':embed1
        ,'starboard':embed4}


        if ctx.message.content=='s-help':
         cate='help'
        else:
         cate = str(ctx.message.content.replace('s-help ','').strip().lower())
        print(cate)

        embed1.description= f'**MUSIC**\n{m}\n\n**CHAT**\n{c}\n\n**STARBOARD**\n{s}\n\nTo get help on the different categories use `s-help [category]`\nexample : `s-help starboard`\n\nIf you are having any type of issue with the bot just contact *Rishi#5250*'
        embed1.add_field(name='-',value=f"[invite me](https://discord.com/api/oauth2/authorize?client_id=732342819510812713&permissions=37223488&scope=bot)",inline=True)

        embed3.add_field(name='`s-poll ["question in double quotes"] [options separated by spaces]`',value='conduct a poll \n example: s-poll "How is this bot ?" good bad',inline=False)
        embed3.add_field(name='`s-urban [word]`',value='gives the meaning of the word from urban dictionary ',inline=False)
        embed3.add_field(name='`s-idea`',value='gives a random idea',inline=False)
        embed3.add_field(name='`s-joke`',value='tells a joke',inline=False)
        embed3.add_field(name='`s-meme`',value='fetches a meme from reddit',inline=False)
        embed3.add_field(name='`s-makenews [news]`',value='make a news banner',inline=False)
        embed3.add_field(name='`s-twitchgame or s-tg [game] [key-words (optional)]`',value='get live streams related to the game \n example : s-twitchgame minecraft',inline=False)
        embed3.add_field(name='`s-twitchstreamer or s-ts [streamer]`',value='get status of the streamer \n example : s-twitchstreamer ninja ',inline=False)
        embed3.add_field(name='-',value=f"[invite me](https://discord.com/api/oauth2/authorize?client_id=732342819510812713&permissions=37223488&scope=bot)",inline=True)

        embed2.add_field(name='`s-song or s-s [genre/mood]`',value='get a song recommended by Sensei along with the Spotify link \n example : s-song lofi',inline=False)
        embed2.add_field(name='`s-songplay or s-sp [genre/mood]`',value='play a song recommended by Sensei \n example : s-sp metal',inline=False)
        embed2.add_field(name='`s-listening [song/artist]`',value='Get a list of all the people in your server listening to that song/artist',inline=False)
        embed2.add_field(name='`s-listeningall or s-la`',value='Get a list of all the members in your server currently listening to songs',inline=False)
        embed2.add_field(name='`s-genres`',value='get a list of genres that Sensei supports',inline=False)
        embed2.add_field(name='`s-moods`',value='get a list of moods that Sensei supports',inline=False)
        embed2.add_field(name='`s-play [youtube url/song name]`',value='play any song of your choice',inline=False)
        embed2.add_field(name='`s-pause`',value='pause the music',inline=False)
        embed2.add_field(name='`s-resume`',value='resume the music',inline=False)
        embed2.add_field(name='`s-skip`',value='skip the current currently playing song',inline=False)
        embed2.add_field(name='`s-remove [index in queue]`',value='remove a song from the queue',inline=False)
        embed2.add_field(name='`s-bye`',value='leaves voice channel',inline=False)
        embed2.add_field(name='-',value=f"[invite me](https://discord.com/api/oauth2/authorize?client_id=732342819510812713&permissions=37223488&scope=bot)",inline=True)
        embed2.add_field(name='-',value=f"[support server](https://discord.gg/EYQrwpy)",inline=True)

        embed4.description="*A starboard is a popular feature in bots that serve as a channel of messages that users of the server find funny, stupid, or both! \nThe members react to a message they like and if it gets as many stars as set in the command then it goes to starboard*\n\nCreate a starboard in your server by using command : \n`s-starboard_add [channel name] [stars required for starboard]`\n\nExample : `s-starboard_add #starboard 3` \n\n-Update the channel or starcount requirement by using this same command\n\n-It is recommended to set starboard channel to some channel which does not allow user to send messages \n\n-**Allow Sensei to read messages and add reactions to all the channels which you wish to be starred**\n**In starboard channel remember to allow Sensei to**  : \n`send messages` , `manage messages ` , `embed links` , `attach files` ,\n`read message history` , `add reactions` , `use external emojis`\n\n **VIDEOS CANNOT BE STARRED** "
        embed4.add_field(name='-',value=f"[invite me](https://discord.com/api/oauth2/authorize?client_id=732342819510812713&permissions=37223488&scope=bot)",inline=True)
        embed4.add_field(name='-',value=f"[support server](https://discord.gg/EYQrwpy)",inline=True)

        q=em[cate]
        await ctx.send(embed=q)#hello


    @commands.command()
    async def update(self,ctx):
        print(str(ctx.message.author))
        if('Rishi#5250' in (str(ctx.message.author))):
          activeServers = self.bot.guilds
          summ=0
          for s in activeServers:
              summ += len(s.members)
          print(summ)
          summ1=146003
          print('Yare Yare Dazei')
          await self.bot.change_presence(activity=Game(name=f's-help | Supporting {summ} members.'))
          await ctx.send(summ)
          sum=0
        else:
          await ctx.send('Not authorized')
  
    @commands.command(brief='s-genres : get a list of genres')
    async def genres(self, ctx):
        embed = Embed(color=0x9240FF, title='Genres : ')
        m=''
        embed.add_field(name='`s-songplay or s-sp [genre]` :get a song played of the genre by music sensei',value='Example : s-songplay heavymetal',inline=False)
        embed.add_field(name='`s-song or s-s [genre]` :get a song recommended of the genre by Music Sensei',value='Example : s-song heavymetal',inline=True)
        for i in range(0,len(genres)):
          m=m+' `{}`, '.format(genres[i])
        embed.description=m
        embed.set_footer(text='more to be added soon...')
        try:
            await ctx.message.delete()
        except:
            pass


        await ctx.send(embed=embed)


    @commands.command()
    async def invite(self,ctx):
      e=Embed(color=0xde2312,description=f"**[invite me](https://discord.com/api/oauth2/authorize?client_id=732342819510812713&permissions=37223488&scope=bot)**")
      await ctx.send(embed=e)


    @commands.command(brief='s-moods : get a list of moods')
    async def moods(self,ctx):
        embed = Embed(color=0x9240FF, title='Moods : ')
        embed.add_field(name='`s-songplay or s-sp [mood]` :get a song played of the mood by Music Sensei',value='Example : s-songplay happy')
        embed.add_field(name='`s-song or s-s [mood]` :get a song recommended of the mood by Music Sensei',value='Example : s-song happy')
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


    @commands.command(brief='s-urban [word] : gives the meaning of the word from urban dictionary')
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


    @commands.command(brief='s-idea : gives a random idea')
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


    @commands.command(brief='s-joke : tells a joke')
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


  #  @commands.command(brief='s-scanurl')
  #  async def scanurl(self,ctx):
  #    import time
  #    url=ctx.message.content.replace('s-scanurl','').strip()
  #    if not url.startswith('https://'):
  #      embed = Embed(title="❌ Enter a valid url", color=0xe74c3c)
  #      await ctx.send(embed=embed)
  #    else:
  #      e=mal(url)
  #      e2 = Embed(color=0xC52430)
  #      e2.set_author(name='Processing...',icon_url='https://media.giphy.com/media/5th8zFFsvNOuM6nGsq/giphy.gif') 
  #      msg = await ctx.send(embed=e2)
  #      time.sleep(3)
  #      await msg.edit(embed=e)

    @commands.command(brief='s-poll ["question"] [answers separated by spaces]')
    async def poll(self, ctx, *items):
         question = items[0]     
         answers = '\n'.join(items[1:])
         emojis = {1:'1️⃣',2:'2️⃣',3:'3️⃣',4:'4️⃣',5:'5️⃣',6:'6️⃣',7:'7️⃣',8:'8️⃣',9:'9️⃣'}
         embed = Embed(title=f"**{question}**", color=0x3498db)
         embed.set_footer(text=f'Asked by {ctx.author}')

         des=''
         for i in range(1, len(items)):
             des=des+emojis[i]+'.'+items[i]+'\n'
         embed.description=des
         message = await ctx.channel.send(embed=embed)
         reactions = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
 
         for i in range(len(items[1:])):
             await message.add_reaction(reactions[i])
 

    @commands.command(brief='s-meme')
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
  

    #@commands.command(aliases=['help tts']) 
   # async def help_tts(self,ctx):
   #   emb=Embed(color=0x9240FF)
   #   dialects=[
#
   #     'f-us;English (US)',
   #     'f-in;English (India)',
   #     'f-ca;English (Canada)',
   #     'f-uk;English (UK)',
   #     'f-gb;English (UK)',
   #     'f-au;English (Australia)',
   #     'f-gh;English (Ghana)',
   #     'f-ie;English (Ireland)',
   #     'f-nz;English (New Zealand)',
   #     'f-ng;English (Nigeria)',
   #     'f-ph;English (Philippines)',
   #     'f-za;English (South Africa)',
   #   ]
#
   #   hagf=''
#
   #   for d in dialects :
   #     d1=d.split(';')
   #     print(d1)
   #     hagf=hagf+'*{}*'.format(d1[0])+' = '+d1[1]+' \n'
   #   print(hagf)
   #   emb.title='TTS'
   #   emb.description='1. ** s-tts [gender] [text] ** \n\n gender: m for male , f for female \n example command : `s-tts m hello there` \n\n -(optional) For **female** voice different dialects can be chosen \n\n Dialects : \n {} \n example: `s-tts f-in hello there` \n\n **WARNING : Dialects are available only for female voice**'.format(hagf)
   #   await ctx.send(embed=emb)

    
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


    @commands.command(aliases=['sb_add'])
    @has_permissions(manage_channels=True)
    async def starboard_add(self,ctx,channel_mention,star_count):

      g_id=ctx.message.guild.id
      c_id=int(channel_mention.replace('<','').replace('>','').replace('#','').replace('@','').strip())

      conn = sqlite3.connect('starboard.db')
      c=conn.cursor()

      c.execute("SELECT * FROM sb WHERE guildid= ? AND channelid= ? AND starcount = ?",(g_id,c_id,star_count))
      exist=c.fetchone()

      if exist is None:
        c.execute("SELECT * FROM sb WHERE guildid=? ",(g_id,))
        exist2=c.fetchone()
        if not exist2 is None:
          gi,ci,sc=exist2
          if(ci != c_id):
            c.execute('''UPDATE sb
                         SET channelid=?
                         WHERE guildid = ?''',(c_id,g_id))
            await ctx.send('**STARBOARD CHANNEL SUCCESFULLY CHANGED**')
          elif(sc != star_count):
            c.execute('''UPDATE sb
                         SET starcount=?
                         WHERE guildid = ?''',(star_count,g_id))
            await ctx.send('**STARBOARD CHANNEL STARCOUNT SUCCESFULLY CHANGED**')      

        else:
          c.execute('''INSERT INTO sb
                       VALUES(?,?,?) ''',(g_id,c_id,star_count))
          await ctx.send('**STARBOARD CHANNEL SUCCESFULLY SET**')

        conn.commit()

      else:
          await ctx.send('**SPECIFIED CHANNEL WITH THIS STARCOUNT ALREADY ADDED**')
      
      conn.close()

    @starboard_add.error
    async def sb_error(self,error, ctx):
     if isinstance(error, MissingPermissions):
         text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
         await ctx.send(ctx.message.channel, text)


def setup(bot):
    bot.add_cog(chat(bot))


# %%
