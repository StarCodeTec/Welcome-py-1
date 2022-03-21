from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='.', intents=intents)

bot.run("OTU1NDQwMjc5NDUwNzEwMDc2.YjhtGQ.kozZwra_R36aBqlq6PabGzgATVk")
