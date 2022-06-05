from discord.ext import commands
import sys
sys.path.append('..')
from extras.text_zone import all_id as id_0
import extras.IDS as ID

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
    self.cooldown = commands.CooldownMapping.from_cooldown(1, 30, commands.BucketType.member) # 1 reaction ADD every 30 seconds.
    
  @cog.listener()
  async def on_message(self, msg):
    if msg.guild is None:
      return

    if msg.author.id == botuser:
      return

    if msg.channel.id == cafe.home.insta or msg.channel.category_id == cafe.cats.selfies:
      if msg.channel.id == cafe.selfies.comments:
        return

      rx1 = await msg.guild.fetch_emoji(925500399656509489)
      rxcheck = await msg.guild.fetch_emoji(919007866940182589)
      await msg.add_reaction(rx1)
      await msg.add_reaction(rxcheck)
      await msg.add_reaction(r3)          
      await msg.add_reaction(r4)          
      await msg.add_reaction(r5)
    
    elif msg.channel.id == cafe.mod.news:
      rxcheck = await msg.guild.fetch_emoji(919007866940182589)
      await msg.add_reaction(rxcheck)
    
    elif msg.channel.id == cafe.friends.connect:
      await msg.add_reaction("📥")
  
  @cog.listener()
  async def on_raw_reaction_add(self, payload):

    guild=self.bot.get_guild(payload.guild_id) or await self.bot.fetch_guild(payload.guild_id)
    channel=guild.get_channel(payload.channel_id) or await guild.fetch_channel(payload.channel_id)
    msg=await channel.fetch_message(payload.message_id)
    
    
    if msg.author.id == botuser:
      return
    
    if payload.member.id == botuser:
      return
    
    if guild is None:
      return
    
    if guild.id != ID.server.cafe:
      return
    
    if channel.id != cafe.friends.connect:
      return
    
    if payload.emoji.id == 973078040336797696:
      """await self.bot.bio.upsert(
          {
            "_id":msg.author.id,
            "bio":msg.content
          }
        )"""
        
        await msg.clear_reactions()
        
    if str(payload.emoji) !="📥":
      return
          
    # ensures people can't spam reactions
    # uses a rate limit bucket
    bucket = self.cooldown.get_bucket(msg)
    retry_after = bucket.update_rate_limit()

    if retry_after: # rate limited. don't continue
      return await payload.member.send("Please wait a little bit before reacting again.")
    
    send = self.bot.get_channel(cafe.friends.inbox) or await self.bot.fetch_channel(cafe.friends.inbox) 
    inbox_msg = await send.send(f"<@{payload.member.id}> is interested <@{msg.author.id}>")
    
    await self.bot.inbox.upsert(
      {
        "_id": inbox_msg.id,
        "user": payload.user_id,
        "orignal": msg.id, 
      }
    )
    
  @cog.listener()
  async def on_raw_reaction_remove(self, payload):
    guild=self.bot.get_guild(payload.guild_id) or await self.bot.fetch_guild(payload.guild_id)
    channel=guild.get_channel(payload.channel_id) or await guild.fetch_channel(payload.channel_id)
    msg=await channel.fetch_message(payload.message_id)

    if channel.id != cafe.friends.connect:
      return
    
    if msg.author.id == botuser:
      return
    
    if guild is None:
      return
    
    filter = {"user": payload.user_id, "orignal": msg.id}

    data = await self.bot.inbox.find_by_custom(filter)
    
    if not data:
      return
    
    inbox = self.bot.get_channel(cafe.friends.inbox)

    msg_to_delete = await inbox.fetch_message(data["_id"])
    await msg_to_delete.delete()

    await self.bot.inbox.delete(data["_id"]) # We don't need to store it anymore
