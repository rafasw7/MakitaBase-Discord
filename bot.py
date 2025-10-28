import discord
from discord.ext import commands
import json
import os
import asyncio

with open("config.json") as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f"Bot online! Logado como {bot.user}")

async def main():
    await load_cogs()
    await bot.start(config["token"])

asyncio.run(main())