import sqlite3

conn= sqlite3.connect('starboard.db')

c=conn.cursor()

c.execute('DROP TABLE sb')

c.execute(""" CREATE TABLE sb(
            guildid int,
            channelid int,
            starcount int
           )""")

gid=654635
cid=98698
#c.execute('''INSERT INTO sb 
#             VALUES(?,?) ''',(gid,cid))
c.execute("SELECT * FROM sb WHERE guildid= ? AND channelid= ?",(gid,cid))
exist=c.fetchone()
if exist is None:
    print('not in database')
else:
    print('in database')