# moderation_bot/user_reporting.py

import discord
from discord.ext import commands

class UserReporting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='report', help='Report a user violation to the bot')
    async def report_user(self, ctx, user: discord.User, reason: str):
        guild = ctx.guild
        reporter = ctx.author

        # Perform actions based on the reported user and reason
        # Add your logic here

        await ctx.send(f'{reporter.mention} has reported {user.mention} for {reason}. Thank you for your report.')

def setup(bot):
    bot.add_cog(UserReporting(bot))