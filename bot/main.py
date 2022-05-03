#cogs--------------------------------------------------------------------------------------------  

#personal_import---------------------------------------------------------------------------------

#import------------------------------------------------------------------------------------------
import os
import discord
import time
import traceback
import asyncio
from discord.ext import tasks, commands

#EXTRA_VARS--------------------------------------------------------------------------------------
key = os.environ['CUSTOM_ENV']
null = None

#intents----------------------------------------------------------------------------------------
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix=commands.when_mentioned_or('F^ ', 'F^'), intents=intents)
botuser = 955440279450710076
#-----------------------------------------------------------------------------------------------

@bot.event
async def on_message(msg): 
    auth = msg.author.id
    if auth != botuser && msg.context == "test":
        msg.channel.send("bot?")
    
    
    
    
    
    
    
async def main_start():
    async with bot:
        #gen.start()
        #bump.start()
        #bystander.start()
        #await bot.add_cog(test)
        await bot.start(str(key)) 

asyncio.run(main_start())
