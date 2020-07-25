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
async def embed(ctx):

    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title="Test Title",
        description="This is a test"
    )


    embed.add_field(name="hello", value="This has the bot say hello", inline=False)
    embed.add_field(name="Test Field 2", value="this is test 2", inline=False)
    embed.add_field(name="test field 3", value="This is a test 3", inline=False)
    embed.set_author_footer(name="Made by MegicalAlex", icon_url="https://cdn.discordapp.com/avatars/717480562155192381/df15e97304ee47e04fe912b22a5ebdd5.jpg?size=1024")

    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def help_me(ctx):
    author = ctx.message.author

    test_e = discord.Embed(
        colour=discord.Colour.purple()
    )
    test_e.set_author(name="Bot prefix = !")
    test_e.add_field(name="embed", value="This will post an embed into the discord", inline=False)
    test_e.add_field(name="good day", value="today is a good day")

    await ctx.send(embed=test_e)


bot.run(token)
