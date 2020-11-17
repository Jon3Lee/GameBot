import discord
import random
from discord.ext import commands

class Sauce(commands.Cog):

	def __init__ (self, client):
		self.client = client
	

	#Events
	@commands.Cog.listener()
	async def on_ready(self):
		print('Bot is online')

	#Commands
	@commands.command()
	async def sauce(self, ctx):
		sce = random.randrange(100000, 336478)
		embed = discord.Embed(title = "Sauce", description = "Here is your sauce!", url = (f'https://www.nhentai.net/g/{sce}'), color = 0xFC039D)
		await ctx.send(embed = embed)

def setup(client):
	client.add_cog(Sauce(client))
