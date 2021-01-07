import discord
import random
import json
import pyimgur
import re
import requests
import re
from bs4 import BeautifulSoup
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json',mode = 'r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

CLIENT_ID = "16837f6cdd1e5a4"
im = pyimgur.Imgur(CLIENT_ID)
gif = im.get_album('RFnz4AQ')
img = im.get_album('dqE0kVw')
jojo = im.get_album('j3QcZgp')


class Random(Cog_Extension):
    @commands.command()
    async def hiten(self,ctx):
        hiten_pic = random.choice(jdata['hiten'])   
        await ctx.send(f'https://pixiv.cat/{hiten_pic}.jpg') #https://pixiv.cat/59580629.jpg

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
    async def holo(self,ctx):
        holo = random.randint(1,51)
        rholo = discord.File(f"C:\\Users\\USER\\Documents\\GitHub\\discord_bot-testng\\random_pic\\{holo}.gif")
        await ctx.send(file = rholo) 

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
    async def twitch_emo(self,ctx,msg,num:int):        
        id = msg #圖奇id 15027034
        result = requests.get(f"https://www.twitchemotes.com/channels/{id}") #把網頁抓進來讀
        soup = BeautifulSoup(result.text,"html.parser") #將網頁資料以 html.parser 解析器來解析
        divs = soup.find_all("div",  {"class": "col-md-2"})
        counter = 1
        for div in divs:
            img = div.find("img")
            img_id = re.findall("v1/(.+?)/",str(img['src']))
            jdata['href'][counter] = img['src']
            counter += 1
        try:
            twitch_pic = jdata['href'][num]
            await ctx.send(twitch_pic)
        except:
            await ctx.send("This index does not exist!")   



def setup(bot):
    bot.add_cog(Random(bot))