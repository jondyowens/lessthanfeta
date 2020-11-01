# bot.py
import os

import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    list_of_cheese = ["<:CHEESE:746596359280263209>", ":cheese:", "<:cheese:767272983214686228>"]
    if "cheese" in message.content.lower():
        await message.add_reaction(random.choice(list_of_cheese))

    if "!emojis" in message.content:
        emoji_dump = str()
        for emojis in client.emojis:
            if not emojis.managed:
                emoji_dump += str(emojis) + " "

        await message.channel.send(emoji_dump)

client.run(TOKEN)