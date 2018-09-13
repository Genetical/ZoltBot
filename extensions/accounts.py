import discord, asyncio, sys
sys.path.append("..")
import utils
from discord.ext import commands
import os

class web_accounts:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def account(self,ctx):
        r = utils.api.lookup(ctx.author.id)
        r.items = ["test item 1", "test item 2", "test item 3"]
        if r.items != None:
            items = "\n".join(r.items)
        else:
            items = "*No items owned*"

        await ctx.send(f":credit_card: **You have *{round(r.zc, 2)}* ZoltCoins and own the following items:**```\n{items}```")

def setup(bot):
    bot.add_cog(web_accounts(bot))