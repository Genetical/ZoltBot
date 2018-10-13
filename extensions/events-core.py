import discord
import sys
sys.path.append("..")
import utils
from discord.ext import commands
import os
from profanityfilter import ProfanityFilter
pf = ProfanityFilter()

class events_core:
    def __init__(self, bot):
        self.bot = bot


    async def on_member_join(self, member):
        if not pf.is_clean(member.name):
            await member.send("Your username has profanity in it and for that reason, you have been kicked, please change your name and rejoin")
            await member.kick(reason="Profanity in username")
            log.info(f"User {pf.censor(member.name)} was kicked for profanity.")


def setup(bot):
    bot.add_cog(events_core(bot))
