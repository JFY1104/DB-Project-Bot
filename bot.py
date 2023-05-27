#coding:utf-8
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
                                        value="命途:存護\n稀有度:★4\n屬性:冰",
                                        inline=True) 
            march7_info_embed.add_field(name="聲優",
                                        value="華語CV:諾亞\n日語CV:小倉唯\n英語CV:Skyler Davenport\n韓語CV:정혜원",
                                        inline=False)
            march7_info_embed.set_image(url="https://media.tenor.com/OQiJiZ0MzycAAAAC/honkai-star-rail.gif")
            await interaction.message.edit(embed=march7_info_embed)
            await interaction.response.defer()
        elif  self.values[0] == '行跡':
            march7_talent_embed = discord.Embed(title= "三月七",
                                              description="",
                                              color=0x3498DB,
                                              )
            march7_talent_embed.add_field(name="普通攻擊:極寒弓矢",
                                          value="對指定敵方單體造成等同於三月七50%攻擊力的冰屬性傷害。",
                                          inline=False
                )
            march7_talent_embed.add_field(name="戰技:可愛即是正義",
                                          value="為指定我方單體施加強度等同於三月七38%防禦力+190護盾,持續3回合。若該目標生命值百分比大於等於30%，則遭到敵方攻擊的機率大幅提高。",
                                          inline=False
                )
            march7_talent_embed.add_field(name="終結技:冰刻箭雨之時",
                                          value="對敵方全體造成等同於三月七90%攻擊力的冰屬性傷害。受到攻擊的敵方目標有50%基礎機率陷入凍結狀態,持續1回合。凍結狀態下,敵方目標不能行動,並且在每回合開始時受到等同於三月七30%攻擊力的冰屬性持續傷害。",
                                          inline=False
                )
            march7_talent_embed.add_field(name="天賦:少女的特權",
                                          value="當持有護盾的我方目標受到敵方目標攻擊後,三月七立即向攻擊者發動反擊,對其造成等同於三月七50%攻擊力的冰屬性傷害,該效果每回合可觸發2次。",
                                          inline=False
                )
            march7_talent_embed.add_field(name="密技:凍人的瞬間",
                                          value="立即攻擊敵人,進入戰鬥後有100%的基礎機率使隨機敵方單體陷入凍結狀態,持續1回合。\n凍結狀態下,敵方目標不能行動,同時每回合開始時受到等同於三月七50%攻擊力的冰屬性附加傷害。",
                                          inline=False
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
            march7_star_embed.add_field(name="星魂二:記憶中的它",
                                          value="進入戰鬥時，為生命值百分比最低的我方目標提供強度等同於三月七24%防禦力+320的護盾，持續3回合。",
                                          inline=False
                )
            march7_star_embed.add_field(name="星魂三:記憶中的一切",
                                          value="終結技等級+2，最多不超過15級；普通攻擊等級+1，最多不超過10級。",
                                          inline=False
                )
            march7_star_embed.add_field(name="星魂四:不願再失去",
                                          value="天賦的反擊效果每回合可觸發的次數增加1次。使反擊造成的傷害值提高，提高數值等同於三月七防禦力的30%。",
                                          inline=False
                )
            march7_star_embed.add_field(name="星魂五:不想再忘卻",
                                          value="戰技等級+2，最多不超過15級；天賦等級+2，最多不超過15級。",
                                          inline=False
                )
            march7_star_embed.add_field(name="星魂六:就這樣，一直……",
                                          value="在戰技提供的護盾保護下的我方目標，每回合開始時回復等同於各自4%生命上限+106的生命值。",
                                          inline=False
                )
            
            march7_star_embed.set_image(url="https://wiki.hoyolab.com/_ipx/f_webp/https://upload-static.hoyoverse.com/hoyolab-wiki/2023/04/28/125413385/db3a53277b7f8001542acae757e7ed58_4234173604942154140.png")
            await interaction.message.edit(embed=march7_star_embed)
            await interaction.response.defer()
class search_jinyun_info(discord.ui.Select):
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
        if  self.values[0] == '基本資料':
            jinyun_info_embed = discord.Embed(title= "景元",
                                              description="仙舟聯盟的六位將軍之一，節制仙舟「羅浮」的雲騎軍。\n師從前代「羅浮」劍首，但並不顯名於武力。",
                                              color=0xEEEFF1,
                                              url="https://wiki.hoyolab.com/pc/hsr/entry/26")
            jinyun_info_embed.set_thumbnail(url="https://upload-static.hoyoverse.com/hoyowiki/2023/02/21/df37aacd31ab40efdcb16ef03a5b68ed_4983283866355038276.png")
            """ march7_info_embed.set_image(url="https://wiki.hoyolab.com/_ipx/f_webp/https://upload-static.hoyoverse.com/hoyowiki/2023/02/21/1721c5c450299615748e2fa4971e2746_2999314882560891227.png") """
            jinyun_info_embed.add_field(name="基本資料",
                                        value="陣營:仙舟聯盟\n所屬:仙舟「羅浮」",
                                        inline=True)
            jinyun_info_embed.add_field(name="戰鬥資料",
                                        value="命途:智識\n稀有度:★5\n屬性:雷",
                                        inline=True) 
            jinyun_info_embed.add_field(name="聲優",
                                        value="華語CV:孫曄\n日語CV:小野大輔\n英語CV:Alejandro Saab\n韓語CV:류승곤",
                                        inline=False)
            jinyun_info_embed.set_image(url="https://media.tenor.com/H0PNUUY8jnwAAAAd/starrail-jingyuan.gif")
            await interaction.message.edit(embed=jinyun_info_embed)
            await interaction.response.defer()
        elif  self.values[0] == '行跡':
            jinyun_talent_embed = discord.Embed(title= "景元",
                                              description="",
                                              color=0xEEEFF1,
                                              )
            jinyun_talent_embed.add_field(name="普通攻擊:石火流光",
                                          value="對指定敵方單體造成等同於景元50%攻擊力的雷屬性傷害。",
                                          inline=False
                )
            jinyun_talent_embed.add_field(name="戰技:紫霄震曜",
                                          value="對敵方全體造成等同於景元50%攻擊力的雷屬性傷害，同時增加2段【神君】下回合的攻擊段數。",
                                          inline=False
                )
            jinyun_talent_embed.add_field(name="終結技:吾身光明",
                                          value="對敵方全體造成等同於景元120%攻擊力的雷屬性傷害，同時增加3段【神君】下回合的攻擊段數。",
                                          inline=False
                )
            jinyun_talent_embed.add_field(name="天賦:斬勘神形",
                                          value="戰鬥開始時召喚【神君】。【神君】初始擁有60點速度以及3段攻擊段數，行動時發動追加攻擊，每段攻擊對隨機敵方單體造成等同於景元攻擊力33%的雷屬性傷害，同時對其相鄰目標造成等同於主目標25%的雷屬性傷害。\n【神君】最多累計10段攻擊段數且每增加1段攻擊段數，速度提高10點，行動結束後速度和攻擊段數恢復至初始狀態。當景元陷入無法戰鬥狀態時【神君】消失。當景元受到控制類負面狀態影響時【神君】也無法行動。",
                                          inline=False
                )
            jinyun_talent_embed.add_field(name="密技:持籙",
                                          value="用秘技後，下一次戰鬥開始時【神君】第1回合的攻擊段數增加3段。",
                                          inline=False
                )
            
            jinyun_talent_embed.set_image(url="https://upload-static.hoyoverse.com/hoyolab-wiki/2023/05/16/125413385/9924a49340890a487fd34fd6c81fa320_3498437733606547324.gif")
            await interaction.message.edit(embed=jinyun_talent_embed)
            await interaction.response.defer()
        elif  self.values[0] == '星魂':
            jinyun_star_embed = discord.Embed(title= "景元",
                                              description="",
                                              color=0xEEEFF1,
                                              )
            jinyun_star_embed.add_field(name="星魂一:星流霆擊碎昆岡",
                                          value="【神君】施放攻擊時，對指定敵方單體的相鄰目標造成的傷害倍率額外提高，提高數值等同於對主目標傷害倍率的25%。",
                                          inline=False
                )
            jinyun_star_embed.add_field(name="星魂二:戎戈動地開天陣",
                                          value="【神君】行動後，景元的普攻、戰技、終結技造成的傷害提高20%，持續2回合。",
                                          inline=False
                )
            jinyun_star_embed.add_field(name="星魂三:移鋒驚電衝霄漢",
                                          value="終結技等級+2，最多不超過15級；普通攻擊等級+1，最多不超過10級。",
                                          inline=False
                )
            jinyun_star_embed.add_field(name="星魂四:刃卷橫雲落玉沙",
                                          value="【神君】每段攻擊後，景元恢復2點能量。",
                                          inline=False
                )
            jinyun_star_embed.add_field(name="星魂五:百戰棄軀輕死生",
                                          value="戰技等級+2，最多不超過15級；天賦等級+2，最多不超過15級。",
                                          inline=False
                )
            jinyun_star_embed.add_field(name="星魂六:威靈有應破敵讎",
                                          value="【神君】每段攻擊後會使指定敵方目標額外陷入易傷狀態。易傷狀態下的敵方目標受到的傷害提高12 %，持續至【神君】本次攻擊結束，該效果最多疊加3層。",
                                          inline=False
                )
            
            jinyun_star_embed.set_image(url="https://wiki.hoyolab.com/_ipx/f_webp/https://upload-static.hoyoverse.com/hoyolab-wiki/2023/04/28/125413385/e4ffd8cb504b25046bc61be6ca89fee4_8632838892177407721.png")
            await interaction.message.edit(embed=jinyun_star_embed)
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
        if self.values[0] == "量子套":
                   
            artifact_info_embed = discord.Embed(title= "繁星璀璨的天才",
                                              description="",
                                              color=0x3498DB,
                                              url="https://wiki.hoyolab.com/pc/hsr/entry/145")
            artifact_info_embed.set_thumbnail(url="https://wiki.hoyolab.com/_ipx/f_webp/https://upload-static.hoyoverse.com/hoyowiki/2023/02/21/67b9c778a1a6080472e6b1deeb340d37_3108138781323191767.png")
            artifact_info_embed.add_field(name="基本資訊:",
                                        value="名稱:繁星璀璨的天才\n來源:睿治之徑·侵蝕隧洞",
                                        inline=True)
            artifact_info_embed.add_field(name="遺器效果:",
                                        value="二件套:量子屬性傷害提高10%。\n四件套:當裝備者對敵方目標造成傷害時，無視其10%的防禦力。若目標擁有量子屬性弱點，則額外無視其10%的防禦力。",
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
        elif self.values[0] == "拂曉之前" :
            weapon_info_embed = discord.Embed(title= "拂曉之前",
                                              description="「將軍，此事請務必慎重……往後歷史會怎麼評論將軍您……」\n雲騎將軍雙目半闔，聽取手下來報。\n「歷史自然會有判斷，但我對歷史的結論無甚興趣。」\n「事成，我此時便是胸有成竹，神閒氣定。」\n「事敗，我此時便是逸樂無度，愛雀失眾。」\n一隻雀兒跳下他的肩膀，他順勢抬手接住。\n「我只是做了我的判斷罷了。」",
                                              color=0xEEEFF1,
                                              url="https://wiki.hoyolab.com/pc/hsr/entry/73")
            weapon_info_embed.add_field(name="基本資訊",
                                        value="名稱:拂曉之前\n命途:智識",
                                        inline=True)
            weapon_info_embed.add_field(name="屬性",
                                        value="生命值:48-1058\n攻擊力:26-582\n防禦力:21-463",
                                        inline=True)            
            weapon_info_embed.add_field(name="光錐效果",
                                        value="使裝備者暴擊傷害提高36%/42%/48%/54%/60%。使裝備者戰技和終結技造成的傷害提高18%/21%/24%/27%/30%。裝備者施放戰技或終結技後，獲得【夢身】效果。觸發追加攻擊時，消耗【夢身】，使追加攻擊造成的傷害提高48%/56%/64%/72%/80%。",
                                        inline=False) 
            weapon_info_embed.set_image(url="https://wiki.hoyolab.com/_ipx/f_webp/https://upload-static.hoyoverse.com/hoyowiki/2023/02/21/ac79e739072fa86b2f6d5f851bb2c916_952669953280599733.png")
            await interaction.message.edit(embed=weapon_info_embed)
            await interaction.response.defer()
        


class characterlist(discord.ui.View):
    option_value =""
    @discord.ui.select(
        placeholder="請選擇要查詢的角色",
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
        elif select.values[0] == '景元':
            select.disabled = True
            await interaction.response.defer()
            self.add_item(search_jinyun_info())
            await interaction.message.edit(view=self)
class search_category(discord.ui.View):
    @discord.ui.select(
        placeholder="請選擇要查詢的類別",
        min_values=1, 
        max_values=1, 
        options = [
            discord.SelectOption(label="遺器(裝備)", value="遺器", description="提供各個遺器套裝的介紹"),
            discord.SelectOption(label="角色", value="角色", description="提供各角色的行跡,故事,命途介紹"),
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
