import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import asyncio



bot = commands.Bot(command_prefix="*", intents=discord.Intents.all())
bot_status = cycle(["Genshin Impact", "Star Rail", "Honkai 3rd"])


@tasks.loop(seconds=5)
async def change_status():
    """轉換機器人遊戲狀態"""
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
            print(f"cogs.{filename[:-3]} is already")


@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"RELOAD cogs.{extension} DONE")


class Myselect2(discord.ui.Select):
    def __init__(self):
        options2 = [
            discord.SelectOption(label="天賦", value="天賦", description="提供各個星球的介紹"),
            discord.SelectOption(
                label="稀有度", value="稀有度", description="提供各角色的天賦,稀有度,職業介紹"
            ),
            discord.SelectOption(label="職業介紹", value="職業", description="提供武器故事及卡面資料"),
        ]
        super().__init__(placeholder="", min_values=1, max_values=1, options=options2)

    async def callback(
        self,
        interaction: discord.Interaction,
    ):
        pass


class Myselect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="世界", value="世界", description="提供各個星球的介紹"),
            discord.SelectOption(
                label="角色", value="角色", description="提供各角色的天賦,稀有度,職業介紹"
            ),
            discord.SelectOption(label="光錐(武器)", value="光錐", description="提供武器故事及卡面資料"),
        ]
        super().__init__(
            placeholder="請選擇要查詢的類別", min_values=1, max_values=1, options=options
        )

    async def callback(
        self,
        interaction: discord.Interaction,
    ):
        if "角色" in interaction.data["values"]:
            await interaction.response.send_message(view=Myselect2())
            await interaction.response.send_message(
                f"Your favourite colour is {self.values[0]}"
            )


class menuview(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180):
        super().__init__(timeout=timeout)
        self.add_item(Myselect())


@bot.command()
async def menu(ctx):
    view = menuview()
    await ctx.send(view=view)


async def main():
    async with bot:
        await load()
        await bot.start(
            "MTEwMDAyNjU3MDA2MTY1MTk4OA.GugS6_.OHQe1OpMsvZr2PjKrZj7knK8At5hSLY56pJ5f8"
        )


asyncio.run(main())
