from discord import Game
from discord.ext import commands
from discord import Client
from discord.ext import tasks
from discord.utils import get
from discord import Embed
import sqlite3
from config import botkey


async def reaction_func():
    if ctx.emoji.name == "⭐":
        ch = bot.get_channel(ctx.channel_id)
        message = await ch.fetch_message(ctx.message_id)
        if not message.author == 'Sensei#7392':
            gid = ctx.guild_id
            conn = sqlite3.connect('starboard.db')
            c = conn.cursor()
            c.execute('SELECT * FROM sb WHERE guildid = ?', (gid,))
            ex = c.fetchone()
            if not ex is None:
                c.execute('SELECT * FROM mess WHERE msgid = ?',
                          (ctx.message_id,))
                x = c.fetchone()
                if x is None:
                    print('adding message to mess')
                    c.execute('''INSERT INTO mess
                             VALUES(?)''', (ctx.message_id,))
                    guid, chid, sco = ex
                    print('b')
                    if not ch == bot.get_channel(chid):
                        e = Embed(color=0xffdd54)
                        if(len(message.attachments)):
                            e.set_image(url=message.attachments[0].url)

                        e.description = message.content
                        e.set_author(name=message.author,
                                     icon_url=message.author.avatar_url)

                        try:
                            c.execute(
                                'SELECT * FROM sb WHERE guildid = ?', (gid,))
                            g, cid, scount = c.fetchone()
                        except:
                            pass
                        conn.commit()
                        conn.close()

                        print('c')
                        if ctx.emoji.name == "⭐":
                            print('d')
                            message = await ch.fetch_message(ctx.message_id)

                            done = bot.get_emoji(743133763596320889)
                            reaction = get(message.reactions, emoji="⭐")
                            if(reaction.count > scount-1):
                                try:
                                    print(message.jump_url)
                                    ch = bot.get_channel(cid)
                                    e.set_footer(
                                        text=str((str(message.created_at).split(' '))[0]))
                                    ti = (f'💫 | {message.channel.mention}')
                                    msg = await ch.send(content=ti, embed=e)
                                    await msg.add_reaction('⭐')
                                    await message.add_reaction('💫')

                                    await message.add_reaction('💫')
                                except Exception as e:
                                    print(e)
