import sys
sys.path.append("..")
import utils
from discord.ext import commands

localise = utils.localisation.localise
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
            ctx.send(localise("MODERATION_PRUNE_FAIL_INT", amount=amount))
            return

        deletable = []
        async for message in ctx.channel.history(limit=amount):
            deletable.append(message)

        m = await ctx.send(localise("MODERATION_PRUNE_DELETING", amount=amount))

        for message in deletable:
            await message.delete()

        await m.edit(content=localise("MODERATION_PRUNE_DELETED", amount=amount), delete_after=5)

def setup(bot):
    bot.add_cog(moderation(bot))
