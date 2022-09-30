import sys
sys.path.append('..')
from imports.discord import *
import extras.IDS as ID
class gifs(commands.Cog):

  def __init__(self, bot: commands.Bot):
    self.bot: commands.Bot = bot
  
  @commands.hybrid_command(name="bingus")
  @discord.app_commands.guilds(ID.server.fbc, ID.server.cafe)
  async def bingus(self, ctx: commands.Context):
    """Posts random bingus image. :p"""
    file  = ["Z5EW9Ij", "apGRbbd", "bxSmibQ", "0pld30P", "ekv5sS", "cTQxzzz", "Qz0o2au", "0o0YOq9", "Cie89pF", "n4E8Eo7", "a52YHBu", "lYDqcIH", "TZ227yu", "T4RJ0mC", "UqnkEGP", "wAg3rsf", "wSWdCaT", "RqT1tFS", "3VJGRpY", "raerLvq", "xtrV1fj", "GePK3z5", "qOKGQ9p", "dYt8wZk", "qvtC6Ix", "2vgNv4u"]
    
    files = random.choice(file);embed = discord.Embed();embed.set_image(url=f"https://i.imgur.com/{files}.gif")
    await ctx.send(embed=embed)
  
  @commands.hybrid_command(name="hug")
  @discord.app_commands.guilds(ID.server.fbc, ID.server.cafe)
  async def hug(self, ctx: commands.Context, member: discord.Member, gender_specific: Optional[bool] = False):
    """Beta hug command"""
    member = ctx.message.reference.resolved.author if not member else member
    user   = member.mention;  x_y= gender_specific

    if x_y == True:
      await ctx.send("This feature is a work in progress command")


    elif x_y == False:
      aray=range(1, 93);main=[];ex=[29, 38, 47, 51, 56, 63, 64, 77, 78, 83, 87]

      for i in aray:
        if i not in ex:
          main.append(str(i).zfill(3))

      url=(f"https://purrbot.site/img/sfw/hug/gif/hug_{random.choice(main)}.gif");embed = discord.Embed(); embed.set_image(url=url)
      await ctx.send(f"***{ctx.author.mention} hugs {user}***", embed=embed)
    
    try:    await ctx.message.delete()
    except: return