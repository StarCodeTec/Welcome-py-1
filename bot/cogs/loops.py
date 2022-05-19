import discord
from discord.ext import tasks, commands
import sys
sys.path.append('..')
from extras.text_zone import BIG as b
from extras.text_zone import all_id as id_0
import extras.System_Id as ID
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

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
class loops(commands.Cog):
  def __init__(self, bot):
    self.bot=bot
  
  @tasks.loop(time=datetime.time("0", "0", "0", tzinfo=ZoneInfo("Etc/UTC")))
  async def purge(self):
    cha = await self.bot.fetch_channel(976322762631172147) or self.bot.get_channel(976322762631172147)
    await cha.purge(limit=500)
  @purge.before_loop
  async def waiting(self):
    await self.bot.wait_until_ready()
  
  async def loop_start_main(self):
    async with self.bot:
      await purge.start()
