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

class web_accounts:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def link(self,ctx):
        temp = await ctx.send(f"<a:loading:495280632067522600> **|** Loading...")
        try:
            r = utils.api.lookup(ctx.author.id)
            await temp.edit(content="<:xmark:495282541347995667> **|** Your account is already linked!")
            return
        except utils.api.NoAccountException:
            pass

        await temp.edit(content="<:wait:500630336657555466> **|** Go to: https://www.zolts.ga/accounts/login/ and log in with your discord account. I should detect when you have connected your account.")

        for i in range(5):
            print(i)
            try:
                r = utils.api.lookup(ctx.author.id)
                break
            except utils.api.NoAccountException:
                r = False
            await asyncio.sleep(10)
        if r != False:
            await temp.edit(content="<:done:500630347890032640> **|** Congratulations! Your account is successfully linked. Type `!account` to view your account.")
        else:
            await temp.edit(content="<:fail:500632092942532628> **|** Looks like you didn't link your account in time, you can try again or contact an Admin.")

    @commands.command(pass_context=True)
    async def account(self,ctx):
        try:
            r = utils.api.lookup(ctx.author.id)
        except utils.api.NoAccountException:
            await ctx.send(f"<:xmark:495282541347995667> **|** Looks like you don't have an account, type `!link` to connect your account.")

        if r.items != None:
            items = "\n".join([item["name"] for item in r.items])
        else:
            items = "*No items owned*"

        await ctx.send(f":credit_card: ** | You have *{round(r.zc, 2)}* ZoltCoins and own the following items:**```\n{items}```")

    @commands.command(pass_context=True)
    async def setup(self,ctx):
        temp = await ctx.send(f"<a:loading:495280632067522600> **|** Generating embed")


        embed = discord.Embed(title="Account Registration", colour=ctx.me.color, description="\nTo fully access all the functionality of this server, you must agree with the below rules and privacy policy:")

        embed.set_author(name="ZoltBot", icon_url=self.bot.user.avatar_url_as(format='png'))

        embed.add_field(name="__Privacy__", value="Your discord account ID, which is already public information, will be stored on our server along with your email address. We store your email to prevent multiple accounts from being created by the same person. Your email will never be used and is only to link to an account.")
        embed.add_field(name="\n__Rules__", value="**1 )** Only one account per user\n**2)** Use of any exploit to gain currency or any other item will lead to removal of all your items\n**3) ** Moderating outside of your jurisdiction will lead to the bannding of the respective sub-community")
        embed.add_field(name=f"\n{empty}", value="*If you agree to the above conditions, type `!link`*")

        await temp.edit(content="",embed=embed)

def setup(bot):
    bot.add_cog(web_accounts(bot))
