import discord
from discord.ext import commands

class Example(commands.Cog):
    # constructor
    def __init__(self, client):
        self.client = client

    # events
    @commands.Cog.listener()
    async def on_message(self, message):
        # if message.author.id == 117448042529030153:
        #     await message.channel.send('Go back to Putin :)')
        if message.author.id == 611276583176765440:
            await message.channel.send('Shut up you hic :(((')
        elif message.author.id == 430177541785911306:
            await message.channel.send('Why do you have your dinner as your profile pic. LOSER')
        # elif message.author.id == 583463945789112352:
        #     await message.channel.send("Your new song is a bop")  
        # elif message.author.id == 690797899180670976:
        #     await message.channel.send("Thats why you're gay") 
        # elif "join" in message.content:
        #     await message.channel.send("Leave me alone you prick")

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status = discord.Status.idle, activity = discord.Game("Valorant"))
        print("Bot is ready")
        
    # commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.client.latency * 1000)}ms')
        

def setup(client): # create a client object
    client.add_cog(Example(client))