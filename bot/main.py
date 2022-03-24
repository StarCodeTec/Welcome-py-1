import discord
import traceback
from discord.ext import commands

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix=commands.when_mentioned_or('F^ ', 'F^'), intents=intents)
welcome_text = "to the server. Feel free to make a bio and enjoy your stay!"
Fenne = 474984052017987604 
Equinox = 599059234134687774


@bot.check
async def check(ctx):
    logs = bot.get_channel(956322799411150952) or await bot.fetch_channel(956322799411150952)
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
        await logs.send(id_member)
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
```"""
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
                allwordg=f"Everyone please welcome <@!{userid}> {words}"
            else:     
                if admin_role in ctx.roles:
                    allwordg=f"Everyone please welcome <@!{userid}> {words} Welcomed by <@!{member}>"
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
        
@bot.command()
async def mod_send(ctx, words, userid):
    mod = bot.get_channel(901215227662696469) or await bot.fetch_channel(901215227662696469)
    if userid == "none":
        await mod.send(words)
    else:
        allwordm=f"<@!{userid}> {words}"
        await mod.send(allwordm)

@bot.event
async def on_raw_reaction_add(payload):
  user = bot.get_user(payload.user_id) 
  channel = bot.get_channel(payload.channel_id)
  msg = await channel.fetch_message(payload.message_id)
  member = payload.member
  auth = msg.author.id
  emoji = str(payload.emoji)
  auth_role = member.guild.get_role(945086022142808075)
  entrance = bot.get_channel(945087125831958588) or await bot.fetch_channel(945087125831958588)
  if auth_role in payload.member.roles:
      rolev = payload.member.guild.get_role(889011345712894002)
      roleu = payload.member.guild.get_role(889011029428801607)

      if channel == entrance:
          if emoji == "✅":
              await msg.author.add_roles(rolev)
              await msg.author.remove_roles(roleu)
              await msg.delete()
              await gen_send(member, welcome_text, auth)
      

bot.run("OTU1NDQwMjc5NDUwNzEwMDc2.YjhtGQ.kozZwra_R36aBqlq6PabGzgATVk")
