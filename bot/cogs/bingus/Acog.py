import discord
import random
import os
from pathlib import Path
from discord.ext import tasks, commands
cog = commands.Cog
Fenne = 474984052017987604 
Equinox = 599059234134687774
null = None
botuser = 966392608895152228 
class bingus(commands.Cog):
  def __init__(self, bot):
    self.bot=bot
  
  @commands.command()
  async def bingus(self, ctx):
    files=["bingus!.gif", "bingus-beloved.gif", "bingus-bongus.gif", "bingus-cat.gif", "bingus-cube.gif", "bingus-cult.gif", "bingus-cults.gif", "bingus-dance.gif", "bingus-dances.gif", "bingus-delilah.gif", "bingus-dimension.gif", "bingus-evolution.gif", "bingus-hater.gif", "bingus-haters.gif", "bingus-hi.gif", "bingus-love.gif", "bingus-loves.gif", "bingus-mar.gif", "bingus-meme.gif", "bingus-phone.gif", "bingus-tat.gif", "bingus.gif", "bingus_army.gif", "bingus_heart.gif", "bingus_smart.gif", "dead-chat.gif"]
    filess=random.choice(files)
    file=discord.File(f"/home/container/bot/cogs/bingus/{filess}", filename="image.gif")
    embed = discord.Embed()
    embed.set_image(url=f"attachment://image.gif")
    await ctx.send(embed=embed)
