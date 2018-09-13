import sqlite3

#open("persistence.db", "w").close()

conn = sqlite3.connect("persistence.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS bans (
id integer PRIMARY KEY,
moderator text NOT NULL,
target text NOT NULL,
start_date real NOT NULL,
end_date real NOT NULL,
reason text NOT NULL
)""")
for i in range(50):
    c.execute(f"""INSERT INTO bans(moderator, target, start_date, end_date, reason)
    VALUES
    (
    "test",
    "target",
    datetime("now"),
    datetime(1536842125, 'unixepoch', 'localtime'),
    "{i}"
    )""")

    conn.commit()

    for item in c.execute("""SELECT * FROM bans""").fetchall():
        print(item)
