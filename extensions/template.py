import sys
sys.path.append("..")
from discord.ext import commands

# Just a template, use for when adding extensions.

class template:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def ping(self,ctx):
        pass

def setup(bot):
    bot.add_cog(template(bot))
