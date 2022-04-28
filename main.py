#cogs--------------------------------------------------------------------------------------------  
#import version2_0 as twozz
#test=twozz.test()
#import------------------------------------------------------------------------------------------  

import os
import discord
import time
import traceback
import asyncio
from discord.ext import tasks, commands
import os


#EXTRA_TEXT--------------------------------------------------------------------------------------

from text_zone import BIG as b
from text_zone import all_id as id_0
Fenne = 474984052017987604 
Equinox = 599059234134687774
welcome_text = b.wt
r1 = id_0.fenne
rcheck = id_0.check
r3 = id_0.heart
r4 = id_0.P_heart
r5 = id_0.thumb_up
null = None
botuser = 955440279450710076
key = os.environ['API_ENDPOINT']
#intents----------------------------------------------------------------------------------------

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix=commands.when_mentioned_or('F^ ', 'F^'), intents=intents)

#-----------------------------------------------------------------------------------------------

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
        await mod.send(allwordm)
@bot.event
async def on_member_join(mem):
  try:
    await mem.send(f"""⇀ Welcome <@!{mem.id}> {b.welcome_text_dm}""")
  except:
    print("not accepting dms")
    

@bot.event
async def on_guild_channel_create(cha):
  if cha.category.id == 888482510013628476:
    print("found category")
    if "ticket" in str(cha.name):
      print("Found channel ticket")
      time.sleep(3)
      await cha.send("Hey there, how can we help you?")

@bot.event
async def on_message(msg):
    if msg.author.id != botuser:
        def is_me(msg):
            return msg.author.id == botuser
        if msg.channel.id == 940444730515415100:
            await msg.add_reaction(r1)
            await msg.add_reaction(rcheck)
            await msg.add_reaction(r3)            
            await msg.add_reaction(r4)            
            await msg.add_reaction(r5)
        elif msg.channel.id == 901207969922949161:
            await msg.add_reaction(rcheck)
        elif msg.channel.id == 888482614351134720:
            bioxtt = bot.get_channel(888482614351134720) or await bot.fetch_channel(888482614351134720)
            await bioxtt.purge(limit=2, check=is_me)
            await bioxtt.send(b.bt)
        elif msg.channel.id == 904501391299608586:
            if msg.author.id != botuser:
                self_xtt = bot.get_channel(904501391299608586) or await bot.fetch_channel(904501391299608586)
                await self_xtt.purge(limit=2, check=is_me)
                await self_xtt.send("Server boosters can post <#904501391299608586> in every 30 minutes!") 
        elif msg.channel.category_id == 889022488720330816:
            if msg.channel.id != 889219939192410222:
                await msg.add_reaction(r1)
                await msg.add_reaction(rcheck)
                await msg.add_reaction(r3)            
                await msg.add_reaction(r4)           
                await msg.add_reaction(r5)
        else:
            await bot.process_commands(msg)


@bot.event
async def on_raw_reaction_add(payload):
  user = bot.get_user(payload.user_id) 
  channel = bot.get_channel(payload.channel_id)
  msg = await channel.fetch_message(payload.message_id)
  member = payload.member
  auth = msg.author.id
  author = msg.author
  emoji = str(payload.emoji)
  auth_role = member.guild.get_role(945086022142808075)
  entrance = bot.get_channel(957737342028890112) or await bot.fetch_channel(957737342028890112)
  if auth_role in payload.member.roles:
      rolev = payload.member.guild.get_role(889011345712894002) 
      roleu = payload.member.guild.get_role(889011029428801607)
      logs = bot.get_channel(956322799411150952) or await bot.fetch_channel(956322799411150952)
      general = bot.get_channel(950085161872154694) or await bot.fetch_channel(950085161872154694)
      admin_role = member.guild.get_role(945086022142808075)
      memberz = member.id
      if channel == entrance:
          if str(emoji) == rcheck:
              await msg.author.add_roles(rolev)
              await msg.author.remove_roles(roleu)
              await msg.delete()
              if memberz == Fenne:
                  allwrodg=f"Everyone please welcome <@!{auth}> {welcome_text}"
              else:     
                  if admin_role in member.roles:
                      allwrodg=f"Everyone please welcome <@!{auth}> {b.wt} Welcomed by <@!{memberz}>"
              generalmsg = await general.send(allwrodg)
             
              await logs.send(f"""```
         WELCOMED LOG
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
      
async def main(bot, key):
    #async with bot:
        #gen.start()
        #bump.start()
        #bystander.start()
        #await bot.add_cog(test)
    await bot.start(key) 
        
asyncio.run(main(bot, key))

