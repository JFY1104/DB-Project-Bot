import discord
from discord.ext import commands

class test(commands.Cog):
    def __init__(self,bot) -> None:
        self.bot = bot 

    @commands.Cog.listener()
    async def on_ready(self):
        print("test is already")
    
    @commands.command()
    async def ping(self,ctx):
        bot_lantency = round(self.bot.latency * 1000)
        await ctx.send(f"ping is {bot_lantency}ms.")

async def setup(bot):
    await bot.add_cog(test(bot))