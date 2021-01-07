import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import random,asyncio,json


with open('setting.json',mode = 'r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

from pixivpy3 import *

api = AppPixivAPI()
api.login("ggdaserding", "vm3tp6u.4")   # Not required


class Pixiv(Cog_Extension):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def get_url(self,ctx,id):
        # get origin url
        json_result = api.illust_detail(id)
        illust = json_result.illust
        # print(illust.image_urls)
        img = illust.image_urls['large'].replace("i.pximg.net", "i.pixiv.cat")
        await ctx.send(f'url:{img}')

    @commands.command()
    async def pixiv_ranking(self,ctx,kind,num:int):
        # get ranking: 1-30
        # mode: [day, week, month, day_male, day_female, week_original, week_rookie, day_manga]
        # json_result = api.illust_ranking(kind)
        # next_qs = api.parse_qs(json_result.next_url)
        # json_result2 = api.illust_ranking(**next_qs)
        # next_qs = api.parse_qs(json_result.next_url)
        # json_result3 = api.illust_ranking(**next_qs)
        page_num  = 1
        jdata['ranking_page'][page_num] = api.illust_ranking(kind)
        while page_num != num:
            next_qs = api.parse_qs(jdata['ranking_page'][page_num].next_url)
            page_num += 1
            jdata['ranking_page'][page_num] = api.illust_ranking(**next_qs)
            

        for illust in jdata['ranking_page'][page_num].illusts:
            img = illust.image_urls.large.replace("i.pximg.net", "i.pixiv.cat")
            await ctx.send(f"[{illust.title}] {img}") 
            await asyncio.sleep(2)

    @commands.command()
    async def pixiv_tag(self,ctx,kind,num : int):
        json_result = api.search_illust(kind, search_target='partial_match_for_tags')
        print(json_result)
        # print(json_result)
        for illust in json_result.illusts:
            if illust.tags[0].name == 'R-18':
                continue
            img = illust.image_urls.large.replace("i.pximg.net", "i.pixiv.cat")            
            await ctx.send(f"[{illust.title}] {img}")
            num -= 1
            if(num == 0):
                break 
            await asyncio.sleep(1)

    @commands.command()
    async def pixiv_getuserpic(self,ctx,name,num1 : int,num2 : int):
        artist = api.search_user(name)
        artist_id = artist.user_previews[num1 - 1]['user']['id']
        json_result = api.user_illusts(artist_id)
        # print(json_result)
        for illust in json_result.illusts:
        # print(illust)
            img = illust.image_urls['large'].replace("i.pximg.net", "i.pixiv.cat")       
            await ctx.send(f"[{illust.title}] {img}")
            num2 -= 1
            if(num2 == 0):
                break 
            await asyncio.sleep(1)
        # print(">>> %s, origin url: %s" % (illust.title, illust.image_urls['large'])) 

    @commands.command()
    async def pixiv_user(self,ctx,name):        
        artist = api.search_user(name)
        for page in range(5):          
            # print(artist.user_previews[0])
            artist_id = artist.user_previews[page]['user']['id']
            artist_name = artist.user_previews[page]['user']['name']
            artist_icon = artist.user_previews[page]['user']['profile_image_urls']['medium'].replace("i.pximg.net", "i.pixiv.cat")
            illust_id = artist.user_previews[page]['illusts'][0]['id']
            illust_title = artist.user_previews[page]['illusts'][0]['title']
            illust_caption = artist.user_previews[page]['illusts'][0]['caption']
            illust_icon = artist.user_previews[page]['illusts'][0]['image_urls']['large'].replace("i.pximg.net", "i.pixiv.cat") 
            # await ctx.send(illust_id)                
            embed=discord.Embed(title= illust_title, url=f"https://www.pixiv.net/artworks/{illust_id}", description=illust_icon)
            embed.set_author(name=artist_name, url=f"https://www.pixiv.net/users/{artist_id}", icon_url=artist_icon)
            embed.set_image(url = illust_icon)
            if(illust_caption != ""):            
                embed.add_field(name="contents", value=illust_caption, inline=True)               
            embed.set_footer(text="click the title or the artist name to see more info")
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('👉')
            await msg.add_reaction('👎')
            def check(reaction, user):
                return user == ctx.author and reaction.message.id == msg.id
            try:
                reaction, user = await self.bot.wait_for('reaction_add',timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await msg.delete()
                return

            if str(reaction.emoji) == '👉':  #next
                await msg.delete()
                continue
            else:
                await msg.delete()
                break
        await ctx.send("Not find anything you want? :( ",delete_after=30)

     
    @pixiv_user.error
    async def pixiv_user_error(self,ctx,error):
        # if isinstance(error,commands.errors.IndexError):
        await ctx.send("This index doesn't exist!")





    




def setup(bot):
    bot.add_cog(Pixiv(bot))