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
    return ctx.author.id == 173494216263991296

class development:
    def __init__(self, bot):
        self.bot = bot
        self.name = "Development"

    @commands.command(pass_context=True)
    @commands.check(is_owner)
    async def reload(self,ctx):
        """Reloads the bot

        [p]**reload**: Restarts the bot with the most updated push."""
        ctx.send("Reloading! This may take up to 30 seconds.")
        os.system("printf '\n\n' & sleep 5s && git pull && ./run.sh")
        quit()

"""
    @commands.command(pass_context=True)
    @commands.check(is_owner)
    async def countdown(self,ctx):
        msg = await ctx.send("Loading")
        count = 24
        while count >= 0 and count < 43200:
            now = datetime.now()
            count = int((timedelta(hours=24) - (now - now.replace(hour=21, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600))
            message = f"**BETA Launch Time**\nPlanned BETA time: 21:00-01:00 GMT\n\n**Countdown to launch**\n*{utils.timeframe.seconds(count)}*"
            await msg.edit(content=message)
            await asyncio.sleep(1)

        await msg.delete()
        await ctx.send("<@&466222227449184256>\n\nThe BETA has begun!")"""

def setup(bot):
    bot.add_cog(development(bot))
