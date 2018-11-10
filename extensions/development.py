import sys
sys.path.append("..")
import utils
from discord.ext import commands
import os
import discord
import asyncio

# Just a template, use for when adding extensions.
from datetime import datetime, timedelta
os.environ['TZ'] = 'Europe/London'

now = datetime.now()
(timedelta(hours=24) - (now - now.replace(hour=6, minute=30, second=0, microsecond=0))).total_seconds() % (24 * 3600)

empty = u'\u200b'

async def is_owner(ctx):
    return ctx.author.id in (173494216263991296, 303953507889840129)

async def localise_perm(ctx):
    check = False
    for role in ctx.author.roles:
        if role.permissions.manage_guild:
            check = True
            break
    check = is_owner(ctx)
    return check

localise = utils.localisation.localise
class development:
    def __init__(self, bot):
        self.bot = bot
        self.name = "Development"

    @commands.command(pass_context=True)
    @commands.check(is_owner)
    async def reload(self,ctx):
        """Reloads the bot

        [p]**reload**: Restarts the bot with the most updated push."""

        await ctx.send("Reloading! This may take up to 30 seconds.")
        asyncio.sleep(5)
        os.system("printf '\n\n' & sleep 5s && git pull && ./run.sh")
        quit()

    @commands.command(pass_context=True)
    @commands.check(localise_perm)
    async def localise(self, ctx, operation, key=None, value=None):
        """Edits or views localisation data

        [p]**localise** update [key] [value]: Updates the specific localisation string
        [p]**localise** read [key]: Will give the stored localisation string for that key
        [p]**localise** list: Will give a list of all localisation
        [p]**localise** reset: Will reset localisation to default
        """
        if operation == "update":
            temp = await ctx.send(f"<a:loading:495280632067522600> **|** Loading...Finding key {key}")
            old_value = utils.localisation.read(key)

            if value == None:
                await temp.edit(content=f"<:xmark:495282541347995667> **|** Key {key} doesn't exist")
                return
            await temp.edit(content=f"<a:loading:495280632067522600> **|** Current value for key {key}:\n{old_value}\n\n This is changing to:\n{value}")

            value = utils.localisation.write(key, value)

            await temp.edit(content=f"<:check:495282532968038430> **|** {key} set to {value}")


        elif operation == "read":
            temp = await ctx.send(f"<a:loading:495280632067522600> **|** Loading...Finding key {key}")


            old_value = utils.localisation.read(key)


            if old_value == None:
                await temp.edit(content=f"<:xmark:495282541347995667> **|** Key {key} doesn't exist")
                return

            try:
                meta = utils.localisation.meta[key]
            except KeyError:
                meta = []

            clean_meta = '\n'.join(meta)
            clean_value = old_value.replace("`","'")
            await temp.edit(content=f"Key: `{key}` has value:\n```{clean_value}```\n This local string has {len(meta)} variable(s) attached:\n{clean_meta}")

        elif operation == "reset":
            temp = await ctx.send(f"<a:loading:495280632067522600> **|** Resetting localisation")
            utils.localisation.reset()
            await temp.edit(content=f"<:check:495282532968038430> **|** Localisation reset")

        elif operation == "list":
            temp = await ctx.send(f"<a:loading:495280632067522600> **|** Fetching localisation")
            embed = discord.Embed(title="Localisation list", colour=ctx.me.colour)

            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url_as(format='png'))

            for key, value in utils.localisation.read().items():
                clean_value = value.replace('`','\'')
                embed.add_field(name=key, value=f"```{clean_value}```", inline=False)
                embed.add_field(name=empty, value=empty, inline=False)

            await temp.edit(content="", embed=embed)

        else:
            await ctx.send(f"<:xmark:495282541347995667> **|** Operation {operation} doesn't exist, see !help localise")



def setup(bot):
    bot.add_cog(development(bot))
