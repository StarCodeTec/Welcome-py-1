import discord
from discord.ext import tasks, commands
from . import AAA as bingus
cog = commands.Cog
Fenne = 474984052017987604 
Equinox = 599059234134687774
null = None
botuser = 966392608895152228 
class bingus(commands.Cog):
  def __init__(self, bot):
    self.bot=bot
  
  @commands.command()
  async def bingus(self, ctx):
    embed = discord.Embed()
    Bingus=bingus.bingus
    file=Bingus
    await ctx.send(embed=embed, file=file)
  
