import discord
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
  async def hug(self, ctx: commands.Context, user: str, x_y: Optional[bool] = False):
    """currently testing"""
    if x_y == True:
      await ctx.send("test 1")
      return
    await ctx.send("test 2")
