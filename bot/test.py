from imports.config import bot
import asyncio
 
async def initalize_connection():
    database = bot.dpg
    try:
        await database.connect()
        print('Connected to Database')
        await database.disconnect()
        print('Disconnecting from Database')
    except :
        print('Connection to Database Failed')
 
if __name__ == '__main__':
    asyncio.run(initalize_connection())