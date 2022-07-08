import discord
import random
from discord.ext import commands

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
  async def hug(self, ctx: commands.Context, user: str):
    """currently testing"""
    if ctx.message.content == f"/hug {user} True":
      await ctx.send("test 1")
      return
    await ctx.send("test 2")
