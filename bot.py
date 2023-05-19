import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import asyncio
from discord import embeds

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



class search_danhen_info(discord.ui.Select):
    def __init__(self):
        options2 = [
            discord.SelectOption(label="基本資料", value="基本資料", description=""),
            discord.SelectOption(label="行跡", value="行跡", description=""),
            discord.SelectOption(label="星魂", value="星魂", description=""),
        ]
        super().__init__(placeholder="請選擇想查詢的資料", min_values=1, max_values=1, options=options2)

    async def callback(
        self,
        interaction: discord.Interaction,
    ):
        print(characterlist.option_value)
        if  self.values[0] == '基本資料':
            print("丹恆的基本資料")
        elif  self.values[0] == '行跡':
            print("丹恆的行跡")
        elif  self.values[0] == '星魂':
            print("丹恆的星魂")
class search_jfy_info(discord.ui.Select):
    def __init__(self):
        options2 = [
            discord.SelectOption(label="基本資料", value="基本資料", description=""),
            discord.SelectOption(label="行跡", value="行跡", description=""),
            discord.SelectOption(label="星魂", value="星魂", description=""),
        ]
        super().__init__(placeholder="請選擇想查詢的資料", min_values=1, max_values=1, options=options2)

    async def callback(
        self,
        interaction: discord.Interaction,
    ):
        print(characterlist.option_value)
        if  self.values[0] == '基本資料':
            print("主角的基本資料")
        elif  self.values[0] == '行跡':
            print("主角的行跡")
        elif  self.values[0] == '星魂':
            print("主角的星魂")
class search_marchseven_info(discord.ui.Select):
    def __init__(self):
        options2 = [
            discord.SelectOption(label="基本資料", value="基本資料", description=""),
            discord.SelectOption(label="行跡", value="行跡", description=""),
            discord.SelectOption(label="星魂", value="星魂", description=""),
        ]
        super().__init__(placeholder="請選擇想查詢的資料", min_values=1, max_values=1, options=options2)

    async def callback(
        self,
        interaction: discord.Interaction,
    ):
        print(characterlist.option_value)
        if  self.values[0] == '基本資料':
            march7_info_embed = discord.Embed(title= "三月七",
                                              description="一度沉睡於恆冰，對過去一無所知的少女。為了尋找身世的真相，選擇與銀河列車同行。目前為自己準備了約六十七種「身世故事」。",
                                              color=0x3498DB,
                                              url="https://wiki.hoyolab.com/pc/hsr/entry/7")
            march7_info_embed.set_thumbnail(url="https://wiki.hoyolab.com/_ipx/f_webp/https://upload-static.hoyoverse.com/hoyowiki/2023/02/21/0047e5284a840424de8b21d1ccd042cd_933159568797000001.png")
            """ march7_info_embed.set_image(url="https://wiki.hoyolab.com/_ipx/f_webp/https://upload-static.hoyoverse.com/hoyowiki/2023/02/21/1721c5c450299615748e2fa4971e2746_2999314882560891227.png") """
            march7_info_embed.add_field(name="基本資料",
                                        value="陣營:無名客\n所屬:星穹列車",
                                        inline=True)
            march7_info_embed.add_field(name="戰鬥資料",
                                        value="命途:存護\n稀有度:★5\n屬性:冰",
                                        inline=True) 
            march7_info_embed.add_field(name="聲優",
                                        value="華語CV:諾亞\n日語CV:小倉唯\n英語CV:Skyler Davenport\n韓語CV:정혜원",
                                        inline=False)
            march7_info_embed.set_image(url="https://upload-static.hoyoverse.com/hoyolab-wiki/2023/03/20/125413385/f638dbaf3994bbac67972792e450a362_4599282032612966860.gif")
            await interaction.message.edit(embed=march7_info_embed)
            await interaction.response.defer()
        elif  self.values[0] == '行跡':
            print("三月七的行跡")
        elif  self.values[0] == '星魂':
            print("三月七的星魂")
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
class characterlist(discord.ui.View):
    option_value =""
    @discord.ui.select(
        placeholder="請選擇要查詢的類別",
        min_values=1, 
        max_values=1,
        options = [
            discord.SelectOption(label="三月七", value="三月七", description=""),
            discord.SelectOption(label="丹恆", value="丹恆", description=""),
            discord.SelectOption(label="主角", value="主角", description=""),
        ]
        )
    async def callback(self,interaction:discord.Interaction,select):
        if select.values[0] == '三月七':
            select.disabled = True
            await interaction.response.defer()
            self.add_item(search_marchseven_info())
            await interaction.message.edit(view=self)
        elif select.values[0] == '丹恆':
            select.disabled = True
            await interaction.response.defer()
            self.add_item(search_danhen_info())
            await interaction.message.edit(view=self)
        elif select.values[0] == '主角':
            select.disable = True
            await interaction.response.defer()
            self.add_item(search_jfy_info())
            await interaction.message.edit(view=self)
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
            await interaction.response.send_message(view=characterlist())
            await interaction.response.defer()
        elif select.values[0] == '光錐':
            select.disabled = True
            self.add_item(weapon())
            await interaction.message.edit(view=self)
            await interaction.response.defer()


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
