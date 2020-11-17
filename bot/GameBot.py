import discord
import random
import os
from discord.ext import commands

#Enable Intents.members
intents = discord.Intents.default()
intents.members = True 

client = commands.Bot(command_prefix = 'g.', help_command = None, intents = intents)
token = open("token.txt", mode = "r").readline()



@client.event
async def on_connect():
	print('Game Bot is now connected to discord.')
@client.event
async def on_ready():
	print('Game Bot is ready and running.')

@client.event
async def on_member_join(member):
	#await member.send(f"Welcome {member.name} to Game Server! <TEST>") #Sends a DM to member on join.
	await client.get_channel(768660907433000994).send(f'Welcome {member.name} to Game!')


@client.event
async def on_member_remove(member):
	await client.get_channel(768660907433000994).send(f'Goodbye! {member.name} has left Game.')


# @client.event
# async def on_message(message):
# 	if message.content.startswith("What's up bot"):
# 		await message.channel.send("Hey! Thanks for creating me!")



#COMMANDS
@client.command(help = 'this is a test')
async def ping(ctx):
	await ctx.send(f'Pong! Response time is {round(client.latency * 1000)}ms')


@client.command(aliases = ['for'])
async def fortune(ctx, *, question):
	responses = ['Yes.', 'No.', 'Only time will tell.', 'What kind of question even is that?', 'lmao no', 'Maybe? Ask again', 'Only god can answer this one.', 
				'Look at yourself in the mirror before you ask that question.', 'Most definitely.', 'Hell no']
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command(aliases = ['al'])
async def animelist(ctx, name):
	embed = discord.Embed(title = f'{name}s list', url = (f'https://myanimelist.net/profile/{name}'), color = 0x03C6FC)
	await ctx.send(embed = embed)

@client.command()
async def roll(ctx, num = 100):
	await ctx.send(f"{ctx.author.mention}'s roll is: {random.randrange(0,num)}")



@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')

#goes through cogs folder for files
for filename in os.listdir('./cogs'):
	#checks if filename is a python file
	if filename.endswith('.py'):
		#removes .py from the filename
		client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)