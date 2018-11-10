import discord
import sys
sys.path.append("..")
import utils
from discord.ext import commands
import os
import asyncio

empty = u'\u200b'

"""
        try:
            r = utils.api.lookup(ctx.author.id)
            await temp.edit(content="<:xmark:495282541347995667> **|** Your account is already linked!")
        except utils.api.NoAccountException:
            pass
"""
localise = utils.localisation.localise
class web_accounts:
    def __init__(self, bot):
        self.bot = bot
        self.name = "Accounts"

    @commands.command(pass_context=True)
    async def link(self,ctx):
        """Begins account linking process.

        [p]**link**: Will take you through the steps to link your account to our servers."""
        temp = await ctx.send(localise("ACCOUNT_LINK_LOADING"))
        try:
            r = utils.api.lookup(ctx.author.id)
            await temp.edit(content=localise("ACCOUNT_LINK_ALREADY_LINKED"))
            return
        except utils.api.NoAccountException:
            pass

        await temp.edit(content=localise("ACCOUNT_LINK_TUTORIAL"))

        for i in range(5):
            print(i)
            try:
                r = utils.api.lookup(ctx.author.id)
                break
            except utils.api.NoAccountException:
                r = False
            await asyncio.sleep(10)
        if r != False:
            await temp.edit(content=localise("ACCOUNT_LINK_SUCCESS"))
        else:
            await temp.edit(content=localise("ACCOUNT_LINK_TIMEOUT"))

    @commands.command(pass_context=True)
    async def account(self,ctx):
        """Shows your account

        [p]**account**: Will show how many ZC you have and your purchased items."""
        try:
            r = utils.api.lookup(ctx.author.id)
        except utils.api.NoAccountException:
            await ctx.send(localise("ACCOUNT_LOOKUP_NO_ACCOUNT"))

        if r.items != None:
            items = "\n".join([item["name"] for item in r.items])
        else:
            items = localise("ACCOUNT_LOOKUP_ITEMS_NONE")
        zc = round(r.zc, 2)

        await ctx.send(localise("ACCOUNT_LOOKUP_OUTPUT", zc=zc, items=items))

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def setup(self,ctx):
        """Sets up the notice for !link

        [p]**setup**: Will build the embed on the command."""
        temp = await ctx.send(localise("ACCOUNT_SETUP_LOADING"))


        embed = discord.Embed(title=localise("ACCOUNT_SETUP_DEBUG_TITLE"), colour=ctx.me.color, description=localise("ACCOUNT_SETUP_DEBUG_DESCRIPTION"))

        embed.set_author(name="ZoltBot", icon_url=self.bot.user.avatar_url_as(format='png'))

        embed.add_field(name=localise("ACCOUNT_SETUP_DEBUG_PRIVACY_TITLE"), value=localise("ACCOUNT_SETUP_DEBUG_PRIVACY_DESC"))
        embed.add_field(name=localise("ACCOUNT_SETUP_DEBUG_RULES_TITLE"), value=localise("ACCOUNT_SETUP_DEBUG_RULES_DESC"))
        embed.add_field(name=f"\n{empty}", value=localise("ACCOUNT_SETUP_DEBUG_CONF"))

        await temp.edit(content="",embed=embed)

def setup(bot):
    bot.add_cog(web_accounts(bot))
