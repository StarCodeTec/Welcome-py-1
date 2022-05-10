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
"""
@bot.command()
async def gen_send(ctx, words, userid):
        general = bot.get_channel(950085161872154694) or await bot.fetch_channel(950085161872154694)
        if userid == "none":
            await general.send(words)
        else:
            allwordg=f"<@!{userid}> {words}"
            await general.send(content=allwordg)
                
@bot.command()
async def ent_send(ctx, words, userid):
    entrance = bot.get_channel(945087125831958588) or await bot.fetch_channel(945087125831958588)
    if userid == "none":
        await entrance.send(words)
    else:
        allworde=f"<@!{userid}> {words}"
        await entrance.send(allworde)

@bot.command()
async def mod_send(ctx, words, userid):
    mod = bot.get_channel(901215227662696469) or await bot.fetch_channel(901215227662696469)
    if userid == "none":
        await mod.send(words)
    else:
        allwordm=f"<@!{userid}> {words}"
        await mod.send(allwordm)"""

@bot.event
async def on_member_join(mem):
  try:
    await mem.send(f"""⇀ Welcome <@!{mem.id}> {b.welcome_text_dm}""")
  except:
    print("not accepting dms")
    

@bot.event
async def on_guild_channel_create(cha):
  if cha.category.id != cafe.cats.Home:return
  if "ticket" in str(cha.name):
    time.sleep(3)
    await cha.send("Hey there, how can we help you?")

@bot.event
async def on_message(msg):
  if msg.author.id == botuser:return
  def is_me(msg):
    return msg.author.id == botuser
  if msg.channel.id == cafe.Little_fenne.News or msg.channel.category_id == cafe.cats.Selfies:
    if msg.channel.category_id == cafe.cats.Selfies and msg.channel.id == cafe.Selfies.Comments:return
    
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
  else:
    await bot.process_commands(msg)

@bot.event
async def on_raw_reaction_add(payload):
  cha = bot.get_channel(payload.channel_id)
  msg = await cha.fetch_message(payload.message_id)
  gen = bot.get_channel(cafe.Chat.General) or await bot.fetch_channel(cafe.Chat.General)
  entrance = bot.get_channel(cafe.Verify.Entrance) or await bot.fetch_channel(cafe.Verify.Entrance)
  auth_role = payload.member.guild.get_role(928077514411233350) or await payload.member.guild.fetch_role(928077514411233350)
  print(auth_role.members)
  print(payload.member)
  if payload.member in autho_role.members:
    if cha != entrance: return
    if str(payload.emoji) == rcheck:
      await msg.author.add_roles(rolev)
      await msg.author.remove_roles(roleu)
      await msg.delete()
      if memberz == Fenne:
        words=f"Everyone please welcome <@!{msg.author.id}> {b.wt}"
      else:     
        words=f"Everyone please welcome <@!{msg.author.id}> {b.wt} Welcomed by <@!{payload.member.id}>"
      generalmsg = await general.send(words)
      await logs.send(f"""```
         WELCOMED LOG
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
Welcomed user: 
 {msg.author}
              
Welcomed userid: 
 {msg.author.id}
              
Message content: 
 {msg.content}
              
Welcomer user: 
 {payload.member}
              
Welcomer userid: 
 {payload.member.id}
              
              
Log time: {generalmsg.created_at}
        
         END LOG              
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯```""")
      if str(emoji) == "<:x_:962053785566474290>":
        await msg.delete()
        generalmsgz = await author.send("Your application to The Femboy Cafe was rejected. Please try again!")
        await logs.send(f"""```
       UNWELCOMED LOG
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
Welcomed user: 
 {msg.author}
              
Welcomed userid: 
 {auth}
              
Message content: 
 {msg.content}
              
Welcomer user: 
 {member}
              
Welcomer userid: 
 {memberz}
              
              
Log time: {generalmsgz.created_at}
        
         END LOG              
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯```""")
      
async def main_start():
    async with bot:
        await bot.start(str(key)) 
        #gen.start()
        #bump.start()
        #bystander.start()
        #await bot.add_cog(test)
        
run(main_start())
