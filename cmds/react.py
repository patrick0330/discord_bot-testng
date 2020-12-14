import discord
import random
import json
from discord.ext import commands
from core.classes import Cog_Extension
with open('setting.json',mode = 'r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def hi(self,ctx):
        await ctx.send(f'{ctx.author.mention} onichan ohayo')

    @commands.command()
    async def imoto(self,ctx):
        if(ctx.author.name == 'GGDaserding'):
            await ctx.send(f'{ctx.author.mention} onichan i want to %%')
        else:
            await ctx.send(f'{ctx.author.mention} kimochi warui')

    @commands.command()
    async def ahe(self,ctx):
        ahegao = discord.File(jdata['ahegao'])
        await ctx.send(file = ahegao)

    @commands.command()
    async def botavatar(self,ctx):
        ava = discord.File(jdata['avatar'])
        await ctx.send(file = ava)

    @commands.command()
    async def holo(self,ctx):
        random_pic = random.choice(jdata['random_pic'])
        rpic = discord.File(random_pic)
        await ctx.send(file = rpic)

    @commands.command()
    async def hiten(self,ctx):
        hiten_pic = random.choice(jdata['hiten'])   
        await ctx.send(hiten_pic)
def setup(bot):
    bot.add_cog(React(bot))
