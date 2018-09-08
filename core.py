import argparse, discord, asyncio, sys, logging
from discord.ext import commands
import os

## Enforce parsing of token argument
parser = argparse.ArgumentParser()
parser.add_argument("token", help="Must be a valid discord bot token")
args = parser.parse_args()


## Initialise Logging
from utils.loggerinit import *
log = logger("logs\\critical.log","logs\\information.log")

## Load extensions
from utils import *

bot = commands.Bot(command_prefix="!")

#Rip readability, this lists all file names in the extensions folder, removes the ".*" extension and prefixes with "extensions." it then imports the extension
[bot.load_extension(f"extensions.{os.path.splitext(f)[0]}") for f in os.listdir(f"{os.getcwd()}/extensions") if os.path.isfile(os.path.join(f"{os.getcwd()}/extensions", f))]

## Initialise bot

@bot.event
async def on_ready():
    u = bot.user
    connected_servers = len([guilds for guilds in bot.guilds])
    print("Bot profile loaded")
    print(f"Username: {u.name} with display name: {u.display_name}",
          f"ID: {u.id}", sep="\n")
    print("STATISTICS:",
          f"Created at (UTC) {u.created_at}",
          f"Currently connected to {connected_servers} server(s).", sep="\n")
    #log.info(f"Initialised as {u.name} with ID: {u.id}")

try:
    bot.run(args.token, bot=True, reconnect=True)
except Exception as e:
    log.critical(f"Could not initialise bot. {e}")
