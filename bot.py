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

async def main():
    async with bot:
        await load()
        await bot.start("MTEwMDAyNjU3MDA2MTY1MTk4OA.GugS6_.OHQe1OpMsvZr2PjKrZj7knK8At5hSLY56pJ5f8")

asyncio.run(main())