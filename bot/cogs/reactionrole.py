import discord
from discord.ext import commands

class reactionrole(commands.Cog):
    def __init__ (self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel_id = payload.channel_id
        emoji = payload.emoji
        guild_id = payload.guild_id
        user_id = payload.user_id
        if channel_id == 780317227421401108:
            #Find guild
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)
            #Only works if emoji name is similar to role name, create if statement if there is a
            #case where the role name != emoji name
            role = discord.utils.get(guild.roles, name = emoji.name)

            #Assign role
            if role is not None:
                #Find member within guild
                member = discord.utils.find(lambda m: m.id == user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        channel_id = payload.channel_id
        emoji = payload.emoji
        guild_id = payload.guild_id
        user_id = payload.user_id
        if channel_id == 780317227421401108:
            #Find guild
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)
            #Only works if emoji name is similar to role name, create if statement if there is a
            #case where the role name != emoji name
            role = discord.utils.get(guild.roles, name = emoji.name)

            #Remove role
            if role is not None:
                #Find member within guild
                member = discord.utils.find(lambda m: m.id == user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)

def setup(client):
    client.add_cog(reactionrole(client))