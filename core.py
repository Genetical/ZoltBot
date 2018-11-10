import argparse
from discord.ext import commands
import os
global DEBUG

os.environ["DEBUG"] = "False" # Would be actual bool but environment vars cant be

## Enforce parsing of token argument
parser = argparse.ArgumentParser()
parser.add_argument("token", help="Must be a valid discord bot token")
parser.add_argument("client_key", help="The api client key for zolts.ga")
args = parser.parse_args()


## Load extensions
import utils

utils.api.client_key = args.client_key


bot = commands.Bot(command_prefix="!")

#Rip readability, this lists all file names in the extensions folder, removes
# the ".*" extension and prefixes with "extensions." it then imports the extension. P.S Che did something annoying
[bot.load_extension(f"extensions.{os.path.splitext(f)[0]}") for f in os.listdir(f"{os.getcwd()}/extensions") if os.path.isfile(os.path.join(f"{os.getcwd()}/extensions", f))]

if os.environ["DEBUG"] == "True":
    bot.unload_extension("extensions.statistics")
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
    print(f"Could not initialise bot. {e}")
