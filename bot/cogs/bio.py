import discord
from discord.ext import commands
import sys
sys.path.append('..')
from extras.text_zone import all_id as id_0
import extras.IDS as ID
cafe = ID.cafe

class Bios(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_raw_message_edit(self, payload):
    if payload.channel_id != cafe.friends.bio:
      return

    channel = self.bot.get_channel(payload.channel_id)
    msg = await channel.fetch_message(payload.message_id)

    await self.bot.bio.upsert(
      {
        "_id": msg.author.id,
        "bio": str(msg.content),
         "msg_id": msg.id
      }
    )
        
  @commands.command()
  async def bio(self, ctx, member: discord.Member=None):
    """Posts someones bio."""
    member = ctx.author if not member else member
    data = await self.bot.bio.find(member.id)
    if ctx.channel.id != ID.cafe.chat.bot:
      print("----")
      if ctx.channel.id != ID.cafe.friends.explore:
        print("---")
        if ctx.channel.id != ID.fbc.commands:
          print("--")
          return
    guild = self.bot.get_guild(ID.server.cafe) or await self.bot.fetch_guild(ID.server.cafe)
    roles = guild.roles
    member = await guild.fetch_member(ctx.author.id)
    has_role = False
    for i in roles:
      if i in member.roles and i.id == 889011345712894002:
        has_role = True
      else:
        pass
    if has_role:
      pass
    else:
      return
    
    if not data:
      if member == ctx.author:
        return await ctx.send("You don't have a bio stored.")
      else:
        return await ctx.send("They don't have a bio stored.")
    
    bio_channel = self.bot.get_channel(cafe.friends.bio) or await self.bot.fetch_channel(cafe.friends.bio)
    msg = await bio_channel.fetch_message(data["msg_id"])
  
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Go to bio post", url=msg.jump_url))
  
    await ctx.send(discord.utils.escape_mentions(f"**Bio for {member.name}**\n{data['bio']}"), view=view)
