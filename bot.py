import discord
import asyncio
import time
import datetime
import arrow
import pytz
import random
import discord


from discord.ext import commands


from datetime import datetime, timezone
from time import gmtime, strftime

utc_dt = datetime.now(timezone.utc)

CST = pytz.timezone('America/Chicago')
PST = pytz.timezone('America/Los_Angeles')
EST = pytz.timezone('America/New_York')
MST = pytz.timezone('US/Arizona')
fmt = '%Y-%m-%d %H:%M:%S $Z$z'


TOKEN = 'NjcxMjYzMDQ5NjUwNDA1Mzc5.Xi7MbA.rXh-fVFq8htYHnj2DtY0wKziv3M'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


#message events
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # if message.content.startswith('$hello'):
       # await message.channel.send('Howdy!')

    if message.content.startswith('$hello'):
        await message.channel.send(file=discord.File('hello.gif'))
 

    if message.content.startswith('$cb'):
        await message.channel.send('crab moment.')

    if message.content.startswith('$goodnight'):
        await message.channel.send('gn gamer')

  # if 'bot' in message.content:
       # await message.channel.send("I'm more than a bot :frowning:")

    if 'Russia' in message.content:
        await message.channel.send("Россия – священная наша держава," + " Россия – любимая наша страна." + " Могучая воля, великая слава –" + " Твоё достоянье на все времена!")

    if 'Hitler' in message.content:
        await message.channel.send("Sieg Heil!")
        
    if 'Trump' in message.content:
     await message.channel.send("Trump 2020 #MAGA")
     
  #  if 'President' in message.content:
       # await message.channel.send("Trump 2020 #MAGA")

   # if 'Charli' in message.content:
        #await message.channel.send("cringe.")

    # if 'charli' in message.content:
        #await message.channel.send("cringe.")

#timezones
    if message.content.startswith('$CST') or message.content.startswith('$cst'):
        await message.channel.send("CST Time:   {}".format(utc_dt.astimezone(CST).isoformat()))

    if message.content.startswith('$PST') or message.content.startswith('$pst'):
        await message.channel.send("PST Time:   {}".format(utc_dt.astimezone(PST).isoformat()))

    if message.content.startswith('$MST') or message.content.startswith('$mst'):
        await message.channel.send("MST Time:   {}".format(utc_dt.astimezone(MST).isoformat()))

    if message.content.startswith('$EST') or message.content.startswith('$est'):
        await message.channel.send("EST Time:   {}".format(utc_dt.astimezone(EST).isoformat()))

    if message.content.startswith('$UTC') or message.content.startswith('$utc'):
        await message.channel.send("UTC Time:   {}".format(utc_dt.isoformat()))

    





#pics

    if message.content.startswith('tercel'):
        await message.channel.send(file=discord.File('tercel.jpg'))

    if message.content.startswith('$crab'):
        await message.channel.send(file=discord.File('honkler.jpg'))

    if message.content.startswith('$hehe'):
        await message.channel.send(file=discord.File('pepelaugh.gif'))

    if message.content.startswith('$bonk'):
        await message.channel.send(file=discord.File('bonk.gif'))

    if message.content.startswith('$bing'):
        await message.channel.send(file=discord.File('GlockedUpGamer.mp4'))
                                   
client.run('NjcxMjYzMDQ5NjUwNDA1Mzc5.Xi7MbA.rXh-fVFq8htYHnj2DtY0wKziv3M')
