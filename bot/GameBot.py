import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = 'g.', help_command = None)
token = open("token.txt", mode = "r").readline()

@client.event
async def on_ready():
	print('Game Bot is ready.')

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
async def sauce(ctx):
	sce = random.randrange(100000, 336478)
	embed = discord.Embed(title = "Sauce", description = "Here is your sauce!", url = (f'https://www.nhentai.net/g/{sce}'), color = 0xFC039D)
	await ctx.send(embed = embed)

@client.command()
async def help(ctx):
	embed = discord.Embed(title = "Commands", color=0xff9500, description = 
					   "The prefix for all commands is ``g.[command]``.\n\n**help** | *Pulls up this help menu*\n**Ping** |\
					   *Checks Game Bot's ping against Discord's Server.*\n**fortune** <question> |\
					   *Game Bot answers your yes or no question.*\n**roll** <OPTIONAL> |\
				       *Rolls a dice from 0 to 100 by default or 0 to OPTIONAL\n**sauce**  |\
				       *Gives you a randomly generated sauce* ;)\n **animelist** <NAME> |\
				       *Pulls up NAME's MyAnimeList*")
	embed.set_author(name = "Game Bot Help")
	await ctx.send(embed=embed)
#Hello gurl


'''@client.event
async def on_message(message):
	if message.content.startswith("What's up bot"):
		await message.channel.send("Hey! Thanks for creating me!")'''

client.run(token)