import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import config
from config import token

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("yeah sure")
   
@client.command(pass_context=True)
async def gdpscmds(ctx):
    await client.say("")

client.run(token)