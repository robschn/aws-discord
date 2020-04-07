import os
import time

from discord.ext import commands
from dotenv import load_dotenv

import botfunctions


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='start', help='Starts Minecraft server')
async def purchase_price(ctx, purchase_price: int):
    mention = ctx.author.id
    await ctx.send(f'<@{mention}> Starting instance..')

@bot.command(name='stop', help='Starts Minecraft Server')
async def purchase_price(ctx, purchase_price: int):
    mention = ctx.author.id
    await ctx.send(f'<@{mention}> Stopping instance..')

bot.run(TOKEN)