import sys
sys.path.append("..")
import utils
import asyncio
import time
from discord.ext import commands

async def is_owner(ctx):
    return ctx.author.id == 173494216263991296

class statistics:

    def __init__(self, bot):
        self.bot = bot
        self.command_counter = 0
        self.message_counter = 0
        self.command_errors = 0
        self.last_error = "No errors so far!"

    async def stats(self, start_time):
        await asyncio.sleep(5)
        self.start_time = start_time
        while True:
            utils.terminal.clear()
            uptime = utils.timeframe.seconds(int(time.time() - start_time))
            messages = self.message_counter
            print(f"Time since execution: {uptime}")
            print(f"\nMessages caught since executed: {self.message_counter}")
            print(f"Commands ran since execution: {self.command_counter}",end="\n\n")
            print(f"There have been {self.command_errors} errors since launch, last error:\n\n{self.last_error}\n\n\n")
            print(f"Type in any server, '!reload' to restart and update the bot to the latest version")

            await asyncio.sleep(1)

    async def on_ready(self):
        self.bot.loop.create_task(self.stats(time.time()))


    async def on_message(self, message):
        self.message_counter += 1

    async def on_command(self, ctx):
        self.command_counter += 1

    async def on_command_error(self, ctx, error):
        self.command_errors += 1
        self.last_error = f"Command: {ctx.command}\nMessage:{ctx.args}\nError:{error}"

    @commands.command(pass_context=True, name='stats')
    @commands.check(is_owner)
    async def statistics(self, ctx):
        a = (f"**Time since execution:** *{utils.timeframe.seconds(int(time.time() - self.start_time))}*")
        a += (f"\n**Messages caught since executed:** {self.message_counter}")
        a += (f"\n**Commands ran since execution:** {self.command_counter}\n")
        a += (f"\nThere have been *{self.command_errors}* errors since launch, last error:\n```{self.last_error}```")
        await ctx.send(a)


def setup(bot):
    bot.add_cog(statistics(bot))
