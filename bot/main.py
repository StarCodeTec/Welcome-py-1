from text_zone import welcome_text_dm as wtd
import os
import discord
import time
import datetime
from zoneinfo import ZoneInfo
import traceback
import asyncio
from discord.ext import tasks, commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
key = os.getenv('MAIN_KEY')
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix=commands.when_mentioned_or('F^ ', 'F^'), intents=intents)
welcome_text = "to the server. Feel free to make a bio and enjoy your stay!"
Fenne = 474984052017987604 
Equinox = 599059234134687774

@bot.check
async def check(ctx):
    logs = bot.get_channel(956322799411150952) or await bot.fetch_channel(956322799411150952)
    member = ctx.author
    admin_V = ctx.guild.get_role(955572063383482479)
    if int(member.id) == Equinox or int(member.id) == Fenne or admin_V in ctx.member.roles:
        print(member)
        print(member.id)
        id_member = f"""```
        AUTHORIZED ACCESS 
        Command: {ctx.command}
        Member id: {member.id} 
        Member name: {member}```"""
        await logs.send(id_member)
        print("true")
        return(True)
    else:
        print(member)
        print(member.id)
        id_member = f"""```
UNAUTHORIZED ACCESS 
Command: {ctx.command}
Member id: {member.id} 
Member name: {member}
```"""
        await logs.send(id_member)
        return(False)

@tasks.loop(time=[datetime.time(hour=10, tzinfo=ZoneInfo("US/Eastern")), datetime.time(hour=18, tzinfo=ZoneInfo("US/Eastern"))], count=None)
async def botxc():
        botxc = bot.get_channel(940377877214548008) or await bot.fetch_channel(940377877214548008)
        await botxc.send("Check out the pinned message to bump the server so more people can join!")

@tasks.loop(time=[datetime.time(hour=9, tzinfo=ZoneInfo("US/Eastern")), datetime.time(hour=16, tzinfo=ZoneInfo("US/Eastern")), datetime.time(hour=21, tzinfo=ZoneInfo("US/Eastern"))], count=None)
async def gen():
        gen = bot.get_channel(950085161872154694) or await bot.fetch_channel(950085161872154694)
        await gen.send(content="Remember everyone, please don't use profanity here!", delete_after=5)

@tasks.loop(time=[datetime.time(hour=3, minute=0, second=0, microsecond=0), datetime.time(hour=6, minute=0, second=0, microsecond=0), datetime.time(hour=9, minute=0, second=0, microsecond=0), datetime.time(hour=12, minute=0, second=0, microsecond=0), datetime.time(hour=15, minute=0, second=0, microsecond=0), datetime.time(hour=18, minute=0, second=0, microsecond=0), datetime.time(hour=21, minute=0, second=0, microsecond=0), datetime.time(hour=0, minute=0, second=0, microsecond=0)], count=None)
async def bystander():
        xent = bot.get_channel(945087125831958588) or await bot.fetch_channel(945087125831958588)
        await xent.send(content="If you are a <@&889011029428801607> please verify today to join our server!", delete_after=3600)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        return
    traceback.print_exception(error)

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
  time.sleep(3)
  await mem.send(f"""⇀ Welcome <@!{mem.id}> {wtd}""")

@bot.event
async def on_guild_channel_create(cha):
  if cha.category.id == 888482510013628476:
    print("found category")
    if "ticket" in str(cha.name):
      print("Found channel ticket")
      await cha.send("Hey there, how can we help you?")
      

@bot.event
async def on_raw_reaction_add(payload):
  user = bot.get_user(payload.user_id) 
  channel = bot.get_channel(payload.channel_id)
  msg = await channel.fetch_message(payload.message_id)
  member = payload.member
  auth = msg.author.id
  emoji = str(payload.emoji)
  auth_role = member.guild.get_role(945086022142808075)
  entrance = bot.get_channel(957737342028890112) or await bot.fetch_channel(957737342028890112)
  if auth_role in payload.member.roles:
      rolev = payload.member.guild.get_role(889011345712894002)
      roleu = payload.member.guild.get_role(889011029428801607)

      if channel == entrance:
          if emoji == "✅":
              await msg.author.add_roles(rolev)
              await msg.author.remove_roles(roleu)
              await msg.delete()
              general = bot.get_channel(950085161872154694) or await bot.fetch_channel(950085161872154694)
              logs = bot.get_channel(956322799411150952) or await bot.fetch_channel(956322799411150952)
              admin_role = member.guild.get_role(945086022142808075)
              memberz = member.id
              if memberz == Fenne:
                  allwrodg=f"Everyone please welcome <@!{auth}> {welcome_text}"
              else:     
                  if admin_role in member.roles:
                      allwrodg=f"Everyone please welcome <@!{auth}> {welcome_text} Welcomed by <@!{memberz}>"
              generalmsg = await general.send(allwrodg)
              await logs.send(f"""```
         WELCOME LOG
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
              
async def main():
    async with bot:
        gen.start()
        botxc.start()
        bystander.start()
        await bot.start(key)

asyncio.run(main())

