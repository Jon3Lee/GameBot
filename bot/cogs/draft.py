import discord
from discord.ext import commands
import random
class Draft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("READY")

    @commands.command(aliases = ['dt'])
    async def draft(self, ctx, number=1):
        file = discord.File('/home/lee/GameBot/bot/pictures/drafted.jpg', filename = 'drafted.jpg')
        embed = discord.Embed(title = "Welcome to War", color = 0xFC039D)
        embed.set_image(url = "attachment://drafted.jpg")
        number = int(number)
        if number >= 5 or number < 1:
            await ctx.send("Number must be between 1 and 4.")
            return
        if ctx.author.voice is None:
            await ctx.send("You must be in a voice channel to use this command.")
            return
        
        mychannel = ctx.author.voice.channel
        role = discord.utils.get(ctx.guild.roles, name="valorant")
        picks = {m for m in mychannel.members if role in m.roles and not m.voice.self_deaf and m != ctx.author}
        drafted = random.sample(picks, k=number)
        
        for draft in drafted:
            await ctx.send(f"<@!{draft.id}> You were drafted.")
        await ctx.send(file = file, embed = embed)   
        
async def setup(bot):
    await bot.add_cog(Draft(bot))