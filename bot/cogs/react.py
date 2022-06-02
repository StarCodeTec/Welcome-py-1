import discord
from discord.ext import tasks, commands
import sys
sys.path.append('..')
from extras.text_zone import BIG as b
from extras.text_zone import all_id as id_0
import extras.System_Id as ID

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
class auto_react(commands.Cog):
  def __init__(self, bot):
    self.bot=bot
    
  @cog.listener()
  async def on_message(self, msg):
    if msg.guild is None:return
    if msg.author.id == botuser:return
    if msg.channel.id == cafe.Little_fenne.News or msg.channel.category_id == cafe.cats.Selfies:
      if msg.channel.id == cafe.Selfies.Comments:return
      rx1 = await msg.guild.fetch_emoji(925500399656509489)
      rxcheck = await msg.guild.fetch_emoji(919007866940182589)
      await msg.add_reaction(rx1)
      await msg.add_reaction(rxcheck)
      await msg.add_reaction(r3)            
      await msg.add_reaction(r4)            
      await msg.add_reaction(r5)
    elif msg.channel.id == cafe.Mod.News:
      rxcheck = await msg.guild.fetch_emoji(919007866940182589)
      await msg.add_reaction(rxcheck)
    elif msg.channel.id == 976322762631172147:
      await msg.add_reaction("📥")
  
  @cog.listener()
  async def on_raw_reaction_add(self, payload):
    guild=self.bot.get_guild(payload.guild_id) or await self.bot.fetch_guild(payload.guild_id)
    channel=guild.get_channel(payload.channel_id) or await guild.fetch_channel(payload.channel_id)
    msg=await channel.fetch_message(payload.message_id)
    if msg.author.id == botuser:return
    if payload.member.id == botuser: return
    if guild is None:return
    if guild.id != ID.cafe_channel:return
    if channel.id == 976322762631172147:
      if str(payload.emoji) !="📥":return
      send = self.bot.get_channel(976322463807971389) or await self.bot.fetch_channel(976322463807971389) 
      inbox_msg = await send.send(f"<@{payload.member.id}> is interested <@{msg.author.id}>")
      await self.bot.inbox.upsert({"_id": inbox_msg.id, "user": payload.user_id, "orignal": msg.id})
    
  @cog.listener()
  async def on_raw_reaction_remove(self, payload):
    guild=self.bot.get_guild(payload.guild_id) or await self.bot.fetch_guild(payload.guild_id)
    channel=guild.get_channel(payload.channel_id) or await guild.fetch_channel(payload.channel_id)
    msg=await channel.fetch_message(payload.message_id)

    if channel.id != 976322762631172147:return
    if msg.author.id == botuser:return
    if guild is None:return
    
    filter = {"user": payload.user_id, "orignal": msg.id}

    data = await self.bot.inbox.find_by_custom(filter)
    if not data:return
    
    msg_to_delete = await inbox.fetch_message(data["_id"])

    inbox = self.bot.get_channel(976322463807971389)
  
    await msg_to_delete.delete()

