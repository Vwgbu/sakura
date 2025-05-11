import discord
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.warns = {}

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided"):
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="🔨 Member Banned",
                description=f"{member.mention} has been banned.",
                color=discord.Color.red()
            )
            embed.add_field(name="Reason", value=reason)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("❌ I don't have permission to ban this user!")
        except discord.HTTPException:
            await ctx.send("❌ Failed to ban the user (HTTP error).")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌ Please mention a user to ban. Example: `!ban @user [reason]`")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("❌ User not found. Please mention a valid user.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You don't have permission to ban members!")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention} 👢")

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def mute(self, ctx, member: discord.Member, duration: int = 5, *, reason=None):
        await member.timeout(discord.utils.utcnow() + discord.timedelta(minutes=duration), reason=reason)
        await ctx.send(f"Muted {member.mention} for {duration} minutes 🔇")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        if member.id not in self.warns:
            self.warns[member.id] = 1
        else:
            self.warns[member.id] += 1
        
        await ctx.send(f"⚠ {member.mention} has been warned ({self.warns[member.id]}/3). Reason: {reason}")
        
        if self.warns[member.id] >= 3:
            await member.kick(reason="Too many warns")
            del self.warns[member.id]
            await ctx.send(f"🚨 {member.mention} was kicked for exceeding 3 warns!")

async def setup(bot):
    await bot.add_cog(Mod(bot))