# moderation_bot.py

import discord
from discord.ext import commands
import sqlite3

# Import other files
import settings
import database
import machine_learning
import user_reporting

# Connect to the SQLite database
conn = sqlite3.connect('logs/moderation_logs.db')
c = conn.cursor()

# Initialize the bot
bot = commands.Bot(command_prefix='!')

# Event when the bot is ready
@bot.event
async def on_ready():
    print('Bot is ready!')

# Command to set up moderation settings
@bot.command()
async def setup(ctx):
    # User-friendly interface to set up moderation settings
    await ctx.send('Setting up moderation settings...')

# Command to log moderation actions
@bot.event
async def on_message(message):
    # Log all moderation actions for transparency
    c.execute("INSERT INTO moderation_logs (user_id, action) VALUES (?, ?)", (message.author.id, message.content))
    conn.commit()
    await bot.process_commands(message)

# Command to detect and remove inappropriate content using machine learning
@bot.command()
async def remove_inappropriate(ctx, content):
    # Call machine learning algorithm to detect inappropriate content
    if machine_learning.detect_inappropriate(content):
        await ctx.send('Inappropriate content detected and removed.')
    else:
        await ctx.send('Content is appropriate.')

# Command for users to report violations
@bot.command()
async def report_violation(ctx, user_id, reason):
    # User reporting feature for prompt action on violations
    user_reporting.report_violation(user_id, reason)
    await ctx.send('Violation reported successfully.')

# Run the bot
bot.run(settings.DISCORD_TOKEN)