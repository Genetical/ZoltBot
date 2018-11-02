import discord
import sys
sys.path.append("..")
import utils
from discord.ext import commands
import os

# Just a template, use for when adding extensions.

class community:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def create_community(self, ctx, name):
        return
        overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
        ctx.author: discord.PermissionOverwrite(read_messages=True, manage_channels=True)
        }
        category = await ctx.guild.create_category(name, overwrites=overwrites)

def setup(bot):
    bot.add_cog(community(bot))
