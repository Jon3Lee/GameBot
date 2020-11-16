import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'g.')

@client.event
async def on_ready():
	print('Game Bot is ready.')
	
@client.command()
async def ping(ctx):
	await ctx.send(f'Ping! Response time is {round(client.latency * 1000)}ms')
	
@client.command(aliases = ['fortune' , 'question'])
async def YesNo(ctx, *, question):
	responses = ['Yes.', 'No.']
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
	
client.run('TOKEN OMITTED')
