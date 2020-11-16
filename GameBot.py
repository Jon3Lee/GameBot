import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'g.')

@client.event
async def on_ready():
	print('Game Bot is ready.')

client.run('TOKEN OMITTED')
