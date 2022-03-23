import discord
import traceback
from discord.ext import commands

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix=commands.when_mentioned_or('F^ ', 'F^'), intents=intents)
welcome_text = " to the server, you can make a #✦📑┊bio if you want"
Fenne = 474984052017987604 
Equinox = 599059234134687774


@bot.check
async def check(ctx):
    logs = bot.get_channel(956235842525999175) or await bot.fetch_channel(956235842525999175)
    member = ctx.author
    admin_V = ctx.guild.get_role(955572063383482479)
    if int(member.id) == Equinox or int(member.id) == Fenne or admin_V in ctx.member.roles:
        print(member)
        print(member.id)
        id_member = f"""```
        AUTHORIZED ACCESS 
        Command: {ctx.command}
        Member id: {member.id} 
        Member name: {member}```"""
        print("true")
        return(True)
    else:
        print(member)
        print(member.id)
        id_member = f"""```
UNAUTHORIZED ACCESS 
Command: {ctx.command}
Member id: {member.id} 
Member name: {member}
```
@speak"""
        await logs.send(id_member)
        return(False)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        return
    traceback.print_exception(error)

@bot.command()
async def gen_send(ctx, words, userid):
        general = bot.get_channel(950085161872154694) or await bot.fetch_channel(950085161872154694)
        if words == welcome_text:
            admin_role = ctx.guild.get_role(945086022142808075)
            member = ctx.id
            if member == Fenne:
                allwordg=f"Welcome <@!{userid}> {words}"
            else:     
                if admin_role in ctx.roles:
                    allwordg=f"Welcome <@!{userid}> {words} sent by <@!{member}>"
        else:
            allwrodg=f"<@!{userid}> {words}"

        if userid == "none":
            await general.send(words)
        else:
            await general.send(allwordg)
      

@bot.command()
async def ent_send(ctx, words, userid):
    entrance = bot.get_channel(945087125831958588) or await bot.fetch_channel(945087125831958588)
    if userid == "none":
        await entrance.send(words)
    else:
        allworde=f"<@!{userid}> {words}"
        await entrance.send(allworde)
    

@bot.event
async def on_raw_reaction_add(payload):
  user = bot.get_user(payload.user_id) 
  channel = bot.get_channel(payload.channel_id)
  msg = await channel.fetch_message(payload.message_id)
  member = payload.member
  auth = msg.author.id
  emoji = str(payload.emoji)
  auth_role = member.guild.get_role(945086022142808075)
  entrance = bot.get_channel(955517941812719687) or await bot.fetch_channel(955517941812719687)
  if auth_role in payload.member.roles:
      rolev = payload.member.guild.get_role(889011345712894002)
      roleu = payload.member.guild.get_role(889011029428801607)

      if channel == entrance:
          if emoji == "✅":
              await member.add_roles(rolev)
              await member.remove_roles(roleu)
              await msg.delete()
              await gen_send(member, welcome_text, auth)
      

bot.run("OTU1NDQwMjc5NDUwNzEwMDc2.YjhtGQ.kozZwra_R36aBqlq6PabGzgATVk")
