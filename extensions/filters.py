import discord
import sys
sys.path.append("..")
import re


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
                        await member.send(f"```prolog\nYOU WERE KICKED FOR HAVING AN INVITE LINK ON YOUR NAME\nPLEASE CHANGE YOUR NAME AND REJOIN```")
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
                        await message.channel.send(f"**{message.author.mention}**```prolog\nMESSAGE DELETED FOR CONTAINING AN INVITE TO A DIFFERENT SERVER```", delete_after=7)
                        await message.delete()
                except discord.NotFound:
                    pass


def setup(bot):
    bot.add_cog(filters(bot))
