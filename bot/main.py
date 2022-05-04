#cogs--------------------------------------------------------------------------------------------  
   
#personal_import---------------------------------------------------------------------------------
from text_zone import BIG as b
from text_zone import all_id as id_0
import System_Id as SI

#import------------------------------------------------------------------------------------------
import os
import discord
import time
import traceback
import asyncio
from discord.ext import tasks, commands

#EXTRA_VARS--------------------------------------------------------------------------------------
key = os.environ['CUSTOM_ENV']
null = None
welcome_text = b.wt
r1 = id_0.fenne
rcheck = id_0.check
r3 = id_0.heart
r4 = id_0.P_heart
r5 = id_0.thumb_up
GEN = int(SI.cafe.Chat.General)

#intents----------------------------------------------------------------------------------------
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix=commands.when_mentioned_or('F^ ', 'F^'), intents=intents)
botuser = 955440279450710076
#-----------------------------------------------------------------------------------------------

@bot.event
async def on_message(msg): 
    auth = msg.author.id
    channel = msg.channel.id
    if auth == botuser:return
    def is_me(msg):
        return msg.author.id == 955440279450710076
    async def react():
        await msg.add_reaction(r1)
        await msg.add_reaction(rcheck)
        await msg.add_reaction(r3)            
        await msg.add_reaction(r4)            
        await msg.add_reaction(r5)
    if channel == SI.cafe.Chat.Bio:
        bioxtt = bot.get_channel(888482614351134720) or await bot.fetch_channel(888482614351134720)
        await bioxtt.purge(limit=2, check=is_me)
        await bioxtt.send(b.bt)
    
    
    
    
@bot.event
async def on_raw_reaction_add(payload):
  cafe = bot.get_channel(payload.channel_id)
  msg = await cafe.fetch_message(payload.message_id)
  author = msg.author #Reacted
  member = payload.member #Reacter
  gen = bot.get_channel(GEN) or await bot.fetch_channel(GEN)
  auth_role = member.guild.get_role(928077514411233350) or await member.guild.fetch_role(928077514411233350)
  if auth_role in member.roles: 
      await gen.send(auth_role)
      await gen.send(member.roles)
      await gen.send("test")

    
async def main_start():
    async with bot:
        #gen.start()
        #bump.start()
        #bystander.start()
        #await bot.add_cog(test)
        await bot.start(str(key)) 

asyncio.run(main_start())
