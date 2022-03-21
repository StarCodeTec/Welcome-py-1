import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='.', intents=intents)

bot.run(os.environ['TOKEN'])
