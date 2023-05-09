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


class characterinfo(discord.ui.Select):
    def __init__(self):
        options2 = [
            discord.SelectOption(label="天賦", value="天賦", description="提供各個星球的介紹"),
            discord.SelectOption(
                label="稀有度", value="稀有度", description="提供各角色的天賦,稀有度,職業介紹"
            ),
            discord.SelectOption(label="職業介紹", value="職業", description="提供武器故事及卡面資料"),
        ]
        super().__init__(placeholder="請選擇想查詢的角色資料", min_values=1, max_values=1, options=options2)

    async def callback(
        self,
        interaction: discord.Interaction,
    ):
        pass
class characterlist(discord.ui.Select):
    def __init__(self):
        options2 = [
            discord.SelectOption(label="三月七", value="三月七", description=""),
            discord.SelectOption(label="丹恆", value="丹恆", description=""),
            discord.SelectOption(label="主角", value="主角", description=""),
        ]
        super().__init__(placeholder="請選擇想查詢的角色資料", min_values=1, max_values=1, options=options2)

    async def callback(
        self,
        interaction: discord.Interaction,
    ):
        pass
class world(discord.ui.Select):
    def __init__(self):
        options2 = [
            discord.SelectOption(label="太空站", value="太空站", description=""),
            discord.SelectOption(label="貝洛柏格", value="貝洛柏格", description=""),
            discord.SelectOption(label="仙舟", value="仙舟", description=""),
        ]
        super().__init__(placeholder="請選擇想查詢的世界資料", min_values=1, max_values=1, options=options2)

    async def callback(
        self,
        interaction: discord.Interaction,
    ):
        pass
class weapon(discord.ui.Select):
    def __init__(self):
        options2 = [
            discord.SelectOption(label="早餐的儀式感", value="早餐的儀式感", description=""),
            discord.SelectOption(label="舞舞舞", value="舞舞舞", description=""),
            discord.SelectOption(label="論劍", value="論劍", description=""),
        ]
        super().__init__(placeholder="請選擇要查詢的光錐資料", min_values=1, max_values=1, options=options2)

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
            await interaction.response.send_message(view=weapon())
            await interaction.response.send_message(
                f"Your favourite colour is {self.values[0]}"
            )
class menuview(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180):
        super().__init__(timeout=timeout)
        self.add_item(Myselect())
class search_category(discord.ui.View):
    @discord.ui.select(
        placeholder="請選擇要查詢的類別",
        min_values=1, 
        max_values=1, 
        options = [
            discord.SelectOption(label="世界", value="世界", description="提供各個星球的介紹"),
            discord.SelectOption(label="角色", value="角色", description="提供各角色的天賦,稀有度,職業介紹"),
            discord.SelectOption(label="光錐(武器)", value="光錐", description="提供武器故事及卡面資料"),
        ]
        )
    async def select_callback(self,interaction:discord.Interaction,select):
        if select.values[0] == '世界':
            select.disabled = True
            self.add_item(world())
            await interaction.message.edit(view=self)
            await interaction.response.defer()
        elif select.values[0] == '角色':
            select.disabled = True
            self.add_item(characterlist())
            await interaction.message.edit(view=self)
            await interaction.response.defer()
        elif select.values[0] == '光錐':
            select.disabled = True
            self.add_item(weapon())
            await interaction.message.edit(view=self)
            await interaction.response.defer()


@bot.command()
async def menu(ctx):
    view = menuview()
    await ctx.send(view=view)

@bot.command()
async def search(ctx):
    view = search_category()
    await ctx.send(view=view)

async def main():
    async with bot:
        await load()
        await bot.start(
            "MTEwMDAyNjU3MDA2MTY1MTk4OA.GugS6_.OHQe1OpMsvZr2PjKrZj7knK8At5hSLY56pJ5f8"
        )


asyncio.run(main())
