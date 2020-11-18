import discord
from discord.ext import commands


class autorole(commands.Cog):
	def __init__ (self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_member_join(self, member):
		#await member.send(f"Welcome {member.name} to Game Server! <TEST>") #Sends a DM to member on join.
		channel = member.guild.system_channel
		role = discord.utils.get(member.guild.roles, name ='Casuals')
		if channel is not None:
			await channel.send(f'Welcome {member.mention} to Game!')
			await member.add_roles(role)


	@commands.Cog.listener()
	async def on_member_remove(self, member):
		channel = member.guild.system_channel
		if channel is not None:
			await channel.send(f'Goodbye! {member.mention} has left Game.')

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.content.startswith("What's up bot"):
	 		await message.channel.send("Hey! Thanks for creating me!")

#Setup
def setup(client):
	client.add_cog(autorole(client))