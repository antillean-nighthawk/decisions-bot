import os, random
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix='~', intents=intents)
random.seed()

token = os.getenv('TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(aliases=['coin', 'flip'], help="Flip a coin")
async def coinflip(ctx):
    await ctx.send(random.choice(["Heads", "Tails"]))

@client.command(aliases=['die', 'd'], help="Roll dice")
async def dice(ctx):
    await ctx.send("You rolled a " + str(random.randint(1, 6)) + '!')

@client.command(aliases=['c'], help="Draw a card")
async def card(ctx):
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "King", "Queen"]
    await ctx.send("You got a " + random.choice(number) + " of " + random.choice(suits) + '!')

@client.command(aliases=['m'], help="Pick a member in the channel", pass_context=True)
async def member(ctx):
    names = []
    members = ctx.message.guild.members
    for member in members:
        names.append(member.display_name)
    await ctx.send(random.choice(names))

client.run(token)