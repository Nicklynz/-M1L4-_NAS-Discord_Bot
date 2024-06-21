import discord
from discord.ext import commands
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, pass_ltr = 12):
    await ctx.send(gen_pass(pass_ltr))

@bot.command()
async def gen_emoji(ctx):
    await ctx.send(gen_emodji())

@bot.command()
async def coin_flip(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def ask_bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool. \U0001F60E')

bot.run("TOKEN HERE")
