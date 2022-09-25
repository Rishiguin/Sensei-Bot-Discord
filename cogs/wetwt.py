import sqlite3

conn= sqlite3.connect('starboard.db')

c=conn.cursor()


#c.execute(""" CREATE TABLE mess(
#            msgid int
#           )""")

gid=654635
cid=98698
#c.execute('''INSERT INTO sb 
#             VALUES(?,?) ''',(gid,cid))
c.execute("SELECT * FROM mess WHERE msgid=?",(gid,))
exist=c.fetchone()
if exist is None:
    print('not in database')
else:
    print('in database')