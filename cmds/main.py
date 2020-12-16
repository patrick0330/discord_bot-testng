import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import random

class Main(Cog_Extension):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def attackontitan(self,ctx):
        embed=discord.Embed(title=" Attack on Titan", url="https://en.wikipedia.org/wiki/Attack_on_Titan", description="《進擊的巨人》（日語：進撃の巨人）是日本漫畫家諫山創創作漫畫作品，是他的首部連載作品，在講談社《別冊少年Magazine》2009年10月號（創刊號）上開始連載。故事建立在人類與巨人的衝突上，人類居住在由高牆包圍的城市，對抗會食人的巨人。", color=0xffffff,
        timestamp = datetime.datetime.utcnow())
        embed.set_author(name="Hajime Isayama(諫山創)", url="https://zh.wikipedia.org/zh-tw/%E9%80%B2%E6%93%8A%E7%9A%84%E5%B7%A8%E4%BA%BA")
        embed.set_thumbnail(url="https://m.media-amazon.com/images/M/MV5BMTY5ODk1NzUyMl5BMl5BanBnXkFtZTgwMjUyNzEyMTE@._V1_.jpg")
        embed.add_field(name="主要角色：", value="艾連·葉卡， 三笠·阿克曼， 阿爾敏·亞魯雷特", inline=False)
        embed.add_field(name="類型：", value=" 動作， 黑暗奇幻， 末日及末日後幻想", inline=True)
        embed.add_field(name="工作室：", value=" WIT STUDIO， MAPPA， Production I.G", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def demonslayer(self,ctx):
        embed=discord.Embed(title=" Demon Slayer: Kimetsu no Yaiba", url="https://zh.wikipedia.org/wiki/%E9%AC%BC%E6%BB%85%E4%B9%8B%E5%88%83", description="《鬼滅之刃》（日語：鬼滅の刃），簡稱《鬼滅》，是日本漫畫家吾峠呼世晴所創作的奇幻漫畫作品，描述主角炭治郎為了尋求讓被變成鬼的妹妹復原的方法，踏上斬鬼之旅的和風刀劍奇譚。於2016年2月15日至2020年5月18日在《週刊少年Jump》連載，全205話。漫畫改編電視動畫於2019年4月至9月播放，並於2020年10月16日上映續集電影《鬼滅之刃劇場版 無限列車篇。", color=0xffffff,
        timestamp = datetime.datetime.utcnow())
        embed.set_author(name="Koyoharu Gotōge(吾峠呼世晴)", url="https://zh.wikipedia.org/zh-tw/%E5%90%BE%E5%B3%A0%E5%91%BC%E4%B8%96%E6%99%B4")
        embed.set_thumbnail(url="https://img.technews.tw/wp-content/uploads/2020/11/11143051/kv_game_sp.jpg")
        embed.add_field(name="主要角色：", value="竈門炭治郎", inline=False)
        embed.add_field(name="動畫製作：", value=" ufotable", inline=True)
        embed.add_field(name="音樂製作： ", value=" Aniplex", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit = num + 1)

    @commands.command()
    async def random_squad(self,ctx):
        online = []        
        for member in ctx.guild.members:
            if str(member.status) == 'online':                
                online.append(member)
        random_online = random.sample(online,k = 15)
        for i in random_online:
            print(i)
      
            
       
        

def setup(bot):
    bot.add_cog(Main(bot))