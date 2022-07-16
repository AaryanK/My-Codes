import discord

client = discord.Client()
TOKEN = "OTA2MDM3OTg1MDQ3MzgwMDIw.YYSzoQ.rVrxJehS49zJnph0sOoFQBytsjo"

@client.event
async def on_ready():
    print("DONE")

# <Message id=906046434887991327 channel=<DMChannel id=906040526992715828 recipient=<User id=489787401431154688 name='Aaryan' discriminator='2293' bot=False>> type=<MessageType.default: 0> author=<User id=489787401431154688 name='Aaryan' discriminator='2293' bot=False> flags=<MessageFlags value=0>>

@client.event
async def on_message(message):
    message_author = str(message.author)
    message_author_id = message.author.id
    is_bot = message.author.bot
    if message.author.id !=906037985047380020:
        if str(message.channel.type) == "private":
            #For Private Channels (DM)
            if message.author.id ==489787401431154688:
                async with message.channel.typing():
                    await message.channel.send('Hey from private')
            else:
                await message.channel.send(f'Hey {message.author.name},Nice seeing you but I\'m sorry pal I only talk to Aaryan in DMs\'.See you later Bye for Now. ;)')
        else:
            #For Group Messages (Servers)
            async with message.channel.typing():
                await message.channel.send("Hey")
        print(message.author)
        print(message)
        


client.run(TOKEN)