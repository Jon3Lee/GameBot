import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!jk')

@client.event
async def on_ready():
	print('Game Bot is ready.')

client.run('NjUxNTk3MTMwMTc5NDExOTcx.XecNHQ.MnQxyHKuCAAaF3LCkk5AAE9NSaY')