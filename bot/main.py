#imports-V2--------------------------------------------------------------------------------------
from imports.cogs       import COGS
from imports.asyncio    import *
from imports.discord    import *
from imports.time       import *
from imports.config     import *
from imports.passcodes  import *
#EXTRA_IMPORTS----------------------------------------------------------------------------------
from   extras.text_zone import BIG      as b
from   extras.text_zone import all_id   as id_0
from   extras           import IDS      as ID

cafe    =  ID.cafe
key     =  main.fenne.key

#loops------------------------------------------------------------------------------------------
@tasks.loop(time=[DT.time(hour=0, minute=0, second=0, tzinfo=ZoneInfo("US/Eastern"))])
async def purge():
  array=[cafe.friends.connect, cafe.friends.inbox]
  for channel in array:
    cha = bot.get_channel(channel) or await bot.fetch_channel(channel)
    await cha.purge(limit=500)
    if channel == cafe.friends.connect:
      await cha.send("Connect Post Example:\n```Topics:\nMood:\nActivities & Interests:```\n\nMust be text only, you can delete your status at any time!")
  
  entries = await bot.inbox.get_all()
  for entry in entries:
    await bot.inbox.delete(entry["_id"])

#-----------------------------------------------------------------------------------------------

@bot.event
async def on_member_join(mem):
  welcomed =  discord.Object(id=889011345712894002)
  regular  =  discord.utils.get(mem.guild.roles, name="Regular")
  
  try:    await mem.send(f"""⇀ Welcome <@!{mem.id}> {b.wd()}""")
  except: return
  finally:
    if regular in mem.roles: await mem.remove_roles(welcomed)
    
@bot.event
async def on_member_remove(mem): 
  bot.db.bio.delete_many({"_id": mem.id})
  cha = await bot.fetch_channel(cafe.friends.explore) or bot.get_channel(cafe.friends.explore)
  def check(msg):return msg.author.id == mem.id 
  await cha.purge(check=check)
  
@bot.event
async def on_guild_channel_create(cha):
  if cha.category.id == cafe.cats.home and "ticket" in str(cha.name):
    await asyncio.sleep(3)
    await cha.send("Hey there, how can we help you?")

  elif cha.id != cafe.verify:
    if cha.category_id != cafe.cats.verify:return
    await asyncio.sleep(2.5)
    await cha.send(b.vt())

async def main_start(run):
  async with bot:
    await bot.dpg.connect()
    purge.start()

    for gcogs in COGS: await bot.add_cog(gcogs(bot))

    await bot.start(str(key))
        
run(main_start(run))
####
