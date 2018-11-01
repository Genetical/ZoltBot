import discord
import sys
sys.path.append("..")
import utils
from discord.ext import commands
import os
import asyncio
import time
import psutil


class statistics:

    def __init__(self, bot):
        self.bot = bot
        self.command_counter = 0
        self.message_counter = 0
        self.pid = os.getpid()
        self.py = psutil.Process(self.pid)

    async def stats(self, start_time):
        await asyncio.sleep(5)
        while True:
            utils.terminal.clear()
            print(f"Time since execution: {round(time.time() - start_time, 0)} seconds")
            print(f"Messages caught since executed: {self.message_counter}")
            print(f"Commands ran since execution: {self.command_counter}",end="\n\n")
            print("=" * 50)
            print(f"Memory usage: {round(self.py.memory_info()[0]/2.**30, 2)} GB")
            print(f"CPU Usage: {psutil.cpu_percent()}%")

            await asyncio.sleep(1)

    async def on_ready(self):
        self.bot.loop.create_task(self.stats(time.time()))


    async def on_message(self, message):
        self.message_counter += 1

    async def on_command(self, message):
        self.command_counter += 1

def setup(bot):
    bot.add_cog(statistics(bot))
