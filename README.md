# ZoltBot

[![Zolts GA icon](https://i.imgur.com/XYYjfuN.png)](https://zolts.ga)

ZoltBot will be a personalized Discord Bot which integrates sub communities in one discord server along with a currency system backed by cryptocurrency.

# Current Features

  - A core skeleton which makes growth and management of systems much easier and allows collaborative flow during development

# Planned Features

  - Interactive Menu's within discord
  - Internalized roles to stop clutter in discord's own system
  - User management system including softbans and muting
  - A system to reward more active users
  - A database to store data such as bans and user activity

### Dependencies

ZoltBot uses a number of open source projects to work properly:

* [python 3](https://www.python.org/) - The language ZoltBot is written in
* [discord-rewrite](https://github.com/Rapptz/discord.py/tree/rewrite) - An API wrapper library which ZoltBot uses

#### Python  Internal Libraries
These come preinstalled with python 3
* [argparse](https://docs.python.org/3/library/argparse.html) - A python library allowing command line argument parsing
* [asyncio](https://docs.python.org/3/library/asyncio.html) -  A library which allows asynchronous programs
* [sys](https://docs.python.org/3/library/sys.html) - A python library for accessing and modifying system variables
* [logging](https://docs.python.org/3/library/logging.html) - Allows logging within a python program
* [os](https://docs.python.org/3/library/os.html) - Provides better OS functionality
* [pickle](https://docs.python.org/3/library/pickle.html) - Implements binary protocols for serializing and de-serializing a Python object structure.
* [sqlite3](https://docs.python.org/3/library/sqlite3.html) - Provides a lightweight disk-based database that doesn’t require a separate server process.


### Installation

```git
pip install discord-rewrite
git clone https://github.com/Genetical/ZoltBot.git
```

If you are having problems with aiohttp, do this:
```
pip install -U "yarl>1.2"
```
