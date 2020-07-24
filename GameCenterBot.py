import discord
from discord.ext import commands
import time
import os

token = os.environ.get('HIDE_BOT_TOKEN') # no u

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot is online. Be happy :)')

@bot.command()
async def send(ctx, *, arg):
    await ctx.send(arg)

@bot.command()
async def hello(ctx):
	author = message.author
	await ctx.send('Hello, ' + author.mention)





bot.run(token)
