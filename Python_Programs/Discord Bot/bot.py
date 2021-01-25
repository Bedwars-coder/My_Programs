import discord
from discord.ext import commands
import datetime

def time():
    return str(datetime.datetime.now())

prefixes = ['=', '??']
client = commands.Bot(command_prefix=prefixes)

@client.event
async def on_ready():
    print("I am happy to see that you have coded your bot successfully,\nYour bot is online and ready to be used! ")


@client.command()
async def hi(ctx):
    print("'hi' command was used!")
    await ctx.send("Welcome! I am a bot! I Can't do Anything for the time being. Stay Tuned!")

@client.command()
async def whodevedyou(ctx):
    print("'whodevedyou' command was used!")
    await ctx.send("☆꧁༒IAmBedwars༒꧂☆#9549 has developed me!")

@client.command()
async def helppls(ctx):
    print("'_help' command was used!")
    await ctx.send("Welcome to the A1bot's helpdesk!\nOnly 3 commands are programmed for the time being! They are '=hi' and '=whodevedyou' and '=helppls'!\nTry them!")

@client.command()
async def lol(ctx):
    await ctx.send("Idk why do you want to laugh. I will make you laugh but later!\nStay Tuned!")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount+1)

@client.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member, *, reason):
    with open(member+".txt", "a") as warnlogging:
        warnlogging.write(time()+" )"+reason+"\n")
    await ctx.send(f"I have warned {member}!")

@client.command()
async def warnings(ctx, *, member: discord.Member):
    with open(member+".txt") as warnret:
        count = 0
        for lines in warnret:
            count += 1
        await ctx.send(f"I found {count} warnings for {member}!")
        for warningss in warnret:
            await ctx.send(warningss)

@client.command()
@commands.has_permissions(kick_members=True)
async def clearwarn(ctx, *, member: discord.Member):
    with open(member+".txt", "w") as op:
        op.write("")
    await ctx.send(f"Cleared all warnings for {member}!")

client.run("Bot's token as a string")
