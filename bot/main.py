#cogs--------------------------------------------------------------------------------------------  
#import version2_0 as twozz
#test=twozz.test()

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

#EXTRA_IMPORTS-----------------------------------------------------------------------------------
from password import Admin_key as key
from text_zone import BIG as b
from text_zone import all_id as id_0
import System_Id as id
#EXTRA_TEXT--------------------------------------------------------------------------------------
cafe = id.cafe
Fenne = 474984052017987604 
Equinox = 599059234134687774
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
bot = commands.Bot(command_prefix=commands.when_mentioned_or('F^ ', 'F^'), intents=intents)

#-----------------------------------------------------------------------------------------------

@bot.event
async def on_member_join(mem):
  try:
    await mem.send(f"""⇀ Welcome <@!{mem.id}> {b.welcome_text_dm}""")
  except:
    return

@bot.event
async def on_guild_channel_create(cha):
  if cha.category.id == cafe.cats.Home and "ticket" in str(cha.name):
    time.sleep(3)
    await cha.send("Hey there, how can we help you?")
  if cha.category.id == cafe.cats.Verify and "ticket" in str(cha.name):
    print(cha.guild.roles)    

@bot.event
async def on_message(msg):
  if msg.author.id == botuser:return
  def is_me(msg):
    return msg.author.id == botuser
  if msg.channel.id == cafe.Little_fenne.News or msg.channel.category_id == cafe.cats.Selfies:
    if msg.channel.id == cafe.Selfies.Comments:return
    await msg.add_reaction(r1)
    await msg.add_reaction(rcheck)
    await msg.add_reaction(r3)            
    await msg.add_reaction(r4)            
    await msg.add_reaction(r5)
  elif msg.channel.id == cafe.Mod.News:
    await msg.add_reaction(rcheck)
  elif msg.channel.id == cafe.Chat.Promo:
    cha = bot.get_channel(cafe.Chat.Promo) or await bot.fetch_channel(cafe.Chat.Promo)
    await cha.purge(limit=2, check=is_me)
    await cha.send("Server boosters can post <#904501391299608586> in every 30 minutes!")
  elif msg.channel.id == cafe.Chat.Bio:
    cha = bot.get_channel(cafe.Chat.Bio) or await bot.fetch_channel(cafe.Chat.Bio)   
    await cha.purge(limit=2, check=is_me)
    await cha.send(b.bt)

      
async def main_start():
    async with bot:
        await bot.start(str(key)) 
        #gen.start()
        #bump.start()
        #bystander.start()
        #await bot.add_cog(test)
        
asyncio.run(main_start())

