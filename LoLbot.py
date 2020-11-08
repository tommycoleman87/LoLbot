import os
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv
import cassiopeia as cass
from player_class import Player
load_dotenv()


LOL_TOKEN = os.getenv('LOL_TOKEN')
TOKEN = os.getenv('DISCORD_TOKEN')

cass.set_riot_api_key(LOL_TOKEN)  # This overrides the value set in your configuration/settings.
cass.set_default_region("NA")

bot = commands.Bot(command_prefix='!')
summoner = ''

def role(role_obj):
    if 'TOP_LANE' in role_obj:
        return role_obj.TOP_LANE
    else:
        return None

@bot.command(name='summoner')
async def get_summoner(ctx, arg):
   global summoner
   summoner = cass.get_summoner(name=arg)
   await ctx.send(f'{summoner.name} is level {summoner.level}')

@bot.command(name='match')
async def get_match_stats(ctx):
    matches = summoner.match_history
    role_dict = {}
    # if len(matches) > 100:
    #     matches = matches[:100]
    # for match in matches:
    #     current_summoner = [player for player in match.participants if player.summoner.name == summoner.name]
    #     current_summoner = current_summoner[0]
    #     if current_summoner.lane is not None and current_summoner.role is not None:
    #         key = (str(current_summoner.lane.name) + str(current_summoner.role.name))
    #         if key in role_dict:
    #             role_dict[key] += 1
    #         else:
    #             role_dict[key] = 0
       
    await ctx.send(len(matches))
    # for player in team_1:
    #     ranks = player.league_entries.copy()
    #     ranks = [(rank.wins, rank.queue, rank.tier, rank.division) for rank in ranks]
    #     message = f'Summoner: {player.name} \n Rank: {ranks} \n Level: {player.level}'
    #     await ctx.send(message)

@bot.command(name='roles')
async def roles(ctx):
    summoner = cass.get_summoner(name='aresyama')
    match = summoner.match_history[0]
    teams = match.teams
    team_1 = teams[0].participants
    player_1 = Player(team_1[0].summoner.name, team_1[0].champion.name)
    best_role = player_1.main_role()
    await ctx.send(best_role)
  



bot.run(TOKEN)