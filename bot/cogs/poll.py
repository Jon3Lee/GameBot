import discord
from discord.ext import commands

class poll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def poll(self, ctx, *, poll = []):
        pass
        #Appends to poll list, uses for loop to add options of list
        #to poll, then counts number of items in list and reacts to message based
        #on that.

#Setup:
async def setup(client):
    await client.add_cog(poll(client))
