import discord 
from discord.ext import commands

class Manage(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def test(self, ctx):
        await ctx.send('test')

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    # kick a player
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason=reason)
    

    # ban a player
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason=reason)
        # if member.clear(ctx, amount > 5):
        #     await member.kick(reason = "Too many Clears") 

    # unban a player 
    @commands.command()
    async def unban(self, ctx, *, member):
        banned = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#') # seperate the number from the 4 digit id 
        for entry in banned:
            user = entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user) 
                await ctx.send(f'unbanned {user.mention}')
                return 
                
def setup(client):
    client.add_cog(Manage(client))