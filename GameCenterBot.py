import discord
from discord.ext import commands
import time
import os
import asyncio
import random

token = os.environ.get('HIDE_BOT_TOKEN') # no u

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    pass


@bot.command()
async def hui(ctx, member: discord.Member):
    author = ctx.message.author
    qweqwe = discord.Embed( description='**Аватарка пользователя ' + str(member.mention) + '**', colour=discord.Colour.purple())
    qweqwe.set_image(url=member.avatar_url)








bot.run(token)
