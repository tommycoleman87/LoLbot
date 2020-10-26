import os
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

LOL_TOKEN = os.getenv('LOL_TOKEN')
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
riot_api = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
summoner_id = ''
headers = {'X-Riot-Token' : f'{LOL_TOKEN}'}
@bot.command(name='summoner')
async def get_summoner(ctx, arg):
    response = requests.get(riot_api + f'{arg}', headers=headers)
    global summoner_id
    summoner_id = response.json()['id']
    if response.status_code == 200:
        await ctx.send(f'Summoner set to {arg}')
    else:
        await ctx.send(f'Error {response.status_code}')

@bot.command(name='match')
async def get_match_stats(ctx):
    response = requests.get(f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}', headers=headers )
    print(summoner_id)
    if response.status_code == 200:
        await ctx.send(response.json())
    else:
        await ctx.send(f'Error {response.status_code}')

bot.run(TOKEN)