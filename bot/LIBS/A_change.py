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
    DEBUG_CHANGED.MAIN_SCRIPT(command=command, y=[], x=text, z=0)