import sqlite3
import pickle
import sys
import sqlite3
sys.path.append("..")
from utils import timeframe
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
def ban(moderator, target, length, reason):
    command = """INSERT INTO bans(moderator, target, start_date, end_date, reason) VALUES (?,?,datetime('now'),datetime(?, 'unixepoch', 'localtime'),?)"""

    c.execute(command, (
      pickle.dumps(moderator),
      pickle.dumps(target),
      timeframe(length),
      reason
      ))
    conn.commit()

def fetch_ban():
    output = []
    for item in c.execute("""SELECT * FROM bans""").fetchall():
          item = dict(zip(list(map(lambda x: x[0], c.description)), item))
          item["moderator"] = pickle.loads(item["moderator"])
          item["target"] = pickle.loads(item["target"])
          output.append(item)
    return output
