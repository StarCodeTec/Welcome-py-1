#cogs--------------------------------------------------------------------------------------------  
import cogs.sticky as sticky
import cogs.react as react
#async_run---------------------------------------------------------------------------------------
import asyncio
def run(run):
  asyncio.run(run)
#import------------------------------------------------------------------------------------------  

import os
import discord
import time
import traceback
from discord.ext import tasks, commands
from pytz import timezone
TZX = timezone('EST')
from zoneinfo import ZoneInfo
import datetime as DT

#EXTRA_IMPORTS-----------------------------------------------------------------------------------
from password import Admin_key as key
from extras.text_zone import BIG as b
from extras.text_zone import all_id as id_0
import extras.System_Id as ID
#EXTRA_TEXT--------------------------------------------------------------------------------------
cafe = ID.cafe
Fenne = 474984052017987604 
Luna = 599059234134687774
r1 = id_0.fenne
rcheck = id_0.check
r3 = id_0.heart
r4 = id_0.P_heart
r5 = id_0.thumb_up
null = None
botuser = 966392608895152228
#intents----------------------------------------------------------------------------------------

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
ACTIVITY=discord.Activity(type=discord.ActivityType.watching, name="discord.gg/FemboyCafe")
bot = commands.Bot(command_prefix=commands.when_mentioned_or('F^ ', 'F^'), intents=intents, activity=ACTIVITY)

#-----------------------------------------------------------------------------------------------
@tasks.loop(time=[DT.time(hour=0, minute=0, second=0, tzinfo=TZX), DT.time(hour=10, minute=10, second=8, tzinfo=TZX)])
async def purge():
  print("check")
  cha = bot.get_channel(976322762631172147) or await bot.fetch_channel(976322762631172147) 
  print("check2")
  await cha.purge(limit=500)
  print("mhmmmmmmm")
  await cha.send(f"<@{Luna}>")

@bot.event
async def on_member_join(mem):
  try:
    await mem.send(f"""⇀ Welcome <@!{mem.id}> {b.welcome_text_dm}""")
  except:
    return
  finally:
    welcomed= discord.Object(id=889011345712894002)
    reg= discord.utils.get(mem.guild.roles, name="Regular")
    if reg not in mem.roles:return
    await mem.remove_roles(welcomed)

@bot.event
async def on_guild_channel_create(cha):
  if cha.category.id == cafe.cats.Home and "ticket" in str(cha.name):
    time.sleep(3)
    await cha.send("Hey there, how can we help you?")
  elif cha.id != cafe.Verify.Entrance:
    if cha.category_id != cafe.cats.Verify:return
    time.sleep(2)
    await cha.send("Please put all answers in one message and do not close the ticket!")

@bot.event
async def on_message(msg):
  if msg.guild is None:return
  if msg.author.id == botuser:return
  elif msg.content.startswith(".speak"):
    if msg.channel.id != 956295021676601386:return
    message = msg.content.removeprefix(".speak").lstrip()
    if message.endswith("GEN"):
      cha = bot.get_channel(cafe.Chat.General) or await bot.fetch_channel(cafe.Chat.General)
      text=message.removesuffix("GEN")
    elif message.endswith("MOD"):
      cha = bot.get_channel(901215227662696469) or await bot.fetch_channel(901215227662696469)
      text=message.removesuffix("MOD")
    elif message.endswith("NONE"):
      cha=msg.channel
      text = message.removesuffix("NONE")
    if msg.content.split()[-3] == "@":
      ping = msg.content.split()[-2]
      content = text.split()
      del content[-1] 
      del content[-1]
      tex = ' '.join(content)
      await cha.send(f"{tex}<@{ping}>")
    else:
      await cha.send(text)
  elif msg.channel.id != cafe.Verify.Entrance:
    if msg.channel.category_id != cafe.cats.Verify:return
    if msg.reference == None:return
    """needed space"""
    welcomed= discord.Object(id=889011345712894002)
    unwelcomed= discord.Object(id=889011029428801607)
    admin= discord.utils.get(msg.author.guild.roles, name="Server Staff")
    reply = msg.reference.resolved
    member = reply.author
    gen = bot.get_channel(cafe.Chat.General) or await bot.fetch_channel(cafe.Chat.General)
    logs = bot.get_channel(ID.Logs.logs) or await bot.fetch_channel(ID.Logs.logs)
    if admin not in msg.author.roles:return
    if msg.content == ".verify" or msg.content == "<:approved:973046001118101514>":
      await member.remove_roles(unwelcomed)
      await member.add_roles(welcomed)
      if msg.author.id == Fenne:
        await gen.send(f"Welcome <@{member.id}> please make a <#888482614351134720> and enjoy your stay.")
      else:
        await gen.send(f"Welcome <@{member.id}> please make a <#888482614351134720> and enjoy your stay. Welcomed by <@{msg.author.id}>")
      time = await msg.channel.send("time holder(dont delete)")
      await logs.send(f"\tWelcome <@{member.id}>\n{reply.content}\n\nWelcomed by: <@{msg.author.id}>\n\nWelcomed at: {time.created_at}")
      await msg.channel.delete()
      

  
async def main_start(run):
    async with bot:
        purge.start()
        #bump.start()
        #bystander.start()
        await bot.add_cog(sticky.sticky(bot))
        await bot.add_cog(react.auto_react(bot))
        await bot.start(str(key)) 

        
run(main_start(run))
