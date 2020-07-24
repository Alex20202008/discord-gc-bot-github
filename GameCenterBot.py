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
	author = ctx.message.author
	await ctx.send('Hello, ' + author.mention)


@bot.command()
async def привет(ctx):
	author = ctx.message.author
	await ctx.send('Привет, ' + author.mention)


@bot.command(pass_context = True)
async def add_reaction(ctx):
    accept_decline = await ctx.send("Test")
    cross = self.bot.get_emoji(558322190060093441)
    checkM = self.bot.get_emoji(558322116685070378)
    await accept_decline.add_reaction(checkM)
    await accept_decline.add_reaction(cross)


bot.run(token)
