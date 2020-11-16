import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'g.')

@client.event
async def on_ready():
	print('Game Bot is ready.')
	
@client.command()
async def ping(ctx):
	await ctx.send(f'Ping! Response time is {round(client.latency * 1000)}ms')
	
client.run('TOKEN OMITTED')
