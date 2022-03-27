import os
import requests
import discord
from discord.abc import PrivateChannel
from discord.ext import commands, tasks
from dotenv import load_dotenv
from Authorization import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='$')
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('MAL Bot | $help'))
    print(f'{client.user} has connected to Discord!')


@client.command()
async def hello(ctx):
    confirmation = await ctx.author.send('Successfully authorized.')
    emoji = '\N{THUMBS UP SIGN}'
    await confirmation.add_reaction(emoji)


@client.command()
async def authorize(ctx, auth_code=None):
    user_auth = check_user_auth(ctx.message.author.id)
    if user_auth:
        await ctx.author.send('You\'re already authorized')
    else:
        if auth_code is None:
            await ctx.author.send('In order to authorize you have to open this link, copy your authorization code and '
                                  'reply to this DM with $authorize {your_code} command')
            auth_link = generate_authorization_link()
            await ctx.author.send(auth_link)
        elif isinstance(ctx.channel, PrivateChannel):
            generate_new_user_token(auth_code, ctx.author.id)
            confirmation = await ctx.send('Successfully authorized.')
            emoji = '\N{THUMBS UP SIGN}'
            await confirmation.add_reaction(emoji)


@client.command(alias=['recommendation'])
async def random_recommendation(ctx):
    pass

client.run(TOKEN)
