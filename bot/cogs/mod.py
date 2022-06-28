from discord.ext import tasks, commands
import discord
import asyncio
import sys
import os
import traceback
sys.path.append('..')
from extras.text_zone import all_id as id_0
import extras.IDS as ID
from zoneinfo import ZoneInfo
import datetime as dt
from typing import Optional
sys.path.append('../..')
from passcodes import main
sudoPassword=main.dbc
sys.path.append('busboy/bot')
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

      
  

class mod(commands.Cog):
  def __init__(self, bot):
    self.bot=bot

  async def cog_check(self, ctx):
    logs = self.bot.get_channel(ID.fbc.logs.gen) or await self.bot.get_channel(ID.fbc.logs.gen)
    if ctx.guild is None or ctx.guild.id == ID.server.cafe:
      guild = self.bot.get_guild(ID.server.cafe) or await self.bot.fetch_guild(ID.server.cafe) 
      member = guild.get_member(ctx.message.author.id) or await guild.fetch_member(ctx.message.author.id)
      mod = member.get_role(928077514411233350)
      if mod in member.roles: return True
      await ctx.send("You are not allowed to use that command")
      
      embed = discord.Embed(
          color=0xff0000,
          title="COMMAND USAGE NOT PERMITED"
        )
      embed.add_field(name="User: ", value=ctx.author, inline=True)
      embed.add_field(name="ID: ", value=ctx.author.id, inline=True)
      embed.add_field(name="Command used: ", value=ctx.message.content, inline=True)
      embed.add_field(name="Date/time: ", value=ctx.message.created_at, inline=True)
      
      await logs.send(embed=embed)
      return False
    else:
      embed = discord.Embed(
        color=0xff0000,
        title="ALERT"
      )
      embed.add_field(name="Guild: ", value=ctx.guild.name)
      embed.add_field(name="Guild ID: ", value=ctx.guild.id)
      embed.add_field(name="User: ", value=ctx.author, inline=True)
      embed.add_field(name="ID: ", value=ctx.author.id, inline=True)
      embed.add_field(name="Command used: ", value=ctx.message.content, inline=True)
      embed.add_field(name="Date/time: ", value=ctx.message.created_at, inline=True)
      await logs.send(embed=embed)
      return False

  @commands.command(hidden=True)
  async def sync_id(self, ctx, Id):
    self.bot.tree.copy_global_to(guild=discord.Object(id=Id))

  @commands.command(hidden=True)
  async def MODtest(self, ctx):
    await ctx.send("workin")

  @commands.command(hidden=True)
  async def restart(self, ctx):
    have_role = False
    if ctx.guild.id != ID.server.fbc:
      return
    for i in ctx.guild.roles:
      if i in ctx.author.roles and i.id == 983492505167339670:
        have_role = True
    
    if have_role == False:
        return
    if ctx.channel.id != 970411065638780988:
        return
    os.system('exit && start')
  @commands.command(hidden=True)
  async def speak(self, ctx, channel: Optional[discord.TextChannel], member: Optional[discord.Member], *, message: str):
    """Sends a message as the bot. Only works in the busboy-cmds channel.
    :
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
  async def verify(self, ctx):
    """Reply this command to verify a member verification."""
    msg=ctx.message
    gen=self.bot.get_channel(cafe.chat.gen) or await self.bot.fetch_channel(cafe.chat.gen)
    admin=discord.utils.get(msg.author.guild.roles, name="Server Staff")
    logs=self.bot.get_channel(ID.fbc.logs.verify) or await self.bot.fetch_channel(ID.fbc.logs.verify)
    logs2 = self.bot.get_channel(cafe.mod.logger) or await self.bot.get_channel(cafe.mod.logger)
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
        await gen.send(f"Welcome <@{member.id}>, please make a <#{cafe.friends.bio}> and enjoy your stay! <@&986761088852967504> give our newest members a warm welcome.")
      else:
        await gen.send(f"Welcome <@{member.id}>, please make a <#{cafe.friends.bio}> and enjoy your stay! <@&986761088852967504> give our newest members a warm welcome. Verified by <@{msg.author.id}>")
      time = await msg.channel.send("time holder(dont delete)")
      embed=discord.Embed(
          color=0x00ff28,
          title=f"Welcome {member.mention}"
        )
      embed.add_field(name="Welcomed user: ", value=member, inline=True)
      embed.add_field(name="Welcomed ID: ", value=member.id, inline=True)
      embed.add_field(name="Application: ", value=msg.reference.resolved.content, inline=False)
      embed.add_field(name="Welcomer: ", value=msg.author, inline=True)
      embed.add_field(name="Welcomers ID: ", value=msg.author.id, inline=True)
      embed.add_field(name="Date/time: ", value=time.created_at, inline=True)
      await logs2.send(embed=embed)
      await logs.send(embed=embed)
      await msg.channel.delete()

  @commands.command()
  async def unverify(self, ctx, member: discord.Member=None):
    """Reply this command to unverify a member."""
    msg=ctx.message
    admin=discord.Object(id=928077514411233350)
    logs=self.bot.get_channel(ID.fbc.logs.gen) or await self.bot.fetch_channel(ID.fbc.logs.gen)
    logs2=self.bot.get_channel(cafe.mod.logger) or await self.bot.get_channel(cafe.mod.logger)
    welcomed=discord.Object(id=889011345712894002)
    unwelcomed=discord.Object(id=889011029428801607)
    if msg.guild is None:
      return

    if not any([msg.reference, member]): # warns if no member is supplied or there's no message reference
      return await ctx.send("Reply to a message or specify the member.", delete_after=10.0)
        
    member = msg.reference.resolved.author if not member else member

    await member.add_roles(unwelcomed)
    await member.remove_roles(welcomed)

    embed=discord.Embed(
      color=0xff0000,
      title=f"Unverified {member.mention}"
    )
    embed.add_field(name="Unverified user: ", value=member, inline=True)
    embed.add_field(name="Unverified ID: ", value=member.id, inline=True)
    embed.add_field(name="Mod who unverified: ", value=msg.author, inline=True)
    embed.add_field(name="Mods ID: ", value=msg.author.id, inline=True)
    embed.add_field(name="Date/time: ", value=msg.created_at, inline=True)
    await logs.send(embed=embed)
    await logs2.send(embed=embed)

  @commands.command()
  async def deny(self, ctx, member: discord.Member=None):
    """Reply this command to deny a member verification."""
    msg=ctx.message
    admin=discord.utils.get(msg.author.guild.roles, name="Server Staff")
    logs=self.bot.get_channel(ID.fbc.logs.denied) or await self.bot.fetch_channel(ID.fbc.logs.denied)
    logs2=self.bot.get_channel(cafe.mod.logger) or await self.bot.get_channel(cafe.mod.logger)
    if msg.guild is None:
      return

    if msg.author.id == botuser:
      return

    if msg.channel.id != cafe.verify:
      if msg.channel.category_id != cafe.cats.verify:
        return

      if admin not in msg.author.roles:
        return

      if not any([msg.reference, member]): # warns if no member is supplied or there's no message reference
        return await ctx.send("Reply to a message or specify the member.", delete_after=10.0)
      
      member = msg.reference.resolved.author if not member else member

      await member.timeout(dt.timedelta(days=7), reason="denied application try again later") 
      time = await msg.channel.send("time holder(dont delete)")
      embed=discord.Embed(
        color=0xff0000,
        title=f"Denied {member.mention}"
      )
      embed.add_field(name="Denied user: ", value=member, inline=True)
      embed.add_field(name="Denied ID: ", value=member.id, inline=True)
      embed.add_field(name="Denier: ", value=msg.author, inline=True)
      embed.add_field(name="Deniers ID: ", value=msg.author.id, inline=True)
      embed.add_field(name="Date/time: ", value=time.created_at, inline=True)
      await logs.send(embed=embed)
      await logs2.send(embed=embed)
      await msg.channel.delete()
      

  @commands.command()
  async def getroles(self, ctx, member: discord.Member=None):
    """Reply this command to alert a new member to get roles or profile picture."""
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

    if not any([msg.reference, member]): # warns if no member is supplied or there's no message reference
        return await ctx.send("Reply to a message or specify the member.", delete_after=10.0)

    member = msg.reference.resolved.author if not member else member

    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Click me to get pronoun roles", url="https://discordapp.com/channels/871938782092480513/889009278088773632/889009427213066240"))
    await member.send("You need roles(pronoun roles are required) and a profile picture for your verification to get accepted! Click below to go to the <#889009278088773632> channel.", view=view)
    await ctx.message.delete()

    logs = self.bot.get_channel(ID.fbc.logs.gen) or await self.bot.fetch_channel(ID.fbc.logs.gen)
    logs2 = self.bot.get_channel(cafe.mod.logger) or await self.bot.get_channel(cafe.mod.logger)
    await logs.send(f"{ctx.author}(id: {ctx.author.id}) told {member}(id: {member.id}) to get roles.")
    await logs2.send(f"{ctx.author}(id: {ctx.author.id}) told {member}(id: {member.id}) to get roles.")
    await ctx.send(f"{member.mention} has been told to get roles by a staff member")
  
  @commands.command()
  async def welcome(self, ctx, member: discord.Member=None):
    """Reply this command to alert a new member how to verify/dm them the welcome message."""
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

    if not any([msg.reference, member]): # warns if no member is supplied or there's no message reference
      return await ctx.send("Reply to a message or specify the member.", delete_after=10.0)

    member = msg.reference.resolved.author if not member else member

    await member.send(f"""{member.mention} Welcome! 
To verify for the server please answer the survey.
```
1. How did you find the server? 
2. Why did you join?
3. Do you identify as LGBTQ+?
```
**You must have <#889009278088773632> and a profile picture.**
    """)
    await ctx.message.delete()

    logs = self.bot.get_channel(ID.fbc.logs.gen) or await self.bot.fetch_channel(ID.fbc.logs.gen)
    logs2 = self.bot.get_channel(cafe.mod.logger) or await self.bot.get_channel(cafe.mod.logger)
    text=f"{member.mention} have been dmed the welcome message."
    text2=f"{ctx.author}(id: {ctx.author.id}) made the bot dm {member}(id: {member.id}) the welcome message."
    await logs.send(text2)
    await logs2.send(text2)
    await ctx.send(text)
