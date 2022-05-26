import discord
from discord.ext import tasks, commands
import sys
sys.path.append('.')
from bingusVAR import *
cog = commands.Cog
cafe = ID.cafe
Fenne = 474984052017987604 
Equinox = 599059234134687774
r1 = id_0.fenne
rcheck = id_0.check
r3 = id_0.heart
r4 = id_0.P_heart
r5 = id_0.thumb_up
null = None
botuser = 966392608895152228 
class bingus(commands.Cog):
  def __init__(self, bot):
    self.bot=bot
  
  @cog.command()
  async def bingus(ctx):
    embed = discord.Embed()
    file=FILE()
    embed.set_image(url=file)
    await ctx.send(embed=embed)
  
