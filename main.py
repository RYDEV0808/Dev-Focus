from discord.ext import commands
from dotenv import load_dotenv
import discord
import logging
import os

load_dotenv()

token = os.getenv('DISCORD_TOKEN')
handler = logging.FileHandler(filename='discord.log', encodings='utf-8', mode='w')
intents = discord.intents.default()