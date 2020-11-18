import discord
import random
from discord.ext import commands

class cmds(commands.Cog):
	def __init__ (self, client):
		self.client = client



	#Commands
	@commands.command(help = 'this is a test')
	async def ping(self, ctx):
		await ctx.send(f'Pong! Response time is {round(self.client.latency * 1000)}ms')

	@commands.command(aliases = ['for'])
	async def fortune(self, ctx, *, question):
		responses = ['Yes.', 'No.', 'Only time will tell.', 'What kind of question even is that?', 'lmao no', 'Maybe? Ask again', 'Only god can answer this one.', 
					'Look at yourself in the mirror before you ask that question.', 'Most definitely.', 'Hell no']
		await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

	@commands.command(aliases = ['al', 'mal'])
	async def animelist(self, ctx, name):
		embed = discord.Embed(title = f'{name}s list', url = (f'https://myanimelist.net/profile/{name}'), color = 0x03C6FC)
		await ctx.send(embed = embed)

	@commands.command()
	async def roll(self, ctx, num = 100):
		roll = random.randrange(0,num)
		if num > 999999999:
			await ctx.send('Sorry, your roll number is too high.')
		else:
			await ctx.send(f"{ctx.author.mention}'s roll is: {roll}")
		if roll == 69:
			await ctx.send(file = discord.File('./pictures/nice.jpg'))

	@commands.command(aliases = ['flip'])
	async def coinflip(self, ctx):
		flip = random.randrange(0,100)
		if flip >= 50:
			face = "heads"
		else:
			face = "tails"
		await ctx.send(f'{ctx.author.mention} flips {face} on his coin.')



def setup(client):
		client.add_cog(cmds(client))