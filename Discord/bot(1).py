import discord
import time
import asyncio
token = 'NzI0ODE4ODU4NDI2NDk5MDcy.XvFuKg.ABJ4PeLleu9Nkgp4h3YifQ_fFtw'

joined = messages = 0
client = discord.Client()

'''async def update_tasks():
    await client.wait_until_ready()
    global messages, joined


    while not client.is_closed():
        try:
            file = open('stats.txt','a')
            file.write(f'Time: {int(time.time())},messages : {messages},Joined : {joined}\n')

            joined=messages=0

            await asyncio.sleep(5)
        except Exception as e:
            print(e)

        await asyncio.sleep(5)'''

@client.event

async def on_member_join(member):
    global join
    join += 1
    print(member.server_er_name)
    for channel in member.server.channels:
        if channel == 'welcome':
            await channel.send_message(f'Welcome {member.mention}')
    await member.send_message(f'Welcome to {member.server_er_name}')

@client.event


async def on_message(message):
    if message.channel.type is discord.ChannelType.private:
        uneligible = ['Assistant😎#6148']
        if str(message.author) not in uneligible:
            if message.content.find('hello') != -1:
                await message.author.send('hello')

    else:
        global messages
        messages += 1
        id = client.get_guild(724817010860752968)

        #eligible = ['Aaryan#2293']
        uneligible = ['Assistant😎#6148']


        if str(message.author) not in uneligible:
            print(message.content)
            if message.content.find('hello') != -1:
                await message.author.send('hi')

            if message.content.find('users') != -1:
                await message.channel.send(f'{message.author.mention} Total number of Users in {id.name} are : {id.member_count}')

            if 'talk' in message.content:
                await message.author.send(f'Hey {message.author} What\'s up?')
                await message.channel.send(f'{message.author.mention} check your Direct Messages :raised_hands:')







#client.loop.create_task(update_tasks())
client.run(token)