import discord
from discord.ext import commands
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
    channel = bot.get_channel(787873726376706058)
    await channel.send(f'{member} join')

@bot.event
async def on_member_remove(member):
    print(f"{member} leave!")
    channel = bot.get_channel(787873751844651050)
    await channel.send(f'{member} leave')

@bot.command()
async def hello(ctx):
    await ctx.send(f'{ctx.author} onichan ohayo')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

bot.run('Nzg3NzUxNjcxNTM4Nzc4MTIy.X9Zg6g.lFTZwAoD2t9eXOyVNw9N86bsmQw')
