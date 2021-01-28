import discord
import random
import re
import difflib
import time
import asyncio
import os
from dotenv import load_dotenv
from discord import channel
from discord import message
from discord.client import Client
from discord.enums import _is_descriptor
from discord.ext import commands
from cogs import *

# the prefix is what you write before commands
client = commands.Bot(command_prefix= '.')

load_dotenv()

GUILD = os.getenv("DISCORD_GUILD")

id = client.get_guild(GUILD)

TOKEN = os.getenv("DISCORD_TOKEN")

# to see if a member of the guild/server has joined 
@client.event
async def on_member_join(member):
    print(f'{member} ,a fellow bot, has joined the server.')
    # can welcome the user
    await member.create_dm()
    await member.dm_channel.send(
        f'Welcome {member.name}, to a squad of losers, except me ofc! :)'
    )

# to see if a member of the guild/server has left
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

# fun stuff
@client.command(aliases=['roasty', 'Roast'])
async def roast(ctx, *, name, help = 'Responds with a "roast" tailored to the name of the server member given'):
    roasting_dict = {'ngawang' : 'Ngawangs toes', 'sam' : 'sams a pedo', 
                    'biraj' : 'biraj is gay', 'ibra' : 'barry is great ofc', 
                    'tadi' : 'tadi is a lil bum'}
    for i in roasting_dict:
        if name == i:
            answer = roasting_dict[i]
            await ctx.send(f'name: {name}\nAnswer: {answer}')


# working with cogs 
# load a cog
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

# unload a cog
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

# reload a cog
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def displayembed(ctx):
    embed = discord.Embed(
        title = "Titile",
        description = "Description",
        color = discord.Color.blue()
    )
    embed.set_footer(text="text this is a footer.")

    await ctx.send(embed=embed)

@client.command()
async def points(ctx):
    await ctx.send("10 or 20 points")

    def check(msg):
        return msg.author == ctx.author and msg.content.lower() in ["10", "20"]

    msg = await client.wait_for("message", check=check)
    if msg.content.lower() == "10":
        points = discord.Embed(
            title = "Number of Points",
            color = discord.Color.red()
        )
        points.add_field(name="points", value=10)
        await ctx.send(embed=points)
    elif msg.content.lower() == "20":
        points = discord.Embed(
            title = "Number of Points",
            color = discord.Color.red()
        )
        points.add_field(name="points", value=20)
        await ctx.send(embed=points)    

@client.command()
async def play(ctx):
    intro = discord.Embed(
        title = 'Geography Stuff',
        description = "Me trying to make the geography game",
        colour = discord.Color.blue()
    )
    intro.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQPVXjXxgMY-3nNO0XaCFc4reXJuUfvsyDQg&usqp=CAU")
    await ctx.send(embed=intro)
    data = {'China' : 'Beijing', 'Mexico' : 'Mexico City', 
                    'Egypt' : 'Cairo', 'Russia' : 'Moscow', 
                    'Spain' : 'Madrid'}
    def check(msg):
        return msg.author == ctx.author or msg.author in client.get_all_members 

    country = random.choice(list(data.keys()))
    question = discord.Embed(
        title = "Guess the capital of " + country,
        color = discord.Color.blue()
    )
    await ctx.send(embed=question)
    start = time.time()
    msg = await client.wait_for("message", check=check)
    end = time.time()
    if (end - start) > 20:
        await ctx.send("You took too long")
        return
    if msg.content.lower() == data[country].lower():
        print('here1')
        points = discord.Embed(
            title = "Number of Points",
            color = discord.Color.red()
        )
        points.add_field(name="points", value=1)
        await ctx.send(embed=points)
    else:
        await ctx.send('INCORRECT')


@client.command()
async def type(ctx,*, rounds = 10, help = 'enter the number of words you want to type'):
    imgUrls = ["https://simplycoding.org/wp-content/uploads/2020/09/Nitro-Type.png",
                "https://typingtestnow.com/scripts/js/games/typeracer-type-racer/media/typeracer-type-racer.png"
              ]
    intro = discord.Embed(
        title = 'Typing test',
        description = "type the sentence given",
        colour = discord.Color.blue()
    )
    intro.set_image(url=random.choice(imgUrls))
    await ctx.send(embed=intro)

    def check(msg):
        return msg.author == ctx.author

    test = ""
    data = []
    file = open('data.txt')
    for line in file:
        word = line.strip()
        data.append(word)
    file = open('data2.txt', encoding="utf8")
    read = file.read().strip().replace('\n',' ').split('   ')
    print(read[0])

    prompt = discord.Embed(
            description = "Do you want punctuation, [Y/N]",
            color = discord.Color.red()
    )
    await ctx.send(embed=prompt)
    ask = await client.wait_for("message", check=check)
    if (ask.content == "Y" or ask.content == "y"):
        rand = random.randint(0, len(read) - 1)
        test = read[rand]
        print("this is the test string -> ", test)
        sentence = discord.Embed(
            description = test,
            color = discord.Color.blue()
        )
        await ctx.send(embed=sentence)
    elif (ask.content == "N" or ask.content == "n"):
        for i in range(0, int(rounds)):
            random.shuffle(data)
            test += " " + data[5]
        print("this is the test string -> ", test)
        sentence = discord.Embed(
            description = test,
            color = discord.Color.blue()
        )
        await ctx.send(embed=sentence)
    
    start = time.time()
    msg = await client.wait_for("message", check=check)
    end = time.time()
    total = end - start

    import math
    timerFormula = round(( math.log(len(test) / 5) * 30 ))
    print("this is the time needed for this text: ", timerFormula)
    if total > timerFormula: # or total 2 > timer formula 
        await ctx.send("You took too long my friend")
        return
    
    msgStr = msg.content
    print(msgStr)
    # sentenceLen = len(re.findall(r'\w+', test))
    sentenceLen = len(test)
    rawAcc = difflib.SequenceMatcher(None, test.strip(), msgStr.strip()).ratio()
    grosswpm  = round( ( (sentenceLen) / 5) / ((total / 60)), 2)
    print("this is the length of the sentence -> ", sentenceLen)
    accuracy = round(rawAcc * 100, 2)
    wpm = round(grosswpm * rawAcc, 2) 

    result = discord.Embed(
        title = "Your score: ",
        color = discord.Color.red()
    )
    result.add_field(name="Name", value=msg.author.name, inline=False)
    result.add_field(name="wpm", value=wpm, inline=True)
    result.add_field(name="raw wpm", value=grosswpm, inline=True)
    result.add_field(name="accuracy", value=accuracy, inline=True)

    await ctx.send(embed=result)


@client.command()
async def test2(ctx):
    numPlayers = discord.Embed(
        description = "All players click the play button",
        color = discord.Color.blue()
        
    )
    sending = await ctx.send(embed=numPlayers)
    await sending.add_reaction('▶')

    def check(reaction, user):
        return user != client.user and user == ctx.author and str(reaction.emoji) in ['▶']


    players = []
    while True:
        try:
            
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
            if str(reaction.emoji) == "▶":
                # await ctx.send('{} participants'.format(user))
                users = await reaction.users().flatten()
                for i in users:
                    await ctx.send(i)
                    players.append(i)

            else:
                await sending.remove_reaction(reaction, user)

        except asyncio.TimeoutError:
            await sending.delete()
            break
    def users():
        return players
    
    peeps = users()
    if ctx.message.author in peeps and ctx.message.author != client.user:
        await ctx.message.channel.send("You are {}".format(ctx.message.author))


    


client.run(TOKEN)

