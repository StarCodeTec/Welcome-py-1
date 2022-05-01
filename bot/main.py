import discord
from discord.ext import tasks, commands
botuser=955440279450710076

class Mainbot(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, msg):
      channel=msg.channel.id
      author=msg.author.id
      if author==botuser:return
      def add_react():
            await msg.add_reaction(r1)
            await msg.add_reaction(rcheck)
            await msg.add_reaction(r3)            
            await msg.add_reaction(r4)            
            await msg.add_reaction(r5)
      if 
