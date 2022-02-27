import os
import requests
import discord
from discord.abc import PrivateChannel
from discord.ext import commands, tasks
from dotenv import load_dotenv
from Authorization import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='#')
client.remove_command('help')

token_list = dict()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('MAL Bot | $help'))
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'authorize' in message.content.lower():
        await message.author.send('Hello dude')
    if 'random' in message.content.lower():
        r = requests.get('https://api.jikan.moe/v4/random/anime')
        data = r.json()
        await message.channel.send(f'Random anime {data["data"]["title"]}\nLink: {data["data"]["url"]}')
    if 'best anime' in message.content.lower():
        r = requests.get('https://api.jikan.moe/v4/top/anime')
        data = r.json()
        await message.channel.send(str(data))


@client.command()
async def hello(ctx):
    confirmation = await ctx.send('Successfully authorized.')
    emoji = '\N{THUMBS UP SIGN}'
    await confirmation.add_reaction(emoji)


@client.command()
async def authorize(ctx, auth_code=None):
    if ctx.message.author in token_list.keys():
        await ctx.send('You\'re already authorized')
    else:
        if auth_code is None:
            await ctx.send('In order to authorize u have to open this link, copy your authorization code and '
                           'send it back with $authorize {your_code} command')
            auth_link = generate_authorization_link()
            await ctx.send(auth_link)
        elif isinstance(ctx.channel, PrivateChannel):
            user_token = generate_new_user_token(auth_code)
            confirmation = await ctx.send('Successfully authorized.')
            emoji = '\N{THUMBS UP SIGN}'
            await confirmation.add_reaction(emoji)


client.run(TOKEN)
