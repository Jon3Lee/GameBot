import discord
from discord.ext import commands


class Help(commands.Cog):


	def __init__ (self, client):
		self.client = client
	
	#Events
	# @commands.Cog.listener()
	# async def on_ready(self):
	# 	print('Bot is online')
	
	#Help command
	@commands.command()
	async def help(self, ctx):
		embed = discord.Embed(title = "Commands", color=0xff9500, description = 
						   "The prefix for all commands is ``g.[command]``.\n\n**help** | *Pulls up this help menu*\n**ping** |\
						   *Checks Game Bot's ping against Discord's Server.*\n**fortune** <question> |\
						   *Game Bot answers your yes or no question.*\n**roll** <OPTIONAL> |\
					       *Rolls a dice from 0 to 100 by default or 0 to OPTIONAL\n**sauce**  |\
					       *Gives you a randomly generated sauce* ;)\n **animelist** <NAME> |\
					       *Pulls up NAME's MyAnimeList*\n **flip** |\
					       *Flips a coin*")
		embed.set_author(name = "Game Bot Help")
		await ctx.send(embed=embed)
		print(f'{ctx.author} called the help command.')


def setup(client):
	client.add_cog(Help(client))