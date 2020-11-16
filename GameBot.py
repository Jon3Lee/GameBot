import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'g.')

@client.event
async def on_ready():
	print('Game Bot is ready.')
	
@client.event
async def on_message(message):

	if message.content.startswith("What's up bot"):
		await message.channel.send("Ur trash kid get good at life")

client.run('TOKEN OMITTED')
