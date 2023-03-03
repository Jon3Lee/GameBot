import discord
import os
from discord.ext import commands
import json
import asyncio


#Enable Intents
intents = discord.Intents.all()
intents.members = True 
intents.reactions = True
intents.messages = True
intents.guilds = True

client = commands.Bot(command_prefix = 'g.', help_command = None, intents = intents)
token = open("token.txt", mode = "r").readline()


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

async def load_extensions():
    for filename in os.listdir('cogs/'):
        print (filename)
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
    async with client:
        await load_extensions()
        await client.start(token)


asyncio.run(main())
