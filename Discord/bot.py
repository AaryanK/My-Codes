import discord
import asyncio
import time

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('running')

@client.event
async def on_member_join(member):
    print('joined')
    id = client.get_guild(791942970324418611)
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            await channel.send(f"""Welcome to the server {member.mention}""")
    member.send(f'Hello {member.mention} welcome to {id.name}')

@client.event
async def on_message(message):
    print('received')
    server_id = client.get_guild(791942970324418611)

    if message.content == ("users"):
        await message.channel.send(f"""There are {server_id.member_count}""")


    if message.content == ('code'):
        await message.channel.send(f'```py\nprint(\'Hello world\')```')



client.run('NzI0ODE4ODU4NDI2NDk5MDcy.XvFuKg.2WfOdWBp34UOzrllJKVmWURbOJk')
