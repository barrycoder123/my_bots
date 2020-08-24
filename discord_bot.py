import discord
import random
import os
from discord.ext import commands
from cogs import *

# the prefix is what you write before commands
client = commands.Bot(command_prefix= '.')

# to see if a member of the guild/server has joined 
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
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


client.run('NzMzMTA2OTQwMzMwMTE1MDgy.Xw-VCw.Kud4WTsacSWNeDZZ8iJv1Q_IcDg')
