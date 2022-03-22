import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='F^ ', intents=intents)
    
@bot.command()
async def gen_send(ctx, words, userid):
    general = bot.get_channel(923084022249320490) or await bot.fetch_channel(923084022249320490)
    if userid == none:
        await general.send(words)
    else:
        allwords="<@!"+userid."> "+words
        await general.send(allwords)
    

@bot.command()
async def ent_send(ctx, words):
    entrance = bot.get_channel(955071525256568892) or await bot.fetch_channel(955071525256568892)
    await entrance.send(words)
    

@bot.event
async def on_raw_reaction_add(payload):
  user = bot.get_user(payload.user_id) 
  channel = bot.get_channel(payload.channel_id)
  msg = channel.get_partial_message(payload.message_id)
  emoji = str(payload.emoji)
  if emoji == "✅":
    await test(general)

bot.run("OTU1NDQwMjc5NDUwNzEwMDc2.YjhtGQ.kozZwra_R36aBqlq6PabGzgATVk")
