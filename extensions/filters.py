import discord
import sys
sys.path.append("..")
import utils
import re

localise = utils.localisation.localise
class filters:
    def __init__(self, bot):
        self.bot = bot
        self.name = "Filters"

    async def on_member_join(self, member):
        invites = re.findall("discord.gg/([^\s]+)", member.display_name)
        if invites:
            for invite in invites:
                try:
                    invite = await self.bot.get_invite(invite)
                    if invite.guild != member.guild:
                        await member.send(localise = utils.localisation.localise("FILTERS_JOIN_INVITE_LINK"))
                        await member.kick(reason="Invite link in name")
                except discord.NotFound:
                    pass


    async def on_message(self, message):
        invites = re.findall("discord.gg/([^\s]+)", message.content)
        if invites:
            for invite in invites:
                try:
                    invite = await self.bot.get_invite(invite)
                    if invite.guild != message.guild:
                        mention = message.author.mention
                        await message.channel.send(utils.localisation.localise("FILTERS_MESSAGE_INVITE_LINK", mention=mention), delete_after=7)
                        await message.delete()
                except discord.NotFound:
                    pass


def setup(bot):
    bot.add_cog(filters(bot))
