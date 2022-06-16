import discord
from discord.ext import commands
from extras.IDS import cafe

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
    if ctx.channel.id != cafe.chat.bot or ctx.channel.id != cafe.friends.explore or ctx.channel.id == ID.fbc.commands:
      print("--")
      return
    guild = self.bot.get_guild(ID.server.cafe) or await self.bot.fetch_guild(ID.server.cafe) 
    member = guild.get_member(ctx.message.author.id) or await guild.fetch_member(ctx.message.author.id)
    reg = member.get_role(889011345712894002)
    if reg not in ctx.author.roles: 
      print("-")
      return
    if not data:
      if member == ctx.author:
        return await ctx.send("You don't have a bio stored.")
      else:
        return await ctx.send("They don't have a bio stored.")
    
    bio_channel = self.bot.get_channel(cafe.friends.bio)
    msg = await bio_channel.fetch_message(data["msg_id"])
  
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Go to bio post", url=msg.jump_url))
  
    await ctx.send(discord.utils.escape_mentions(f"**Bio for {member.name}**\n{data['bio']}"), view=view)
