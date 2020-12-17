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
        # print(msg.content)
        if msg.content == "<@!787751671538778122>":
            embed=discord.Embed()
            embed.add_field(name="Hi I'm Test bot", value="My prefix here is `!!`. type `!!help` for more infos.\nFor those who wants to play music, please use the prefix `?` and type `?help` for more commands.", inline=False)
            await msg.channel.send(embed=embed)
            return
        for keyword in jdata['keywords'].keys():            
            if msg.content == keyword:
                await msg.channel.send(jdata['keywords'][keyword])
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await ctx.send("This command needs argument(s)!")
        elif isinstance(error,commands.errors.CommandNotFound):
            await ctx.send("This command does not exist!")
        else:
            # print(error)
            await ctx.send("Error!")

    
def setup(bot):
    bot.add_cog(Event(bot))