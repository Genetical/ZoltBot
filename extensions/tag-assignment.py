import discord
import sys
sys.path.append("..")
import utils
from discord.ext import commands
import os

# Just a template, use for when adding extensions.

class tag_assignment:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def tag(self, ctx, role: discord.Role):
        temp = await ctx.send(f"<a:loading:495280632067522600> **|** Saving role *{role.name}*")
        if role.permissions.value != 0:
            await temp.edit(content=f"<:xmark:495282541347995667> **|** Failed to add tag *{role.name}*. Only roles with no permissions can be used as tags", delete_after=5)
            ctx.message.delete()
            return

        if utils.persistence.add_tag(role.id):
            await temp.edit(content=f"<:check:495282532968038430> **|** Added tag *{role.name}* successfully", delete_after=5)
            ctx.message.delete()
        else:
            await temp.edit(content=f"<:xmark:495282541347995667> **|** Failed to add tag *{role.name}*. This is probably to do with the database. <@&388020265222668288>")

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def rtag(self, ctx, role: discord.Role):
        temp = await ctx.send(f"<a:loading:495280632067522600> **|** Removing role *{role.name}*")

        if utils.persistence.del_tag(role.id):
            await temp.edit(content=f"<:check:495282532968038430> **|** Removed tag *{role.name}* successfully", delete_after=5)
            ctx.message.delete()
        else:
            await temp.edit(content=f"<:xmark:495282541347995667> **|** Failed to remove tag *{role.name}*. This is probably to do with the database. <@&388020265222668288>")

    @commands.command(pass_context=True)
    async def assign(self, ctx, role: discord.Role):
        temp = await ctx.send(f"<a:loading:495280632067522600> **|** Finding role *{role.name}*")
        if utils.persistence.verify_tag(role.id):
            await ctx.author.add_roles(role)
            await temp.edit(content=f"<:check:495282532968038430> **|** Assigned tag *{role.name}* successfully", delete_after=5)
        else:
            await temp.edit(content=f"<:xmark:495282541347995667> **|** Failed to assign tag *{role.name}*. This may be because you are not authorised to assign this tag.", delete_after=5)
        ctx.message.delete()

    @commands.command(pass_context=True)
    async def unassign(self, ctx, role: discord.Role):
        temp = await ctx.send(f"<a:loading:495280632067522600> **|** Finding role *{role.name}*")
        if utils.persistence.verify_tag(role.id):
            await ctx.author.remove_roles(role)
            await temp.edit(content=f"<:check:495282532968038430> **|** Unassigned tag *{role.name}* successfully", delete_after=5)
        else:
            await temp.edit(content=f"<:xmark:495282541347995667> **|** Failed to Unassign tag *{role.name}*. This may be because you are not authorised to Unassign this tag.", delete_after=5)
        ctx.message.delete()
        
    @commands.command(pass_context=True)
    async def tags(self, ctx):
        temp = await ctx.send(f"<a:loading:495280632067522600> **|** Fetching roles")

        end = []
        tags = utils.persistence.dump_tags()
        if tags != False:
            for role in ctx.guild.roles:
                if str(role.id) in tags:
                    end.append(role.name)

            nl = "\n".join(end)

            await temp.edit(content=f"<:check:495282532968038430> **|** The following roles are authorised as tags:\n```\n{nl}```")
            ctx.message.delete()
        else:
            await temp.edit(content=f"<:xmark:495282541347995667> **|** Error! This is probably to do with the database. <@&388020265222668288>")


def setup(bot):
    bot.add_cog(tag_assignment(bot))
