from discord.ext import commands
import sys
sys.path.append('..')
from extras.text_zone import BIG as b
import extras.IDS as ID

cog = commands.Cog
botuser = 966392608895152228
cafe = ID.cafe

class sticky(commands.Cog):
  def __init__(self, bot):
    self.bot=bot
  
  @cog.listener()
  async def on_message(self, msg):
    if msg.guild is None:
      return

    if msg.author.id == botuser:
      return

    def is_me(msg):
      return msg.author.id == botuser

    if msg.channel.id == cafe.home.promo:
      cha = self.bot.get_channel(cafe.home.promo) or await self.bot.fetch_channel(cafe.home.promo)
      await cha.purge(limit=2, check=is_me)
      await cha.send(f"Server boosters can post <#{cafe.home.promo}> in every 30 minutes!")

    elif msg.channel.id == cafe.friends.bio:
      cha = self.bot.get_channel(cafe.friends.bio) or await self.bot.fetch_channel(cafe.friends.bio)   
      await cha.purge(limit=2, check=is_me)
      
      await self.bot.bio.upsert(
          {
            "_id": msg.author.id,
            "bio": str(msg.content),
            "msg_id": msg.id
          }
        )
      
      await cha.send(b.bt)
    
    elif msg.channel.id == cafe.chat.dm:
      cha = self.bot.get_channel(cafe.chat.dm) or await self.bot.fetch_channel(cafe.chat.dm)
      await cha.purge(limit=2, check=is_me)
      await cha.send(f"""
This is for asking members to DM only. Any advertising of your own DM's or friend requests may be removed and warned! 
Please use the <#{cafe.friends.zone}> if you would like to find somebody to talk to.""")
      
    elif msg.channel.id == cafe.friends.connect:
      cha = self.bot.get_channel(cafe.friends.connect) or await self.bot.fetch_channel(cafe.friends.connect)
      await cha.purge(limit=2, check=is_me)
      await cha.send("Connect Post Example:\n```Status:\nMood:\nTopics of interest right now:```\n\nMust be text only, you can delete your status at any time!")
