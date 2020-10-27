import os
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv
import cassiopeia as cass
load_dotenv()


LOL_TOKEN = os.getenv('LOL_TOKEN')
TOKEN = os.getenv('DISCORD_TOKEN')

cass.set_riot_api_key(LOL_TOKEN)  # This overrides the value set in your configuration/settings.
cass.set_default_region("NA")

bot = commands.Bot(command_prefix='!')
summoner = ''
@bot.command(name='summoner')
async def get_summoner(ctx, arg):
   global summoner
   summoner = cass.get_summoner(name=arg)
   await ctx.send(f'{summoner.name} is level {summoner.level}')

@bot.command(name='match')
async def get_match_stats(ctx):
    match = summoner.match_history[0]
    teams = match.teams
    team_1 = teams[0].participants
    team_2 = teams[1].participants
    team_1 = [player.summoner for player in team_1]
    team_2 = [player.summoner for player in team_2]

    for player in team_1:
        ranks = player.league_entries.copy()
        ranks = [(rank.wins, rank.queue, rank.tier, rank.division) for rank in ranks]
        message = f'Summoner: {player.name} \n Rank: {ranks} \n Level: {player.level}'
        await ctx.send(message)
    
  



bot.run(TOKEN)