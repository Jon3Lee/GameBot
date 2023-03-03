import discord
from discord.ext import commands
from pathlib import Path
import os
import json
class credit(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready")

    #Commands
    @commands.command()
    async def credits(self, ctx):
        #await self.check(ctx.author)
        print("Checking Credits")
        with open("/home/lee/GameBot/bot/cogs/scredit.json", "r") as f:
            users = json.load(f)
        for user in users:
            print (user)
        user = ctx.author
        credit_amt = users[str(user.id)]["socialcredits"]
        em = discord.Embed(title = f"{ctx.author.name}'s credit", color = discord.Color.red())
        em.add_field(name = "Credit", value = credit_amt)
        await ctx.send(embed = em)

    @commands.command()
    #@commands.has_role('Power')
    async def give(self, ctx, member, creds):
        #await self.check(ctx.author)
        credits = abs(int(creds))
        role = discord.utils.get(ctx.guild.roles, id = 332012090690633738)
        
        if role not in ctx.author.roles:
            await ctx.send(f"Only Pooh Bear and selected individuals can run this command")
        else:
            with open("scredit.json", "r") as f:
                users = json.load(f)

            user = ctx.author
            #print(member)
            p_member = self.get_mention(member)
            #print(test)
            initialcreds = users[p_member]["socialcredits"]
            users[p_member]["socialcredits"] += credits 
            with open("/home/lee/GameBot/bot/cogs/scredit.json", "w") as f:
                json.dump(users, f, indent = 4)
        
            await ctx.send(f"Comrade you were given {credits} credits")

    @commands.command()
    #@commands.has_permissions(kick_members = True)
    #@commands.has_role('Power')
    async def remove(self, ctx, member : discord.Member, creds):
        #await self.check(ctx.author)
        credits = abs(int(creds))
        role = discord.utils.get(ctx.guild.roles, id = 332012090690633738) 
        if role not in ctx.author.roles:
            await ctx.send(f"Only Pooh Bear and selected individuals can run this command")
        else:
            with open("/home/lee/GameBot/bot/cogs/scredit.json", "r") as f:
                users = json.load(f)
            user = ctx.author
            p_member = self.get_mention(member.id)
            users[p_member]["socialcredits"] -= credits
            await ctx.send(f"Comrade you have lost {credits} credits.")
            if users[p_member]["socialcredits"] <= 0:
                await ctx.send(f"Begone")
                await member.kick(reason = "No more credits")
                users[p_member]["socialcredits"] = 10
            with open("/home/lee/GameBot/bot/cogs/scredit.json", "w") as f:
                json.dump(users, f, indent = 4)

    async def check(self,user):
        
        with open("/home/lee/GameBot/bot/cogs/scredit.json", "r") as f:
            users = json.load(f)
        
        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}
            users[str(user.id)]["socialcredits"] = 10
        with open("/home/lee/GameBot/bot/cogs/scredit.json", "w") as f:
            json.dump(users, f, indent = 4)
    
    async def get_credit_data(self):
        with open("/home/lee/GameBot/bot/cogs/scredit.json", "r") as f:
            users = json.load(f)

    async def get_mention(self, mention):
        mention = str(mention)
        mydict = {ord('<'): None, ord('@'): None, ord('>'): None}
        n_mention = mention.translate(mydict)
        return n_mention

async def setup(client):
    await client.add_cog(credit(client))

