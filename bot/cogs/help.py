import discord
from discord.ext import commands


class Help(commands.Cog):


	def __init__ (self, client):
		self.client = client
	
	#Events
	# @commands.Cog.listener()
	# async def on_ready(self):
	# 	print('Bot is online')



def setup(client):
	client.add_cog(Help(client))