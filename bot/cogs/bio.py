import discord
from discord.ext import commands
from extras.IDS import cafe

class Bios(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_raw_message_edit(self, payload):
        if payload.channel_id != cafe.friends.bio:
            return

        channel = self.bot.get_channel(payload.channel_id)
        msg = await channel.fetch_message(payload.message_id)

        await self.bot.bio.upsert(
          {
            "_id": msg.author.id,
            "bio": str(msg.content),
            "msg_id": msg.id
          }
        )
