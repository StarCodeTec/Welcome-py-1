import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='F^ ', intents=intents)
general = bot.get_channel(923084022249320490)
entrance = bot.get_channel(955071525256568892)
    
@bot.command()
async def send_general(ctx, words):
    await ctx.send(words)

@bot.command()
async def test(ctx):
    await ctx.send("test")

@bot.event
async def on_raw_reaction_add(payload):
  user = bot.get_user(payload.user_id) 
  channel = bot.get_channel(payload.channel_id)
  msg = channel.get_partial_message(payload.message_id)
  emoji = str(payload.emoji)
  if emoji == "✅":
    await test(general)

bot.run("OTU1NDQwMjc5NDUwNzEwMDc2.YjhtGQ.kozZwra_R36aBqlq6PabGzgATVk")
