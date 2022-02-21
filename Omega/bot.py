import os
import requests
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'getrandomanime' in message.content.lower():
        r = requests.get('https://api.jikan.moe/v4/random/anime')
        data = r.json()
        await message.channel.send(f'Random anime {data["data"]["title"]}\nLink: {data["data"]["url"]}')
    if 'best anime' in message.content.lower():
        r = requests.get('https://api.jikan.moe/v4/top/anime')
        data = r.json()
        await message.channel.send(str(data))


client.run(TOKEN)
