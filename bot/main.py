import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='F^ ', intents=intents)

@bot.command()
async def send(ctx, words):
  if words == "general".*:
    await ctx.send(words)

@bot.event
async def on_raw_reaction_add(payload):
  general = bot.get_channel(955195564721573910)
  entrance = 955071525256568892
  member = discord.Member
  user = bot.get_user(payload.user_id) 
  channel = bot.get_channel(payload.channel_id)
  msg = channel.get_partial_message(payload.message_id)
  emoji = str(payload.emoji)
  if payload.channel_id == entrance:
    if emoji == "":
      print(member)

bot.run("OTU1NDQwMjc5NDUwNzEwMDc2.YjhtGQ.kozZwra_R36aBqlq6PabGzgATVk")
