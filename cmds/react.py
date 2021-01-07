import discord
import random
import json
import pyimgur
import re
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
    async def 好油喔(self,ctx):
        peko1 = discord.File(f'C:\\Users\\USER\\Documents\\GitHub\\discord_bot-testng\\peko1.jpg')
        await ctx.send(file = peko1)

    @commands.command()
    async def 好宅喔(self,ctx):
        peko2 = discord.File(f'C:\\Users\\USER\\Documents\\GitHub\\discord_bot-testng\\peko2.jpg')
        await ctx.send(file = peko2) 
    
    @commands.command()
    async def 統神(self,ctx):
        godton = discord.File(f'C:\\Users\\USER\\Documents\\GitHub\\discord_bot-testng\\asiagodton.gif')
        await ctx.send(file = godton) 

    @commands.command()
    async def getavatar(self,ctx,*,member:discord.Member=None):
        userAvatarUrl = member.avatar_url
        await ctx.send(userAvatarUrl)
    
    @commands.group()
    async def wu(self,ctx):
        # pass
        if ctx.message.content.endswith("wu"):
            await ctx.send("This command needs an argument!")
        else:
            pass
    @wu.command()
    async def laugh(self,ctx):
        wulaugh = discord.File(f'C:\\Users\\USER\\Documents\\GitHub\\discord_bot-testng\\Wu\\2.gif')
        await ctx.send(file = wulaugh)

    @wu.command()
    async def yareyare(self,ctx):
        wu = discord.File(f'C:\\Users\\USER\\Documents\\GitHub\\discord_bot-testng\\Wu\\3.jpg')
        await ctx.send(file = wu)

    @wu.command()
    async def evil(self,ctx):
        wu = discord.File(f'C:\\Users\\USER\\Documents\\GitHub\\discord_bot-testng\\Wu\\1.jpg')
        await ctx.send(file = wu)
    
    @wu.command()
    async def sleep(self,ctx):
        wusleep = discord.File(f'C:\\Users\\USER\\Documents\\GitHub\\discord_bot-testng\\Wu\\4.jpg')
        await ctx.send(file = wusleep)

    


def setup(bot):
    bot.add_cog(React(bot))
