import discord
from discord.ext import commands

class reactionrole(commands.Cog):
    def __init__ (self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        roleChannelid = ''

        if reaction.message.channel.id != roleChannelid:
            return
        # if str(reaction.emoji) == '':
        #     await client.add_roles(user, role)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        roleChannelid = ''
        if reaction.message.channel.id != roleChannelid:
            return
        # if str(reaction.emoji) == '':
        #     await client.remove_roles(user, role)

def setup(client):
    client.add_cog(reactionrole(client))