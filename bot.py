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
            march7_talent_embed = discord.Embed(title= "三月七",
                                              description="",
                                              color=0x3498DB,
                                              )
            march7_talent_embed.add_field(name="普通攻擊:極寒弓矢",
                                          value="對指定敵方單體造成等同於三月七50%攻擊力的冰屬性傷害。",
                                          inline=True
                )
            march7_talent_embed.add_field(name="戰技:可愛即是正義",
                                          value="為指定我方單體施加強度等同於三月七38%防禦力+190護盾,持續3回合。若該目標生命值百分比大於等於30%，則遭到敵方攻擊的機率大幅提高。",
                                          inline=True
                )
            march7_talent_embed.add_field(name="終結技:冰刻箭雨之時",
                                          value="對敵方全體造成等同於三月七90%攻擊力的冰屬性傷害。受到攻擊的敵方目標有50%基礎機率陷入凍結狀態,持續1回合。凍結狀態下,敵方目標不能行動,並且在每回合開始時受到等同於三月七30%攻擊力的冰屬性持續傷害。",
                                          inline=True
                )
            march7_talent_embed.add_field(name="天賦:少女的特權",
                                          value="當持有護盾的我方目標受到敵方目標攻擊後,三月七立即向攻擊者發動反擊,對其造成等同於三月七50%攻擊力的冰屬性傷害,該效果每回合可觸發2次。",
                                          inline=True
                )
            march7_talent_embed.add_field(name="密技:凍人的瞬間",
                                          value="立即攻擊敵人,進入戰鬥後有100%的基礎機率使隨機敵方單體陷入凍結狀態,持續1回合。\n凍結狀態下,敵方目標不能行動,同時每回合開始時受到等同於三月七50%攻擊力的冰屬性附加傷害。",
                                          inline=True
                )
            
            march7_talent_embed.set_image(url="https://upload-static.hoyoverse.com/hoyolab-wiki/2023/03/20/125413385/95b4be2fe86a2b681e53824e5c15e196_1074394868228546975.gif")
            await interaction.message.edit(embed=march7_talent_embed)
            await interaction.response.defer()
        elif  self.values[0] == '星魂':
            march7_star_embed = discord.Embed(title= "三月七",
                                              description="",
                                              color=0x3498DB,
                                              )
            march7_star_embed.add_field(name="星魂一:記憶中的你",
                                          value="終結技每凍結1個目標，為三月七恢復6點能量。",
                                          inline=False
                )
            march7_star_embed.add_field(name="星魂二",
                                          value="進入戰鬥時，為生命值百分比最低的我方目標提供強度等同於三月七24%防禦力+320的護盾，持續3回合。",
                                          inline=False
                )
            march7_star_embed.add_field(name="星魂三",
                                          value="終結技等級+2，最多不超過15級；普通攻擊等級+1，最多不超過10級。",
                                          inline=False
                )
            march7_star_embed.add_field(name="星魂四",
                                          value="天賦的反擊效果每回合可觸發的次數增加1次。使反擊造成的傷害值提高，提高數值等同於三月七防禦力的30%。",
                                          inline=False
                )
            march7_star_embed.add_field(name="星魂五",
                                          value="戰技等級+2，最多不超過15級；天賦等級+2，最多不超過15級。",
                                          inline=False
                )
            march7_star_embed.add_field(name="星魂六",
                                          value="在戰技提供的護盾保護下的我方目標，每回合開始時回復等同於各自4%生命上限+106的生命值。",
                                          inline=False
                )
            
            march7_star_embed.set_image(url="https://wiki.hoyolab.com/_ipx/f_webp/https://upload-static.hoyoverse.com/hoyolab-wiki/2023/04/28/125413385/db3a53277b7f8001542acae757e7ed58_4234173604942154140.png")
            await interaction.message.edit(embed=march7_star_embed)
            await interaction.response.defer()
            
class artifact(discord.ui.Select):
    def __init__(self):
        options2 = [
            discord.SelectOption(label="熔岩鍛鑄的火匠", value="火套", description=""),
            discord.SelectOption(label="盜匪荒漠的廢土客", value="廢土套", description=""),
            discord.SelectOption(label="繁星璀璨的天才", value="量子套", description=""),
            discord.SelectOption(label="淨庭教宗的聖騎士", value="防禦套", description=""),
            discord.SelectOption(label="密林臥雪的獵人", value="冰套", description=""),
            discord.SelectOption(label="雲無留跡的過客", value="治療套", description=""),
            discord.SelectOption(label="野穗伴行的快槍手", value="通用套", description=""),
            discord.SelectOption(label="流星追跡的怪盜", value="擊破套", description=""),
            discord.SelectOption(label="激奏雷電的樂團", value="雷套", description=""),
            discord.SelectOption(label="晨昏交界的翔鷹", value="風套", description=""),
            discord.SelectOption(label="街頭出身的拳王", value="物理套", description=""),
            discord.SelectOption(label="戍衛風雪的鐵衛", value="坦克套", description="")
        ]
        super().__init__(placeholder="請選擇想查詢的遺器資料", min_values=1, max_values=1, options=options2)

    async def callback(
        self,
        interaction: discord.Interaction,
    ):
        if self.values[0] == "火套":
                   
            artifact_info_embed = discord.Embed(title= "熔岩鍛鑄的火匠",
                                              description="",
                                              color=0xE74C3C,
                                              url="https://wiki.hoyolab.com/pc/hsr/entry/150")
            artifact_info_embed.set_thumbnail(url="https://wiki.hoyolab.com/_ipx/f_webp/https://upload-static.hoyoverse.com/hoyowiki/2023/02/21/f95029fd78e4a09d8a45a02295cb3028_5326203375186266609.png")
            artifact_info_embed.add_field(name="基本資訊:",
                                        value="名稱:熔岩鍛鑄的火匠\n來源:野焰之徑·侵蝕隧洞",
                                        inline=True)
            artifact_info_embed.add_field(name="遺器效果:",
                                        value="二件套:火屬性傷害提高10%。\n四件套:使裝備者施放戰技時造成的傷害提高12%,並在施放終結技後下次攻擊造成的火屬性傷害提高12%。",
                                        inline=False) 
            await interaction.message.edit(embed=artifact_info_embed)
            await interaction.response.defer()
