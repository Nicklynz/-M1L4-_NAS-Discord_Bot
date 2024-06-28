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
    await ctx.send(f'Hi! I am a bot {bot.user}! Type /help for a list of commands!')

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

@bot.command()
async def meme(ctx):
    mem = random.randint(1, 3)
    with open(f'images/meme_{mem}.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def help(ctx):
    await ctx.send('''Commands (Prefix = "/") :\n\n
                   hello (Greets the user)\n
                   heh (Repeats the word heh, 5 times by default or can be set manually by typing a number after the command)\n
                   password (Generates a random password)\n
                   gen_emoji (Generates a random emoji)\n
                   coin_flip (Does a coin toss, will return either HEADS or TAILS)\n
                   add (Adds two numbers together, type the numbers after the command with spaces inbetween, i.e /add 1 1)\n
                   ask_bot (Asks the bot if its cool or not)
                   meme (Generates a random meme, currently only 3 memes are available)''')

bot.run("TOKEN HERE")
