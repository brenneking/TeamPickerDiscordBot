import random
import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)
maps = ['Haven', 'Ascent', 'Bind', 'Icebox', 'Split', 'Breeze', 'Fracture']
sides = ['Defense', 'Attack']

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(ctx):
    if ctx.author == client.user:
        return
    if 'pickteams' in ctx.content:
        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel
        else:
            await ctx.channel.send("You are not connected to a voice channel")
            return
        members = channel.members
        for member in list(members):
            if member.bot:
                members.remove(member)
            if 'mobile' in str(member):
                members.remove(member)
        if int(len(members)) < 2:
            await ctx.channel.send('Not enough players to make teams. Try inviting more people to play')
            return
        memNames = []
        for member in members:
            if member.nick:
                memNames.append(member.nick)
            else:
                memNames.append(member.name)
        random.shuffle(memNames)
        half = int(len(memNames) / 2)
        i = 0
        teamA_Names = []
        teamB_Names = []
        while i < half:
            teamA_Names.append(memNames[i])
            i += 1
        while i < len(memNames):
            teamB_Names.append(memNames[i])
            i += 1
        teamA_Str = '\n'.join(teamA_Names)
        teamB_Srt = '\n'.join(teamB_Names)
        embed = discord.Embed(title='Teams', description='Here are the teams. Good luck!', color=discord.Color.red())
        embed.add_field(name='Attackers', value=teamA_Str, inline=True)
        embed.add_field(name='Defenders', value=teamB_Srt, inline=True)
        embed.add_field(name='Map', value=maps[random.randint(0, 3)], inline=False)
        await ctx.channel.send(embed=embed)

client.run('Insert Bot Token Here')
