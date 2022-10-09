from click import command
from   extras            import IDS     as ID
from   imports.time      import DT      as dt
from   extras.text_zone  import BIG     as b
from   extras.buttons    import YesNo
from   imports.passcodes import main
from   imports.discord   import *
import os

sudoPassword = main.dbc
cafe         = ID.cafe

class mod(commands.Cog):
  def __init__(self, bot):self.bot=bot

  async def cog_check(self, ctx):
    if ctx.author.id == Fenne or ctx.author.id == Luna: return True
    try:
      command_name = ctx.message.content.split(' ')
      command_name = command_name[0].lower()
      if command_name == ".help":return True
    except Exception as e:       print(e)

    logs = self.bot.get_channel(ID.fbc.logs.gen) or await self.bot.fetch_channel(ID.fbc.logs.gen)
    if ctx.guild is None or ctx.guild.id in ID.server.servers:
      guild  =  self.bot.get_guild(ID.server.cafe) or await self.bot.fetch_guild(ID.server.cafe) 
      member =  guild.get_member(ctx.message.author.id) or await guild.fetch_member(ctx.message.author.id)
      mod    =  member.get_role(928077514411233350)
      dev    =  member.get_role(961726803288928266)
      if mod in member.roles or dev in member.roles: return True
      await ctx.send("You are not allowed to use that command")
      
      embed = discord.Embed(
          color=0xff0000,
          title="COMMAND USAGE NOT PERMITED"
      )

      embed.add_field(name="User: ",         value=ctx.author, inline=True)
      embed.add_field(name="ID: ",           value=ctx.author.id, inline=True)
      embed.add_field(name="Command used: ", value=ctx.message.content, inline=True)
      embed.add_field(name="Date/time: ",    value=ctx.message.created_at, inline=True)
      
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
    for sever in ID.server.servers:synced = await self.bot.tree.sync(guild=discord.Object(id=sever))
    await ctx.send(f"Synced {len(synced)}")

  @commands.command(hidden=True)
  async def MODtest(self, ctx):await ctx.send("workin")

  @commands.command(hidden=True)
  async def restart(self, ctx):
    have_role = False
    if ctx.guild.id != ID.server.fbc:return
    for i in ctx.guild.roles:
      if i in ctx.author.roles and i.id == 983492505167339670:have_role = True
    
    if have_role == False or ctx.channel.id != 970411065638780988:return
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
    if ctx.channel.id != cafe.AP.cmds:return
      
    channel = channel if channel else ctx.channel

    await channel.send(f"{message} {member.mention}" if member else message)

      
  @commands.command()
  async def verify(self, ctx):
    """Reply this command to verify a member verification."""
    msg        = ctx.message
    dpg        = self.bot.dpg
    pg         = self.bot.pg
    verify     = pg.RESULT(await dpg.fetch_one(query=pg.find('config', '_id'), values={"x": 123}), "config")["verify"]
    gen        = self.bot.get_channel(cafe.chat.gen) or await self.bot.fetch_channel(cafe.chat.gen)
    admin      = discord.utils.get(msg.author.guild.roles, name="Server Staff")
    mod_channel= self.bot.get_channel(cafe.mod.chat) or await self.bot.fetch_channel(cafe.mod.chat)        
    logs       = self.bot.get_channel(ID.fbc.logs.verify) or await self.bot.fetch_channel(ID.fbc.logs.verify)
    logs2      = self.bot.get_channel(cafe.mod.logger) or await self.bot.get_channel(cafe.mod.logger)
    welcomed   = discord.Object(id=889011345712894002)
    unwelcomed = discord.Object(id=889011029428801607)
    if not verify:
      await msg.delete()
      return await mod_channel.send(f"{ctx.author.mention} Verifications are currently disabled. Please try again once they are open.")

    if msg.guild is None or msg.author.id == botuser or msg.reference == None or admin not in msg.author.roles:return

    if msg.channel.id != cafe.verify:
      if msg.channel.category_id != cafe.cats.verify:return

    member = msg.reference.resolved.author
    check  = await self.bot.verifies.find(msg.author.id)

    await member.remove_roles(unwelcomed)
    await member.add_roles(welcomed)
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
      await self.bot.verifies.upsert(count)
    if msg.author.id == Fenne: await gen.send(f"Welcome <@{member.id}>, please make a <#{cafe.friends.explore}> and enjoy your stay! <@&986761088852967504> give our newest members a warm welcome.")
    else:                      await gen.send(f"Welcome <@{member.id}>, please make a <#{cafe.friends.explore}> and enjoy your stay! <@&986761088852967504> give our newest members a warm welcome. Verified by <@{msg.author.id}>")
    time  = await msg.channel.send("time holder(dont delete)")
    embed = discord.Embed(
        color=0x00ff28,
        title=f"Welcome {member.mention}"
    )

    embed.add_field( name="Welcomed user: ", value=member,                         inline=True )
    embed.add_field( name="Welcomed ID: ",   value=member.id,                      inline=True )
    embed.add_field( name="Application: ",   value=msg.reference.resolved.content, inline=False)
    embed.add_field( name="Welcomer: ",      value=msg.author,                     inline=True )
    embed.add_field( name="Welcomers ID: ",  value=msg.author.id,                  inline=True )
    embed.add_field( name="Date/time: ",     value=time.created_at,                inline=True )
    await logs2.send(embed=embed)
    await logs.send( embed=embed)
    await msg.channel.delete()
      
  @commands.command()
  @commands.is_owner()
  async def modstats(self, ctx):
    if ctx.guild.id not in ID.server.servers:return
    embed = discord.Embed(title="Mod Stats", description="", color=0x00ff28)
    check = await self.bot.verifies.get_all()
    check.sort(key=lambda item: item.get("verify_count"), reverse=True)
    if check == []:return await ctx.send("There are no stats yet!")
    else:
      num = 0
      for x in range(len(check)):
        embed.description += f"{check[num]['name']} | {check[num]['verify_count']} members verified\n"
        num += 1
      
    await ctx.send(embed=embed)

  @commands.command()
  async def unverify(self, ctx, member: discord.Member=None):
    """Reply this command to unverify a member."""
    msg        = ctx.message
    logs       = self.bot.get_channel(ID.fbc.logs.gen) or await self.bot.fetch_channel(ID.fbc.logs.gen)
    logs2      = self.bot.get_channel(cafe.mod.logger) or await self.bot.get_channel(cafe.mod.logger)
    welcomed   = discord.Object(id=889011345712894002)
    unwelcomed = discord.Object(id=889011029428801607)
    if msg.guild is None:return

    if not any([msg.reference, member]): return await ctx.send("Reply to a message or specify the member.", delete_after=10.0) # warns if no member is supplied or there's no message reference
        
    member = msg.reference.resolved.author if not member else member
    
    await ctx.message.delete()
    await member.add_roles(unwelcomed)
    await member.remove_roles(welcomed)
    await ctx.send(f"Member has been unverified by staff")

    embed=discord.Embed(
      color=0xff0000,
      title=f"Unverified {member.mention}"
    )
    embed.add_field(name="Unverified user: ",    value=member,         inline=True)
    embed.add_field(name="Unverified ID: ",      value=member.id,      inline=True)
    embed.add_field(name="Mod who unverified: ", value=msg.author,     inline=True)
    embed.add_field(name="Mods ID: ",            value=msg.author.id,  inline=True)
    embed.add_field(name="Date/time: ",          value=msg.created_at, inline=True)
    await logs.send(embed=embed)
    await logs2.send(embed=embed)

  @commands.command()
  async def deny(self, ctx, member: discord.Member=None):
    """Reply this command to deny a member verification."""
    msg   = ctx.message
    admin = discord.utils.get(msg.author.guild.roles, name="Server Staff")
    logs  = self.bot.get_channel(ID.fbc.logs.denied) or await self.bot.fetch_channel(ID.fbc.logs.denied)
    logs2 = self.bot.get_channel(cafe.mod.logger) or await self.bot.get_channel(cafe.mod.logger)
    if msg.guild is None or msg.author.id == botuser or admin not in msg.author.roles:return

    if msg.channel.id != cafe.verify:
      if msg.channel.category_id != cafe.cats.verify:return

    if not any([msg.reference, member]): return await ctx.send("Reply to a message or specify the member.", delete_after=10.0) # warns if no member is supplied or there's no message reference
    
    member = msg.reference.resolved.author if not member else member
    time   =   await msg.channel.send("time holder(dont delete)")
    await member.timeout(dt.timedelta(days=7), reason="denied application try again later") 
    embed=discord.Embed(
      color=0xff0000,
      title=f"Denied {member.mention}"
    )
    embed.add_field( name="Denied user: ", value=member,          inline=True)
    embed.add_field( name="Denied ID: ",   value=member.id,       inline=True)
    embed.add_field( name="Denier: ",      value=msg.author,      inline=True)
    embed.add_field( name="Deniers ID: ",  value=msg.author.id,   inline=True)
    embed.add_field( name="Date/time: ",   value=time.created_at, inline=True)
    await logs.send( embed=embed)
    await logs2.send(embed=embed)
    await msg.channel.delete()
      

  @commands.command()
  async def getroles(self, ctx, member: discord.Member=None):
    """Reply this command to alert a new member to get roles or profile picture."""
    zero = 0
    msg  = ctx.message
    if msg.guild is None or msg.author.id == botuser:return

    if msg.channel.id != cafe.verify:
      if msg.channel.category_id != cafe.cats.verify:return

    if not any([msg.reference, member]): return await ctx.send("Reply to a message or specify the member.", delete_after=10.0) # warns if no member is supplied or there's no message reference

    member = msg.reference.resolved.author if not member else member
    view   = discord.ui.View()
    view.add_item(discord.ui.Button(label="Click me to get pronoun roles", url="https://discordapp.com/channels/871938782092480513/889009278088773632/889009427213066240"))
    try:await member.send("You need roles(pronoun roles are required) and a profile picture for your verification to get accepted! Click below to go to the <#889009278088773632> channel.", view=view)
    except:

      zero = 1
      await ctx.send(f"{member.mention} \n You need roles(pronoun roles are required) and a profile picture for your verification to get accepted! Click below to go to the <#889009278088773632> channel.", view=view)

    finally:await ctx.message.delete()
    embed=discord.Embed(
      color=0xff0000,
    )
    embed.add_field(name="getroles", value=f"{ctx.author}(id: {ctx.author.id}) told {member}(id: {member.id}) to get roles.")
    logs   = self.bot.get_channel(ID.fbc.logs.gen) or await self.bot.fetch_channel(ID.fbc.logs.gen)
    logs2  = self.bot.get_channel(cafe.mod.logger) or await self.bot.get_channel(cafe.mod.logger)
    await logs.send(embed=embed)
    await logs2.send(embed=embed)
    if zero == 0: await ctx.send(embed=embed)
  
  @commands.command()
  async def welcome(self, ctx, member: discord.Member=None):
    """Reply this command to alert a new member how to verify/dm them the welcome message."""
    msg  = ctx.message
    zero = 0

    if msg.guild is None or msg.author.id == botuser: return

    if msg.channel.id != cafe.verify:
      if msg.channel.category_id != cafe.cats.verify:return

    if not any([msg.reference, member]): return await ctx.send("Reply to a message or specify the member.", delete_after=10.0) # warns if no member is supplied or there's no message reference

    member = msg.reference.resolved.author if not member else member

    try:await member.send(f"{member.mention} {b.vt()}")

    except:
        await ctx.send(f"{member.mention} {b.vt()}")
        zero=1

    finally: await ctx.message.delete()

    logs  = self.bot.get_channel(ID.fbc.logs.gen) or await self.bot.fetch_channel(ID.fbc.logs.gen)
    logs2 = self.bot.get_channel(cafe.mod.logger) or await self.bot.get_channel(cafe.mod.logger)
    text  = f"{member.mention} have been dmed the welcome message."
    text2 = f"{ctx.author}(id: {ctx.author.id}) made the bot dm {member}(id: {member.id}) the welcome message."
    await logs.send(text2)
    await logs2.send(text2)
    
    if zero == 0: await ctx.send(text)

  @commands.group()
  async def toggle(self, ctx):
    pass
  
  @toggle.command()
  async def verify(self, ctx):
    dpg      = self.bot.dpg
    pg       = self.bot.pg
    verify   = pg.RESULT(await dpg.fetch_one(query=pg.find('config', '_id'), values={"x": 123}), "config")["verify"]
    mod_chat = self.bot.get_channel(cafe.mod.chat) or await self.bot.fetch_channel(cafe.mod.chat) 
    if verify:
      confirm     = YesNo()
      confirm.ctx = ctx
      msg = await ctx.send("**Verrifications are enabled.**\n\nDo you want to disable it?", view=confirm)
      await confirm.wait()
      if confirm.value:
          await self.bot.dpg.execute(query="UPDATE config SET verify = False WHERE _id = 123")
          await ctx.send("Done, alerting mods now.")
          await mod_chat.send("Verifications are now temporarily closed.")
      return await msg.delete()

    confirm     = YesNo()
    confirm.ctx = ctx
    msg = await ctx.send("**Verrifications are disabled.**\n\nDo you want to enable it?", view=confirm)
    await confirm.wait()
    if confirm.value:
        await self.bot.dpg.execute(query="UPDATE config SET verify = True WHERE _id = 123")
        await ctx.send("Done, alerting mods now.")
        await mod_chat.send("Verifications are now open.")
    return await msg.delete()

