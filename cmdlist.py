import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("yeah sure")
   
@client.command(pass_context=True)
async def gdpscmds(ctx):
    await client.say("""----------GDPS Commands List----------
    Coming soon
    -------------------------------------""")

client.run("NjEwNTk5NTIxMTIxOTkyNzA1.XVX13A.hPtsFWLLIKpOaw7TzSyCPHOZOmI")
