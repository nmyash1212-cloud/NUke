
import os
import discord
from discord.ext import commands

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is missing from Render Environment!")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online: {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! Bot is working!")

bot.run(TOKEN)

