import discord
from discord.ext import commands

class Example(commands.Cog):
    # constructor
    def __init__(self, client):
        self.client = client

    # events
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 690797899180670976:
            await message.channel.send('shut up remember you are gay :)')
            
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status = discord.Status.idle, activity = discord.Game("League of Legends"))
        print("Bot is ready")
    # commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.client.latency * 1000)}ms')
        

def setup(client): # create a client object
    client.add_cog(Example(client))