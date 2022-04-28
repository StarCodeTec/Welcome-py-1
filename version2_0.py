import discord
from discord.ext import tasks, commands

cog = commands.Cog
class test(cog):
  def __init__(self):
    intents = discord.Intents.all()
    intents.typing = False
    intents.presences = False
    bot = commands.Bot(command_prefix=commands.when_mentioned_or('F^ ', 'F^'), intents=intents)
    self.bot = bot
  
  @commands.command()
  async def test(self, ctx):
    print("test")
