import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.actions = {
            "kiss": ["😘", "💋", "👩‍❤️‍💋‍👨"],
            "hug": ["🤗", "🫂", "❤️"],
            "slap": ["👋", "🤚", "✋"]
        }

    @commands.command()
    async def kiss(self, ctx, member: discord.Member):
        await ctx.send(f"{ctx.author.mention} kisses {member.mention} {random.choice(self.actions['kiss'])}")

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        await ctx.send(f"{ctx.author.mention} hugs {member.mention} {random.choice(self.actions['hug'])}")

    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        await ctx.send(f"{ctx.author.mention} slaps {member.mention} {random.choice(self.actions['slap'])}")

async def setup(bot):
    await bot.add_cog(Fun(bot))