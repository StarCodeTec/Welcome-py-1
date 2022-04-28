import discord
from discord.ext import tasks, commands

cog = commands.Cog
class test(bot):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def test(self, ctx):
    print("test")
