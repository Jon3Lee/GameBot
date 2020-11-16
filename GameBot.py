import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!jk')

@client.event
async def on_ready():
	print('Game Bot is ready.')

client.run('TOKEN OMITTED')
