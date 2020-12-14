import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json



with open('setting.json',mode = 'r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        # print(f"{member} join!")
        channel = self.bot.get_channel(int(jdata['JoinLeaveLog']))
        await channel.send(f'{member} join')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        # print(f"{member} leave!")
        channel = self.bot.get_channel(int(jdata['JoinLeaveLog']))
        await channel.send(f'{member} leave')

    @commands.Cog.listener()
    async def on_message(self,msg):
        for keyword in jdata['keywords'].keys():
            if msg.content == keyword:
                await msg.channel.send(jdata['keywords'][keyword])
    
    
def setup(bot):
    bot.add_cog(Event(bot))