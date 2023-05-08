from typing import Optional
import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import asyncio


bot = commands.Bot(command_prefix='*', intents=discord.Intents.all())


bot_status = cycle(["Status 1", "Status 2", "Status 3"])


@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(bot_status)))


@bot.event
async def on_ready():
    print("Bot is Online!")
    while True:
        await change_status()
        await asyncio.sleep(10)


async def load():
    for filename in os.listdir("DB-Project-Bot\cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
    


@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'RELOAD cogs.{extension} DONE')


class Myselect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="red", value="1", description="this is red"),
            discord.SelectOption(label="green", value="2",description="this is green"),
            discord.SelectOption(label="blue", value="3",description="this is blue")
        ]
        super().__init__(placeholder='Choose your favourite character',
                         min_values=1, max_values=1, options=options)
    async def callback(self, interaction: discord.Interaction):
        if '1' in interaction.data['values']:
            await interaction.response.send_message("hi")
        if '2' in interaction.data["values"]:
            await interaction.response.send_message(f'Your favourite colour is {self.values[0]}')
class menuview(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Myselect())

@bot.command()
async def menu(ctx):
    view = menuview()
    await ctx.send("hi", view=view)


async def main():
    async with bot:
        await load()
        await bot.start("MTEwMDAyNjU3MDA2MTY1MTk4OA.GugS6_.OHQe1OpMsvZr2PjKrZj7knK8At5hSLY56pJ5f8")

asyncio.run(main())
