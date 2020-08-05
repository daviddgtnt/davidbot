import discord
import random
from discord.ext import commands

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun commands loaded.')

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question):
        responses = ['It is certain.',
                    'It is decidedly so.',
                    'Without a doubt.',
                    'Yes - definitely.',
                    'You may rely on it.',
                    'As I see it, yes.',
                    'Most likely.',
                    'Outlook good.',
                    'Yes.',
                    'Signs point to yes.',
                    'Reply hazy, try again',
                    'Ask again later',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    "Don't count on it."
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Very doubtful.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def hi(self, ctx):
        await ctx.send(f'Hi, {ctx.author}!')
    
    @commands.command()
    async def rr(self, ctx):
        responses = ['Cake!',
                    '1 million dollars!',
                    'You died.',
                    'You died.']
        await ctx.send(f'{random.choice(responses)}')

def setup(client):
    client.add_cog(fun(client))