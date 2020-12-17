import discord
import random
import json
import pyimgur
import re
from discord.ext import commands
from core.classes import Cog_Extension
with open('setting.json',mode = 'r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
CLIENT_ID = "16837f6cdd1e5a4"
im = pyimgur.Imgur(CLIENT_ID)
gif = im.get_album('RFnz4AQ')
img = im.get_album('dqE0kVw')
jojo = im.get_album('j3QcZgp')




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

    @commands.command()
    async def A(self,ctx):
        gura = random.randint(1,26)
        rgura = discord.File(f'C:\\Users\\USER\\Documents\\GitHub\\discord_bot-testng\\gura\\{gura}.jpg')
        await ctx.send(file = rgura)

    @commands.command()
    async def rgif(self,ctx):
        rangif = random.choice(gif.images)
        find_id = re.findall('Image (.+?)>',str(rangif))
        id = find_id[0]
        image = im.get_image(id)
        await ctx.send(image.link)

    @commands.command()
    async def rimg(self,ctx):
        ranimg = random.choice(img.images)
        find_id = re.findall('Image (.+?)>',str(ranimg))
        id = find_id[0]
        image = im.get_image(id)
        await ctx.send(image.link)    
    
    @commands.command()
    async def jojo(self,ctx):
        rjojo = random.choice(jojo.images)
        find_id = re.findall('Image (.+?)>',str(rjojo))
        id = find_id[0]
        image = im.get_image(id)
        await ctx.send(image.link)
    
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
    
    @commands.command()
    async def sleep(self,ctx):
        wusleep = discord.File(f'C:\\Users\\USER\\Documents\\GitHub\\discord_bot-testng\\Wu\\4.jpg')
        await ctx.send(file = wusleep)


def setup(bot):
    bot.add_cog(React(bot))
