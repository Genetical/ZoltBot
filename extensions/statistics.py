import sys
sys.path.append("..")
import utils
import asyncio
import time


class statistics:

    def __init__(self, bot):
        self.bot = bot
        self.command_counter = 0
        self.message_counter = 0
        self.command_errors = 0
        self.last_error = "No errors so far!"

    async def stats(self, start_time):
        await asyncio.sleep(5)
        while True:
            utils.terminal.clear()
            print(f"Time since execution: {round(time.time() - start_time, 0)} seconds")
            print(f"Messages caught since executed: {self.message_counter}")
            print(f"Commands ran since execution: {self.command_counter}",end="\n\n")
            print(f"There have been {self.command_errors} errors since launch, last error:\n{self.last_error}")

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

def setup(bot):
    bot.add_cog(statistics(bot))
