from discord.ext import tasks, commands
import discord
import asyncio
import sys
sys.path.append('..')
from extras.text_zone import all_id as id_0
import extras.IDS as ID
from zoneinfo import ZoneInfo
import datetime as dt
from typing import Optional

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

      
  

class MOD(commands.Cog):
  def __init__(self, bot):
    self.bot=bot

  async def cog_check(self, ctx):
    logs = self.bot.get_channel(ID.fbc.logs.gen) or await self.bot.get_channel(ID.fbc.logs.gen)
    if ctx.guild is None:
      guild = self.bot.get_guild(ID.server.cafe) or await self.bot.fetch_guild(ID.server.cafe) 
      member = guild.get_member(ctx.message.author.id) or await guild.fetch_member(ctx.message.author.id)
      mod = member.get_role(928077514411233350)
      if mod in member.roles: return True
      msg1 = "You are not allowed to use that command"
      msg2 = f"{ctx.message.author} just tried using {ctx.message.content} their id is {ctx.message.author.id} in dms"
      await ctx.send(msg1)
      await logs.send(msg2)
      return False
      
    if ctx.guild.id == ID.server.cafe:
      mod = discord.utils.get(ctx.guild.roles, name="-------- Staff Rank --------")
      if mod not in ctx.message.author.roles:
        msg1 = "You are not allowed to use that command"
        msg2 = f"{ctx.message.author} just tried using {ctx.message.content} their id is {ctx.message.author.id}"
        await ctx.send(msg1)
        await logs.send(msg2)
        return False
      else:
        return True
    elif ctx.guild.id == ID.server.fbc:
      return True
    else:
      msg1 = f"""        ALERT:
Someone used {ctx.message.content} outside of the cafe, the guild name is {ctx.guild.name} and the user is {ctx.message.author} plus their id is {ctx.message.id}
          """
      await logs.send(msg1)
      return False
    
      
  @commands.command()
  async def bio(self, ctx, member: discord.Member=None):
    """Posts someones bio."""
    member = ctx.author if not member else member
    data = await self.bot.bio.find(member.id)
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

  @commands.command(hidden=True)
  async def MODtest(self, ctx):
    await ctx.send(ctx.message.id)
  @commands.command(hidden=True)
  async def speak(self, ctx, channel: Optional[discord.TextChannel], member: Optional[discord.Member], *, message: str):
    """Sends a message as the bot. Only works in the busboy-cmds channel.
    
    Example usage:
    .speak Hello people (posts in current channel)
    .speak #general Hello people (posts in #general)
    .speak 474984052017987604 Hello people (posts in current channel and pings the person with that ID)
    .speak #general 474984052017987604 Hello people (posts in #general and pings the person with that ID)"""
    if ctx.channel.id != cafe.AP.cmds:
      return
      
    channel = channel if channel else ctx.channel

    await channel.send(f"{message} {member.mention}" if member else message)

  @commands.command()
  async def deny(self, ctx):
    "Denys a user if you reply to them in the verification proccess"
    msg=ctx.message
    admin=discord.utils.get(msg.author.guild.roles, name="Server Staff")
    denied_logs=self.bot.get_channel(ID.fbc.logs.denied) or await self.bot.fetch_channel(ID.fbc.logs.denied)
    if msg.guild is None:
      return

    if msg.author.id == botuser:
      return

    if msg.channel.id != cafe.verify:
      if msg.channel.category_id != cafe.cats.verify:
        return

      if msg.reference == None:
        return

      if admin not in msg.author.roles:
        return
      
      member = msg.reference.resolved.author
      await member.timeout(dt.timedelta(days=7), reason="denied application try again later") 
      time = await msg.channel.send("time holder(dont delete)")
      await denied_logs.send(f"\tDenied <@{member.id}>\n Denied id: {member.id}\nDenied:{member}\nDenied by: <@{msg.author.id}>\nDenied by user: {msg.author}\n\nDenied at: {time.created_at}")
      await msg.channel.delete()
      
  @commands.command()
  async def verify(self, ctx):
    "Verifys a user if you reply to them in the verification proccess"
    msg=ctx.message
    gen=self.bot.get_channel(cafe.chat.gen) or await self.bot.fetch_channel(cafe.chat.gen)
    admin=discord.utils.get(msg.author.guild.roles, name="Server Staff")
    verify_logs=self.bot.get_channel(ID.fbc.logs.verify) or await self.bot.fetch_channel(ID.fbc.logs.verify)
    welcomed=discord.Object(id=889011345712894002)
    unwelcomed=discord.Object(id=889011029428801607)
    if msg.guild is None:
      return

    if msg.author.id == botuser:
      return

    if msg.channel.id != cafe.verify:
      if msg.channel.category_id != cafe.cats.verify:
        return

      if msg.reference == None:
        return

      member = msg.reference.resolved.author
      if admin not in msg.author.roles:
        return
     
      await member.remove_roles(unwelcomed)
      await member.add_roles(welcomed)
      if msg.author.id == Fenne:
        await gen.send(f"Welcome <@{member.id}> please make a <#{cafe.friends.bio}> and enjoy your stay.")
      else:
        await gen.send(f"Welcome <@{member.id}> please make a <#{cafe.friends.bio}> and enjoy your stay. Welcomed by <@{msg.author.id}>")
      time = await msg.channel.send("time holder(dont delete)")
      await verify_logs.send(f"\tWelcome <@{member.id}>\nWelcome id: {member.id}\nWelcome:{member}\n{msg.reference.resolved.content}\n\nWelcomed by: <@{msg.author.id}>\nWelcomer: {msg.author}\n\nWelcomed at: {time.created_at}")
      await msg.channel.delete()
