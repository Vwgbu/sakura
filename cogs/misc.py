import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"🏓 Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def emoji(self, ctx, emoji: discord.Emoji):
        await ctx.send(f"Emoji URL: {emoji.url}")

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(title=f"{member.name}'s Avatar")
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)

    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title=f"ℹ️ {guild.name}", color=discord.Color.blue())
        embed.add_field(name="👥 Members", value=guild.member_count)
        embed.add_field(name="📆 Created", value=guild.created_at.strftime("%Y-%m-%d"))
        embed.add_field(name="👑 Owner", value=guild.owner.mention)
        embed.set_thumbnail(url=guild.icon.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Misc(bot))