import discord, asyncio, sys
sys.path.append("..")
import utils
from discord.ext import commands
import os

# Just a template, use for when adding extensions.

class help_command:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", pass_context=True)
    @commands.has_permissions(administrator=True)
    async def help_command(self,ctx):
        pass

def setup(bot):
    bot.add_cog(help_command(bot))
