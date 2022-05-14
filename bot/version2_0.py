import discord
from discord.ext import tasks, commands

cog = commands.Cog
class test(cog):
  def __init__(self):
    self.bot = bot
  
  @commands.command()
  async def test(self, ctx):
    print("test")
