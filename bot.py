import discord
import os
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot started.')
    await client.change_presence(activity=discord.Game('Space Network and DavidDGTNT'))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments.')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Unknown command. Use .help for a list of commands')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have the required permissions to run this command.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {client.latency * 1000}ms')

def owner(ctx):
    return ctx.author.id == 317394276189208576

@client.command()
@commands.check(owner)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.check(owner)
async def shutdown(ctx):
    exit()

@client.command()
@commands.check(owner)
async def status(ctx, *, txt):
    await client.change_presence(activity=discord.Game(txt))

@client.command()
@commands.check(owner)
async def log(ctx, *, txt):
    print(txt)

@client.command()
@commands.check(owner)
async def say(ctx, *, txt):
    await ctx.channel.purge(limit=1)
    await ctx.send(txt)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

<<<<<<< HEAD
client.run('NzM5NjYxMDA4OTQ3MjQ5MTYy.Xyds_g.YigQtK5UJ-gGI8WsibIfMDctiII')
=======
client.run('NzM5NjYxMDA4OTQ3MjQ5MTYy.Xyds_g.f_emwqA3AjEvE-cCVArh9H66DV4')
>>>>>>> parent of f89db24... Update bot.py
