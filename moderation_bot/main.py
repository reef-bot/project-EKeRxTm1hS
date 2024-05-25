# main.py

import discord
from discord.ext import commands
import sqlite3

# Import custom modules
from moderation_bot import moderation_bot
from moderation_bot import settings
from moderation_bot import database
from moderation_bot import machine_learning
from moderation_bot import user_reporting

# Initialize the bot
bot = commands.Bot(command_prefix='!')

# Connect to the SQLite database
conn = sqlite3.connect('moderation_bot/logs/moderation_logs.db')
cursor = conn.cursor()

# Event listener for when the bot is ready
@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user}')

# Event listener for when a message is received
@bot.event
async def on_message(message):
    # Check if message is from a bot
    if message.author.bot:
        return

    # Check message content for inappropriate content using machine learning
    if machine_learning.detect_inappropriate_content(message.content):
        await message.delete()
        await message.channel.send(f'{message.author.mention}, please refrain from using inappropriate language.')

    await bot.process_commands(message)

# Command to set up bot settings
@bot.command()
async def setup(ctx):
    await settings.setup_bot(ctx)

# Command to report violations
@bot.command()
async def report(ctx, user: discord.User, reason: str):
    await user_reporting.report_violation(ctx, user, reason)

# Run the bot
bot.run('YOUR_DISCORD_BOT_TOKEN')