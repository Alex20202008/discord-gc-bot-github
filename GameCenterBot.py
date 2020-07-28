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
    print('Bot is online. Be happy :)')
    activity = discord.Activity(name='Бот срёт!!', type=1)
    await bot.change_presence(activity=activity)# .Status.(Idle, do_not_disturb, online)


@bot.command()
async def hui(ctx, member: discord.Member):
    author = ctx.message.author
    embed = discord.Embed( description='**Аватарка пользователя ' + str(member.mention) + '**', colour=discord.Colour.purple())
    embed.set_image(url=member.avatar_url)








bot.run(token)
