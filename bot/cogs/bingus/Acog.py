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
    files=["bingus.png", "bingus!.gif", "bingus-beloved.gif", "bingus-bongus.gif", "bingus-cat.gif", "bingus-cube.gif", "bingus-cult.gif", "bingus-cults.gif", "bingus-dance.gif", "bingus-dances.gif", "bingus-delilah.gif", "bingus-dimension.gif", "bingus-evolution.gif", "bingus-hater.gif", "bingus-haters.gif", "bingus-hi.gif", "bingus-love.gif", "bingus-loves.gif", "bingus-mar.gif", "bingus-meme.gif", "bingus-phone.gif", "bingus-tat.gif", "bingus.gif", "bingus_army.gif", "bingus_heart.gif", "bingus_smart.gif", "dead-chat.gif"]
    filess=random.choice(files)
    os.chdir("/home/container/bot/cogs/bingus/")
    print(os.getcwd())
    file = discord.File(f"attachment://{filess}")
    embed = discord.Embed(title="Bingus")
    embed.set_image(url=file)
    await ctx.send(embed=embed)
