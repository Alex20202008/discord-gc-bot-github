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


@bot.command()
@commmands.has_permissions(administrator = True)
async def mute_role(ctx, member: discord.Member);
    mute_role = discord.utils.get(ctx.message.guild.roles, name = '𝕄𝕦𝕥𝕖🔇')
    await member.add_roles(mute_role)





bot.run(token)
