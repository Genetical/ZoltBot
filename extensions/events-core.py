import discord, asyncio, sys
sys.path.append("..")
import utils
from discord.ext import commands
import os
from profanityfilter import ProfanityFilter
pf = ProfanityFilter()

class events_core:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        # Handle points gained for sending messages
        ## Cache last message from user to stop spam
        ## Cooldown of 30 seconds
        ## Add credits
        self.bot.process_commands(message)

    async def on_member_join(self, member):
        log.info(f"Member: '{member.display_name}' has joined the channel.")
        if pf.is_clean(member.name):
            member.send("Your username has profanity in it and for that reason, you have been kicked, please change your name and rejoin")
            member.kick(reason="Profanity in username")
            log.info(f"User {pf.censor(member.name)} was kicked for profanity.")


def setup(bot):
    bot.add_cog(events_core(bot))
