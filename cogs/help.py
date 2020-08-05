import discord
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help command loaded')

    @commands.command()
    async def help(self, ctx):

        helpembed = discord.Embed(
            colour = discord.Colour.blue(),
            title = 'Command List:',
            description = '.help | Show this message\nFun:\n.8ball | Ask the Magic 8 Ball a question.\n.hi | Says Hello to you.\n.rr | Lets you play Russian Roulette\nTroubleshooting:\n.ping | Gets your ping.\nModeration:\n.clear | Clears messages (default 5)\n.kick | Kicks members\n.ban | Bans members\n.unban | Unbans members'
        )
        helpembed.set_footer(text='DavidBot by DavidDGTNT')
        await ctx.send(embed=helpembed)

def setup(client):
    client.add_cog(help(client))