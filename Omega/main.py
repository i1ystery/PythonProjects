import discord
from discord.ext import commands,tasks
import pandas as pd
import openpyxl as op
from datetime import datetime
from dateutil.relativedelta import relativedelta
import random

client = commands.Bot(command_prefix='#')
client.remove_command('help')
#fileName = 'Suplovani.xlsx'
#date = date.strftime("%#d.%#m.")
#sheets = pd.ExcelFile(fileName).sheet_names
#unordered_map = {'a1': 1, 'c1a': 2, 'c1b': 3, 'c1c': 4, 'e1': 5, 'a2': 6, 'c2a': 7, 'c2b': 8, 'c2c': 9, 'c2d': 10,
#                 'e2': 11, 'a3': 12, 'c3a': 13, 'c3b': 14, 'e3': 15, 'a4': 16, 'c4a': 17, 'c4b': 18, 'e4a': 19,
#                 'e4b': 20}
#hrs = pd.read_excel(fileName).iloc[[0]].values.tolist()[0]
#hrs.pop(0)
rng = ['retard', 'curak', 'borec', 'frajer', 'nejlepsi']
def update_sheets():
    sheets = pd.ExcelFile(fileName).sheet_names

def get_sheet_by_date(date):
    for sheet in sheets:
        if '.' in sheet:
            if date == sheet.split(' ', 1)[1].replace(" ","") or date == sheet.split(' ', 1)[1].replace(" ","")[:-1]:
                return pd.read_excel(fileName, sheet_name=sheet)

def get_classes(table, schoolclass):
    if schoolclass not in unordered_map:
        return 'There is no class with this name'
    else:
        temp = table.iloc[unordered_map[schoolclass]].values.tolist()
        temp.pop(0)
        return temp

def get_output(list):
    output = ''
    for i in range(len(list)):
        if str(list[i]) != 'nan':
            output += f'{hrs[i]} {list[i]}\n'
    return output


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('SPSE Jecna | #help'))
    print('Bot is ready.')


@client.event
async def on_message(message):
    if 'coze' == message.content.lower() or 'cože' == message.content.lower():
        await message.channel.send(file=discord.File('vidlicky_a_noze.png'))
    elif 'co?' == message.content.lower() or 'co' == message.content.lower():
        await message.channel.send(file=discord.File('nikdo_nic_anton_space_engineers.png'))
    await client.process_commands(message)
@client.command()
async def remind(ctx):
    loop.start()
    await ctx.send('Bot připomene rozvrh za 8 hodin.')

@client.command(aliases=['_suplovani', 'date', 'classroom'])
async def suplovani(ctx, date, classroom):
    output = ''
    if str(date).lower() == 'zitra' or str(date).lower() == 'zítra':
        date = datetime.now() + relativedelta(days=1)
        date = date.strftime("%#d.%#m.")
    if 'NoneType' not in str(type(get_sheet_by_date(date))):
         output_list = get_classes(get_sheet_by_date(date), classroom.lower())
         output = f'Suplování na {date} pro tridu {classroom}:\n{get_output(output_list)}'
    else:
        output = f'Suplování na {date} neexistuje.'
    await ctx.send(output)

@client.command()
async def update(ctx):
    update_sheets()
    await ctx.send('Obnoveno')

@client.command()
async def help(ctx):
    await ctx.send('Dostupné příkazy:\n  #suplovani datum(day.month) třída - vypíše suplování na zadaný datum pro určitou třídu.\n  #update - obnoví databázi suplování\n  #remind - bot bude připomínat rozvrh kazdých 8 hodin\n  #ifykyk name - if you know you know\n  #spam user pocet zprava\n  #kopec')

@client.command()
async def author(ctx):
    await ctx.send('Autor: Max Kuzma')

@client.command(aliases=['_ifykyk','name'])
async def ifykyk(ctx, name):
    bruh = random.choice(rng)
    await ctx.send(f'{name} je {bruh}')

@client.command()
async def spam(ctx, victim: discord.User, amount, *, message):
    for _ in range(int(amount)):
        await victim.send(message)

@client.command()
async def wakeup(ctx, victim: discord.Member):
    vc = victim.voice.channel
    voiceChannel = client.get_channel(823632078632386582)
    await ctx.send(victim.mention + ' wake up')
    for _ in range(3):
        await victim.move_to(voiceChannel)
        await victim.move_to(vc)

#@tasks.loop(hours=8)
#async def loop():
#    channel = client.get_channel(792181133303218187)
#    output = ''
#    date = datetime.now() + relativedelta(days=1)
#    date = date.strftime("%#d.%#m.")
#    if 'NoneType' not in str(type(get_sheet_by_date(date))):
#        output_list = get_classes(get_sheet_by_date(date), 'c3a')
#        output = f'Suplování na zítra pro tridu c3a:\n{get_output(output_list)}'
#    else:
#        output = f'Suplování na {date} neexistuje'
#    await channel.send(output)

@client.command()
async def kopec(ctx):
    kopec = '<@580462585065766928>'
    await ctx.send('%s wakey wakey it\'s time for school '% kopec)

@client.command()
async def coze(ctx):
    await ctx.send(file=discord.File('vidlicky_a_noze.png'))

client.run('ODI2NTY5NDAyNjAxOTYzNTcx.YGOYvg.4wck6HawZPTl2UGLN_ERbvtwX0Y')


