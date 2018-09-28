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
)""") # oof i haven't properly used primary keys before, i've done them manually

c.execute("""CREATE TABLE IF NOT EXISTS warnings (
id integer PRIMARY KEY,
moderator text NOT NULL,
target text NOT NULL,
warning_time real NOT NULL,
reason text NOT NULL
)""")

c.execute("""CREATE TABLE IF NOT EXISTS tags (
tag_id integer NOT NULL
)""")

def ban(moderator, target, length, reason):
    command = """INSERT INTO bans
    (moderator, target, start_date, end_date, reason)
    VALUES (
    ?,
    ?,
    datetime('now'),
    datetime(?, 'unixepoch', 'localtime'),
    ?)
    """

    c.execute(command, (
      moderator.id,
      target.id,
      timeframe.convert(length),
      reason
      ))
    conn.commit()

def fetch_ban(moderator=None, target=None, limit=10):
    import calendar, time
    current_time = calendar.timegm(time.gmtime())

    # Generate sqlite command and append extra filter if two arguments parsed (moderator and target)
    command = """SELECT (moderator, target, start_date, end_date, reason) FROM bans"""
    if moderator != None:
        command += """ WHERE moderator=?"""
        if target != None:
            command += """ AND target=?"""
    elif target != None:
        command = """ WHERE target=?"""
        if moderator != None:
            command += """ AND moderator=?"""
    if limit > 10:
        command += f" LIMIT 10" ## Spam proof!
    else:
        command += f" LIMIT {limit}"

    r = []
    row_list = c.execute(command).fetchall()
    for row in row_list:
        moderator, target, start_date, end_date, reason = row
        r.append(f"```{moderator} banned {target} at {start_date} for {reason}. Expiring {end_date}```")
    return r

        ## IMPORTANT CODE WHICH INTERSECTS EACH ITEM OF ROW WITH REPECTIVE COLUMN INTO A DICT (and actually changes it)

        ## TODO: Make the returned rows look nice
        ## 1 ) Return it into a discord ```???``` too make it look nice [X]
        ## 2 ) Return that to the command !bans and then output it [ ]
        ## 3 ) Hide the existenial dread [ ]
        ## 4 ) No more nihilism! [ ]


def remove_ban(user: str):
    if user in c.execute("""SELECT user FROM bans"""):
        command = """DELETE FROM bans WHERE user=(?)"""
        try:
            c.execute(command, (user,))
            return "Ban removed successfully!"
        except Exception as error:
            raise Exception(f"There was a problem removing the ban on {user}. Please try again later.")
    else:
        raise Exception(f"There was a problem removing the ban on {user}, are you sure they're banned?")

def warn(moderator, target, reason):
    command = """INSERT INTO warnings VALUES (?,?,?)"""
    c.execute(command, (moderator.id,
                        target.id,
                        reason))
    return f"Warned user successfully!"

def find_warnings(user, mode="user"):
    if mode == "user":
        all_warnings = c.execute("SELECT * FROM warnings WHERE target=(?)", (user.id,))
    elif mode == "moderator":
        all_warnings = c.execute("SELECT * FROM warnings WHERE moderator=(?)", (user.id,))
    warnings_output = []
    for warning in all_warnings:
        moderator = warning["moderator"]
        target    = warning["target"]
        time      = warning["time"]
        reason    = warning["reason"]
        warnings_output.append(f"```md\n[{moderator}] warned ({target}) on {time} for {reason}```")
    return "\n".join(warnings_output)

def add_tag(role_id):
    command = """INSERT INTO tags VALUES (?)"""
    try:
        if (role_id,) not in c.execute("""SELECT tag_id FROM tags""").fetchall():
            c.execute(command, (role_id,))
            conn.commit()
        else:
            return False
    except Exception as e:
        print(e)
        return False
    return True


def del_tag(role_id):
    command = """DELETE FROM tags WHERE tag_id=?"""
    try:
        if (role_id,) in c.execute("""SELECT tag_id FROM tags""").fetchall():
            c.execute(command, (role_id,))
            conn.commit()
        else:
            return False
    except Exception as e:
        print(e)
        return False
    return True

def verify_tag(role_id):
    if (role_id,) in c.execute("""SELECT tag_id FROM tags""").fetchall():
        return True
    else:
        return False

def dump_tags():
    try:
        return [str(row[0]) for row in c.execute("""SELECT tag_id FROM tags""").fetchall()]
    except:
        return False
