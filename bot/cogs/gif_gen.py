import discord
from typing import Optional
import random
from discord.ext import commands
import sys
sys.path.append('..')
import extras.IDS as ID

cog = commands.Cog
Fenne = 474984052017987604 
Equinox = 599059234134687774
null = None
botuser = 966392608895152228 
cctx=commands.Context
class gifs(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot: commands.Bot = bot
  
  @commands.hybrid_command(name="hug")
  @discord.app_commands.guilds(ID.server.fbc)
  async def hug(self, ctx: commands.Context, member: discord.Member=None, gender_specific: Optional[bool] = False):
    """currently testing"""
    x_y=Gender_Specific
    if x_y == True:
      await ctx.send("This feature is a work in progress comman")
    elif x_y == False:
      member = ctx.message.reference.resolved.author if not member else member
      user=member.mention
      aray=range(1, 93)
      ex=[29, 38, 47, 51, 56, 63, 64, 77, 78, 83, 87]
      main=[]
      for i in aray:
        if i not in ex:
          main.append(str(i).zfill(3))
      url=(f"https://purrbot.site/img/sfw/hug/gif/hug_{random.choice(main)}.gif")
      embed = discord.Embed()
      embed.set_image(url=url)
      await ctx.send(f"{ctx.author.mention} hugs {user}", embed=embed)
    try:
      await ctx.message.delete()
    except:
      return
