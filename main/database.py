import sqlite3 as sq

db = sq.connect('/?Korean/db/tg.db')
cur = db.cursor()

async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS users("
    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
    "username text, "
    "tg_id INTEGER )")
    db.commit()

#Собираю id юзеров
async def cmd_start_db(user_id):
    user = cur.execute("SELECT * FROM users WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO users (tg_id) VALUES ({key})".format(key=user_id))
    db.commit()
    cur.close()
    db.close()

"""async def cmd_start_db_name(username):
    user = cur.execute("SELECT * FROM accounts WHERE username == {key}".format(key=f"{username}")).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (username) VALUES ({key})".format(key=f"{username}"))
    db.commit()
"""
