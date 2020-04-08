import os
import time

import boto3
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('DISCORD_TOKEN')
region = os.getenv('REGION_ID')
instance = os.getenv('INSTANCE_ID')

ec2 = boto3.client('ec2', region_name=region)
bot = commands.Bot(command_prefix='!')

@bot.command(name='start', help='Starts Minecraft server')
async def start_instance(ctx):
    mention = ctx.author.id
    ec2.start_instances(InstanceIds=[instance])
    await ctx.send(f'<@{mention}> Starting Minecraft server..')

@bot.command(name='stop', help='Stops Minecraft Server')
async def stop_instance(ctx):
    mention = ctx.author.id
    ec2.stop_instances(InstanceIds=[instance])
    await ctx.send(f'<@{mention}> Stopping Minecraft server..')

@bot.command(name='status', help='Displays the status of the Minecraft server')
async def status_instance(ctx):
    mention = ctx.author.id
    instance_info = ec2.describe_instances()
    # if instance_info['Reservations']['Instances']['InstanceId'] == instance:
    #     instance_ip = instance_info['Reservations']['Instances']['PublicIpAddress']
    # await ctx.send(f'<@{mention}> Minecraft server IP: {instance_ip}')
    await ctx.send(instance_info['Reservations']['Instances']['InstanceId'])

bot.run(token)