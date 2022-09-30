import sys
sys.path.append('..')
import extras.IDS as ID
cafe = ID.cafe
from imports.discord import *

class Bios(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_raw_message_edit(self, payload):
    if payload.channel_id != cafe.friends.explore:return

    channel = self.bot.get_channel(payload.channel_id)
    msg     = await channel.fetch_message(payload.message_id)

    await self.bot.bio.upsert(
      {
        "_id": msg.author.id,
        "bio": str(msg.content),
         "msg_id": msg.id
      })
        
  @commands.command()
  async def bio(self, ctx, member: discord.Member=None):
    """Posts someones bio."""
    member   = ctx.author if not member else member
    data     = await self.bot.bio.find(member.id)
    guild    = self.bot.get_guild(ID.server.cafe) or await self.bot.fetch_guild(ID.server.cafe)
    mem      = await guild.fetch_member(ctx.author.id)
    has_role = False;roles = guild.roles
    for i in roles:
      if i in mem.roles and i.id == 889011345712894002:has_role = True
      else:pass
    if has_role==False:return
    
    if not data:
      if member == ctx.author: return await ctx.send("You don't have a bio stored.")
      else:                    return await ctx.send("They don't have a bio stored.")
    
    bio_channel = self.bot.get_channel(cafe.friends.explore) or await self.bot.fetch_channel(cafe.friends.explore)
    message     = await bio_channel.fetch_message(data["msg_id"])
  
    view = discord.ui.View();view.add_item(discord.ui.Button(label="Go to bio post", url=message.jump_url))
    await ctx.send(discord.utils.escape_mentions(f"**Bio for {member.name}**\n{data['bio']}"), view=view)
