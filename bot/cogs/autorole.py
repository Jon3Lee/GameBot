import discord
from discord.ext import commands


class autorole(commands.Cog):
	def __init__ (self, client):
		self.client = client

	
	async def on_member_join(self, member):
		#await member.send(f"Welcome {member.name} to Game Server! <TEST>") #Sends a DM to member on join.
		await client.get_channel(768660907433000994).send(f'Welcome {member.name} to Game!')
		await member.add_roles(226897097012674571)


	
	async def on_member_remove(self, member):
		await client.get_channel(768660907433000994).send(f'Goodbye! {member.name} has left Game.')

	
	async def on_message(self, message):
		if message.content.startswith("What's up bot"):
	 		await message.channel.send("Hey! Thanks for creating me!")
def setup(client):
	client.add_cog(autorole(client))