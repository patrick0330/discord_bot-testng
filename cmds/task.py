import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json,asyncio,datetime

class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.counter = 1
        # async def interval():
        #     await self.bot.wait_until_ready()
        #     self.channel = self.bot.get_channel(582920350506156034)
        #     while not self.bot.is_closed():
        #         await self.channel.send("Hi i'm running!")
        #         await asyncio.sleep(5) #單位:秒
        # self.bg_task = self.bot.loop.create_task(interval())

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(582920350506156034)            
            while not self.bot.is_closed():                
                now_time = datetime.datetime.now().strftime('%A %H:%M')
                with open('setting.json',mode = 'r',encoding='utf8') as jfile:
                    jdata = json.load(jfile)
                if now_time == jdata['time']:                                        
                    if(self.counter <= 2):
                        # await self.channel.send("<@!239008552205811714> 是個噁男!!")
                        await self.channel.send("<@!239008552205811714> <@!344871743749357592> <@!239013040786243585> <@!391837295612919818> <@!330957184542310401> 該打殲滅作戰囉!!")
                        self.counter += 1                    
                    # if(self.counter > 5 and self.counter < 7):
                    #     await self.channel.send("https://static-cdn.jtvnw.net/emoticons/v1/118086/3.0")
                    #     self.counter +=1
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass
        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel: {self.channel.mention}')
    
    @commands.command()
    async def set_time(self,ctx,*,time):
        self.counter = 1
        with open('setting.json',mode = 'r',encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['time'] = time
        with open('setting.json',mode = 'w',encoding='utf8') as jfile:
            json.dump(jdata,jfile,indent=4)
def setup(bot):
    bot.add_cog(Task(bot))