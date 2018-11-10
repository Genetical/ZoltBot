import discord
import sys
sys.path.append("..")
import utils
from discord.ext import commands
import os

# Just a template, use for when adding extensions.
localise = utils.localisation.localise

class tag_assignment:
    def __init__(self, bot):
        self.bot = bot
        self.converter = commands.RoleConverter()
        self.name = "Tag assignment"

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def tag(self, ctx, *role):
        """Adds a community tag.

        [p]**tag** role: Assigns a role as a tag.
        """
        argument = " ".join(role)
        role = await self.converter.convert(ctx=ctx, argument=argument)
        name = role.name
        temp = await ctx.send(localise("", name=name))
        if role.permissions.value != 0:
            await temp.edit(content=localise("ASSIGNMENT_TAG_PERM_0", name=name), delete_after=5)
            ctx.message.delete()
            return

        if utils.persistence.add_tag(role.id):
            await temp.edit(content=localise("ASSIGNMENT_TAG_SUCCESS", name=name), delete_after=5)
            ctx.message.delete()
        else:
            await temp.edit(content=localise("ASSIGNMENT_TAG_PERM_FAIL_GENERIC", name=name))

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def rtag(self, ctx, *role):
        """Removes a tag.

        [p]**rtag** tag: Unassigns a role as a tag.
        """
        argument = " ".join(role)
        role = await self.converter.convert(ctx=ctx, argument=argument)
        name = role.name
        temp = await ctx.send(localise("ASSIGNMENT_RTAG_SAVING", name=name))

        if utils.persistence.del_tag(role.id):
            await temp.edit(content=localise("ASSIGNMENT_RTAG_SUCCESS", name=name), delete_after=5)
            ctx.message.delete()
        else:
            await temp.edit(content=localise("ASSIGNMENT_RTAG_FAIL", name=name))

    @commands.command(pass_context=True)
    async def assign(self, ctx, *role):
        """Assigns a tag.

        [p]**assign** tag: Gives you the chosen tag.
        """
        argument = " ".join(role)
        role = await self.converter.convert(ctx=ctx, argument=argument)
        name = role.name
        temp = await ctx.send(localise("ASSIGNMENT_ASSIGN_FINDING", name=name))
        if utils.persistence.verify_tag(role.id):
            await ctx.author.add_roles(role)
            await temp.edit(content=localise("ASSIGNMENT_ASSIGN_SUCCESS", name=name), delete_after=5)
        else:
            await temp.edit(content=localise("ASSIGNMENT_ASSIGN_FAIL", name=name), delete_after=5)
        ctx.message.delete()

    @commands.command(pass_context=True)
    async def unassign(self, ctx, *role):
        """Unssigns a tag.

        [p]**unassign** tag: Removes the chosen tag.
        """
        argument = " ".join(role)
        role = await self.converter.convert(ctx=ctx, argument=argument)
        name = role.name
        temp = await ctx.send(localise("ASSIGNMENT_UNASSIGN_FINDING", name=name))
        if utils.persistence.verify_tag(role.id):
            await ctx.author.remove_roles(role)
            await temp.edit(content=localise("ASSIGNMENT_UNASSIGN_SUCCESS", name=name), delete_after=5)
        else:
            await temp.edit(content=localise("ASSIGNMENT_UNASSIGN_FAIL", name=name), delete_after=5)
        ctx.message.delete()

    @commands.command(pass_context=True)
    async def tags(self, ctx):
        """Lists all tags.

        [p]**list**: Provides a list of all assigned tags.
        """
        temp = await ctx.send(localise("ASSIGNMENT_TAGS_LOADING"))

        end = []
        tags = utils.persistence.dump_tags()
        if tags != False:
            for role in ctx.guild.roles:
                if str(role.id) in tags:
                    end.append(role.name)

            tags = "\n".join(end)

            await temp.edit(content=localise("ASSIGNMENT_TAGS_SUCCESS", tags=tags))
            ctx.message.delete()
        else:
            await temp.edit(content=localise("ASSIGNMENT_TAGS_FAIL"))


def setup(bot):
    bot.add_cog(tag_assignment(bot))
