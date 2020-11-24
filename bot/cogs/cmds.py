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
		print(f'Ping command used by {ctx.author}.')

	@commands.command(aliases = ['for'])
	async def fortune(self, ctx, *, question):
		responses = ['Yes.', 'No.', 'Only time will tell.', 'lmao no', 'Maybe? Ask again',
		 			'Only God can answer this one.', 'Look at yourself in the mirror before you ask that question.', 'Most definitely.'
		 			, 'Hell no', 'For sure.', 'Yeahhhhh no.', 'It is certain.', 'Without a doubt.', "I don't think so"]
		await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
		print(f'I just gave {ctx.author} their fortune!')

	@commands.command(aliases = ['al', 'mal'])
	async def animelist(self, ctx, name):
		embed = discord.Embed(title = f'{name}s list', url = (f'https://myanimelist.net/profile/{name}'), color = 0x03C6FC)
		await ctx.send(embed = embed)
		print(f"I have pulled up {name}'s MyAnimeList.")

	@commands.command()
	async def roll(self, ctx, num = 100):
		roll = random.randrange(0,num)
		if num > 999999999:
			await ctx.send('Sorry, your roll number is too high.')
			print(f'{ctx.author} tried to roll but the number was too high.')
		else:
			await ctx.send(f"{ctx.author.mention}'s roll is: {roll}")
			print(f'{ctx.author} has rolled {roll}.')
		if roll == 69:
			await ctx.send(file = discord.File('bot/pictures/nice.jpg'))
			print(f'Hey! {ctx.author} has rolled 69! Nice.')

	@commands.command(aliases = ['flip'])
	async def coinflip(self, ctx):
		flip = random.randrange(0,100)
		if flip >= 50:
			face = "heads"
		else:
			face = "tails"
		await ctx.send(f'{ctx.author.mention} flips {face} on his coin.')
		print(f'{ctx.author} flipped {face}.')



def setup(client):
		client.add_cog(cmds(client))