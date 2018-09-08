import discord, asyncio, sys
sys.path.append("..")
import utils
from discord.ext import commands
import os

class web_accounts:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def bank_account(self,ctx):
        r = utils.api.lookup(ctx.author.id)
        if r.items != None:
            items = "\n        ".join(r.items)
        else:
            items = "*No items owned*"

        ctx.send(f"You have {round(r.zc, 2)} ZoltCoins and own the following items:\n        {items}")

def setup(bot):
    bot.add_cog(web_accounts(bot))
