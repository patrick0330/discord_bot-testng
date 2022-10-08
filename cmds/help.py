import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import random

class Help(Cog_Extension):

    @commands.command()
    async def cmdhelp(self,ctx):
        embed=discord.Embed(title="Commands")
        embed.add_field(name="`!!attackontitan`", value=" show info about Attack on titan", inline=False)
        embed.add_field(name="`!!clean [number]` ", value="clean certain amount of msgs", inline=False)
        embed.add_field(name="`!!demonslayer`", value="show info about Demon slayer", inline=False)
        embed.add_field(name="`!!ping`", value="show pings of the bot", inline=False)
        embed.add_field(name="`!!random_squad`", value="random group 4 online or idle people into  2 groups", inline=False)
        embed.add_field(name="`!!sayd [msg]`", value="make the bot say something for you", inline=False)
        embed.add_field(name="`!!get_url [id]`", value="get the pixiv image url ", inline=False)
        embed.add_field(name="`!!pixiv_ranking [mode] [num]`", value="get ranked pixiv images mode:[day, week, month, day_male, day_female, week_original, week_rookie, day_manga] ,and input a number for what page", inline=False)
        embed.add_field(name="`!!pixiv_tag [tag] [num]`", value="search pixiv image base on tags,and input a number for how many images you want to see", inline=False)
        embed.add_field(name="`!!pixiv_getuserpic [name] [num1] [num2]`", value="get the pixiv user's images,input num1 for which result you want to see,num2 for how many images you want to see", inline=False)
        embed.add_field(name="`!!pixiv_user [name]`", value="see info of a pixiv user,press next to see next one,press down to quit", inline=False)
        embed.add_field(name="`!!A`", value="send some random gura pictures", inline=False)
        embed.add_field(name="`!!ahe`", value="send a disgusting picture(nsfw)", inline=False)
        embed.add_field(name="`!!botavatar`", value="watch the bot's avatar", inline=False)
        embed.add_field(name="`!!getavatar [user_id]`", value="get someone's avatar", inline=False)
        embed.add_field(name="`!!hi`", value="make the bot say hello to you", inline=False)
        embed.add_field(name="`!!hiten`", value="send random hiten pictures", inline=False)
        embed.add_field(name="`!!holo`", value="send random hololive pictures", inline=False)
        embed.add_field(name="`!!imoto`", value="you are disgusting! even the bot won't like you", inline=False)
        embed.add_field(name="`!!jojo`", value="send random jojo pictures", inline=False)
        embed.add_field(name="`!!rgif`", value="send random gifs", inline=False)
        embed.add_field(name="`!!rimg`", value="send random images", inline=False)
        #embed.add_field(name="`!!wu`", value="send some wu pictures(including `laugh` `evil` `sleep` `yareyare`)", inline=False)
        embed.add_field(name="`!!好油喔`", value="send a picture to say someone is a weeb", inline=False)
        embed.add_field(name="`!!好宅喔`", value="send a picture to say someone is a weeb", inline=False)
        embed.add_field(name="`!!統神`", value="send a picture about asiagodton", inline=False)
        embed.add_field(name="`!!twitch_emo [channel_id] [number]`", value="send some twitch channel emotes.To use this command, please go to `https://www.twitchemotes.com/` and search for the channel,then input the id(should look like https://www.twitchemotes.com/channels/ `[channel_id]` ) and number of which picture you want to send", inline=False)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Help(bot))