class weaponinfo(discord.ui.Select):
    def __init__(self):
        
        options3 = [
            discord.SelectOption(label="拂曉之前", value="拂曉之前", description=""),
            discord.SelectOption(label="於夜色中", value="於夜色中", description=""),
            discord.SelectOption(label="時節不居", value="時節不居", description=""),
            discord.SelectOption(label="如泥酣眠", value="如泥酣眠", description=""),
            discord.SelectOption(label="制勝的瞬間", value="制勝的瞬間", description=""),
            discord.SelectOption(label="以世界之名", value="以世界之名", description=""),
            discord.SelectOption(label="但戰鬥還未結束", value="但戰鬥還未結束", description=""),
            discord.SelectOption(label="無可取代的東西", value="無可取代的東西", description=""),
            discord.SelectOption(label="銀河鐵道之夜", value="銀河鐵道之夜", description="")
        ]
        super().__init__(placeholder="請選擇要查詢的光錐資料", min_values=1, max_values=1, options=options3)

    async def callback(
        self,
        interaction: discord.Interaction,
    ):
        if self.values[0] == "於夜色中" :
            weapon_info_embed = discord.Embed(title= "於夜色中",
                                              description="少女露出一絲不易察覺的微笑。\n「為什麼呢?」\n「此時此刻此地,明明只有我一個人……」\n「卻感覺……很熱鬧呢。」",
                                              color=0x5865F2,
                                              url="https://wiki.hoyolab.com/pc/hsr/entry/68")
            weapon_info_embed.add_field(name="基本資訊",
                                        value="名稱:於夜色中\n命途:巡獵",
                                        inline=True)
            weapon_info_embed.add_field(name="屬性",
                                        value="生命值:48-1058\n攻擊力:26-582\n防禦力:21-463",
                                        inline=True)            
            weapon_info_embed.add_field(name="光錐效果",
                                        value="使裝備者的暴擊率提高18%/21%/24%/27%/30%。當裝備者在戰鬥中速度達到100以上時,每超過10點,普通攻擊和戰技的傷害便提高6%/7%/8%/9%/10%,同時終結技的暴擊傷害提高12%/14%/16%/18%/20%,該效果可疊加6次。",
                                        inline=False) 
            weapon_info_embed.set_image(url="https://wiki.hoyolab.com/_ipx/f_webp/https://upload-static.hoyoverse.com/hoyowiki/2023/02/21/f342952758193dcdcd8dd1dde1cc969d_4815329713662711142.png")
            await interaction.message.edit(embed=weapon_info_embed)
            await interaction.response.defer()



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
            discord.SelectOption(label="景元", value="景元", description=""),
            discord.SelectOption(label="三月七", value="三月七", description=""),
            discord.SelectOption(label="白露", value="白露", description=""),
            discord.SelectOption(label="彥卿", value="彥卿", description=""),
            discord.SelectOption(label="克拉拉", value="克拉拉", description=""),
            discord.SelectOption(label="傑帕德", value="傑帕德", description=""),
            discord.SelectOption(label="希兒", value="希兒", description=""),
            discord.SelectOption(label="布洛尼婭", value="布洛尼婭", description=""),
            discord.SelectOption(label="瓦爾特", value="瓦爾特", description=""),
            discord.SelectOption(label="姬子", value="姬子", description=""),
            discord.SelectOption(label="開拓者-存護", value="開拓者-存護", description=""),
            discord.SelectOption(label="開拓者-毀滅", value="開拓者-毀滅", description=""),
            discord.SelectOption(label="素裳", value="素裳", description=""),
            discord.SelectOption(label="青雀", value="青雀", description=""),
            discord.SelectOption(label="黑塔", value="黑塔", description=""),
            discord.SelectOption(label="丹恆", value="丹恆", description=""),
            discord.SelectOption(label="艾斯妲", value="艾斯妲", description=""),
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
        elif select.values[0] == '開拓者':
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
            discord.SelectOption(label="遺器(裝備)", value="遺器", description="提供各個遺器套裝的介紹"),
            discord.SelectOption(label="角色", value="角色", description="提供各角色的天賦,稀有度,職業介紹"),
            discord.SelectOption(label="光錐(武器)", value="光錐", description="提供武器故事及卡面資料")
        ]
        )
    async def select_callback(self,interaction:discord.Interaction,select):
        if select.values[0] == '遺器':
            select.disabled = True
            self.add_item(artifact())
            await interaction.message.edit(view=self)
            await interaction.response.defer()
        elif select.values[0] == '角色':
            select.disabled = True
            await interaction.message.edit(view=characterlist())
            await interaction.response.defer()
        elif select.values[0] == '光錐':  
            select.disabled = True
            self.add_item(weaponinfo())
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
