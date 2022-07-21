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
sys.path.append('/home/dev/')
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
    command_name=ctx.content.split(' ')
    command_name2=command_name[1]
    command_name=command_name[0]
    if command_name == ".help":
      if command_name2.lower() == "mod":
        pass
      else:
        return True
    logs = self.bot.get_channel(ID.fbc.logs.gen) or await self.bot.fetch_channel(ID.fbc.logs.gen)
    print(ctx.command.name.lower())
    print(ctx.command.qualified_name)
    if ctx.guild is None or ctx.guild.id in ID.server.servers:
      guild = self.bot.get_guild(ID.server.cafe) or await self.bot.fetch_guild(ID.server.cafe) 
      member = guild.get_member(ctx.message.author.id) or await guild.fetch_member(ctx.message.author.id)
      mod = member.get_role(928077514411233350)
      dev = member.get_role(961726803288928266)
      if mod in member.roles or dev in member.roles: return True
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
  async def sync(self, ctx):
    for sever in ID.server.servers:
      synced = await self.bot.tree.sync(guild=discord.Object(id=sever))
    await ctx.send(f"Synced {len(synced)}")

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
      check = await self.bot.verifies.find(msg.author.id)
      if check is None:
        count = {
            "_id" : msg.author.id,
            "name": msg.author.name,
            "verify_count" : 1
        }
        await self.bot.verifies.insert(count)
      else:
        new_num = check["verify_count"] + 1
        count = {
            "_id" : msg.author.id,
            "name": msg.author.name,
            "verify_count" : new_num
        }
        await self.bot.verifies.update(count)
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
  async def modstats(self, ctx):
    print("1")
    if ctx.guild.id not in ID.server.servers:
      return
    print("2")
    embed = discord.Embed(title="Mod Stats", description="", color=0x00ff28)
    check = await self.bot.verifies.get_all()
    print(check)
    if check == []:
      return await ctx.send("There are no stats yet!")
    else:
      num = 0
      for x in range(len(check)):
        print("+")
        embed.description += f"{check[num]['name']} | {check[num]['verify_count']} members verified\n"
        num += 1
      
    print("1")
    await ctx.send(embed=embed)

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
    
    await ctx.message.delete()
    await member.add_roles(unwelcomed)
    await member.remove_roles(welcomed)
    await ctx.send(f"Member has been unverified by staff")

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
    zero = 0
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
    try:
      await member.send("You need roles(pronoun roles are required) and a profile picture for your verification to get accepted! Click below to go to the <#889009278088773632> channel.", view=view)
    except:
      zero = 1
      await ctx.send(f"{member.mention} \n You need roles(pronoun roles are required) and a profile picture for your verification to get accepted! Click below to go to the <#889009278088773632> channel.", view=view)
    finally:
      await ctx.message.delete()

    logs = self.bot.get_channel(ID.fbc.logs.gen) or await self.bot.fetch_channel(ID.fbc.logs.gen)
    logs2 = self.bot.get_channel(cafe.mod.logger) or await self.bot.get_channel(cafe.mod.logger)
    await logs.send(f"{ctx.author}(id: {ctx.author.id}) told {member}(id: {member.id}) to get roles.")
    await logs2.send(f"{ctx.author}(id: {ctx.author.id}) told {member}(id: {member.id}) to get roles.")
    if zero == 0:
      await ctx.send(f"{member.mention} has been told to get roles by a staff member")
  
  @commands.command()
  async def welcome(self, ctx, member: discord.Member=None):
    """Reply this command to alert a new member how to verify/dm them the welcome message."""
    zero=0
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

    try:
      await member.send(f"""{member.mention} Welcome! 
To verify for the server please answer the survey.
```
1. How did you find the server? 
2. Why did you join?
3. Do you identify as LGBTQ+?
```
**You must have <#889009278088773632> and a profile picture.**
    """)
    except:
      zero=1
      await ctx.send(f"""{member.mention} Welcome! 
      To verify for the server please answer the survey.
      ```
      1. How did you find the server? 
      2. Why did you join?
      3. Do you identify as LGBTQ+?
      ```
      **You must have <#889009278088773632> and a profile picture.**
          """)
    finally:
      await ctx.message.delete()

    logs = self.bot.get_channel(ID.fbc.logs.gen) or await self.bot.fetch_channel(ID.fbc.logs.gen)
    logs2 = self.bot.get_channel(cafe.mod.logger) or await self.bot.get_channel(cafe.mod.logger)
    text=f"{member.mention} have been dmed the welcome message."
    text2=f"{ctx.author}(id: {ctx.author.id}) made the bot dm {member}(id: {member.id}) the welcome message."
    await logs.send(text2)
    await logs2.send(text2)
    if zero == 0:
      await ctx.send(text)
