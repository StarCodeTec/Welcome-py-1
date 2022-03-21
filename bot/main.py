import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='W^ ', intents=intents)

@bot.event
async def on_raw_reaction_add(payload):
  user = bot.get_user(payload.user_id) 
  channel = bot.get_channel(payload.channel_id)
  print(channel)
  msg = channel.get_partial_message(payload.message_id)
  emoji = str(payload.emoji)
  

bot.run("OTU1NDQwMjc5NDUwNzEwMDc2.YjhtGQ.kozZwra_R36aBqlq6PabGzgATVk")
