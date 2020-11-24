import discord
import os
from discord.ext import commands

#Enable Intents
intents = discord.Intents.default()
intents.members = True 
intents.reactions = True
intents.messages = True
intents.guilds = True

client = commands.Bot(command_prefix = 'g.', help_command = None, intents = intents)
token = open("bot/token.txt", mode = "r").readline()


#Checks if bot is connected and ready
@client.event
async def on_connect():
	print('Game Bot is now connected to discord.')
@client.event
async def on_ready():
	print('Game Bot is ready and running.')


#Cogs
@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')

#goes through cogs folder for files
for filename in os.listdir('bot/cogs'):
	#checks if filename is a python file
	if filename.endswith('.py'):
		#removes .py from the filename
		client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)