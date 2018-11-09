import sys
sys.path.append("..")
import utils
from discord.ext import commands
import os
import discord
import asyncio

# Just a template, use for when adding extensions.
from datetime import datetime, timedelta
os.environ['TZ'] = 'Europe/London'

now = datetime.now()
(timedelta(hours=24) - (now - now.replace(hour=6, minute=30, second=0, microsecond=0))).total_seconds() % (24 * 3600)


async def is_owner(ctx):
    return ctx.author.id in (173494216263991296, 303953507889840129)

class development:
    def __init__(self, bot):
        self.bot = bot
        self.name = "Development"

    @commands.command(pass_context=True)
    @commands.check(is_owner)
    async def reload(self,ctx):
        """Reloads the bot

        [p]**reload**: Restarts the bot with the most updated push."""

        await ctx.send("Reloading! This may take up to 30 seconds.")
        asyncio.sleep(5)
        os.system("printf '\n\n' & sleep 5s && git pull && ./run.sh")
        quit()

def setup(bot):
    bot.add_cog(development(bot))
