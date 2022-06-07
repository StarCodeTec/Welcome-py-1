import discord
import random
from discord.ext import commands

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
    """Posts random bingus image. :p"""
    file=["Z5EW9Ij", "apGRbbd", "bxSmibQ", "0pld30P", "ekv5sS", "cTQxzzz", "Qz0o2au", "0o0YOq9", "Cie89pF", "n4E8Eo7", "a52YHBu", "lYDqcIH", "TZ227yu", "T4RJ0mC", "UqnkEGP", "wAg3rsf", "wSWdCaT", "RqT1tFS", "3VJGRpY", "raerLvq", "LH8VqGH", "xtrV1fj", "GePK3z5", "qOKGQ9p", "dYt8wZk", "qvtC6Ix", "2vgNv4u"]
    files=random.choice(file)
    embed = discord.Embed()
    embed.set_image(url=f"https://i.imgur.com/{files}.gif")
    await ctx.send(embed=embed)
