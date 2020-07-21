import discord
import random
from discord.ext import commands
# the prefix is what you write before commands
client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print("Bot is ready")

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

@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms')

# fun stuff
@client.command(aliases=['roast'])
async def _roast(ctx, *, name, help = 'Responds with a "roast" tailored to the name of the server member given'):
    roasting_dict = {'ngawang' : 'Ngawangs toes', 'sam' : 'sams a pedo', 
                    'biraj' : 'biraj is gay', 'ibra' : 'barry is great ofc', 
                    'tadi' : 'tadi is a lil bum'}
    for i in roasting_dict:
        if name == i:
            answer = roasting_dict[i]
            await ctx.send(f'name: {name}\nAnswer: {answer}')
# clear messages
@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)

# kick a player
@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason=reason)
    if member.clear(ctx, amount > 5):
        await member.kick(reason = "Too many Clears") 

# ban a player
@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason=reason)

# unban a player 
@client.command()
async def unban(ctx, *, member):
    banned = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#') # seperate the number from the 4 digit id 
    for entry in banned:
        user = entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user) 
            await ctx.send(f'unbanned {user.mention}')
            return 










        

client.run('NzMzMTA2OTQwMzMwMTE1MDgy.Xw-_Nw.hp_h6jl2_rJhGOFGCfQme58-Cz8')
