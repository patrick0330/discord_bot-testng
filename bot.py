import discord
import json
from discord.ext import commands
with open('setting.json',mode = 'r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True


client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!!',intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")
    


@bot.event
async def on_member_join(member):
    # print(f"{member} join!")
    channel = bot.get_channel(int(jdata['JoinLeaveLog']))
    await channel.send(f'{membem} join')

@bot.event
async def on_member_remove(member):
    print(f"{member} leave!")
    channel = bot.get_channel(int(jdata['JoinLeaveLog']))
    await channel.send(f'{member} leave')

@bot.command()
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention} onichan ohayo')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

bot.run(jdata['TOKEN'])
