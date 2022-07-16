import discord
from discord.ext import commands
import sys
sys.path.append('..')
from LIBS.A_LIB_change import CHANGE as DEBUG_CHANGED
from extras.text_zone import BIG 
import extras.IDS as ID
cafe = ID.cafe

class CHANGED(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(hidden=True)
  async def CHANGE(self, ctx, command: str, *, text: str):
    print("1")
    try:
      DEBUG_CHANGED.MAIN_SCRIPT(DEBUG_CHANGED, 0, command, y=[], x=text)
    except Exception as e:
      print(e)
