import argparse, discord, asyncio, sys, logging
from discord.ext import commands
import os

## Enforce parsing of token argument
parser = argparse.ArgumentParser()
parser.add_argument("token", help="Must be a valid discord bot token")
args = parser.parse_args()

## Initialise Logging
from utils.loggerinit import *
log = initialize_logger()

## Load extensions
from utils import *

bot = commands.Bot(command_prefix="!")

mpath = f"{os.getcwd()}/extensions"
print([bot.load_extension(f"extensions.{os.path.splitext(f)[0]}") for f in os.listdir(mpath) if os.path.isfile(os.path.join(mpath, f))])

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

try:
    bot.run(args.token, bot=True, reconnect=True)
except Exception as e:
    logger.critical(f"Could not initialise bot. {e}")
