import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = 'g.')

@client.event
async def on_ready():
	print('Game Bot is ready.')

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! Response time is {round(client.latency * 1000)}ms')

@client.command(aliases = ['fortune' , 'for'])
async def yesno(ctx, *, question):
	responses = ['Yes.', 'No.', 'Only time will tell.', 'What kind of question even is that?', 'lmao no', 'Maybe? Ask again', 'Only god can answer this one.', 
	'Look at yourself in the mirror before you ask that question.', 'Most definitely.', 'Hell no']
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def roll(ctx, num=100):
	await ctx.send(f"{ctx.author.mention}'s roll is: {random.randrange(0,num)}")
	
client.run('TOKEN OMITTED')
