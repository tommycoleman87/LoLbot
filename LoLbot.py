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
    matches = summoner.match_history
    await ctx.send(matches[0])

bot.run(TOKEN)