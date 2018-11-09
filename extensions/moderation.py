import sys
sys.path.append("..")
from discord.ext import commands


class moderation:
    def __init__(self, bot):
        self.bot = bot
        self.name = "Moderation"

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def prune(self, ctx, amount: int):
        """Prunes an amount of messages.

        [p]**prune** amount: Deletes an amount of messages from latest to earliest.
        """
        if type(amount) != int:
            ctx.send(f"<:xmark:495282541347995667> **|** {amount} isn't a number!")
            return

        deletable = []
        async for message in ctx.channel.history(limit=amount):
            deletable.append(message)

        m = await ctx.send(f"<a:loading:495280632067522600> **|** Deleting {amount} message{'s' if amount != 1 else ''}")

        for message in deletable:
            await message.delete()

        await m.edit(content="<:done:500630347890032640> **|** Messages deleted!", delete_after=5)

def setup(bot):
    bot.add_cog(moderation(bot))
