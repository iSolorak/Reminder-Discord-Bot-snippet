import discord
import os
import time
import asyncio
import io
from discord.ext import tasks 
from datetime import datetime
import discord
from discord.utils import get
from discord import channel
from discord import client
from discord.ext import commands
from discord.ext.commands import Bot
import random
import string
import discord
from discord.utils import get
# Import the following modules

from PIL import Image, ImageFont, ImageDraw

intents = discord.Intents.default()
intents.members = True
bot1 = Bot("!")
bot = discord.Client(intents=intents)



@bot.event
async def on_ready():
 
    await mytask.start()

@tasks.loop(seconds=5) # Add the seconds or minutes or hours to repeat the action (to remind)
async def mytask():
    reminder = time.asctime()
    reminderspli = reminder.split(' ')
    user1 = await bot.fetch_user("you put the ID (not with the '')") # the user that the dm is going to be sent
  
    if reminderspli[0] == 'Thu' and reminderspli[4].startswith('21') == True :   # the reminderspli[0] is the day , the reminderspli[4] is the hour 
        await user1.send('example1')
               
    elif reminderspli[0] == 'Mon' and reminderspli[4].startswith('21') == True:
        await user1.send('example1')
       


bot.run('bot token')


