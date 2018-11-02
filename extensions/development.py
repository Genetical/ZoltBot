import sys
sys.path.append("..")
from discord.ext import commands
import os

# Just a template, use for when adding extensions.

async def is_owner(ctx):
    return ctx.author.id == 173494216263991296

class development:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.check(is_owner)
    async def reload(self,ctx):
        os.system("sleep 5s && git pull && sleep 10s && ./run.sh")
        quit()

def setup(bot):
    bot.add_cog(development(bot))
