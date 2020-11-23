import discord
from discord.ext import commands

class reactionrole(commands.Cog):
    def __init__ (self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        roleChannelid = '780317227421401108'

        #If not in roles channel, do nothing.
        if reaction.message.channel.id != roleChannelid:
            return
        
        #Add roles per reaction addition
        if str(reaction.emoji) == '👍':
            role = discord.utils.get(user.guild.roles, name = 'wow')
            await self.client.add_roles(user, role)
        elif str(reaction.emoji) == '<:valorant:780320609946566667>':
            role = discord.utils.get(user.guild.roles, name = 'valorant')
            await self.client.add_roles(user, role)


    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        roleChannelid = '780317227421401108'

        #If not in roles channel, do nothing.
        if reaction.message.channel.id != roleChannelid:
            return

        #Remove roles per reaction removal
        if str(reaction.emoji) == '<:wow:780323199732416564>':
            role = discord.utils.get(user.guild.roles, name = 'wow')
            await self.client.remove_roles(user, role)
        elif str(reaction.emoji) == '<:valorant:780320609946566667>':
            role = discord.utils.get(user.guild.roles, name = 'valorant')
            await self.client.remove_roles(user, role)

def setup(client):
    client.add_cog(reactionrole(client))