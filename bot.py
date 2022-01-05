#by zabtxd#2000

from discord.ext import commands
import json

with open("config.json") as file: 
    info = json.load(file)
    token = info["token"]
    prefix = info["prefix"]


bot = commands.Bot(command_prefix=prefix)

bot.lava_nodes = [
    {
        'host': 'lava.link',
        'port': '80',
        'rest_uri': f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'lol',
        'region': 'europa',
    }

]

@bot.event
async def on_ready():
    print('Bot is ready')
    bot.load_extension('dismusic')
    bot.load_extension('dch')


bot.run(token)