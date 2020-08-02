import discord
from discord.ext import commands
# import discord.voice_client
import time
import os
import asyncio

token = os.environ.get('HIDE_BOT_TOKEN') # no u

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot is online. Be happy :)')
    activity = discord.Activity(name=' -->  💻  <--', type=1)
    await bot.change_presence(activity=activity)# .Status.(Idle, do_not_disturb, online) | , status=discord.Status.do_not_disturb



@bot.command()
async def avatar(ctx, member: discord.Member):
    author = ctx.message.author
    embed = discord.Embed( description='**Аватарка пользователя ' + str(member.mention) + '**', colour=discord.Colour.purple())
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def random_user(ctx):
    channel = ctx.message.channel
    randomMember = random.choice(channel.guild.members)
    while randomMember.bot == True:
        randomMember = random.choice(channel.guild.members)
    await channel.send('Рандомный участник сервера: 'f'{randomMember.mention}')


@bot.command()
async def random_bot(ctx):
    channel = ctx.message.channel
    randomMember = random.choice(channel.guild.members)
    while randomMember.bot == False:
        randomMember = random.choice(channel.guild.members)
    await channel.send('Рандомный бот: ' + f'{randomMember.mention}')
# @bot.command()
# async def join_voice(ctx):
#     channel = ctx.author.voice.channel
#     await channel.connect()
#
#
# @bot.command()
# async def leave_voice(ctx):
#     await ctx.voice_client.disconnect()


@bot.command()
async def kiss(ctx, member: discord.Member):
    author = ctx.message.author
    if author != member :
        # ctx.send(str(author.mention) + ' и ' str(member.mention) + ' поцеловались')
        embed = discord.Embed( description='**' + str(author.mention) + ' и ' + str(member.mention) + ' поцеловались**', colour=discord.Colour.red())
        embed.set_image(url='https://i.pinimg.com/originals/69/cf/45/69cf45b7947fe8318ee8c899873066cd.gif')
        await ctx.send(embed=embed)
    else:
        if author == member:
            # ctx.send(str(author.mention) + ' и ' str(member.mention) + ' поцеловались')
            embed = discord.Embed( description='**' + str(author.mention) + 'поцеловал сам себя....**', colour=discord.Colour.red())
            await ctx.send(embed=embed)




@bot.command()
async def idea(ctx, *, args):
    author = ctx.message.author
    channel_all = ctx.message.channel
    channel_idea = bot.get_channel(718153307880947712)
    channel_vote = bot.get_channel(727967281547837440)


    if (channel_all != channel_idea):
        await ctx.send(str(author.mention) + ', идеи нужно писать в канале ' + str(channel_idea.mention))
    else:
        if (channel_all == channel_idea):
            await ctx.message.delete()
            idk0 = await channel_idea.send(str(author.mention) + ', твоя идея успешно отправлена в канал ' + str(channel_vote.mention))
            idk = await channel_vote.send('@everyone\n' + 'Идея:\n' + '**' + args + '**' + '\n\nИдею предложил(a): ' + str(author.mention))#+'\n✅ - Одобрение\n❌ - Несогласие\n❓ - Нейтрально'
            await idk0.add_reaction('✅')
            await idk.add_reaction('✅')
            await idk.add_reaction('❌')
            await idk.add_reaction('❓')


@bot.command()
async def kiss_other(ctx, member: discord.Member, member1: discord.Member):
    author = ctx.message.author
    if member != member1 :
        # ctx.send(str(author.mention) + ' и ' str(member.mention) + ' поцеловались')
        embed = discord.Embed( description='**' + str(member.mention) + ' и ' + str(member1.mention) + ' поцеловались**', colour=discord.Colour.red())
        embed.set_image(url='https://i.pinimg.com/originals/69/cf/45/69cf45b7947fe8318ee8c899873066cd.gif')
        embed.set_footer(text='А кто у нас тут шипперит, ' + str(author.display_name) + ':)?')
        await ctx.send(embed=embed)
    else:
        if member == member1:
            # ctx.send(str(author.mention) + ' и ' str(member.mention) + ' поцеловались')
            embed = discord.Embed(description='**Сори, ' + str(author.mention) + ', но нужно тегнуть двух разных людей**', colour=discord.Colour.red())
            nope = await ctx.send(embed=embed)
            await nope.add_reaction('❌')


# @bot.command()
# async

@bot.command()
async def userinfo(ctx, member: discord.Member):

    roles = [role for role in member.roles]

    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at)

    embed.set_author(name=f"Информация пользователя {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Имя на сервере:", value=member.display_name, inline=True)
    embed.add_field(name="ID:", value=member.id, inline=False)

    embed.set_footer(text=f"Запрос на команду: {ctx.author}", icon_url=ctx.author.avatar_url)


    # embed.add_field(name="Bot?", value=member.bot)

    embed.add_field(name="Аккаунт создан:", value=member.created_at.strftime("%a, %#d %B %Y"), inline=True)
    embed.add_field(name="Присоединился к серверу:", value=member.joined_at.strftime("%a, %#d %B %Y"), inline=False)

    embed.add_field(name=f"Роли ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Высшая роль:", value=member.top_role.mention)


    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
        messages.append(message)

    await channel.delete_messages(messages)
    yes = await ctx.send('Успешно удалено.')
    await yes.add_reaction("✅")


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


    embed.set_image(url="https://cdn.discordapp.com/attachments/443208943213477889/601699371221909504/imagesfidosfhdis.jpg")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/443208943213477889/601699371221909504/imagesfidosfhdis.jpg")
    embed.add_field(name="hello", value="This has the bot say hello", inline=False)
    embed.add_field(name="Test Field 2", value="this is test 2", inline=False)
    embed.add_field(name="test field 3", value="This is a test 3", inline=False)
    embed.set_footer(text="Made by MagicalAlex", icon_url='https://cdn.discordapp.com/avatars/717480562155192381/df15e97304ee47e04fe912b22a5ebdd5.jpg?size=1024')
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
