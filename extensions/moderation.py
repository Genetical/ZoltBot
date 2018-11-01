import sys
sys.path.append("..")
from discord.ext import commands


class moderation:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def prune(self,ctx,amount):
        async for message in ctx.channel.history(amount):
            await message.delete()

def setup(bot):
    bot.add_cog(moderation(bot))